# Entity Frontmatter Schema

Every entity file has a YAML frontmatter block at the top with structured fields. Prose stays canonical; frontmatter is parseable for indexes, views, search, and downstream tools.

The regen script (`scripts/regen.py`) reads frontmatter and:

1. Regenerates each layer's `INDEX.md` from truth — INDEX columns are sourced from frontmatter, not hand-maintained.
2. Dumps a single `survey.json` for filter queries / SQLite / downstream tools.

If you edit an entity, only the frontmatter fields that change matter for the index — rerun the regen script and commit the diff.

## 1. Common fields (all layers)

```yaml
---
name: "Llama"                  # canonical display name
maker: "Meta"                  # org/person (informal OK)
license: "Llama Community License"  # specific license string
license_category: "custom-permissive"  # see §7 vocab
status: "active"               # active | archived | deprecated | borderline
url: "https://github.com/meta-llama"  # primary source — repo or HF org
last_verified: "2026-06-14"
---
```

## 2. Models

```yaml
---
name: "Llama"
maker: "Meta"
license: "Llama Community License"
license_category: "custom-permissive"
status: "active"
url: "https://huggingface.co/meta-llama"
last_verified: "2026-06-14"
variants: ["1B", "3B", "8B", "70B", "405B", "Scout-17B-16E", "Maverick-17B-128E"]
params_total: "405B"           # largest variant
has_moe: true
params_active: "17B"           # for the MoE variants
context_window: 128000          # tokens, native (largest non-experimental variant)
modalities: ["text", "vision"]  # text | vision | audio
gated: true                     # license-acceptance required to download
released: "2024-07"             # most-recent major release YYYY-MM
hardware_tiers: ["12gb", "16gb", "24gb", "24gb+"]  # tiers where SOMETHING in the family fits
best_for: ["coding", "research", "writing", "automation", "data"]  # any subset
notes: ""                       # one-line — optional
---
```

## 3. Runtimes

```yaml
---
name: "vLLM"
maker: "vLLM Project"
license: "Apache-2.0"
license_category: "apache-2.0"
status: "active"
url: "https://github.com/vllm-project/vllm"
last_verified: "2026-06-14"
language: "Python"
platforms: ["linux", "wsl2"]     # linux | macos | windows | wsl2
gpu_backends: ["cuda", "rocm", "cpu", "tpu", "xpu", "gaudi"]  # cuda | rocm | metal | cpu | vulkan | sycl | tpu | xpu | gaudi | ascend
api_openai_compat: true
supports_mcp: "native"           # native | adapter | none
formats: ["safetensors", "awq", "gptq", "fp8", "bitsandbytes", "gguf-experimental"]
best_for: ["serving", "high-throughput", "production"]  # general purpose tags
notes: ""
---
```

## 4. Frameworks

```yaml
---
name: "LangGraph"
maker: "LangChain"
license: "MIT"
license_category: "mit"
status: "active"
url: "https://github.com/langchain-ai/langgraph"
last_verified: "2026-06-14"
language: "Python"
supports_mcp: "adapter"          # native | adapter | none
programming_model: "graph"       # graph | imperative | declarative | role-based | code-emitting | composable
best_for: ["coding", "research", "writing", "automation", "data"]
notes: ""
---
```

## 5. Applications

```yaml
---
name: "OpenCode"
maker: "Anomaly"
license: "MIT"
license_category: "mit"
status: "active"
url: "https://github.com/anomalyco/opencode"
last_verified: "2026-06-14"
language: "TypeScript"
interfaces: ["cli", "tui", "desktop"]  # cli | tui | ide-plugin | web-ui | mobile | desktop | api
providers: ["openai", "anthropic", "ollama", "openrouter", "gemini"]  # major providers supported
supports_mcp: "native"           # native | adapter | none
byok: true
focus: "agentic-coding"          # primary use case: agentic-coding | general-agent | code-execution | chat-ui | personal-assistant | research
hardware_tiers: ["any"]          # if it runs on any reasonably modern machine, "any"; else 8gb/12gb/...
best_for: ["coding", "research", "writing", "automation", "data"]
notes: ""
---
```

## 6. MCP servers (category files)

```yaml
---
name: "Filesystem"
license_category: "apache-2.0"   # category-level; the dominant license of leading impls
status: "active"
url: "https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem"
last_verified: "2026-06-14"
transport: "stdio"               # stdio | sse | http (dominant for category)
has_anthropic_reference: true
auth: "none"                     # none | api-key | oauth (dominant for category)
best_for: ["coding", "research", "writing", "automation", "data"]
notes: ""
---
```

