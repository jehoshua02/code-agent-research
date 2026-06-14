# Open Self-Hostable AI Stack — Survey

Unbiased research on the open, free, self-hostable AI ecosystem. Entity files (per model, runtime, framework, etc.) document facts neutrally. Views are where opinion lives.

**Breadth before depth.** This survey documents every open-weight model and self-hostable component worth knowing about — including ones that don't fit on the reader's current hardware. The `by-hardware` view filters for fit; the survey itself does not. Hardware is a runtime constraint, not a research-scope constraint.

## 1. Why this exists

Prior art at single layers is abundant. Nothing combines all five layers with task / hardware / license cuts under one structured template, as of June 2026.

Surveyed June 2026:

- [HuggingFace Open LLM Leaderboard](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard) — model benchmarks only
- [Presenc AI: Open-Source LLM Landscape 2026](https://presenc.ai/research/open-source-llm-landscape-2026), [Lushbinary April 2026 guide](https://lushbinary.com/blog/best-open-source-llms-april-2026-comparison-guide/) — model-only narratives
- [Codersera runtime comparison 2026](https://codersera.com/blog/ollama-vs-lm-studio-vs-vllm-vs-llama-cpp-vs-mlx-2026/), [Quantize Lab benchmarks](https://www.quantizelab.dev/articles/vllm-vs-llama-cpp-vs-ollama-benchmark-guide) — runtime-only
- [Turing AI agent frameworks 2026](https://www.turing.com/resources/ai-agent-frameworks), [awesome-llm-agents](https://github.com/kaushikb11/awesome-llm-agents) — agent-only
- [PulseMCP Server Directory](https://www.pulsemcp.com/servers) — MCP-only, disconnected from model/agent choice
- [awesome-local-llm](https://github.com/rafska/awesome-local-llm) — broadest single repo; link-dump, no structure

What this adds: all five layers under one schema; hardware tiers applied to models *and* runtimes; task and license cuts across layers; entity-vs-view separation (facts vs opinion); templated, comparable entries.

Known risk: single-layer articles refresh monthly. Stale entries here will look worse than no entry. Each entity carries a "Last verified" date and links to live sources; reader gets a structured index plus links to whoever is closest to the source.

## 2. Scope

In: open-weight models, self-hostable inference runtimes, open agent frameworks, MCP servers, and techniques. Tasks include coding, research, writing, automation, and data analysis.

In-scope regardless of size: a 405B model with no chance of running on a 8 GB card still belongs here.

Relationship to `../models/` and `../tools/`: those track the broader coding-tool comparison (open and closed). This survey is task-agnostic and covers the open ecosystem at full breadth.

## 3. Structure

```
Building blocks (the stack — composable layers):
  models/         — open-weight model families (variants enumerated within)
  runtimes/       — inference engines (ollama, vllm, llama.cpp, ...)
  frameworks/     — agent framework libraries to build with (langgraph, autogen, crewai, ...)
  mcp-servers/    — MCP server implementations
  techniques/     — patterns (rag, tool-use, planning, ...)

Finished products (consume the stack — installable applications):
  applications/   — opencode, aider, openhands, ... (agentic coding/general; later: chat UIs, eval, fine-tuning)

Cross-cuts:
  views/          — curated views (by-task, by-hardware, by-license, by-layer)
```

Each layer has:

- `TEMPLATE.md` — required structure for entity files in that layer.
- `INDEX.md` — full table of all entities in that layer (unbiased reference).

Each entity = one file. Small, focused. No multi-topic files. Authoritative facts live in the entity file; views excerpt or link.

## 4. Deployment notes

Entities are surveyed at full breadth regardless of platform. Each entity file documents its own supported platforms. The notes below are reader-facing context, not a scope filter — the survey includes Linux-only, Mac-only (e.g. MLX), and Windows-native components alike.

Common patterns observed in entries so far:

- **Runtimes** typically need GPU access and run best on bare-metal Linux. WSL2 on Windows supports NVIDIA CUDA. Apple Silicon runtimes (MLX, llama.cpp Metal) target macOS directly. ROCm runtimes target AMD on Linux.
- **Agent frameworks** typically need broad filesystem and process access; they run best on the agent operator's host OS directly, not inside a container.
- **MCP servers** vary — some need host access (filesystem, shell), some are isolated (web fetch, remote API) and run fine in containers.

If a model or runtime requires a platform the reader doesn't currently have, that is a deployment cost the reader can choose to pay — not a reason to exclude it from the survey.

## 5. Views

- [By layer](views/by-layer.md) — curated picks at each layer
- [By task](views/by-task.md) — coding, research, writing, automation, data
- [By hardware](views/by-hardware.md) — 8 / 12 / 16 / 24 / 24+ GB tiers
- [By license](views/by-license.md) — Apache 2.0, MIT, custom permissive, source-available

## 6. Glossary

[Glossary](GLOSSARY.md) — terminology used throughout the survey (layers, model concepts, hardware, protocols).

## 7. Plan

[Plan](PLAN.md) — breadth-first method, inventory, and status.
