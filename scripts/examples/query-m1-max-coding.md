# Example — picking an agentic-coding stack for M1 Max (32 GB) via `query.py`

> **Worked example showing `scripts/query.py` in action.** Drawn from a real session on a MacBook Pro M1 Max with 32 GB unified memory targeting agentic coding. Output snapshots are from 2026-06-15 (post-audit) and will drift; rerun against the current `survey.sqlite` for current results. See [`query-small-vram-coding.md`](query-small-vram-coding.md) for the 3070 / 8 GB version of the same exercise.

## Constraints

| Field | Value |
|---|---|
| Hardware | MacBook Pro M1 Max, 32 GB unified memory (~21–24 GB usable for inference at default cap) |
| OS | macOS (Apple Silicon, Metal GPU) |
| Primary task | Agentic coding |
| Required | MCP-compatible application |
| License preference | Apache 2.0 or MIT |
| Stack must be | Free, offline-capable, self-hostable |

**Why this is its own example:** Apple Silicon's unified memory and Metal GPU make the runtime / model picture meaningfully different from a discrete-VRAM scenario. CUDA-only entries drop out; MLX becomes an option; the model size ceiling roughly triples vs an 8 GB card.

## Walkthrough

### Step 1 — Candidate models

Models that (a) the family has at least one variant fitting 16 GB+ (M1 Max comfortably runs 16-class), (b) are Apache 2.0 or MIT, (c) tagged for coding. Sorted by context window.

```sql
SELECT name, params_total, context_window, license_category, license
FROM entities
WHERE layer = 'models'
  AND status = 'active'
  AND license_category IN ('apache-2.0', 'mit')
  AND EXISTS (SELECT 1 FROM json_each(hardware_tiers) WHERE value IN ('16gb', 'any'))
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

Same five families as the 8 GB scenario — the survey's `hardware_tiers` field is upward-closed (an `8gb` tag implies `16gb` too). The 16 GB ceiling lets us go larger.

### Step 1b — See the variants for the family sweet spots

```sql
SELECT name, variants
FROM entities
WHERE layer = 'models' AND name IN ('Qwen', 'DeepSeek', 'Mistral');
```

```
name      variants
DeepSeek  ["V2", "V2.5", "V3", "V3-0324", "R1", "R1-0528",
           "R1-Distill-Qwen-1.5B", "R1-Distill-Qwen-7B", "R1-Distill-Qwen-14B",
           "R1-Distill-Qwen-32B", "R1-Distill-Llama-8B", "R1-Distill-Llama-70B"]
Mistral   ["7B", "Mixtral-8x7B", "Mixtral-8x22B", "NeMo-12B", "Large-2407",
           "Codestral-22B", "Small-3.1-24B", "Large-3-675B"]
Qwen      ["0.6B", "1.7B", "4B", "8B", "14B", "32B", "30B-A3B", "72B", "235B-A22B"]
```

Sweet spots in the ~21 GB-usable budget at Q4_K_M:

| Variant | VRAM at Q4_K_M | Why pick |
|---|---|---|
| **Qwen-14B → Qwen2.5-Coder-14B** | ~9 GB | Coding-tuned; clean fit with KV-cache headroom for 32K+ context |
| **Qwen-32B → Qwen2.5-Coder-32B** | ~18 GB | Pushes ceiling; near-best open coding model at this tier |
| **DeepSeek-R1-Distill-Qwen-32B** | ~18 GB | Strongest reasoning + coding in this range |
| **Codestral-22B (Mistral family)** | ~13 GB | Coding-specialized alternative; non-permissive variants exist so verify the specific checkpoint |
| **Mistral-Small-3.1-24B** | ~14 GB | All-rounder with 256K context |

Default pick: **Qwen2.5-Coder-14B** — best capability-per-GB at this hardware tier. Step up to 32B-class once the workflow is dialed in.

### Step 2 — Candidate runtimes

Mac-friendly: Metal-backed, OpenAI-compatible, Apache 2.0 or MIT.

```sql
SELECT name, license_category, language,
       (SELECT GROUP_CONCAT(value, ', ') FROM json_each(formats)) AS formats
