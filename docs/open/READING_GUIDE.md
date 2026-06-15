# Reading Guide

The survey covers a lot of terrain. This is the path through it if you're new to the space.

## 1. Start here (10 minutes)

Read these two, in order:

1. [README §1 Why this exists](README.md#1-why-this-exists) — what the survey is and isn't.
2. [GLOSSARY §1 Layers](GLOSSARY.md#1-layers) — the five building blocks (model, runtime, framework, MCP server, technique) and the layer stack example.

That's enough to navigate the rest.

## 2. The mental model

When you read an entity entry, locate it on this stack:

```
┌─────────────────────────────────────────────┐
│  Application      (OpenCode, Aider, ...)    │  ← what you install and use
├─────────────────────────────────────────────┤
│  Framework        (LangGraph, CrewAI, ...)  │  ← orchestrates the agent loop
│       │                                     │
│       ├── uses → MCP servers (filesystem,   │
│       │           shell, web, ...)          │
│       │                                     │
│       └── calls → Runtime (vLLM, Ollama, ...)│ ← executes the model
│                       │                     │
│                       └── loads → Model     │ ← the weights
│                                  (Llama,    │
│                                   Qwen, ...) │
└─────────────────────────────────────────────┘
```

**Techniques** (RAG, ReAct, CoT, etc.) are patterns applied at any layer. **Applications** can also implement their own framework-like loop instead of using one off-the-shelf.

## 3. Reading an entity

Every entity file follows the same template. You almost never have to read the whole thing — pick the section you care about:

- **§1 What It Is** — name, maker, license, one-sentence summary. The "is this even relevant to me?" check.
- **§2–§5** vary by layer — install steps, variants/sizes, hardware needed, supported platforms. The "can I actually run this?" sections.
- **§6–§7** vary by layer — capabilities, MCP support, extensibility, API surface, security considerations. The "what does it actually do?" sections.
- **§8–§9** documented strengths and weaknesses with citations. The "how does it compare?" sections.
- **§10–§11** sources. Follow the links if you want the maintainer's own words.

Each entity has a "Last verified" date at the top. Anything dated more than a couple of months ago should be cross-checked against the linked sources.

## 4. Suggested reading paths

Pick a path based on your goal.

### A. "I want to run a local coding agent on my machine"

1. Skim [applications/INDEX.md](applications/INDEX.md) for coding-focused entries.
2. Pick one (start with [OpenCode](applications/opencode.md), [Aider](applications/aider.md), or [Continue](applications/continue.md)).
3. Check its §4 Model Compatibility — which providers and local runtimes it talks to.
4. Pick a runtime that fits your hardware. [Ollama](runtimes/ollama.md) is the easiest starting point.
5. Pick a model that the runtime can load and your VRAM can hold. Use [views/by-hardware.md](views/by-hardware.md) as a filter.

### B. "I want to build my own agent in Python"

1. Read the [agent framework](GLOSSARY.md#framework-agent-framework) glossary entry.
2. Skim [frameworks/INDEX.md](frameworks/INDEX.md). Note the Programming Model column — graph-based (LangGraph), code-emitting (Smolagents), role-based (CrewAI), type-safe (Pydantic AI) all look different from a developer's perspective.
3. Pick 2-3 candidates whose docs you'd be willing to read for an hour.
4. Read their §4 Agent Capabilities (covers tools / planning / memory / multi-agent / HITL / state / observability / retry / async). Pick the one whose tradeoffs match your project.

### C. "I want to learn the LLM-agent space"

1. Read this guide and the [glossary](GLOSSARY.md) end to end.
2. Read 2-3 model entries to get a sense of the weight ecosystem. Start with [Llama](models/llama.md) and [Qwen](models/qwen.md).
3. Read 2-3 runtime entries to see how serving works. [vLLM](runtimes/vllm.md), [Ollama](runtimes/ollama.md), [llama.cpp](runtimes/llama-cpp.md).
4. Read 2-3 framework entries. [LangGraph](frameworks/langgraph.md), [Smolagents](frameworks/smolagents.md), [Letta](frameworks/letta.md) cover most architectural points.
5. Read the [techniques](techniques/) index. Each technique file is short and self-contained.

### D. "I just want to know what's possible without committing"

Read the views — they're the curated lens:

- [views/by-layer.md](views/by-layer.md) — curated picks per layer.
- [views/by-task.md](views/by-task.md) — best combinations for coding, research, writing, automation, data.
- [views/by-hardware.md](views/by-hardware.md) — what fits in 8 / 12 / 16 / 24 / 24+ GB of VRAM.
- [views/by-license.md](views/by-license.md) — sorted by openness/commercial restriction.

## 5. When you hit a term you don't know

Check the [glossary](GLOSSARY.md) first. If it's not there, file an issue — that's a glossary gap we should close.

## 6. When something looks out of date

The "Last verified" date at the top of each entity is the survey's claim to freshness. If you find something stale:

- Update the entity and bump the date. PR welcome.
- If a project changed name, license, or was archived: also update the [INDEX](README.md#5-views), and add a note in [CONSIDERED.md](CONSIDERED.md) if it's now out of scope.

The survey's value comes from being current; staleness is the main risk we acknowledge in [README §1](README.md#1-why-this-exists).
