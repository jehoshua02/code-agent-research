# Cloud APIs

_Last verified: 2026-06-14_

## 1. What It Is

MCP servers in this category wrap cloud-provider APIs (AWS, GCP, Azure) to expose resources, run commands, or query telemetry. Agents need them for cloud operations, cost analysis, and infrastructure-as-code workflows. Notable community: AWS MCP, GCP MCP, Azure MCP, and Cloudflare's official MCP servers.

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

- [PulseMCP — cloud provider servers](https://www.pulsemcp.com/servers?q=cloud) — observed 2026-06-14
