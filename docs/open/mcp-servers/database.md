# Database

_Last verified: 2026-06-14_

## 1. What It Is

MCP servers in this category expose SQL databases — list tables, execute queries (often read-only by default), inspect schemas. Agents need them for data analysis and reporting tasks. Notable community: PostgreSQL, SQLite, MySQL, BigQuery, Snowflake, and DuckDB MCP servers, typically requiring a connection string.

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

- [PulseMCP — database servers](https://www.pulsemcp.com/servers?q=database) — observed 2026-06-14
