# Open Self-Hosted AI Stack — Survey

Unbiased research on the open, free, self-hostable AI ecosystem. The only ceiling is your hardware. Entity files (per model, runtime, framework, etc.) document facts neutrally. Views are where opinion lives.

## 1. Scope

In: open-weight models, self-hostable inference runtimes, open agent frameworks, MCP servers, and techniques. Tasks include coding, research, writing, automation, and data analysis.

Relationship to `../models/` and `../tools/`: those track the broader coding-tool comparison (open and closed). This survey is task-agnostic and limited to what you can run yourself.

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

## 3. Deployment principle

Runtimes need GPU access; agent frameworks need broad host control. Run them on a **Linux host**:

- Bare-metal Linux on the GPU box (preferred for runtimes).
- WSL2 on Windows (GPU passthrough supported with current NVIDIA drivers).
- Cloud Linux VM (rented GPU).
- OrbStack on Mac is fine for non-GPU agent/MCP work, but does not give CUDA — don't use it for runtimes that need NVIDIA acceleration.

Containers fit components that don't need host access — many MCP servers, isolated tools, web-scoped services. Use them where the access tradeoffs justify the isolation.

## 4. Views

- [By layer](views/by-layer.md) — curated picks at each layer
- [By task](views/by-task.md) — coding, research, writing, automation, data
- [By hardware](views/by-hardware.md) — 8 / 12 / 16 / 24 / 24+ GB tiers
- [By license](views/by-license.md) — Apache 2.0, MIT, custom permissive, source-available
