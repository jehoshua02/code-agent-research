# MCP Servers — Index

One row per category. Each entry covers notable implementations within that category. Transport column reflects the dominant transport across the named implementations.

| Server | Capability | License | Transport | Notes |
|---|---|---|---|---|
| [Browser Control](browser-control.md) | Browser Control | _stub_ | stdio | Dominant implementation is Microsoft's playwright-mcp; supports HTTP transport via --port flag. |
| [Cloud APIs](cloud-apis.md) | Cloud APIs | _stub_ | stdio | Cloudflare's official server uses OAuth 2.1 with streamable HTTP; AWS/GCP community servers use stdio with ambient SDK credentials. |
| [Code Execution](code-execution.md) | Code Execution | _stub_ | stdio | E2B is the dominant cloud-sandboxed option and requires an API key; local Docker runners need no auth. |
| [Database](database.md) | Database | _stub_ | stdio | Auth is a database connection string/credentials, not a typical API key; read-only mode is the safe default. |
| [Filesystem](filesystem.md) | Filesystem | _stub_ | stdio | _stub_ |
| [Git / GitHub](git-github.md) | Git / GitHub | _stub_ | stdio | Local git server requires no auth; GitHub/GitLab servers require a personal access token. |
| [Memory](memory.md) | Memory | _stub_ | stdio | Reference implementation stores data in a local JSONL file; no multi-tenant isolation. |
| [Productivity](productivity.md) | Productivity | _stub_ | stdio | OAuth is the dominant auth pattern (Google, Notion, Microsoft 365); some providers use bot/API tokens instead. |
| [Shell](shell.md) | Shell | _stub_ | stdio | No Anthropic reference implementation; highest-risk MCP category due to arbitrary command execution. |
| [Web Fetch](web-fetch.md) | Web Fetch | _stub_ | stdio | _stub_ |
| [Web Search](web-search.md) | Web Search | _stub_ | stdio | All implementations require a paid third-party API key (Brave, Exa, Tavily, etc.). |
