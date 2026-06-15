# Web Search

_Last verified: 2026-06-14_

## 0. TL;DR

A web-search [MCP](../GLOSSARY.md#mcp-model-context-protocol) server lets an agent query a search engine and get back ranked results — useful whenever the agent needs current information that postdates its training cutoff. Use one when building a research or question-answering agent that should cite up-to-date sources. The main catch: every server requires a paid third-party API key (Brave, Exa, Tavily, etc.), and result quality varies significantly between providers.

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

**Query exfiltration** is a subtle but real risk: every search query is transmitted to a third-party provider (Brave, Tavily, Exa, etc.). If the agent constructs queries from sensitive context — internal project names, customer data, proprietary code identifiers — that information leaves the operator's infrastructure and appears in provider logs. This applies even when the search result itself is never acted on.

**API key exposure** follows from how keys are configured: environment variables in process-level config are readable by any process running as the same user, and are often logged by MCP host applications in debug output or error traces. A leaked key allows unlimited query issuance at the operator's expense.

**Quota abuse and cost amplification** are operational risks. An LLM in an agentic loop can issue hundreds of search calls in a single session. Paid-tier APIs (Brave, Exa, Tavily) bill per query; an unbounded loop can generate significant charges or exhaust a monthly quota.

**Rate-limit triggering** can cause downstream task failure: most providers enforce per-minute or per-day rate limits, and a burst of agent-driven queries may hit them, causing the server to return errors and the agent to stall or retry in a loop.

**Mitigation:** treat search queries as potentially sensitive; scope API keys to search-only permissions and set spending limits in the provider console; impose a per-session query budget in the agent orchestrator; avoid passing sensitive identifiers into search queries.

## 7. Documented Strengths

Documented strengths from maintainer docs or community reports. Cite source.

## 8. Documented Weaknesses

Documented limitations from issue tracker or community reports. Cite source.

## 9. Sources

- [PulseMCP — search servers](https://www.pulsemcp.com/servers?q=search) — observed 2026-06-14
