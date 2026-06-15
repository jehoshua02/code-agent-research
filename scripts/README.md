# Scripts

Tools for maintaining and querying the survey's structured data layer. The schema lives at [`../docs/open/SCHEMA.md`](../docs/open/SCHEMA.md).

## Quick reference

```bash
# Install dependency
pip install pyyaml

# Validate every entity's YAML frontmatter
python3 scripts/validate.py

# Regenerate INDEX.md tables and survey.json from frontmatter
python3 scripts/regen.py

# Dry-run — exits non-zero if anything would change
python3 scripts/regen.py --check

# Force regen even if some entities lack frontmatter (drops their rows)
python3 scripts/regen.py --force

# Build the SQLite query cache from survey.json (for ad-hoc SQL)
python3 scripts/build-sqlite.py

# Run raw SQL via the query wrapper (auto-builds sqlite cache if stale)
python3 scripts/query.py "SELECT name FROM entities WHERE layer='models' AND context_window >= 256000"

# Different output formats
python3 scripts/query.py "SELECT layer, COUNT(*) FROM entities GROUP BY layer" --format csv
python3 scripts/query.py "SELECT name FROM entities WHERE layer='frameworks'" --format names

# Or just use sqlite3 CLI directly
sqlite3 docs/open/survey.sqlite "SELECT name FROM entities WHERE layer='models' AND context_window >= 256000"

# Or open an interactive shell
python3 scripts/query.py --shell
```

## When to run what

| You did | Run this | Then |
|---|---|---|
| Added a new entity file | `validate.py`, then `regen.py` | Commit entity + INDEX + survey.json together |
| Edited an existing entity's frontmatter | `validate.py`, then `regen.py` | Commit entity + INDEX + survey.json together |
| Only edited prose | nothing | Commit the prose edit |
| Wanted to confirm everything is clean | `validate.py && python3 scripts/regen.py --check` | Both should exit 0 |

## How it fits together

1. **`validate.py`** — checks each entity's frontmatter against the schema. Required fields, controlled vocab, types, dates, URLs. Fails per file with a clear error list.
2. **`regen.py`** — reads frontmatter, regenerates each layer's `INDEX.md` and `docs/open/survey.json` from truth. INDEXes are derived; don't edit them by hand.
3. **`build-sqlite.py`** — reads `survey.json`, builds `docs/open/survey.sqlite` (gitignored — a query cache, not source of truth).
4. **`query.py`** — thin wrapper over `survey.sqlite`. Takes SQL on the command line, in a file, or on stdin; auto-builds the cache if missing/stale; formats output as tsv (default), csv, json, or names. Optional `--shell` drops into the interactive `sqlite3` CLI. See [`docs/open/QUERIES.md`](../docs/open/QUERIES.md) for patterns and [`examples/`](examples/) for end-to-end walkthroughs.

CI is not wired up. Discipline is local — run validate + regen before committing.

## Worked examples

[`scripts/examples/`](examples/) contains end-to-end demos of using `query.py` on real scenarios. Read these before writing your own queries — they show the queries, the reasoning between them, and the recommendation that falls out.

| File | Scenario |
|---|---|
| [`examples/query-small-vram-coding.md`](examples/query-small-vram-coding.md) | 8 GB GPU, agentic coding, MCP-required, Apache 2.0 / MIT only |

## Safety notes

- `regen.py` refuses to write if any entity lacks frontmatter (would silently drop rows from INDEX). Migrate first, or pass `--force` only when you intentionally want to migrate partial state.
- `regen.py --check` never writes — safe to run anywhere.
- The YAML parser falls back to a tiny built-in if PyYAML isn't installed, so both scripts work in minimal environments.

## Dependencies

- Python 3.10+
- `pyyaml` (optional but recommended; falls back to tiny built-in parser otherwise)
