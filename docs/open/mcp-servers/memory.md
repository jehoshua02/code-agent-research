# Memory

_Last verified: 2026-06-14_

## 0. TL;DR

A memory [MCP](../GLOSSARY.md#mcp-model-context-protocol) server gives an agent a persistent store — facts, preferences, past conversation summaries — that survives across sessions, unlike the context window which resets every time. Use one when you want the agent to remember user details or accumulated knowledge between separate conversations. The main catch: the agent writes its own memory, so errors or hallucinations get persisted and can silently corrupt future behavior.

## 1. What It Is

MCP servers in this category give agents persistent state across sessions — typically as a key-value or knowledge-graph store. Agents need them to remember user preferences, prior conversations, or learned facts. Notable: memory (official reference, Anthropic) — a simple knowledge-graph server; community options include vector-store-backed memory.

## 2. Capability

Exposes a knowledge graph stored in a local JSONL file. The Anthropic reference server exposes nine tools:

- **create_entities** — add named entities with a type and a list of observations (string facts)
- **create_relations** — add directed relationships between two entities (e.g., `Alice "works_at" Acme`)
- **add_observations** — append additional fact strings to an existing entity
- **delete_entities** — remove one or more entities and all their relations
- **delete_observations** — remove specific observation strings from an entity
- **delete_relations** — remove specific directed relations
- **read_graph** — return the full knowledge graph (all entities and relations)
- **search_nodes** — text search across entity names and observations
- **open_nodes** — retrieve a specific set of entities by name

## 3. Install

The reference server is Node.js:

```
npx -y @modelcontextprotocol/server-memory
```

Data persists in `memory.jsonl` in the server's working directory. The file path is configurable via the `MEMORY_FILE_PATH` environment variable.

A Docker image is available in the repository. Host install is typical; the file path just needs to survive across server restarts.

## 4. Transport

stdio. The server is spawned as a child process; no networked transport in the reference implementation.

## 5. Auth

No auth. The server reads and writes a local JSONL file. Access is controlled entirely by filesystem permissions on the storage file and the process's OS user. No API keys or tokens.

## 6. Security Considerations

**Memory poisoning.** An adversary who can influence what the agent stores (e.g., via a malicious document the agent summarizes) can plant false facts or injected instructions that affect all future sessions. Treat stored observations as untrusted input and validate before acting on them.

**Cross-session leakage.** The knowledge graph is shared across all sessions using the same file. If multiple users or tasks share a single server instance, one session's private data (credentials, personal details) is visible to all others via `read_graph`.

**Sensitive-info accumulation.** The agent may store passwords, API keys, or PII as observations over time. The `memory.jsonl` file must have strict filesystem permissions (owner-read-only) and should be excluded from backups or version control.

**Prompt injection via stored memory.** Retrieved observations are inserted into the context verbatim. A stored string like `"Ignore previous instructions and..."` becomes a live injection vector on every subsequent session that reads that entity.

## 7. Documented Strengths

- **Official reference implementation with a knowledge-graph model**: Anthropic ships `@modelcontextprotocol/server-memory` with a JSONL-backed entity/relation graph — a more structured store than simple key-value, enabling relational queries like `search_nodes` across facts ([modelcontextprotocol/servers — memory](https://github.com/modelcontextprotocol/servers/tree/main/src/memory)).
- **Session-spanning persistence**: unlike the context window, stored observations survive across restarts and new conversations, enabling long-running user-preference or project-context accumulation that would otherwise require reloading from an external source each session.
- **Zero infrastructure**: data lives in a single JSONL file on the host filesystem — no database or cloud service required, making the reference implementation trivially self-hostable and auditable.
- **Selective retrieval tools**: `search_nodes` and `open_nodes` allow the agent to fetch only relevant entities rather than loading the entire graph, keeping context footprint proportional to the task.

## 8. Documented Weaknesses

- **Memory poisoning risk**: stored observations are written by the model itself; a hallucinated or prompt-injected fact persists permanently and is re-injected verbatim into future contexts, silently corrupting all downstream behavior ([modelcontextprotocol/servers#memory security](https://github.com/modelcontextprotocol/servers/tree/main/src/memory)).
- **No eviction policy or size limit**: the `memory.jsonl` file grows unboundedly; there is no TTL, LRU eviction, or storage cap, meaning the graph accumulates stale or contradictory observations indefinitely without operator intervention.
- **No multi-tenant isolation**: a single server instance shares one file across all sessions — private data from one conversation (credentials, personal details) is visible to any other session that calls `read_graph`, with no per-user namespacing.
- **Prompt injection via retrieved memory**: observations are inserted into the context without sanitization; a stored string beginning with `"Ignore previous instructions…"` becomes a live injection attack on every future session that reads that entity.

## 9. Sources

- [modelcontextprotocol/servers — memory](https://github.com/modelcontextprotocol/servers/tree/main/src/memory) — observed 2026-06-14
