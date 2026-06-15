#!/usr/bin/env python3
"""
Raw-SQL escape hatch over docs/open/survey.sqlite. Auto-builds the SQLite
cache from survey.json if missing or stale.

Use this when pick.py's flags don't cover what you want — arbitrary WHERE,
JOIN, GROUP BY, sort by any column, exclusion, NOT EXISTS, etc.

See docs/open/QUERIES.md for example patterns.

Usage:
    # Inline SQL
    python3 scripts/query.py "SELECT name FROM entities WHERE context_window >= 256000"

    # From a file
    python3 scripts/query.py --file my-query.sql

    # From stdin
    echo "SELECT layer, COUNT(*) FROM entities GROUP BY layer" | python3 scripts/query.py -

    # Different output formats
    python3 scripts/query.py "SELECT name, license_category FROM entities WHERE layer='models'" --format csv
    python3 scripts/query.py "SELECT * FROM entities WHERE layer='runtimes' LIMIT 1" --format json
    python3 scripts/query.py "SELECT name FROM entities WHERE layer='applications'" --format names

    # Open an interactive shell against the cache
    python3 scripts/query.py --shell
"""
from __future__ import annotations

import argparse
import csv
import json
import os
import sqlite3
import subprocess
import sys
from pathlib import Path

DOCS = Path(__file__).resolve().parent.parent / "docs" / "open"
SURVEY_JSON = DOCS / "survey.json"
SURVEY_SQLITE = DOCS / "survey.sqlite"
BUILD_SCRIPT = Path(__file__).resolve().parent / "build-sqlite.py"


def ensure_sqlite() -> None:
    if not SURVEY_JSON.exists():
        sys.exit(
            f"survey.json not found at {SURVEY_JSON}. "
            "Run `python3 scripts/regen.py` first."
        )
    if SURVEY_SQLITE.exists() and SURVEY_SQLITE.stat().st_mtime >= SURVEY_JSON.stat().st_mtime:
        return
    print(
        f"(building {SURVEY_SQLITE.name} from {SURVEY_JSON.name}...)",
        file=sys.stderr,
    )
    subprocess.check_call([sys.executable, str(BUILD_SCRIPT)])


def read_query(args) -> str:
    if args.file:
        return Path(args.file).read_text()
    if args.query == "-":
        return sys.stdin.read()
    return args.query


def format_tsv(cols: list[str], rows: list[tuple], header: bool):
    if header and cols:
        print("\t".join(cols))
    for row in rows:
        print("\t".join("" if v is None else str(v) for v in row))


def format_csv(cols: list[str], rows: list[tuple]):
    w = csv.writer(sys.stdout)
    if cols:
        w.writerow(cols)
    for row in rows:
        w.writerow(["" if v is None else v for v in row])


def format_json(cols: list[str], rows: list[tuple]):
    out = [{c: v for c, v in zip(cols, row)} for row in rows]
    print(json.dumps(out, indent=2, default=str))


def format_names(rows: list[tuple]):
    """One value per line — only sensible if you SELECT a single column."""
    for row in rows:
        for v in row:
            print("" if v is None else v)


def run(args) -> int:
    ensure_sqlite()
    if args.shell:
        # Drop into the sqlite3 CLI if available; else hint how to use Python.
        sqlite3_bin = os.environ.get("SQLITE3_BIN", "sqlite3")
        try:
            os.execvp(sqlite3_bin, [sqlite3_bin, str(SURVEY_SQLITE)])
        except FileNotFoundError:
            sys.exit(
                "sqlite3 CLI not found. Either install it or use:\n"
                "    python3 -c \"import sqlite3; "
                f"conn = sqlite3.connect('{SURVEY_SQLITE}'); ...\""
            )

    sql = read_query(args)
    if not sql.strip():
        sys.exit("No SQL provided. Pass a query as the positional arg, --file, or '-' for stdin.")

    conn = sqlite3.connect(SURVEY_SQLITE)
    try:
        cur = conn.execute(sql)
    except sqlite3.Error as e:
        sys.exit(f"SQL error: {e}")

    cols = [c[0] for c in cur.description] if cur.description else []
    rows = cur.fetchall()

    if args.format == "tsv":
        format_tsv(cols, rows, header=not args.no_header)
    elif args.format == "csv":
        format_csv(cols, rows)
    elif args.format == "json":
        format_json(cols, rows)
    elif args.format == "names":
        format_names(rows)

    if args.count:
        print(f"({len(rows)} rows)", file=sys.stderr)
    return 0


def parse_args() -> argparse.Namespace:
    ap = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    ap.add_argument(
        "query",
        nargs="?",
        default="",
        help="SQL string. Use '-' to read from stdin. See docs/open/QUERIES.md for patterns.",
    )
    ap.add_argument("--file", "-f", help="read SQL from a file")
    ap.add_argument(
        "--format",
        choices=["tsv", "csv", "json", "names"],
        default="tsv",
        help="output format (default: tsv)",
    )
    ap.add_argument("--no-header", action="store_true", help="suppress header row (tsv)")
    ap.add_argument("--count", action="store_true", help="print row count to stderr after results")
    ap.add_argument(
        "--shell",
        action="store_true",
        help="open the sqlite3 CLI against survey.sqlite (requires `sqlite3` binary in PATH)",
    )
    return ap.parse_args()


if __name__ == "__main__":
    sys.exit(run(parse_args()))
