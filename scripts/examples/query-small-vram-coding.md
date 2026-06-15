# Example — picking a small-VRAM agentic-coding stack via `query.py`

> **Worked example showing `scripts/query.py` in action.** Drawn from a real session on an 8 GB GPU targeting agentic coding. Output snapshots are from 2026-06-15 (re-run after the 2026-06-15 data audit) and will drift; rerun against the current `survey.sqlite` for current results.

## Constraints

| Field | Value |
|---|---|
| Hardware | RTX 3070, 8 GB VRAM |
| OS | Linux (bare-metal or WSL2) |
| Primary task | Agentic coding |
| Required | MCP-compatible application |
| License preference | Apache 2.0 or MIT |
| Stack must be | Free, offline-capable, self-hostable |

## Walkthrough

### Step 1 — Candidate models

Models that (a) fit a 3070, (b) are Apache 2.0 or MIT, (c) tagged for coding. Sorted by context window so we see who's friendliest for long codebases.

```sql
SELECT name, params_total, context_window, license_category, license
FROM entities
WHERE layer = 'models'
  AND status = 'active'
  AND license_category IN ('apache-2.0', 'mit')
  AND EXISTS (SELECT 1 FROM json_each(hardware_tiers) WHERE value IN ('8gb', 'any'))
  AND EXISTS (SELECT 1 FROM json_each(best_for) WHERE value = 'coding')
ORDER BY context_window DESC;
```

```
name     params_total  context_window  license_category  license
Mistral  675B          262144          apache-2.0        Apache-2.0
DeepSeek 685B          131072          mit               MIT
Granite  8B            131072          apache-2.0        Apache-2.0
Phi      42B           131072          mit               MIT
Qwen     235B          131072          apache-2.0        Apache-2.0
```

Five families pass. Mistral leads on context window (256K native). All others give 128K — generous for a coding workflow.

