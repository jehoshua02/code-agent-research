# Web Search

_Last verified: 2026-06-14_

## 1. What It Is

MCP servers in this category expose a search engine (web, code, or vertical) to the agent. Agents need them for current information beyond the model's training cutoff. Notable community servers wrap Brave Search, Exa, Tavily, Perplexity, and Google Programmable Search; each requires a provider API key.

## 2. Capability

Exposes one or more search tools backed by a third-party search API. Common tools across implementations:

- **brave_web_search** / **web_search** — submit a query string, return ranked results with title, URL, and snippet
- **brave_local_search** (Brave server) — location-aware search for local businesses and places
- **search** (Tavily) — web search optimized for factual/research queries; returns full-text content extraction alongside snippets
- **search** / **find_similar** (Exa) — neural search with semantic similarity; supports date filtering and domain restrictions
- Multi-provider servers (e.g., mcp-omnisearch) expose a unified interface wrapping Brave, Tavily, Exa, Kagi, and others under separate named tools

## 3. Install

All major implementations are Node.js and install via npx. Examples:

```
npx -y @brave/brave-search-mcp-server
```

```
npx -y tavily-mcp
```

Exa and other providers follow the same npx pattern with their own package names. No Anthropic reference implementation exists for this category. Host install is standard; the server makes outbound API calls.

## 4. Transport

stdio by default for all major local implementations. The Brave server supports `--transport http` for an HTTP listening mode. Tavily also offers a hosted remote MCP endpoint reachable via streamable HTTP.

## 5. Auth

Provider API key required in all cases, passed as an environment variable:

- Brave: `BRAVE_API_KEY`
- Tavily: `TAVILY_API_KEY`
- Exa: `EXA_API_KEY`

Keys are obtained from each provider's developer console. Tavily's remote hosted server additionally supports OAuth for the remote transport variant.

## 6. Security Considerations

Sandboxing, allowlists, common footguns.

## 7. Documented Strengths

Documented strengths from maintainer docs or community reports. Cite source.

## 8. Documented Weaknesses

Documented limitations from issue tracker or community reports. Cite source.

## 9. Sources

- [PulseMCP — search servers](https://www.pulsemcp.com/servers?q=search) — observed 2026-06-14
