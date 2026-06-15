# Web Fetch

_Last verified: 2026-06-14_

## 0. TL;DR

A web-fetch [MCP](../GLOSSARY.md#mcp-model-context-protocol) server lets an agent download the contents of any URL — documentation pages, REST API responses, or plain HTML — and read them as text. Use one when the agent needs to look something up on the web or call a public HTTP API without using a search index. The main catch: the agent fetches whatever URL it decides to visit, so prompt injection via malicious page content is a real attack vector.

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

**SSRF (Server-Side Request Forgery)** is the primary risk. Because the server process makes HTTP requests from inside the network, an LLM instructed to fetch `http://169.254.169.254/latest/meta-data/` (AWS EC2 instance metadata), `http://10.0.0.1/` (internal services), or `file:///etc/passwd` can exfiltrate internal resources that are not reachable from the public internet. The reference server does not block private IP ranges or `file://` URIs by default.

**Unbounded response size** can cause memory exhaustion or DoS: a URL returning a multi-gigabyte response will be buffered in process unless `max_length` is enforced by the caller. The reference server supports `max_length` but does not impose a hard cap server-side.

**Redirect chains** can be exploited to bypass naive allowlists: an allowed public URL redirects (301/302) to an internal address, and the server follows it transparently.

**Prompt injection** via fetched content is a higher-order risk: a page the agent is instructed to fetch may contain adversarial text that hijacks subsequent model behavior.

**Mitigation:** run the server process with a network policy that blocks RFC-1918 ranges and link-local addresses; set `max_length` conservatively; log all fetched URLs for audit; consider an egress allowlist for production deployments.

## 7. Documented Strengths

- **Official reference implementation**: Anthropic maintains `mcp-server-fetch` as a first-party server with stable, documented tool signatures, making it a reliable baseline for any agent that needs HTTP retrieval ([modelcontextprotocol/servers — fetch](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch)).
- **No API key required**: unlike search servers that require paid credentials, the fetch server calls any public URL directly — zero signup friction for documentation lookups, public APIs, or open data sources.
- **Automatic HTML-to-markdown conversion**: returns clean, token-efficient markdown instead of raw HTML, reducing the context footprint of fetched pages and making the output more reliably parseable by the model.
- **Pagination support**: the `start_index` parameter allows the agent to page through large documents in successive calls without re-fetching the beginning, keeping individual responses within MCP message-size limits.

## 8. Documented Weaknesses

- **JavaScript-heavy sites fail**: the server uses a simple HTTP GET with no browser engine; pages that require JavaScript to render (SPAs, React/Next.js apps) return an empty shell or stub HTML rather than useful content ([modelcontextprotocol/servers #46](https://github.com/modelcontextprotocol/servers/issues/46)).
- **No SPA / login-wall support**: pages behind OAuth flows, cookie-based sessions, or CAPTCHA challenges cannot be fetched — the server has no mechanism to carry authentication state across requests.
- **SSRF risk with no built-in IP blocklist**: the reference implementation does not block RFC-1918 or link-local addresses by default, so a prompt-injected instruction to fetch an internal metadata URL (e.g., `169.254.169.254`) succeeds unless the operator adds network-level controls.
- **robots.txt compliance is opt-out, not enforced**: respecting `robots.txt` is the default but can be disabled by the caller at any time, meaning aggressive scraping is a configuration choice rather than a guardrail.

## 9. Sources

- [modelcontextprotocol/servers — fetch](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch) — observed 2026-06-14
