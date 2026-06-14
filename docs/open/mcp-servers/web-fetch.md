# Web Fetch

_Last verified: 2026-06-14_

## 1. What It Is

MCP servers in this category fetch HTTP(S) URLs and return content (HTML, JSON, markdown). Agents need them to read documentation, fetch APIs, or scrape pages. Notable: fetch (official reference, Anthropic); community variants add markdown conversion and content-type handling.

## 2. Capability

Exposes HTTP(S) retrieval and content conversion. The Anthropic reference server (`mcp-server-fetch`) exposes a single tool:

- **fetch** — fetch a URL and return its contents as markdown (HTML is converted) or raw HTML; parameters include `url`, `max_length`, `start_index` (for pagination through large pages), and `raw` (return HTML instead of markdown)

Community variants extend this pattern with additional tools for specific content types, multi-URL batching, or cookie/header injection.

## 3. Install

The Anthropic reference server is Python-based and installs via `uvx`:

```
uvx mcp-server-fetch
```

Or via pip:

```
pip install mcp-server-fetch
python -m mcp_server_fetch
```

Community Node.js variants install via npx:

```
npx -y @some-org/mcp-fetch
```

Host install is standard; no special container requirement since the server makes outbound HTTP calls rather than accessing local resources.

## 4. Transport

stdio. The process is spawned by the MCP client; no networked listening port in the reference implementation.

## 5. Auth

No auth. The server makes outbound requests to arbitrary URLs using a configurable `User-Agent` header. It respects `robots.txt` by default (can be disabled). Proxy configuration is supported via environment variable. No API keys or tokens are required for the server itself; target URLs may have their own auth requirements which the caller must embed in the URL or pass via headers (implementation-dependent).

## 6. Security Considerations

Sandboxing, allowlists, common footguns.

## 7. Documented Strengths

Documented strengths from maintainer docs or community reports. Cite source.

## 8. Documented Weaknesses

Documented limitations from issue tracker or community reports. Cite source.

## 9. Sources

- [modelcontextprotocol/servers — fetch](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch) — observed 2026-06-14
