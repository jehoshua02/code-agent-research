# Open Self-Hosted AI Stack — Survey

Unbiased research on the open, free, self-hostable AI ecosystem. The only ceiling is your hardware. This survey documents the landscape and leaves tradeoffs to the reader.

## Scope

In: open-weight models, self-hostable inference runtimes, open agent frameworks, MCP servers, and techniques. Tasks include coding, research, writing, automation, and data analysis.

Out: closed/proprietary models and SaaS-only tools — those live in `../models/` and `../tools/`.

## Structure

```
models/         — one file per open-weight model variant
runtimes/       — inference engines (ollama, vllm, llama.cpp, ...)
frameworks/     — agent frameworks (langgraph, autogen, crewai, ...)
mcp-servers/    — MCP server implementations
techniques/     — patterns (rag, tool-use, planning, ...)
views/          — cross-cutting comparisons (links only, no duplicated content)
```

Each layer has:

- `TEMPLATE.md` — required structure for entity files in that layer.
- `INDEX.md` — at-a-glance table of all entities in that layer.

Each entity = one file. Small, focused. No multi-topic files.

## Views

- [By layer](views/by-layer.md) — top picks at each layer
- [By task](views/by-task.md) — coding, research, writing, automation, data
- [By hardware](views/by-hardware.md) — 8GB / 16GB / 24GB+ stacks
- [By license](views/by-license.md) — Apache 2.0, MIT, non-commercial, etc.
