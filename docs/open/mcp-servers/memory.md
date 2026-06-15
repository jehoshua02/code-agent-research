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

Documented strengths from maintainer docs or community reports. Cite source.

## 8. Documented Weaknesses

Documented limitations from issue tracker or community reports. Cite source.

## 9. Sources

- [modelcontextprotocol/servers — memory](https://github.com/modelcontextprotocol/servers/tree/main/src/memory) — observed 2026-06-14
