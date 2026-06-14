# MCP Servers — Index

One row per category. Each entry covers notable implementations within that category. Transport column reflects the dominant transport across the named implementations.

| Server | Capability | License | Transport | Notes |
|---|---|---|---|---|
| [Filesystem](filesystem.md) | Read/write/list/search files | MIT | stdio | Anthropic reference + community |
| [Shell](shell.md) | Run shell commands | varies | stdio | community only (no Anthropic reference) |
| [Web Fetch](web-fetch.md) | Fetch URLs → markdown | MIT | stdio | Anthropic reference + community |
| [Web Search](web-search.md) | Search engine APIs | varies | stdio; streamable HTTP (hosted) | community (Brave, Exa, Tavily, etc.) |
| [Browser Control](browser-control.md) | Drive headless browser | Apache-2.0 | stdio; streamable HTTP (--port) | community (Playwright, Puppeteer) |
| [Git / GitHub](git-github.md) | Git ops + hosted-platform APIs | MIT | stdio | Anthropic reference (git) + community (github, gitlab) |
| [Database](database.md) | SQL query/inspect | varies | stdio | community (Postgres, SQLite, etc.) |
| [Memory](memory.md) | Persistent knowledge-graph state | MIT | stdio | Anthropic reference + community |
| [Code Execution](code-execution.md) | Sandboxed code run | varies | stdio; streamable HTTP (cloud) | community (E2B, Docker runners) |
| [Cloud APIs](cloud-apis.md) | AWS / GCP / Azure / Cloudflare | varies | stdio; streamable HTTP (hosted) | community + official (Cloudflare) |
| [Productivity](productivity.md) | Calendar, email, notes, tasks | varies | stdio; streamable HTTP (some) | community (Google, Notion, Linear, Slack) |
