# Open Self-Hosted AI Stack — Survey

Unbiased research on the open, free, self-hostable AI ecosystem. Entity files (per model, runtime, framework, etc.) document facts neutrally. Views are where opinion lives.

**Breadth before depth.** This survey documents every open-weight model and self-hostable component worth knowing about — including ones that don't fit on the reader's current hardware. The `by-hardware` view filters for fit; the survey itself does not. Hardware is a runtime constraint, not a research-scope constraint.

## 1. Scope

In: open-weight models, self-hostable inference runtimes, open agent frameworks, MCP servers, and techniques. Tasks include coding, research, writing, automation, and data analysis.

In-scope regardless of size: a 405B model with no chance of running on a 8 GB card still belongs here.

Relationship to `../models/` and `../tools/`: those track the broader coding-tool comparison (open and closed). This survey is task-agnostic and covers the open ecosystem at full breadth.

## 2. Structure

```
models/         — one file per open-weight model family (variants enumerated within)
runtimes/       — inference engines (ollama, vllm, llama.cpp, ...)
frameworks/     — agent frameworks (langgraph, autogen, crewai, ...)
mcp-servers/    — MCP server implementations
techniques/     — patterns (rag, tool-use, planning, ...)
views/          — curated cross-cuts (opinion layer; links to entities)
```

Each layer has:

- `TEMPLATE.md` — required structure for entity files in that layer.
- `INDEX.md` — full table of all entities in that layer (unbiased reference).

Each entity = one file. Small, focused. No multi-topic files. Authoritative facts live in the entity file; views excerpt or link.

## 3. Deployment notes

Entities are surveyed at full breadth regardless of platform. Each entity file documents its own supported platforms. The notes below are reader-facing context, not a scope filter — the survey includes Linux-only, Mac-only (e.g. MLX), and Windows-native components alike.

Common patterns observed in entries so far:

- **Runtimes** typically need GPU access and run best on bare-metal Linux. WSL2 on Windows supports NVIDIA CUDA. Apple Silicon runtimes (MLX, llama.cpp Metal) target macOS directly. ROCm runtimes target AMD on Linux.
- **Agent frameworks** typically need broad filesystem and process access; they run best on the agent operator's host OS directly, not inside a container.
- **MCP servers** vary — some need host access (filesystem, shell), some are isolated (web fetch, remote API) and run fine in containers.

If a model or runtime requires a platform the reader doesn't currently have, that is a deployment cost the reader can choose to pay — not a reason to exclude it from the survey.

## 4. Views

- [By layer](views/by-layer.md) — curated picks at each layer
- [By task](views/by-task.md) — coding, research, writing, automation, data
- [By hardware](views/by-hardware.md) — 8 / 12 / 16 / 24 / 24+ GB tiers
- [By license](views/by-license.md) — Apache 2.0, MIT, custom permissive, source-available
