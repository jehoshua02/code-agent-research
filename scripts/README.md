# Scripts

Tools for maintaining the survey's structured data layer. The schema lives at [`../docs/open/SCHEMA.md`](../docs/open/SCHEMA.md).

## Quick reference

```bash
# Install dependency
pip install pyyaml

# Validate every entity's YAML frontmatter
python3 scripts/validate.py

# Regenerate INDEX.md tables and survey.json from frontmatter
python3 scripts/regen.py

# Dry-run (used by CI) — exits non-zero if anything would change
python3 scripts/regen.py --check

# Force regen even if some entities lack frontmatter (drops their rows)
python3 scripts/regen.py --force
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
3. **`.github/workflows/survey-schema.yml`** — runs both on every PR touching `docs/open/**` or `scripts/**`. Catches drift you'd otherwise notice only on next manual run.

## Safety notes

- `regen.py` refuses to write if any entity lacks frontmatter (would silently drop rows from INDEX). Migrate first, or pass `--force` only when you intentionally want to migrate partial state.
- `regen.py --check` never writes — safe to run anywhere.
- The YAML parser falls back to a tiny built-in if PyYAML isn't installed, so both scripts work in minimal environments.

## Dependencies

- Python 3.10+
- `pyyaml` (optional but recommended; falls back to tiny built-in parser otherwise)
