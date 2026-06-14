# Research Plan

How the survey gets built. Breadth before depth.

## 1. Method

Two waves:

1. **Wave 1 — Stub everything.** Create one entity file per known entity at each layer. Each stub uses TEMPLATE structure with empty sections. Add a one-line row to the layer's INDEX. Goal: zero notable entities missing from the survey by end of wave 1.
2. **Wave 2 — Depth passes.** Iterate through entities in passes. Each pass fills specific sections across all entities, not all sections for one entity.

### Wave 2 passes (in order)

- **Pass A — Identity.** `What It Is`, `Sources` (≥1 link). Every entity reaches "minimum viable entry."
- **Pass B — Catalog.** License, sizes/variants, supported platforms. Layer INDEX becomes useful.
- **Pass C — Function.** Capabilities, hardware requirements, API surface, transport, etc. (per layer template).
- **Pass D — Evidence.** Benchmarks, documented strengths/weaknesses with citations.
- **Pass E — Views.** Wire entities into `views/by-task`, `views/by-hardware`, `views/by-license`, `views/by-layer`.

Why pass-based: a complete entity takes hours; one section across many entities takes minutes. Breadth-first compounds value faster — a partial entry on every entity beats a complete entry on a few.

## 2. Initial inventory

Seed list. Add as discovered. Each item below becomes a stub file in Wave 1.

### 2.1 Models (families)

- [x] Llama (Meta) — 3.1, 3.2, 3.3, 4
- [x] Qwen / Qwen-Coder (Alibaba)
- [x] DeepSeek — V2, V3, R1
- [x] Mistral — Mistral, Mixtral, Codestral, Magistral
- [x] Phi (Microsoft)
- [x] Gemma (Google)
- [x] Hunyuan (Tencent)
- [x] Yi (01.ai)
- [x] Falcon (TII)
- [x] Command R / Command A (Cohere)
- [x] StarCoder2 (BigCode)
- [x] OLMo (AI2)
- [x] Granite (IBM)
- [x] Nemotron (NVIDIA)
- [x] DBRX (Databricks)
- [x] SmolLM (HuggingFace)
- [x] Hermes (Nous Research)

### 2.2 Runtimes

- [x] vLLM
- [x] llama.cpp
- [x] Ollama
- [x] LM Studio
- [x] MLX / mlx-lm
- [x] TGI (text-generation-inference)
- [x] SGLang
- [x] ExLlamaV2 / ExLlamaV3
- [x] Aphrodite Engine
- [x] KoboldCpp
- [x] Text Generation WebUI (oobabooga)
- [x] Jan
- [x] LocalAI
- [x] llamafile
- [x] transformers (HF baseline)
- [x] gemma.cpp (Google) — model-specific (Gemma)

### 2.3 Frameworks

- [x] LangGraph (LangChain)
- [x] AutoGen (Microsoft)
- [x] CrewAI
- [x] Letta (MemGPT successor)
- [x] Smolagents (HuggingFace)
- [x] OpenAI Swarm
- [x] LlamaIndex Agents
- [x] Pydantic AI
- [x] Haystack agents
- [x] DSPy
- [x] BeeAI
- [x] Atomic Agents
- [x] mcp-agent
- [x] agno

### 2.4 Applications (finished products)

Installable AI applications that compose the stack. Distinct from frameworks (libraries to build with). Current entries are agentic coding/general-purpose; other categories (chat UIs, eval tools, fine-tuning tools) may be added later.

- [x] OpenCode (Anomaly Co)
- [x] Aider
- [x] OpenHands (formerly OpenDevin)
- [x] AutoGPT
- [x] Open Interpreter
- [x] Continue
- [x] Mentat
- [x] GPT-Engineer
- [x] Goose (Block)
- [x] SWE-agent (Princeton)
- [x] OpenClaw (OpenClaw Foundation)
- [x] GSD-PI (open-gsd) — borderline, under-threshold adoption + recent
- [x] Gemma Chat (ammaarreshi) — model-specific (Gemma)
- [x] Gemma Gem (kessler) — model-specific (Gemma); borderline adoption

### 2.5 MCP servers (by category)

Scope: Anthropic reference servers + notable community servers per category. PulseMCP lists 18k+; this survey covers category leaders, not the long tail.

- [x] Filesystem
- [x] Shell / command execution
- [x] Web fetch
- [x] Web search
- [x] Browser control
- [x] Git / GitHub
- [x] Database (PostgreSQL, SQLite, MySQL)
- [x] Memory / persistent state
- [x] Code execution / sandboxing
- [x] Cloud APIs (AWS, GCP)
- [x] Productivity (calendar, email)

### 2.6 Techniques

- [x] RAG (retrieval-augmented generation)
- [x] ReAct
- [x] Plan-and-execute
- [x] Chain-of-thought
- [x] Tree-of-thought
- [x] Tool use / function calling
- [x] Self-consistency
- [x] Reflection
- [x] Prompt caching
- [x] Few-shot / in-context learning
- [x] Constrained decoding (JSON mode, grammar)
- [x] Speculative decoding
- [x] KV cache reuse

## 3. Status

| Phase | Status | Notes |
|---|---|---|
| Scaffold | Done | structure, templates, indexes, glossary, justification |
| Wave 1 — Stubs | Done | |
| Wave 2 — Pass A (Identity) | Done | every entity has §1 + ≥1 source; layer INDEXes have license + key columns filled where confident |
| Wave 2 — Pass B (Catalog) | Done | per-layer §2-§4/5 (Variants, Install, Hardware, Formats, Model Compatibility, etc.); INDEX columns filled where applicable |
| Wave 2 — Pass C (Function) | Not started | |
| Wave 2 — Pass D (Evidence) | Not started | |
| Wave 2 — Pass E (Views) | Not started | |

Update this table after each commit that advances a phase.

## 4. Done criteria

- **Wave 1 done** — every layer's INDEX lists every inventory item; every inventory item has a stub file.
- **Pass A done** — every entity file has `What It Is` filled and at least one Source link.
- **Pass B done** — every entity file has license, sizes/variants (where applicable), and supported platforms.
- **Pass C done** — every entity file has its layer-specific function sections filled.
- **Pass D done** — every entity file has at least one benchmark or documented claim with citation.
- **Pass E done** — every view file lists every relevant entity, no `_..._` placeholders remain.

## 5. Working rules

- Always work breadth-first within a pass: finish a pass across all entities before starting the next.
- New entities discovered mid-pass: add a stub, append to inventory, then continue current pass.
- Every commit updates the status table or the inventory if either changed.
- Sources required from Pass A onward — no unsourced claims.
