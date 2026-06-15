# Data Audit Log

Record of structural and accuracy audits run against the survey. Goal: trust the data enough to trust the picker's output.

Last audit run: 2026-06-15.

## How to re-audit

```bash
# Schema correctness (required fields, controlled vocab, types, dates, URLs)
python3 scripts/validate.py

# Derived files in sync with frontmatter
python3 scripts/regen.py --check

# Hardware-tier monotonicity (small variants imply larger tiers)
python3 scripts/query.py "
  SELECT name, (SELECT GROUP_CONCAT(value, ',') FROM json_each(hardware_tiers)) AS tiers
  FROM entities WHERE layer='models' ORDER BY name
"

# Dead URL check
python3 scripts/query.py "SELECT layer, name, url FROM entities" | \
  tail -n +2 | while IFS=$'\t' read -r layer name url; do
    code=$(curl -s -o /dev/null -w "%{http_code}" --max-time 8 "$url")
    [ "$code" != "200" ] && [ "$code" != "301" ] && [ "$code" != "302" ] && \
      echo "$code  $layer/$name  $url"
  done

# License vs license_category alignment
python3 scripts/query.py "
  SELECT name, license, license_category, layer FROM entities
  WHERE (license LIKE '%Apache%' AND license_category != 'apache-2.0')
     OR (license = 'MIT' AND license_category != 'mit')
     OR (license LIKE '%AGPL%' AND license_category NOT IN ('source-available'))
     OR (license LIKE '%CC-BY-NC%' AND license_category NOT IN ('source-available'))
     OR (license LIKE '%Llama%' AND license_category != 'custom-permissive')
"

# Field-completeness per layer (NULL/empty in required fields → bug)
python3 -c "
import sqlite3
conn = sqlite3.connect('docs/open/survey.sqlite')
cols = [r[1] for r in conn.execute('PRAGMA table_info(entities)')]
for layer in ['models','runtimes','frameworks','applications','mcp-servers','techniques']:
    total = conn.execute('SELECT COUNT(*) FROM entities WHERE layer=?', (layer,)).fetchone()[0]
    for col in cols:
        if col in ('layer','extras'): continue
        n = conn.execute(f\"SELECT COUNT(*) FROM entities WHERE layer=? AND ({col} IS NULL OR {col}='' OR {col}='[]')\", (layer,)).fetchone()[0]
        if 0 < n < total:
            print(f'  {layer}.{col}: {n}/{total} missing')
"
```

## Audits run on 2026-06-15

### Verified clean

| Check | Result |
|---|---|
| Schema: required fields, vocab, types, dates, URLs | 85/85 clean |
| Frontmatter ↔ INDEX.md / survey.json sync | clean (`regen.py --check` exits 0) |
| `license` text matches `license_category` bucket | 0 mismatches |
| `params_total` matches largest variant in `variants` list (regex match) | 0 real mismatches (false positives explained: DBRX/DeepSeek flagship variants are named without "XB" suffix) |
| Non-active status entries (`archived`, `deprecated`, `borderline`) justified in `notes` | 10/10 documented |
| Field-completeness gaps explained by schema optionality | confirmed (e.g. `params_active` only on `has_moe=true`) |
| Modality claims (`vision`) verified to family-level | 6/6 verified |
| Gated bool aligned with first-download experience | acceptable at family granularity |

### Fixed

| Issue | Affected | Fix |
|---|---|---|
| hardware_tiers monotonicity violations | Granite, OLMo, SmolLM, StarCoder2, Yi | Added missing larger tiers (small variant in family ⇒ larger tiers fit too) |
| Dead URLs in 404 reference paths | mcp-servers Database, Web Search | Repointed to `modelcontextprotocol/servers-archived` (current canonical archive) |
| Missing small variants → hardware_tiers undercounted | Nemotron, Hunyuan | Added Nemotron-Mini-4B / Nemotron-3-Nano-4B; added Hunyuan-0.5B/1.8B/4B/7B dense line; expanded hardware_tiers from `['24gb+']` to full range |

### MCP claim verification

| Claim | Result | Source verified |
|---|---|---|
| vLLM native MCP | ✓ | `vllm.entrypoints.mcp` confirmed in docs |
| Jan native MCP | ✓ | README "MCP integration for agentic capabilities" |
| LM Studio native MCP | ✓ | Lives in v0.3.17+; `/api/v1/chat` MCP host docs |
| Text Generation WebUI native MCP | ✓ | README "MCP servers are also supported" |
| KoboldCpp native MCP | ✓ | Wiki documents `--mcpfile` since v1.106 (not in README) |
| AutoGen / BeeAI / CrewAI / Pydantic AI / Smolagents / agno / mcp-agent native | ✓ all | README MCP mentions cross-verified |
| OpenCode / OpenHands / Continue native (zero README MCP mentions) | ✓ all | Verified via docs sites — README is marketing front, MCP lives in docs |

Lesson learned: a "no MCP in README" grep result is **not** sufficient to disprove a native MCP claim. Check the docs site, wiki, and release notes too.

## Known limitations (accepted, not bugs)

1. **Family-level fields** (`gated`, `context_window`, `params_total`) cannot perfectly represent variant-level diversity. E.g., Mistral-7B is ungated but Mistral-Large-Instruct-2407 is gated under MRL — the family `gated: false` reflects the canonical first-download experience, not every variant. Document this in the per-entity prose.

2. **`hardware_tiers` is "at least one variant fits"**, not "every variant fits." That's what the picker users intuitively want — "what families have something I can run?" — but if you're specifically asking about the flagship variant, query its variant string and consult the per-entity §4 Hardware Requirements prose.

3. **`license` text empty for `mcp-servers`** is intentional — categories cover diverse implementations with diverse licenses. The `license_category` field represents the dominant license category of leading implementations in the category.

4. **`best_for` is family-level intent**, not benchmark-derived. The Pass D `Documented Strengths` section is the place to look for concrete benchmark numbers.

## Not yet audited

- `best_for` tags against Pass D benchmarks per entity (would catch e.g. "coding-tagged but no documented coding strength")
- Recent project re-licensing (post-2026-06-14)
- New entities to add that emerged after 2026-06-14
- Cross-layer compatibility (which model loads on which runtime, beyond the Family-level `formats` hint)

When you re-verify a section, bump the `last_verified` date on the affected entity and `regen.py`. When that's done widely, update the "Last audit run" date at the top of this file.
