---
name: "Filesystem"
license_category: "mit"
status: "active"
url: "https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem"
last_verified: "2026-06-14"
transport: "stdio"
has_anthropic_reference: true
auth: "none"
best_for: ["coding", "research", "automation", "data"]
notes: ""
---

# Filesystem

_Last verified: 2026-06-14_

## 0. TL;DR

A filesystem [MCP](../GLOSSARY.md#mcp-model-context-protocol) server lets an agent read, write, and navigate files on disk — think of it as giving the agent access to your file manager. Pick one when you want the agent to inspect a codebase, edit documents, or generate output files. The main catch: always restrict the server to a sandboxed directory, because a misconfigured allowlist lets the agent read or overwrite anything on the host machine.

## 1. What It Is

MCP servers in this category expose file-tree operations (read, write, list, search, stat) to an agent. Agents need them to inspect and modify repositories or document collections during a task. Notable: filesystem (official reference, Anthropic) for sandbox-rooted file access; community filesystem servers wrap remote storage (S3, Drive, etc.).

## 2. Capability

Exposes file-tree operations against a set of allowed directories configured at startup. Operations include:

- **read_file / read_text_file** — read full file contents; supports head/tail line ranges
- **read_media_file** — read image or audio files as base64 with MIME type
- **read_multiple_files** — batch read several files in one call
- **write_file** — create or overwrite a file
- **edit_file** — apply targeted string replacements within a file
- **create_directory** — create directories (including nested paths), idempotent
- **list_directory / list_directory_with_sizes** — list directory contents with optional size info
- **directory_tree** — return recursive directory structure as JSON
- **move_file** — move or rename files and directories
- **search_files** — glob-pattern recursive file search
- **get_file_info** — retrieve metadata (size, timestamps, permissions)
- **list_allowed_directories** — report which directories the server is permitted to access

## 3. Install

Run directly with npx (Node.js) or via Docker. The server takes one or more allowed directory paths as arguments.

```
npx -y @modelcontextprotocol/server-filesystem /path/to/allowed/dir
```

```
docker run -i --rm mcp/filesystem /projects
```

The reference implementation is Node.js. Host install is typical for local dev; Docker is appropriate when you want to limit which host paths are visible to the process. Build from source: `docker build -t mcp/filesystem -f src/filesystem/Dockerfile .`

## 4. Transport

stdio (the process is spawned as a child; JSON-RPC flows over stdin/stdout). No networked transport in the reference implementation.

## 5. Auth

No credential-based auth. Access control is path-based: the server enforces that all operations stay within directories specified at launch (via CLI args) or provided at runtime via the MCP Roots protocol (`roots/list` / `roots/list_changed`). No API keys or tokens.

## 6. Security Considerations

**Path traversal** is the primary risk: a malicious or hallucinated path like `../../etc/passwd` can escape the intended sandbox if the server's path-normalization logic has gaps. The reference server resolves symlinks before checking allow-lists, but community implementations vary. **Symlink escape** is a related vector — a symlink inside an allowed directory can point anywhere on the filesystem; reads or writes follow the link unless the server explicitly rejects symlinks that resolve outside allowed roots.

**Accidental writes** are a persistent footgun: `write_file` will silently overwrite existing content. There is no dry-run or recycle-bin mechanism. An LLM that mis-identifies a target path can destroy files irreversibly.

**Sensitive-file exposure** is a passive risk in any allowed directory that happens to contain credentials (`.env`, SSH keys, `~/.aws/credentials`). The server has no concept of file sensitivity; it will read anything the OS user can read.

**Mitigation:** restrict allowed directories to the minimum necessary scope; run the server as a low-privilege user; prefer container-mount isolation (Docker with a bind-mount to a specific project directory) over host-wide access.

## 7. Documented Strengths

- **Official reference implementation**: Anthropic ships and maintains `@modelcontextprotocol/server-filesystem` as the canonical example, giving it stable, well-documented tool signatures that community clients target first ([modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem)).
- **Simple, auditable permission model**: allowed directories are declared at startup as CLI arguments, making the attack surface easy to review and lock down without runtime configuration complexity.
- **Batch read support**: `read_multiple_files` lets an agent fetch many files in a single round-trip, reducing latency for codebase-scan tasks.
- **MCP Roots integration**: supports the `roots/list` protocol so hosts can dynamically advertise which directories the agent may access, enabling per-session scoping.

## 8. Documented Weaknesses

- **No native diff / patch operation**: agents must read an entire file, compute a replacement, and write the whole thing back — there is no line-level patch primitive, which wastes tokens and risks clobbering concurrent edits ([modelcontextprotocol/servers #59](https://github.com/modelcontextprotocol/servers/issues/59)).
- **Blocking I/O on large files**: the reference Node.js implementation reads files synchronously into memory; multi-megabyte files stall the server process and can exhaust the MCP message size budget.
- **Silent overwrite**: `write_file` has no dry-run or backup mode — a hallucinated path causes irreversible data loss with no recycle-bin fallback.
- **No directory-level watch / streaming**: agents must poll `list_directory` to detect changes; there is no event-push mechanism for file-system notifications.

## 9. Sources

- [modelcontextprotocol/servers — filesystem](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem) — observed 2026-06-14
