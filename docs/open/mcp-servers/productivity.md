# Productivity

_Last verified: 2026-06-14_

## 0. TL;DR

Productivity [MCP](../GLOSSARY.md#mcp-model-context-protocol) servers connect an agent to tools like Google Calendar, Gmail, Notion, Linear, and Slack — letting it schedule meetings, draft messages, or update tasks on your behalf. Use one when building a personal assistant or workflow automation agent that needs to act inside your existing toolset. The main catch: these servers use OAuth and touch real accounts, so a prompt-injection attack or a misunderstood instruction can send emails or delete tasks for real.

## 1. What It Is

MCP servers in this category expose personal/team productivity tools — calendar, email, notes, task management. Agents need them for scheduling, drafting messages, and organizing work. Notable community: Google Calendar, Gmail, Notion, Linear, Slack, and Microsoft 365 MCP servers; usually require OAuth.

## 2. Capability

Exposes personal and team productivity service operations. Tools vary by service; representative examples:

**Notes / Docs (Notion):**
- **search** — full-text search across pages and databases
- **get_page** / **create_page** / **update_page** — CRUD for Notion pages in Markdown
- **query_database** — filter and retrieve rows from a Notion database

**Task management (Linear):**
- **list_issues** / **create_issue** / **update_issue** — manage issues with status, priority, and assignee
- **list_projects** / **list_teams** — enumerate Linear projects and teams

**Messaging (Slack):**
- **post_message** — send a message to a channel
- **list_channels** / **get_channel_history** — enumerate channels and retrieve message history
- **search_messages** — search across workspace messages

**Email (Gmail) / Calendar (Google Calendar):**
- **list_messages** / **send_email** / **search_emails** — read and send email
- **list_events** / **create_event** — read and create calendar events

## 3. Install

All major productivity servers are Node.js and install via npx. Examples:

```
npx -y @notionhq/notion-mcp-server
```

```
npx -y @modelcontextprotocol/server-slack
```

Linear, Gmail, Google Calendar, and Microsoft 365 servers each have their own npm packages following the same npx pattern. Host install is standard; no special container requirement since servers make outbound API calls.

## 4. Transport

stdio for all locally-spawned implementations. Some servers (Notion's `--transport http` flag) support HTTP listening mode for use from remote clients. Hosted variants use streamable HTTP.

## 5. Auth

OAuth 2.0 or service API tokens, depending on the provider:

- **Notion**: OAuth 2.0 (version 2.0+ of the official server); earlier versions used an `NOTION_API_KEY` integration token
- **Slack**: Slack OAuth app token (`SLACK_BOT_TOKEN`) with appropriate scopes granted during app installation
- **Linear**: Personal API key (`LINEAR_API_KEY`) or OAuth app flow
- **Gmail / Google Calendar**: OAuth 2.0 via Google; credentials JSON from Google Cloud Console, with `credentials.json` and a refresh token stored locally
- **Microsoft 365**: OAuth 2.0 via Azure AD app registration (`MICROSOFT_CLIENT_ID`, `MICROSOFT_CLIENT_SECRET`, `MICROSOFT_TENANT_ID`)

## 6. Security Considerations

**Account-wide write access.** OAuth tokens typically grant write access to the entire account — not just the resources relevant to the task. A miscued agent can delete all calendar events, archive all email, or wipe all Notion pages. Prefer tokens scoped to specific calendars, channels, or workspaces where the provider allows it.

**Mass-action mistakes.** Tools like `send_email` or `post_message` applied in a loop can spam hundreds of contacts or channels before a human can intervene. Rate-limit outbound write calls and require confirmation before bulk actions.

**OAuth scope creep.** Servers often request broad OAuth scopes (e.g., `https://mail.google.com/`) to avoid re-authorization later. Audit the scopes granted during setup and revoke the token if they exceed what the agent actually needs.

**Token storage.** Refresh tokens stored in local files (`credentials.json`) grant long-lived access to personal accounts. Protect these files with owner-only permissions and exclude them from version control; rotation on suspected compromise is manual for most providers.

## 7. Documented Strengths

- **Official first-party servers from major vendors**: Notion, Slack, and Linear each publish and maintain their own MCP servers, ensuring tool signatures track the provider's API and receive timely updates for breaking API changes ([notionhq/notion-mcp-server](https://github.com/makenotion/notion-mcp-server), [@modelcontextprotocol/server-slack](https://github.com/modelcontextprotocol/servers/tree/main/src/slack)).
- **High-value automation on existing accounts**: agents can create calendar events, draft and send emails, and post Slack messages without custom API integrations — tasks that represent the majority of personal-assistant workloads.
- **Structured data access**: services like Notion databases and Linear issue lists expose typed objects (status, priority, due date, assignee) that agents can filter and act on precisely, rather than parsing unstructured text.
- **OAuth 2.0 token scoping**: providers like Google and Microsoft support fine-grained OAuth scope declarations, allowing operators to grant the agent access only to specific resources (e.g., a single calendar) rather than the whole account.

## 8. Documented Weaknesses

- **Tokens grant account-wide write access by default**: most server setup guides request broad OAuth scopes (e.g., `https://mail.google.com/`) rather than minimal ones, giving an agent the ability to delete all email, events, or pages with no additional confirmation.
- **Refresh tokens in local files are long-lived credentials**: `credentials.json` files storing OAuth refresh tokens grant persistent access to personal accounts; loss or accidental commit of these files yields indefinite account access with no automatic expiry ([Gmail MCP setup](https://github.com/modelcontextprotocol/servers/tree/main/src/gmail)).
- **Mass-action mistakes are hard to undo**: `send_email` or `post_message` in a loop can spam hundreds of contacts before a human intervenes — most providers have no unsend capability and rate-limit only at high thresholds.
- **Cross-service orchestration complexity**: building workflows that span Calendar + Gmail + Slack requires chaining multiple MCP servers with separate auth contexts; there is no standard MCP mechanism for cross-server transaction coordination or rollback.

## 9. Sources

- [PulseMCP — productivity servers](https://www.pulsemcp.com/servers?q=productivity) — observed 2026-06-14
