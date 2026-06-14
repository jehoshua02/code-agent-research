# Filesystem

_Last verified: 2026-06-14_

## 1. What It Is

MCP servers in this category expose file-tree operations (read, write, list, search, stat) to an agent. Agents need them to inspect and modify repositories or document collections during a task. Notable: filesystem (official reference, Anthropic) for sandbox-rooted file access; community filesystem servers wrap remote storage (S3, Drive, etc.).

## 2. Capability

What it exposes — files, shell, web, browser, database, API, etc.

## 3. Install

Supported platforms. Concrete install steps. Whether host or container is appropriate depends on this server's access needs — call that out. See [../README.md](../README.md#4-deployment-notes) for general reader-facing deployment context.

## 4. Transport

stdio / sse / streamable HTTP.

## 5. Auth

How auth/secrets are handled, if any.

## 6. Security Considerations

Sandboxing, allowlists, common footguns.

## 7. Documented Strengths

Documented strengths from maintainer docs or community reports. Cite source.

## 8. Documented Weaknesses

Documented limitations from issue tracker or community reports. Cite source.

## 9. Sources

- [modelcontextprotocol/servers — filesystem](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem) — observed 2026-06-14