FROM entities
WHERE layer = 'runtimes'
  AND status = 'active'
  AND license_category IN ('apache-2.0', 'mit')
  AND EXISTS (SELECT 1 FROM json_each(platforms) WHERE value = 'macos')
  AND EXISTS (SELECT 1 FROM json_each(gpu_backends) WHERE value = 'metal')
  AND api_openai_compat = 1
ORDER BY name;
```

```
name          license_category  language  formats
LocalAI       mit               Go        gguf, safetensors, gptq, awq
MLX / mlx-lm  mit               Python    safetensors
Ollama        mit               Go        gguf
llama.cpp     mit               C++       gguf
llamafile     apache-2.0        C++       gguf
```

Five candidates. **Ollama** is the practical default — single-command install, OpenAI-compat on `localhost:11434`, llama.cpp Metal under the hood. **MLX/mlx-lm** is ~10-15% faster on Apple Silicon but Python-only and pickier with model formats (MLX-converted safetensors only). Most users: Ollama. Perf-conscious: MLX.

### Step 3 — Candidate applications

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

Same two as the 8 GB scenario. **OpenCode** wins on simplicity for solo coding; **OpenHands** wins if you want the sandboxed Docker runtime with full browser + terminal.

### Step 4 — MCP servers

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

Same standard four.

## Recommendation

| Layer | Pick |
|---|---|
| Model | **Qwen2.5-Coder-14B** (Q4_K_M, ~9 GB) — Apache 2.0, coding-tuned, fits with ~12 GB headroom for context |
| Runtime | **Ollama** (MIT) — `brew install ollama && ollama pull qwen2.5-coder:14b` |
| Application | **OpenCode** (MIT, native MCP) — points at Ollama via OpenAI-compat |
| MCP servers | Filesystem, Shell, Git/GitHub, Code Execution |
| Framework | skip — OpenCode is finished |
| Techniques | implicit (ReAct + tool use inside OpenCode) |

**Step-up path** (same hardware, more capable models):
- `ollama pull deepseek-r1-distill-qwen-32b` (~18 GB Q4) for stronger reasoning
- `ollama pull qwen2.5-coder:32b` (~18 GB Q4) for top-tier coding

If pushing past 18 GB on a 32 GB Mac, raise the GPU memory cap (default ~67% of RAM):
```bash
sudo sysctl iogpu.wired_limit_mb=28000   # ~28 GB usable
```

**MLX alternative**: if you want max perf, swap Ollama for `mlx-lm`:
```bash
pip install mlx-lm
mlx_lm.server --model mlx-community/Qwen2.5-Coder-14B-Instruct-4bit
```
OpenCode points at `http://localhost:8080/v1` instead.

## What SQL is good at (this scenario)

- **Platform + GPU backend in one query** — `EXISTS (... WHERE value='macos') AND EXISTS (... WHERE value='metal')` immediately rules out CUDA-only entries.
- **Same model query reused** — the 16 GB filter doesn't even need rewriting from the 8 GB version; just bump the tier and read more results.
- **Variant table inline** — see family sweet spots without leaving the picker.
- **License consistency at scale** — every step filters `license_category IN ('apache-2.0', 'mit')`; one place to change the policy if you decide to accept custom-permissive too.

## Comparison to the 3070 (8 GB) pick

| Layer | 3070 pick | M1 Max pick | Why different |
|---|---|---|---|
| Model | Qwen2.5-Coder-7B | Qwen2.5-Coder-14B (or step up to 32B) | M1 Max has ~3× usable inference memory |
| Runtime | Ollama (CUDA) | Ollama (Metal) — or MLX for max perf | Apple Silicon adds MLX as a real option |
| Application | OpenCode | OpenCode | Same — application doesn't care about backend |
| MCP servers | Same four | Same four | Same |

**Why this is a clear upgrade over remoting to the 3070:**
- Lower latency, no SSH hop
- No second machine to keep on
- More usable inference memory
- One device, one stack
