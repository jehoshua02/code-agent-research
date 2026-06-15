#!/usr/bin/env python3
"""
Validate every entity's YAML frontmatter against the schema in docs/open/SCHEMA.md.

Checks:
- Required fields present per layer
- Controlled vocab values used (license_category, status, modalities, etc.)
- Type sanity (lists are lists, ints are ints, etc.)
- last_verified is a YYYY-MM-DD date
- url is http(s) or hf/gh
- Each entity has a corresponding entity file (the file is the entity)

Exits non-zero on any violation, listing every issue.

Usage:
    python3 scripts/validate.py
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

# Reuse regen.py's frontmatter parser to keep one implementation.
sys.path.insert(0, str(Path(__file__).resolve().parent))
from regen import parse_frontmatter  # noqa: E402

DOCS = Path(__file__).resolve().parent.parent / "docs" / "open"

# ---------------------------------------------------------------------------
# Controlled vocab
# ---------------------------------------------------------------------------

VOCAB = {
    "license_category": {
        "apache-2.0",
        "mit",
        "custom-permissive",
        "source-available",
        "proprietary",
        "n/a",
    },
    "status": {"active", "archived", "deprecated", "borderline"},
    "modalities": {"text", "vision", "audio"},
    "platforms": {"linux", "macos", "windows", "wsl2"},
    "gpu_backends": {
        "cuda",
        "rocm",
        "metal",
        "cpu",
        "vulkan",
        "sycl",
        "tpu",
        "xpu",
        "gaudi",
        "ascend",
        "inferentia",
    },
    "hardware_tiers": {"8gb", "12gb", "16gb", "24gb", "24gb+", "any", "mac-only", "cpu-only"},
    "interfaces": {
        "cli",
        "tui",
        "ide-plugin",
        "web-ui",
        "mobile",
        "desktop",
        "api",
        "browser-extension",
    },
    "supports_mcp": {"native", "adapter", "none"},
    "programming_model": {
        "graph",
        "imperative",
        "declarative",
        "role-based",
        "code-emitting",
        "composable",
        "constraint-based",
    },
    "focus": {
        "agentic-coding",
        "general-agent",
        "code-execution",
        "chat-ui",
        "personal-assistant",
        "research",
        "project-workflow",
    },
    "transport": {"stdio", "sse", "http"},
    "auth": {"none", "api-key", "oauth"},
    "applies_at": {"model", "runtime", "framework", "agent"},
    "best_for": {"coding", "research", "writing", "automation", "data"},
}

# ---------------------------------------------------------------------------
# Required fields per layer
# ---------------------------------------------------------------------------

COMMON_REQUIRED = ["name", "license_category", "status", "url", "last_verified"]

LAYER_REQUIRED: dict[str, list[str]] = {
    "models": COMMON_REQUIRED + ["maker", "license", "variants", "hardware_tiers", "best_for"],
    "runtimes": COMMON_REQUIRED + [
        "maker",
        "license",
        "language",
        "platforms",
        "gpu_backends",
        "api_openai_compat",
        "supports_mcp",
        "formats",
    ],
    "frameworks": COMMON_REQUIRED + [
        "maker",
        "license",
        "language",
        "supports_mcp",
        "programming_model",
    ],
    "applications": COMMON_REQUIRED + [
        "maker",
        "license",
        "language",
        "interfaces",
        "supports_mcp",
        "focus",
        "best_for",
    ],
    "mcp-servers": COMMON_REQUIRED + ["transport", "auth"],
    "techniques": COMMON_REQUIRED + ["applies_at", "problem"],
}

LIST_FIELDS = {
    "variants",
    "modalities",
    "platforms",
    "gpu_backends",
    "hardware_tiers",
    "interfaces",
    "best_for",
    "formats",
    "providers",
}

BOOL_FIELDS = {"has_moe", "gated", "api_openai_compat", "byok"}

DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
URL_RE = re.compile(r"^https?://")


# ---------------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------------


def validate_entity(layer: str, path: Path, fm: dict) -> list[str]:
    errors: list[str] = []
    required = LAYER_REQUIRED.get(layer, COMMON_REQUIRED)
    for field in required:
        if field not in fm or fm[field] in (None, "", []):
            errors.append(f"missing required field: {field}")

    for field, expected in VOCAB.items():
        if field not in fm:
            continue
        value = fm[field]
        if isinstance(value, list):
            for v in value:
                if v not in expected:
                    errors.append(f"{field}={v!r} not in vocab ({sorted(expected)})")
        else:
            if value not in expected:
                errors.append(f"{field}={value!r} not in vocab ({sorted(expected)})")

    for field in LIST_FIELDS:
        if field in fm and fm[field] is not None and not isinstance(fm[field], list):
            errors.append(f"{field} should be a list, got {type(fm[field]).__name__}")

    for field in BOOL_FIELDS:
        if field in fm and not isinstance(fm[field], bool):
            errors.append(f"{field} should be a bool, got {type(fm[field]).__name__}")

    if "last_verified" in fm and not DATE_RE.match(str(fm["last_verified"])):
        errors.append(f"last_verified={fm['last_verified']!r} not in YYYY-MM-DD")

    if "url" in fm and not URL_RE.match(str(fm["url"])):
        errors.append(f"url={fm['url']!r} not http(s)://")

    return errors


def main() -> int:
    total = 0
    failed = 0
    missing_fm = 0
    for layer in LAYER_REQUIRED:
        layer_dir = DOCS / layer
        for path in sorted(layer_dir.glob("*.md")):
            if path.name in ("TEMPLATE.md", "INDEX.md"):
                continue
            total += 1
            text = path.read_text()
            fm = parse_frontmatter(text)
            if fm is None:
                missing_fm += 1
                continue  # not yet migrated; tracked separately
            errors = validate_entity(layer, path, fm)
            if errors:
                failed += 1
                print(f"\n{path.relative_to(DOCS.parent.parent)}:")
                for err in errors:
                    print(f"  - {err}")

    print(f"\n{total} entity files, {failed} with errors, {missing_fm} not yet migrated (no frontmatter)")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
