# SQL query examples

`docs/open/survey.sqlite` is a build artifact — gitignored, regenerable any time from `survey.json`:

```bash
python3 scripts/regen.py        # update survey.json from frontmatter
python3 scripts/build-sqlite.py # build survey.sqlite from survey.json
```

Use it for ad-hoc questions that `pick.py` doesn't have flags for. The schema is one table `entities` with all common frontmatter fields as proper columns; list fields are stored as JSON arrays (use SQLite's `json_each` / `json_extract`).

## Connecting

```bash
sqlite3 docs/open/survey.sqlite          # CLI
```

```python
import sqlite3
conn = sqlite3.connect("docs/open/survey.sqlite")
```

Inspect the schema:

```sql
.schema entities          -- sqlite3 CLI
PRAGMA table_info(entities);
```

## Common patterns

### Filter on scalar columns

```sql
SELECT name FROM entities
WHERE layer = 'frameworks'
  AND license_category = 'apache-2.0'
  AND supports_mcp = 'native';
```

### Filter on list columns (JSON arrays)

```sql
-- Models supporting vision
SELECT name FROM entities
WHERE layer = 'models'
  AND EXISTS (
    SELECT 1 FROM json_each(entities.modalities)
    WHERE json_each.value = 'vision'
  );

-- Runtimes that target Apple Silicon Metal
SELECT name FROM entities
WHERE layer = 'runtimes'
  AND EXISTS (SELECT 1 FROM json_each(gpu_backends) WHERE value = 'metal');
```

### Filter on numeric columns

```sql
-- Models with native context >= 256K
SELECT name, context_window FROM entities
WHERE layer = 'models'
  AND context_window >= 256000
ORDER BY context_window DESC;
```

### Exclusion / NOT

```sql
-- All applications EXCEPT archived
SELECT name FROM entities
WHERE layer = 'applications'
  AND status != 'archived';

-- Models that are NOT gated
SELECT name FROM entities
WHERE layer = 'models'
  AND COALESCE(gated, 0) = 0;
```

### Aggregates / GROUP BY

```sql
-- How many entities per license category, per layer?
SELECT layer, license_category, COUNT(*) AS n
FROM entities
GROUP BY layer, license_category
ORDER BY layer, n DESC;

-- How many frameworks are MCP-native vs adapter vs none?
SELECT supports_mcp, COUNT(*) AS n
FROM entities
WHERE layer = 'frameworks'
GROUP BY supports_mcp;
```

### Sort on any field

```sql
-- Models ordered by context window
SELECT name, context_window FROM entities
WHERE layer = 'models'
ORDER BY context_window DESC NULLS LAST;
```

### Cross-layer (self-join via JSON)

The schema doesn't model relations across layers explicitly (no foreign keys between models and runtimes — each entity carries its own structured fields). You can still ask cross-layer questions with self-joins:

```sql
-- Find frameworks AND applications that are both MCP-native + Apache 2.0,
-- side by side
SELECT
  f.name AS framework,
  a.name AS application
FROM entities f
CROSS JOIN entities a
WHERE f.layer = 'frameworks'
  AND a.layer = 'applications'
  AND f.supports_mcp = 'native'
  AND a.supports_mcp = 'native'
  AND f.license_category = 'apache-2.0'
  AND a.license_category = 'apache-2.0';
```

For "model X works with runtime Y" compatibility queries, you'd need an explicit compatibility matrix — currently neither the frontmatter nor SQL captures that. The runtime's `formats` field plus the model's variant names give you a hint; for true compatibility, follow the prose in `models/<family>.md §6 Runtime Support`.

### Fields not in the column list (extras column)

If a field isn't surfaced as a column in `scripts/build-sqlite.py`, it's stored in the `extras` JSON blob:

```sql
SELECT name, json_extract(extras, '$.some_field') AS some_field
FROM entities
WHERE json_extract(extras, '$.some_field') IS NOT NULL;
```

To promote it to a real column, add a row to the `COLUMNS` list in `scripts/build-sqlite.py` and rebuild.

## Cheatsheet

| You want | Pattern |
|---|---|
| Filter by scalar | `WHERE field = 'value'` |
| Filter by list element | `WHERE EXISTS (SELECT 1 FROM json_each(field) WHERE value = 'x')` |
| Numeric comparison | `WHERE field >= 100000` |
| Order by any field | `ORDER BY field DESC NULLS LAST` |
| Count by group | `GROUP BY field` |
| Exclude rows | `WHERE field != 'x'` or `NOT EXISTS (...)` |
| Self-join across layers | `CROSS JOIN entities a` then filter both `f.layer` and `a.layer` |
| Custom field | `json_extract(extras, '$.fieldname')` |
