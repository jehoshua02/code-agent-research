# Open Self-Hostable AI Stack — Survey

Unbiased research on the open, free, self-hostable AI ecosystem. Entity files (per model, runtime, framework, etc.) document facts neutrally. Views are where opinion lives.

**New to the space?** Start with the [Reading Guide](READING_GUIDE.md) — it explains the mental model and gives you a path through the survey based on what you want to do.

**Breadth before depth.** This survey documents every open-weight model and self-hostable component that meets the inclusion criteria in §2 — including ones that don't fit on the reader's current hardware. The `by-hardware` view filters for fit; the survey itself does not. Hardware is a runtime constraint, not a research-scope constraint.

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

### 2.1 Categories

In-scope categories: open-weight models, self-hostable inference runtimes, open agent frameworks, MCP servers, finished open-source applications, and techniques. Tasks include coding, research, writing, automation, and data analysis.

In-scope regardless of size: a 405B model with no chance of running on an 8 GB card still belongs here.

In-scope regardless of model-specificity: a runtime, application, or framework built for one specific model family (e.g., a Gemma-only chat app or a Llama-only inference engine) is a first-class entity, not a second-class one. Being able to switch models is a feature some readers want and others don't — the survey does not privilege multi-model tooling over single-model tooling.

Model-switching is a stack-level property, not necessarily an entity-level one. A reader who wants to switch models can either pick layers that support model switching (multi-model runtimes/frameworks/applications) **or** switch the whole stack to one built around a different model. Both paths are valid. Each entity's documentation states which models it supports — that's the information readers need to choose the right path for them.

### 2.2 Inclusion criteria

To stay objective and bound the long tail, an entity is **in scope** if it meets **at least one** of:

1. **Notable backing** — produced or maintained by a recognized organization (corporate AI lab, university research group, named foundation/standards body).
2. **Adoption signal** — measurable adoption: ≥1,000 GitHub stars (where applicable), or top-N on HuggingFace by downloads in its category, or referenced in another in-scope entity, or cited in PulseMCP / Anthropic reference set (for MCP servers).
3. **Distinct contribution** — introduces an approach, architecture, or capability not already represented by another in-scope entity. Named in a peer-reviewed paper or canonical industry reference qualifies.
4. **Independent coverage** — covered in two or more independent surveys / comparisons / news pieces in the past 12 months.

An entity is **excluded** if any of:

- Private fork or one-off experiment with no maintained release.
- Redundant near-clone of an in-scope entity with no architectural, licensing, or usage distinction.
- Long-tail entry serving the same purpose as already-included alternatives, with substantially lower adoption and no distinct contribution.

**Archived/discontinued projects** can remain (or be added) if they had clear historical significance — they get an "archived" note in their `## 1. What It Is` and in the INDEX. Otherwise, archived projects without successors are excluded.

The criteria are intentionally objective. When two readers might disagree, the inclusion decision should rest on which criterion the entity does or does not meet, not on personal opinion. Disagreement about whether an entity meets a criterion is a normal pull-request conversation.

### 2.3 Considered but not included

Entities we researched and decided **not** to add as full entries are recorded in [CONSIDERED.md](CONSIDERED.md) — with the criterion they failed (or the reason they fall outside scope). Borderline inclusions are tracked there too. This way the research effort isn't lost, and readers can tell "we considered X and chose not to add it" apart from "we never looked at X."

### 2.4 Relationship to other docs

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

[Glossary](GLOSSARY.md) — terminology used throughout the survey (layers, model concepts, hardware, protocols, agent patterns, runtime APIs, memory/state, observability, security, decoding).

## 7. Reading guide

[Reading Guide](READING_GUIDE.md) — mental model and suggested paths through the survey for new readers.

## 8. Audit log

[AUDIT.md](AUDIT.md) — record of structural and accuracy audits run against the survey, the queries used, what's been verified, what's been fixed, and the known limitations the picker accepts.

## 9. Schema & scripts

Each entity has a YAML frontmatter block at the top. INDEX.md tables and `survey.json` are generated from frontmatter — don't edit INDEXes by hand. See:

- [SCHEMA.md](SCHEMA.md) — field definitions per layer, controlled vocab, rules
- [`../../scripts/README.md`](../../scripts/README.md) — `validate.py`, `regen.py`, `build-sqlite.py`, `query.py` quick reference
- [QUERIES.md](QUERIES.md) — example SQL queries against the SQLite build (`survey.sqlite`)

Run `scripts/validate.py` and `scripts/regen.py` locally before committing survey changes.

## 10. Plan

[Plan](PLAN.md) — breadth-first method, inventory, and status.
