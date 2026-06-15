---
name: "Database"
license_category: "mit"
status: "active"
url: "https://github.com/modelcontextprotocol/servers/tree/main/src/postgres"
last_verified: "2026-06-14"
transport: "stdio"
has_anthropic_reference: false
auth: "api-key"
best_for: ["research", "data", "automation"]
notes: "Auth is a database connection string/credentials, not a typical API key; read-only mode is the safe default."
---

# Database

_Last verified: 2026-06-14_

## 0. TL;DR

A database [MCP](../GLOSSARY.md#mcp-model-context-protocol) server lets an agent query SQL databases, inspect schemas, and retrieve data — turning natural-language questions into real query results. Use one when you want the agent to answer questions about data in PostgreSQL, SQLite, BigQuery, or similar stores without hardcoding the SQL yourself. The main catch: most servers default to read-only access for safety, but even read-only access exposes your full schema and data, so keep credentials scoped to a least-privilege role.

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

**SQL injection via prompt-as-query.** Agent-generated SQL is passed directly to the database; a malicious or ambiguous prompt can produce `DROP TABLE` or `DELETE FROM` statements even when only a read was intended. Use a read-only database role or connection string to eliminate write risk.

**Data exfiltration.** A broad `SELECT *` across tables can return sensitive PII or secrets in the model context window, which may be logged. Restrict the database user to only the schemas and tables the agent legitimately needs.

**Row-level security bypass.** Some MCP servers connect as a superuser to avoid permission errors; this bypasses any RLS policies enforced at the application layer. Always connect with the least-privileged database role.

**Schema enumeration.** `list_tables` and `describe_table` expose full schema structure, giving an attacker (or a misbehaving agent) a roadmap to sensitive tables without executing a single data query. Consider restricting these tools or the schemas they can enumerate.

## 7. Documented Strengths

- **Direct query execution with real results**: agents receive actual row data rather than API abstractions, enabling precise aggregations, joins, and analytic queries that would be impractical through any higher-level interface ([modelcontextprotocol/servers — postgres](https://github.com/modelcontextprotocol/servers/tree/main/src/postgres)).
- **Schema introspection built in**: `list_tables` and `describe_table` tools let the agent self-orient in an unfamiliar database — no need to pre-load schema documentation into the prompt, reducing setup overhead for data analysis tasks.
- **Broad engine coverage**: community servers exist for PostgreSQL, SQLite, MySQL, BigQuery, Snowflake, DuckDB, and others; the MCP tool interface is largely consistent across them, making it easy to switch databases without rewriting agent logic.
- **Read-only mode as the safe default**: most PostgreSQL and SQLite implementations default to read-only connections, giving operators a safe baseline where destructive queries are prevented at the connection level rather than relying on prompt instructions.

## 8. Documented Weaknesses

- **SQL injection via agent-generated queries**: there is no parameterization layer between the model's output and the database; a prompt-injected `; DROP TABLE users; --` suffix in an agent-constructed query executes directly unless the server enforces read-only mode ([postgres-mcp security notes](https://github.com/crystaldba/postgres-mcp)).
- **No built-in row-limit enforcement**: a `SELECT *` on a multi-million-row table returns all rows into the MCP response buffer, potentially exhausting memory and filling the model's context window; most servers rely on the caller to add `LIMIT` clauses.
- **Full schema exposed by default**: `list_tables` enumerates every table the connected role can see, revealing the entire schema structure — including sensitive table names — to the agent and any prompt injector in its context.
- **Connection string contains plaintext credentials**: database passwords are passed as CLI arguments or environment variables, where they appear in process lists (`ps aux`), MCP host debug logs, and shell history — a persistent credential-leak vector with no rotation mechanism in the server itself.

## 9. Sources

- [PulseMCP — database servers](https://www.pulsemcp.com/servers?q=database) — observed 2026-06-14
