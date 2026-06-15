#!/usr/bin/env python3
"""
Regenerate docs/open/{layer}/INDEX.md tables and docs/open/survey.json from
the YAML frontmatter on every entity file.

Schema lives at docs/open/SCHEMA.md. Frontmatter is the source of truth for
all structured fields; prose is canonical for human reading.

Usage:
    python3 scripts/regen.py [--check]

--check: exits non-zero if INDEXes or survey.json would change. CI-friendly.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections.abc import Iterable
from pathlib import Path

# ---------------------------------------------------------------------------
# Layer config
# ---------------------------------------------------------------------------

DOCS = Path(__file__).resolve().parent.parent / "docs" / "open"
SURVEY_JSON = DOCS / "survey.json"

LAYERS: dict[str, dict] = {
    "models": {
        "header": ["Family", "Maker", "Sizes", "License", "Context", "Notes"],
        "columns": [
            ("Family", lambda e: link(e["name"], e["__filename"])),
            ("Maker", lambda e: e.get("maker", "_stub_")),
            ("Sizes", lambda e: ", ".join(e.get("variants", [])) or "_stub_"),
            ("License", lambda e: e.get("license", "_stub_")),
            ("Context", lambda e: ctx_str(e.get("context_window"))),
            ("Notes", lambda e: e.get("notes", "_stub_") or "_stub_"),
        ],
        "preamble": "One row per family. Click through for variant details.",
    },
    "runtimes": {
        "header": ["Runtime", "License", "Formats", "API", "Hardware", "Notes"],
        "columns": [
            ("Runtime", lambda e: link(e["name"], e["__filename"])),
            ("License", lambda e: e.get("license", "_stub_")),
            ("Formats", lambda e: ", ".join(e.get("formats", [])) or "_stub_"),
            ("API", lambda e: "OpenAI-compat" if e.get("api_openai_compat") else "_stub_"),
            ("Hardware", lambda e: ", ".join(e.get("gpu_backends", [])) or "_stub_"),
            ("Notes", lambda e: e.get("notes", "_stub_") or "_stub_"),
        ],
        "preamble": None,
    },
    "frameworks": {
        "header": ["Framework", "License", "Language", "MCP", "Programming Model", "Notes"],
        "columns": [
            ("Framework", lambda e: link(e["name"], e["__filename"])),
            ("License", lambda e: e.get("license", "_stub_")),
            ("Language", lambda e: e.get("language", "_stub_")),
            ("MCP", lambda e: e.get("supports_mcp", "_stub_")),
            ("Programming Model", lambda e: e.get("programming_model", "_stub_")),
            ("Notes", lambda e: e.get("notes", "_stub_") or "_stub_"),
        ],
        "preamble": None,
    },
    "applications": {
        "header": ["Application", "Maker", "License", "Interfaces", "Focus", "Notes"],
        "columns": [
            ("Application", lambda e: link(e["name"], e["__filename"])),
            ("Maker", lambda e: e.get("maker", "_stub_")),
            ("License", lambda e: e.get("license", "_stub_")),
            ("Interfaces", lambda e: ", ".join(e.get("interfaces", [])) or "_stub_"),
            ("Focus", lambda e: e.get("focus", "_stub_") or "_stub_"),
            ("Notes", lambda e: e.get("notes", "_stub_") or "_stub_"),
        ],
        "preamble": (
            "Finished, installable open-source AI products that compose the stack "
            "(models + runtimes + framework patterns + MCP). One row per application. "
            "Distinct from [frameworks](../frameworks/INDEX.md) (libraries you build with) "
            'and from "agent" as a general concept (see [GLOSSARY](../GLOSSARY.md#agent)).\n\n'
            "Current entries are agentic coding/general-purpose applications. Other application "
            "categories (chat UIs, evaluation tools, fine-tuning tools) may be added later."
        ),
    },
    "mcp-servers": {
        "header": ["Server", "Capability", "License", "Transport", "Notes"],
        "columns": [
            ("Server", lambda e: link(e["name"], e["__filename"])),
            ("Capability", lambda e: e.get("name", "_stub_")),
            ("License", lambda e: e.get("license", "_stub_") or e.get("license_category", "_stub_")),
            ("Transport", lambda e: e.get("transport", "_stub_")),
            ("Notes", lambda e: e.get("notes", "_stub_") or "_stub_"),
        ],
        "preamble": (
            "One row per category. Each entry covers notable implementations within that category. "
            "Transport column reflects the dominant transport across the named implementations."
        ),
    },
    "techniques": {
        "header": ["Technique", "Problem", "Notes"],
        "columns": [
            ("Technique", lambda e: link(e["name"], e["__filename"])),
            ("Problem", lambda e: e.get("problem", "_stub_")),
            ("Notes", lambda e: e.get("notes", "_stub_") or "_stub_"),
        ],
        "preamble": None,
    },
}


# ---------------------------------------------------------------------------
# Frontmatter parsing
# ---------------------------------------------------------------------------

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)


def parse_frontmatter(text: str) -> dict | None:
    """Parse a YAML frontmatter block. Tolerant of minor formatting."""
    m = FRONTMATTER_RE.match(text)
    if not m:
        return None
    raw = m.group(1)
    # Use the stdlib? No — pyyaml is optional. Write a tiny parser sufficient
    # for our schema (no nested dicts, no anchors).
    try:
        import yaml  # type: ignore

        return yaml.safe_load(raw)
    except ImportError:
        return _tiny_yaml(raw)


def _tiny_yaml(raw: str) -> dict:
    """Minimal YAML for our flat schema. Handles strings, ints, bools, lists."""
    out: dict = {}
    current_key: str | None = None
    current_list: list | None = None
    for line in raw.splitlines():
        if not line.strip() or line.startswith("#"):
            continue
        if line.startswith(" ") and current_list is not None:
            current_list.append(_parse_value(line.strip().lstrip("- ").strip()))
            continue
        if ":" not in line:
            continue
        key, _, value = line.partition(":")
        key = key.strip()
        value = value.strip()
        if not value:
            current_key = key
            current_list = []
            out[key] = current_list
            continue
        if value.startswith("[") and value.endswith("]"):
            inner = value[1:-1]
            out[key] = [_parse_value(x.strip()) for x in _split_csv(inner)]
        else:
            out[key] = _parse_value(value)
        current_key = None
        current_list = None
    return out


def _parse_value(v: str):
    v = v.strip().rstrip(",")
    if v.startswith('"') and v.endswith('"'):
        return v[1:-1]
    if v.startswith("'") and v.endswith("'"):
        return v[1:-1]
    if v.lower() == "true":
        return True
    if v.lower() == "false":
        return False
    if v.lower() in ("null", "none", "~"):
        return None
    try:
        return int(v)
    except ValueError:
        pass
    try:
        return float(v)
    except ValueError:
        pass
    return v


def _split_csv(s: str) -> list[str]:
    out: list[str] = []
    buf = []
    depth = 0
    for ch in s:
        if ch in "[(":
            depth += 1
        elif ch in "])":
            depth -= 1
        if ch == "," and depth == 0:
            out.append("".join(buf))
            buf = []
        else:
            buf.append(ch)
    if buf:
        out.append("".join(buf))
    return out


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def link(name: str, filename: str) -> str:
    return f"[{name}]({filename})"


def ctx_str(n) -> str:
    if not n:
        return "_stub_"
    try:
        n = int(n)
    except (ValueError, TypeError):
        return str(n)
    if n >= 1_000_000:
        return f"{n // 1000}K"
    if n >= 1000:
        return f"{n // 1000}K"
    return str(n)


def load_layer(layer: str) -> tuple[list[dict], list[str]]:
    """Return (entries_with_frontmatter, list_of_files_missing_frontmatter)."""
    out = []
    missing = []
    layer_dir = DOCS / layer
    for path in sorted(layer_dir.glob("*.md")):
        if path.name in ("TEMPLATE.md", "INDEX.md"):
            continue
        text = path.read_text()
        fm = parse_frontmatter(text)
        if not fm:
            missing.append(path.name)
            continue
        fm["__filename"] = path.name
        fm["__layer"] = layer
        out.append(fm)
    return out, missing


def render_index(layer: str, entries: list[dict]) -> str:
    cfg = LAYERS[layer]
    layer_title = layer.replace("-", " ").title().replace("Mcp", "MCP")
    lines = [f"# {layer_title} — Index", ""]
    if cfg["preamble"]:
        lines.append(cfg["preamble"])
        lines.append("")
    lines.append("| " + " | ".join(cfg["header"]) + " |")
    lines.append("|" + "|".join(["---"] * len(cfg["header"])) + "|")
    if not entries:
        lines.append("| " + " | ".join(["_populate as entries are added_"] + ["" for _ in cfg["header"][1:]]) + " |")
    else:
        for entry in entries:
            row = [fn(entry) for _, fn in cfg["columns"]]
            lines.append("| " + " | ".join(row) + " |")
    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main(check_only: bool, force: bool) -> int:
    all_entities: list[dict] = []
    changed: list[Path] = []
    incomplete_layers: list[str] = []
    for layer in LAYERS:
        entries, missing = load_layer(layer)
        if missing:
            incomplete_layers.append(f"{layer} ({len(missing)} missing: {', '.join(missing[:3])}{'...' if len(missing) > 3 else ''})")
        all_entities.extend(entries)
        index_path = DOCS / layer / "INDEX.md"
        new_content = render_index(layer, entries)
        old_content = index_path.read_text() if index_path.exists() else ""
        if new_content != old_content:
            changed.append(index_path)

    if incomplete_layers and not force:
        print("Refusing to write INDEXes — some entities lack frontmatter.")
        print("This would drop their rows from INDEX. Migrate first, or pass --force.")
        for layer_msg in incomplete_layers:
            print(f"  - {layer_msg}")
        return 2

    if not check_only:
        for index_path in changed:
            layer = index_path.parent.name
            entries, _ = load_layer(layer)
            index_path.write_text(render_index(layer, entries))

    # Dump survey.json
    survey_payload = {
        "version": 1,
        "generated_from": "docs/open/{layer}/*.md frontmatter",
        "layers": LAYERS_PUBLIC,
        "entities": [
            {k: v for k, v in e.items() if not k.startswith("__")}
            | {"layer": e["__layer"], "filename": e["__filename"]}
            for e in all_entities
        ],
    }
    new_json = json.dumps(survey_payload, indent=2, sort_keys=True) + "\n"
    old_json = SURVEY_JSON.read_text() if SURVEY_JSON.exists() else ""
    if new_json != old_json:
        changed.append(SURVEY_JSON)
        if not check_only:
            SURVEY_JSON.write_text(new_json)

    if check_only and changed:
        for p in changed:
            print(f"would change: {p.relative_to(DOCS.parent.parent)}")
        return 1
    for p in changed:
        print(f"wrote: {p.relative_to(DOCS.parent.parent)}")
    print(f"total entities: {len(all_entities)}")
    return 0


LAYERS_PUBLIC = list(LAYERS.keys())


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="Exit non-zero if anything would change.")
    ap.add_argument("--force", action="store_true", help="Write INDEXes even if some entities lack frontmatter (drops their rows).")
    args = ap.parse_args()
    sys.exit(main(check_only=args.check, force=args.force))
