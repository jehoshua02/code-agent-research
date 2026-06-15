#!/usr/bin/env python3
"""
Build docs/open/survey.sqlite from docs/open/survey.json.

The SQLite file is a query cache, not source of truth. It's regenerable any
time and gitignored. Use it for ad-hoc questions that pick.py can't express —
arbitrary WHERE, joins-by-self, aggregates, sorts by any field.

Schema: one table `entities` with all common columns; list-typed frontmatter
fields are stored as JSON arrays (use SQLite's json_each / json_extract to
query them).

Usage:
    python3 scripts/build-sqlite.py
    sqlite3 docs/open/survey.sqlite "SELECT name FROM entities WHERE layer='models' AND license_category='mit'"

See docs/open/QUERIES.md for example SQL.
"""
from __future__ import annotations

import json
import sqlite3
import sys
from pathlib import Path

DOCS = Path(__file__).resolve().parent.parent / "docs" / "open"
SURVEY_JSON = DOCS / "survey.json"
SURVEY_SQLITE = DOCS / "survey.sqlite"

# Columns we surface as proper SQL columns. Everything else stays in `extras`
# as a JSON blob. Add a column here if you want indexed/typed access to a
# new field; it'll be added on next rebuild.
COLUMNS = [
    # (name, sql_type, json_type)
    ("layer", "TEXT", "scalar"),
    ("filename", "TEXT", "scalar"),
    ("name", "TEXT", "scalar"),
    ("maker", "TEXT", "scalar"),
    ("license", "TEXT", "scalar"),
    ("license_category", "TEXT", "scalar"),
    ("status", "TEXT", "scalar"),
    ("url", "TEXT", "scalar"),
    ("last_verified", "TEXT", "scalar"),
    ("language", "TEXT", "scalar"),
    ("focus", "TEXT", "scalar"),
    ("supports_mcp", "TEXT", "scalar"),
    ("programming_model", "TEXT", "scalar"),
    ("transport", "TEXT", "scalar"),
    ("auth", "TEXT", "scalar"),
    ("applies_at", "TEXT", "scalar"),
    ("api_openai_compat", "INTEGER", "bool"),  # SQLite has no real bool
    ("has_anthropic_reference", "INTEGER", "bool"),
    ("byok", "INTEGER", "bool"),
    ("gated", "INTEGER", "bool"),
    ("has_moe", "INTEGER", "bool"),
    ("context_window", "INTEGER", "scalar"),
    ("params_total", "TEXT", "scalar"),
    ("params_active", "TEXT", "scalar"),
    ("released", "TEXT", "scalar"),
    ("problem", "TEXT", "scalar"),
    ("notes", "TEXT", "scalar"),
    # List fields stored as JSON arrays
    ("variants", "TEXT", "json"),
    ("modalities", "TEXT", "json"),
    ("hardware_tiers", "TEXT", "json"),
    ("platforms", "TEXT", "json"),
    ("gpu_backends", "TEXT", "json"),
    ("formats", "TEXT", "json"),
    ("interfaces", "TEXT", "json"),
    ("providers", "TEXT", "json"),
    ("best_for", "TEXT", "json"),
]


def coerce(value, json_type: str):
    if value is None:
        return None
    if json_type == "bool":
        return 1 if value else 0
    if json_type == "json":
        if isinstance(value, list):
            return json.dumps(value)
        return None
    return value


def build():
    if not SURVEY_JSON.exists():
        sys.exit(f"Run `python3 scripts/regen.py` first — {SURVEY_JSON.name} missing.")

    survey = json.loads(SURVEY_JSON.read_text())
    SURVEY_SQLITE.unlink(missing_ok=True)

    conn = sqlite3.connect(SURVEY_SQLITE)
    cur = conn.cursor()

    col_defs = ", ".join(f"{n} {t}" for n, t, _ in COLUMNS)
    cur.execute(f"CREATE TABLE entities ({col_defs}, extras TEXT)")
    cur.execute("CREATE INDEX idx_layer ON entities(layer)")
    cur.execute("CREATE INDEX idx_status ON entities(status)")
    cur.execute("CREATE INDEX idx_license ON entities(license_category)")

    known = {n for n, _, _ in COLUMNS} | {"layer", "filename"}
    placeholders = ", ".join(["?"] * (len(COLUMNS) + 1))  # +1 for extras

    rows = []
    for e in survey["entities"]:
        row = [coerce(e.get(n), jt) for n, _, jt in COLUMNS]
        extras = {k: v for k, v in e.items() if k not in known}
        row.append(json.dumps(extras) if extras else None)
        rows.append(row)

    cols_sql = ", ".join(n for n, _, _ in COLUMNS) + ", extras"
    cur.executemany(f"INSERT INTO entities ({cols_sql}) VALUES ({placeholders})", rows)
    conn.commit()
    conn.close()

    print(f"wrote: {SURVEY_SQLITE.relative_to(DOCS.parent.parent)} ({len(rows)} rows)")


if __name__ == "__main__":
    build()
