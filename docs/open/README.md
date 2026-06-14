# Open Self-Hosted AI Stack — Survey

Unbiased research on the open, free, self-hostable AI ecosystem. The only ceiling is your hardware. This survey documents the landscape and leaves tradeoffs to the reader.

## 1. Scope

In: open-weight models, self-hostable inference runtimes, open agent frameworks, MCP servers, and techniques. Tasks include coding, research, writing, automation, and data analysis.

Relationship to `../models/` and `../tools/`: those track the broader coding-tool comparison (open and closed). This survey is task-agnostic and limited to what you can run yourself.

## 2. Structure

```
models/         — one file per open-weight model variant
runtimes/       — inference engines (ollama, vllm, llama.cpp, ...)
frameworks/     — agent frameworks (langgraph, autogen, crewai, ...)
mcp-servers/    — MCP server implementations
techniques/     — patterns (rag, tool-use, planning, ...)
views/          — cross-cutting comparisons (curated, link to entities)
```

Each layer has:

- `TEMPLATE.md` — required structure for entity files in that layer.
- `INDEX.md` — full table of all entities in that layer.

Each entity = one file. Small, focused. No multi-topic files. Authoritative facts live in the entity file; views excerpt or link.

## 3. Deployment principle

These tools need either GPU access (runtimes) or broad host control (agents). Run them on a **Linux host** — bare-metal Linux, WSL2 on Windows, OrbStack on Mac, or a cloud Linux VM. Use containers only for components where isolation justifies the access tradeoffs (most MCP servers, optional for runtimes if GPU passthrough is set up).

## 4. Views

- [By layer](views/by-layer.md) — opinionated top picks at each layer
- [By task](views/by-task.md) — coding, research, writing, automation, data
- [By hardware](views/by-hardware.md) — 8 / 12 / 16 / 24 / 24+ GB tiers
- [By license](views/by-license.md) — Apache 2.0, MIT, custom permissive, source-available
