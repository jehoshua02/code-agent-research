# Database

_Last verified: 2026-06-14_

## 1. What It Is

MCP servers in this category expose SQL databases — list tables, execute queries (often read-only by default), inspect schemas. Agents need them for data analysis and reporting tasks. Notable community: PostgreSQL, SQLite, MySQL, BigQuery, Snowflake, and DuckDB MCP servers, typically requiring a connection string.

## 2. Capability

Exposes SQL database operations to the agent. Common tools across implementations:

- **query** / **execute_query** — run a SQL statement and return results as rows (read-only by default in most implementations; write access is typically opt-in)
- **list_tables** — enumerate tables in the connected database
- **describe_table** / **get_schema** — return column names, types, and constraints for a table
- **list_schemas** — enumerate schemas or databases available on the server
- **explain_query** — run `EXPLAIN` or `EXPLAIN ANALYZE` and return the query plan (PostgreSQL/MySQL)

Specific implementations add engine-specific tools: DuckDB servers expose in-process file querying (CSV, Parquet); BigQuery/Snowflake servers expose project/dataset enumeration; SQLite servers include tools for opening multiple database files.

## 3. Install

No Anthropic reference implementation. Community servers are split between Node.js and Python:

PostgreSQL (Node.js):

```
npx -y @modelcontextprotocol/server-postgres postgresql://user:pass@localhost:5432/db
```

PostgreSQL (Python / crystaldba variant):

```
uvx postgres-mcp --access-mode=unrestricted
```

SQLite (Node.js or Python, various packages) — connection string is a local file path; host install is standard.

BigQuery, Snowflake, and DuckDB servers each have their own npm or PyPI packages. Managed database servers that are not on localhost should be accessed from the host (or VPN) directly; running inside a container requires the container to have network access to the database.

## 4. Transport

stdio for all major community implementations. The client spawns the server process and passes the connection string as a CLI argument or environment variable. Some servers support SSE as an alternative when a persistent networked endpoint is needed.

## 5. Auth

Database credentials are passed at startup, not through MCP protocol-level auth:

- **Connection string** (most common): `postgresql://user:password@host:5432/dbname` passed as CLI argument or `DATABASE_URL` environment variable
- **Managed cloud databases** (BigQuery, Snowflake): credentials via service account JSON file path or cloud SDK ambient credentials (ADC for GCP, `~/.snowflake/config.toml` for Snowflake)
- No MCP-layer auth; the server process inherits OS-level permissions

## 6. Security Considerations

Sandboxing, allowlists, common footguns.

## 7. Documented Strengths

Documented strengths from maintainer docs or community reports. Cite source.

## 8. Documented Weaknesses

Documented limitations from issue tracker or community reports. Cite source.

## 9. Sources

- [PulseMCP — database servers](https://www.pulsemcp.com/servers?q=database) — observed 2026-06-14
