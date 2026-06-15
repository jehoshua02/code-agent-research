#!/usr/bin/env python3
"""
Stack picker. Filters docs/open/survey.json by your constraints and prints
matching entities grouped by layer. Optionally suggests a concrete stack.

Examples:
    # Show everything that fits a 3070 (8 GB) for agentic coding
    python3 scripts/pick.py --hardware 8gb --task coding

    # Restrict to truly-open licenses (Apache 2.0 or MIT) and MCP-native
    python3 scripts/pick.py --task coding --license apache-2.0 --license mit --mcp native

    # Mac M-series user, looking for a research stack
    python3 scripts/pick.py --hardware mac-only --task research --platform macos

    # Print a suggested concrete combination (top 1 per layer)
    python3 scripts/pick.py --hardware 24gb --task data --suggest

    # JSON dump for piping to jq / sqlite
    python3 scripts/pick.py --hardware 16gb --format json | jq '.applications[].name'

Filters compose with AND logic across flag types; multi-valued flags (e.g.
--license apache-2.0 --license mit) compose with OR.
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path

SURVEY = Path(__file__).resolve().parent.parent / "docs" / "open" / "survey.json"


def load_survey() -> dict:
    if not SURVEY.exists():
        sys.exit(
            f"survey.json not found at {SURVEY}. Run `python3 scripts/regen.py` first."
        )
    return json.loads(SURVEY.read_text())


WILDCARD_VALUES = {"any"}


def matches(entity: dict, key: str, want: set[str], strict_list: bool = False) -> bool:
    """Return True iff entity[key] overlaps `want`.

    `strict_list=True` means entity[key] must be a list; otherwise we accept
    scalars and check for equality. A value in WILDCARD_VALUES (e.g. "any" for
    hardware_tiers) matches all queried values — used for hardware-agnostic
    applications."""
    if not want:
        return True
    value = entity.get(key)
    if value is None:
        return False
    if isinstance(value, list):
        if any(v in WILDCARD_VALUES for v in value):
            return True
        return any(v in want for v in value)
    if value in WILDCARD_VALUES:
        return True
    return value in want


def filter_entities(survey: dict, args) -> dict[str, list[dict]]:
    """Apply filters to every layer and return matches grouped by layer."""
    out: dict[str, list[dict]] = defaultdict(list)
    for entity in survey["entities"]:
        layer = entity["layer"]

        # Universal filters
        if args.license:
            if not matches(entity, "license_category", set(args.license)):
                continue
        if args.status:
            if not matches(entity, "status", set(args.status)):
                continue

        # Per-layer filters
        if layer == "models":
            if args.hardware and not matches(entity, "hardware_tiers", set(args.hardware)):
                continue
            if args.task and not matches(entity, "best_for", set(args.task)):
                continue
            if args.modality and not matches(entity, "modalities", set(args.modality)):
                continue

        elif layer == "runtimes":
            if args.platform and not matches(entity, "platforms", set(args.platform)):
                continue
            if args.gpu and not matches(entity, "gpu_backends", set(args.gpu)):
                continue
            if args.mcp and not matches(entity, "supports_mcp", set(args.mcp)):
                continue
            if args.openai_compat and not entity.get("api_openai_compat"):
                continue

        elif layer == "frameworks":
            if args.language and not matches(entity, "language", set(args.language)):
                continue
            if args.mcp and not matches(entity, "supports_mcp", set(args.mcp)):
                continue
            if args.task and not matches(entity, "best_for", set(args.task)):
                continue
            if args.programming_model and not matches(
                entity, "programming_model", set(args.programming_model)
            ):
                continue

        elif layer == "applications":
            if args.hardware and not matches(entity, "hardware_tiers", set(args.hardware)):
                continue
            if args.task and not matches(entity, "best_for", set(args.task)):
                continue
            if args.mcp and not matches(entity, "supports_mcp", set(args.mcp)):
                continue
            if args.interface and not matches(entity, "interfaces", set(args.interface)):
                continue
            if args.focus and not matches(entity, "focus", set(args.focus)):
                continue

        elif layer == "mcp-servers":
            if args.transport and not matches(entity, "transport", set(args.transport)):
                continue
            if args.auth and not matches(entity, "auth", set(args.auth)):
                continue
            if args.task and not matches(entity, "best_for", set(args.task)):
                continue
            if args.anthropic_ref and not entity.get("has_anthropic_reference"):
                continue

        elif layer == "techniques":
            if args.applies_at and not matches(entity, "applies_at", set(args.applies_at)):
                continue
            if args.task and not matches(entity, "best_for", set(args.task)):
                continue

        out[layer].append(entity)
    return dict(out)


# ---------------------------------------------------------------------------
# Output formats
# ---------------------------------------------------------------------------


LAYER_ORDER = ["models", "runtimes", "frameworks", "applications", "mcp-servers", "techniques"]


def print_human(filtered: dict[str, list[dict]], suggest: bool):
    """Pretty terminal output."""
    for layer in LAYER_ORDER:
        entries = filtered.get(layer, [])
        print(f"\n## {layer} ({len(entries)} matches)")
        if not entries:
            print("  _no matches_")
            continue
        # Sort: prefer active over borderline over archived, then alpha
        rank = {"active": 0, "borderline": 1, "deprecated": 2, "archived": 3}
        entries.sort(key=lambda e: (rank.get(e.get("status", "active"), 9), e.get("name", "")))
        for e in entries:
            tags = []
            for k in ("license_category", "language", "interfaces", "supports_mcp", "focus"):
                v = e.get(k)
                if v in (None, "", []):
                    continue
                if isinstance(v, list):
                    tags.append(",".join(v))
                else:
                    tags.append(str(v))
            tags_str = " | ".join(tags) if tags else ""
            status = e.get("status", "active")
            status_marker = "" if status == "active" else f" [{status}]"
            print(f"  - {e['name']}{status_marker} — {tags_str}")

    if suggest:
        print("\n## suggested stack (top match per layer, active only)")
        for layer in LAYER_ORDER:
            entries = [e for e in filtered.get(layer, []) if e.get("status") == "active"]
            if not entries:
                continue
            pick = entries[0]  # already sorted in print_human; re-pick if needed
            entries.sort(key=lambda e: e.get("name", ""))
            print(f"  - {layer}: {pick['name']}")


def print_json(filtered: dict[str, list[dict]]):
    print(json.dumps(filtered, indent=2, sort_keys=True))


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def parse_args() -> argparse.Namespace:
    ap = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    # Universal
    ap.add_argument("--license", action="append", default=[],
                    help="license_category — apache-2.0 | mit | custom-permissive | source-available | proprietary | n/a (repeatable)")
    ap.add_argument("--status", action="append", default=[],
                    help="active | borderline | deprecated | archived (repeatable)")
    # Models + Applications
    ap.add_argument("--hardware", action="append", default=[],
                    help="8gb | 12gb | 16gb | 24gb | 24gb+ | any | mac-only | cpu-only (repeatable)")
    ap.add_argument("--task", action="append", default=[],
                    help="coding | research | writing | automation | data (repeatable)")
    # Models
    ap.add_argument("--modality", action="append", default=[],
                    help="text | vision | audio (repeatable, models only)")
    # Runtimes
    ap.add_argument("--platform", action="append", default=[],
                    help="linux | macos | windows | wsl2 (repeatable, runtimes only)")
    ap.add_argument("--gpu", action="append", default=[],
                    help="cuda | rocm | metal | cpu | vulkan | ... (repeatable, runtimes only)")
    ap.add_argument("--openai-compat", action="store_true",
                    help="filter runtimes to OpenAI-compatible API")
    # Frameworks + Applications + Runtimes
    ap.add_argument("--mcp", action="append", default=[],
                    help="native | adapter | none (repeatable)")
    # Frameworks
    ap.add_argument("--language", action="append", default=[],
                    help="Python | TypeScript | Go | Rust | ... (repeatable)")
    ap.add_argument("--programming-model", action="append", default=[],
                    help="graph | imperative | declarative | role-based | code-emitting | composable | constraint-based (repeatable)")
    # Applications
    ap.add_argument("--interface", action="append", default=[],
                    help="cli | tui | ide-plugin | web-ui | mobile | desktop | api | browser-extension (repeatable)")
    ap.add_argument("--focus", action="append", default=[],
                    help="agentic-coding | general-agent | code-execution | chat-ui | personal-assistant | research | project-workflow (repeatable)")
    # MCP servers
    ap.add_argument("--transport", action="append", default=[],
                    help="stdio | sse | http (repeatable)")
    ap.add_argument("--auth", action="append", default=[],
                    help="none | api-key | oauth (repeatable)")
    ap.add_argument("--anthropic-ref", action="store_true",
                    help="filter mcp-servers to Anthropic reference set")
    # Techniques
    ap.add_argument("--applies-at", action="append", default=[],
                    help="model | runtime | framework | agent (repeatable)")

    # Output
    ap.add_argument("--format", choices=["human", "json"], default="human",
                    help="output format")
    ap.add_argument("--suggest", action="store_true",
                    help="print one suggested pick per layer at the end")
    return ap.parse_args()


def main() -> int:
    args = parse_args()
    survey = load_survey()
    filtered = filter_entities(survey, args)

    # By default, exclude archived/deprecated from human view unless asked
    if args.format == "human" and not args.status:
        for layer in filtered:
            filtered[layer] = [
                e for e in filtered[layer] if e.get("status") not in ("archived", "deprecated")
            ]

    if args.format == "json":
        print_json(filtered)
    else:
        print_human(filtered, args.suggest)
    return 0


if __name__ == "__main__":
    sys.exit(main())