## 7. Techniques

```yaml
---
name: "ReAct"
license_category: "n/a"          # techniques don't have licenses
status: "active"
url: "https://arxiv.org/abs/2210.03629"
last_verified: "2026-06-14"
applies_at: "framework"          # model | runtime | framework | agent — where the technique lives
problem: "Pure reasoning hallucinates; pure tool use lacks reasoning to guide actions"
best_for: ["coding", "research", "writing", "automation", "data"]
notes: ""
---
```

## 8. Controlled vocab

**license_category:** `apache-2.0`, `mit`, `custom-permissive` (Llama-Community, Gemma, Tencent Hunyuan, Nemotron, DBRX), `source-available` (CC-BY-NC, AGPL-3.0, OpenRAIL-M, MRL), `proprietary` (closed-source free-to-use like LM Studio), `n/a` (techniques)

**status:** `active`, `archived`, `deprecated`, `borderline`

**hardware_tiers:** `8gb`, `12gb`, `16gb`, `24gb`, `24gb+`, `any` (for non-GPU-bound apps), `mac-only`, `cpu-only`

**modalities:** `text`, `vision`, `audio`

**platforms:** `linux`, `macos`, `windows`, `wsl2`

**gpu_backends:** `cuda`, `rocm`, `metal`, `cpu`, `vulkan`, `sycl`, `tpu`, `xpu`, `gaudi`, `ascend`, `inferentia`

**interfaces:** `cli`, `tui`, `ide-plugin`, `web-ui`, `mobile`, `desktop`, `api`, `browser-extension`

**supports_mcp:** `native`, `adapter`, `none`

**programming_model** (frameworks): `graph`, `imperative`, `declarative`, `role-based`, `code-emitting`, `composable`, `constraint-based`

**focus** (applications): `agentic-coding`, `general-agent`, `code-execution`, `chat-ui`, `personal-assistant`, `research`, `project-workflow`

**transport** (mcp-servers): `stdio`, `sse`, `http`

**auth** (mcp-servers): `none`, `api-key`, `oauth`

**applies_at** (techniques): `model`, `runtime`, `framework`, `agent`

**best_for:** `coding`, `research`, `writing`, `automation`, `data` (any subset; empty means general-purpose)

## 9. Rules

- Frontmatter is **the source of truth** for what appears in INDEXes and views — if you change a field in the frontmatter, rerun the regen script and INDEX.md updates from there.
- Prose `## 1. What It Is` still describes the entity in human terms; it can repeat frontmatter fields freely. Prose is what humans read; frontmatter is what tools read.
- If a field doesn't apply, omit it (don't write `null` or empty list unless the empty list is meaningful).
- The `notes` field is for one-line caveats that don't fit the vocab (e.g., "AutoGen now in maintenance mode; superseded by MS Agent Framework").
- Update `last_verified` whenever you do any depth-pass work on the entity.

## 10. Consistency & completeness enforcement

Two scripts catch drift, run locally:

1. **`scripts/validate.py`** — checks every entity's frontmatter against the schema:
   - Required fields per layer (see §2–§7 above)
   - Controlled vocab values (see §8)
   - Type sanity (lists, ints, bools, dates)
   - URL well-formedness
   Exits non-zero on any violation; prints every issue.

2. **`scripts/regen.py --check`** — reads frontmatter, regenerates INDEXes and `survey.json` in memory, and compares to disk. Exits non-zero if disk is out of sync. Catches "I edited frontmatter but forgot to rerun regen."

Run both before committing changes to survey content. CI is not wired up — discipline is local.

### Adding a new entity

1. Copy `TEMPLATE.md` to the new entity filename (kebab-case).
2. Add YAML frontmatter at the top (see this schema doc for the field set per layer).
3. Fill the prose sections.
4. Run `python3 scripts/validate.py` — fix any violations.
5. Run `python3 scripts/regen.py` — regenerates the relevant INDEX.md and updates `survey.json`.
6. Commit the entity file, the INDEX.md change, and `survey.json` together.

### Editing an existing entity

If you only edit prose, no script needed. If you edit any frontmatter field:

1. Run `python3 scripts/regen.py` to keep INDEX.md and `survey.json` in sync.
2. Commit the entity edit and the regen output together.

### Regen safety

`regen.py` refuses to run (exit 2) if any entity files lack frontmatter — writing would silently drop rows. Pass `--force` only if you intentionally want to migrate partial state. The CI gate uses `--check`, which never writes anyway.