> _Note: earlier snapshots showed only Granite/Phi/Qwen. The 2026-06-15 data audit caught family-level `hardware_tiers` undercounting (Mistral-7B at Q4 ~4.5 GB fits 8 GB; DeepSeek's R1-Distill-Qwen-7B and R1-Distill-Llama-8B do too). See [`docs/open/AUDIT.md`](../../docs/open/AUDIT.md)._

### Step 1b — See the variants

`params_total` is the family's largest variant. For 8 GB we need to know what smaller variants exist:

```sql
SELECT name, variants
FROM entities
WHERE layer = 'models' AND name IN ('Qwen', 'Phi', 'Granite', 'Mistral', 'DeepSeek');
```

```
name      variants
DeepSeek  ["V2", "V2.5", "V3", "V3-0324", "R1", "R1-0528",
           "R1-Distill-Qwen-1.5B", "R1-Distill-Qwen-7B", "R1-Distill-Qwen-14B",
           "R1-Distill-Qwen-32B", "R1-Distill-Llama-8B", "R1-Distill-Llama-70B"]
Granite   ["Granite-3.1-1B-A400M", "Granite-3.1-2B", "Granite-3.1-3B-A800M",
           "Granite-3.1-8B", "Granite-3.3-2B", "Granite-3.3-8B"]
Mistral   ["7B", "Mixtral-8x7B", "Mixtral-8x22B", "NeMo-12B", "Large-2407",
           "Codestral-22B", "Small-3.1-24B", "Large-3-675B"]
Phi       ["Phi-3-mini-3.8B", "Phi-3-small-7B", "Phi-3-medium-14B",
           "Phi-3.5-mini-3.8B", "Phi-3.5-MoE-42B", "Phi-3.5-Vision-4.2B",
           "Phi-4-14B", "Phi-4-mini-3.8B", "Phi-4-multimodal-5.6B",
           "Phi-4-reasoning-14B", "Phi-4-reasoning-vision-15B"]
Qwen      ["0.6B", "1.7B", "4B", "8B", "14B", "32B", "30B-A3B", "72B", "235B-A22B"]
```

For 8 GB at Q4_K_M:
- **Qwen-8B** (~5 GB) — pair with Qwen2.5-Coder-7B or Qwen3-Coder. The family entry indexes the line; coding-tuned checkpoints are pulled separately.
- **DeepSeek-R1-Distill-Qwen-7B** (~4.5 GB) — strong reasoning + coding at 8 GB.
- **Mistral-7B** (~4.5 GB) — solid all-rounder, but coding-specialized Codestral-22B requires 12 GB+.
- **Granite-3.3-8B** (~5 GB) — strong coding (HumanEval 89.7); IBM-maintained, documented data provenance.
- **Phi-4-mini-3.8B** (~2.5 GB) — leaves substantial KV cache room for long context.

### Step 2 — Candidate runtimes

Linux + CUDA + Apache 2.0 or MIT + OpenAI-compatible API (so applications can talk to it):

```sql
SELECT name, license_category, language, supports_mcp,
       (SELECT GROUP_CONCAT(value, ', ') FROM json_each(formats)) AS formats
FROM entities
WHERE layer = 'runtimes'
  AND status = 'active'
  AND license_category IN ('apache-2.0', 'mit')
  AND EXISTS (SELECT 1 FROM json_each(platforms) WHERE value = 'linux')
  AND EXISTS (SELECT 1 FROM json_each(gpu_backends) WHERE value = 'cuda')
  AND api_openai_compat = 1
ORDER BY name;
```

```
name        license_category  language  supports_mcp  formats
LocalAI     mit               Go        none          gguf, safetensors, gptq, awq
Ollama      mit               Go        none          gguf
SGLang      apache-2.0        Python    none          safetensors, gptq, awq, fp8, gguf
llama.cpp   mit               C++       none          gguf
llamafile   apache-2.0        C++       none          gguf
vLLM        apache-2.0        Python    native        safetensors, gguf, awq, gptq, fp8, bitsandbytes
```

Six candidates. For single-user Q4_K_M GGUF, **Ollama** is the simplest: one binary, `ollama pull qwen2.5-coder:7b`, OpenAI-compatible API on `localhost:11434`. vLLM and SGLang are heavier; LocalAI / llamafile / llama.cpp are all valid alternatives. Note `supports_mcp` doesn't matter at this layer — applications speak MCP, runtimes don't need to.

### Step 3 — Candidate applications

Agentic-coding focused, native MCP, truly open:

```sql
SELECT name, license_category, language, focus,
       (SELECT GROUP_CONCAT(value, ', ') FROM json_each(interfaces)) AS interfaces
FROM entities
WHERE layer = 'applications'
  AND status = 'active'
  AND license_category IN ('apache-2.0', 'mit')
  AND focus = 'agentic-coding'
  AND supports_mcp = 'native'
ORDER BY name;
```

```
name       license_category  language    focus            interfaces
OpenCode   mit               TypeScript  agentic-coding   cli, tui, desktop
OpenHands  mit               Python      agentic-coding   cli, web-ui, api
```

Two clear candidates. Head-to-head:

```sql
SELECT name, language, supports_mcp,
       (SELECT GROUP_CONCAT(value, ', ') FROM json_each(interfaces)) AS interfaces,
       (SELECT GROUP_CONCAT(value, ', ') FROM json_each(providers)) AS providers,
       byok, focus, notes
FROM entities
WHERE layer = 'applications' AND name IN ('OpenCode', 'OpenHands');
```

```json
[
  {"name": "OpenCode",
   "interfaces": "cli, tui, desktop",
   "providers": "anthropic, openai, google, aws-bedrock, azure-openai, openrouter, ollama",
   "notes": "Ships as both MCP server and MCP client; 75+ providers via built-in registry."},
  {"name": "OpenHands",
   "interfaces": "cli, web-ui, api",
   "providers": "anthropic, openai, google, minimax, ollama",
   "notes": "Runs in sandboxed Docker; full browser + terminal environment; formerly OpenDevin."}
]
```

OpenCode wins on simplicity (CLI/TUI vs Docker+web UI). OpenHands wins on capability (sandboxed Docker with full browser+terminal) and on SWE-bench Verified leadership. For this scenario — lightweight single-user agentic coding — OpenCode is the pick. Revisit OpenHands if the workload grows.

### Step 4 — MCP servers

Coding-relevant, truly open, Anthropic-reference where possible:

```sql
SELECT name, license_category, transport, auth, has_anthropic_reference
FROM entities
WHERE layer = 'mcp-servers'
  AND status = 'active'
  AND license_category IN ('apache-2.0', 'mit')
  AND EXISTS (SELECT 1 FROM json_each(best_for) WHERE value = 'coding')
ORDER BY has_anthropic_reference DESC, name;
```

```
name             license_category  transport  auth      has_anthropic_reference
Filesystem       mit               stdio      none      1
Git / GitHub     mit               stdio      api-key   1
Code Execution   apache-2.0        stdio      api-key   0
Shell            mit               stdio      none      0
```

The standard four — all installable, two from Anthropic's reference set.

## Recommendation

| Layer | Pick |
|---|---|
| Model | Qwen2.5-Coder-7B (Q4_K_M, ~5 GB) — Apache 2.0, fits 3070 with KV-cache headroom, explicitly coding-tuned |
| Runtime | Ollama (MIT) — easiest local serving, OpenAI-compat API |
| Application | OpenCode (MIT) — native MCP, CLI/TUI, 75+ providers via Ollama |
| MCP servers | Filesystem, Shell, Git/GitHub, Code Execution |
| Framework | skip — OpenCode is finished |
| Techniques | implicit (ReAct + tool use inside OpenCode) |

The 2026-06-15 audit expanded the model candidate pool (Mistral and DeepSeek became visible) but didn't change the pick — Qwen2.5-Coder-7B remains the safest choice because of explicit coding tuning + Apache 2.0 + comfortable 8 GB fit. DeepSeek-R1-Distill-Qwen-7B is the strongest reasoning-focused alternative.

## What SQL is good at

- **`ORDER BY context_window DESC`** — see who has the longest context, not just who passes the filter.
- **`params_total` inline** — every frontmatter column is directly queryable.
- **`GROUP_CONCAT` on list fields** — formats / interfaces / providers visible in one row instead of as separate query passes.
- **Head-to-head dump** of two specific entities (`name IN (...)`) — quick comparison without recomputing filters.
- **Composable refinements** — each step's query is a copy-and-tweak of the last; the path through the decision is recoverable later.

## Methodology note

Three minutes of SQL after `scripts/query.py` was available. Knowing where to look in the schema was the bottleneck (which fields, which vocab) — `docs/open/SCHEMA.md` and `docs/open/QUERIES.md` make that lookup fast. Future picks for different scenarios should be able to reuse the queries above with light tweaks (different hardware tier, different task, different license set).
