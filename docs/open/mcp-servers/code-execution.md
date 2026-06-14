# Code Execution

_Last verified: 2026-06-14_

## 1. What It Is

MCP servers in this category run code in a sandboxed environment (Python, JavaScript, etc.) and return results. Agents need them for data analysis, math, and any task safer to compute than to reason about. Notable community: E2B Code Interpreter MCP, Pyodide-based browsers, and various Docker-sandboxed runners.

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

- [PulseMCP — code execution servers](https://www.pulsemcp.com/servers?q=code) — observed 2026-06-14
