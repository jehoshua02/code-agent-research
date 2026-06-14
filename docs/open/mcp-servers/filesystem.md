# Filesystem

_Last verified: 2026-06-14_

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

Documented strengths from maintainer docs or community reports. Cite source.

## 8. Documented Weaknesses

Documented limitations from issue tracker or community reports. Cite source.

## 9. Sources

- [modelcontextprotocol/servers — filesystem](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem) — observed 2026-06-14
