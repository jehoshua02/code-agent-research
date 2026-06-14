# Productivity

_Last verified: 2026-06-14_

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

Sandboxing, allowlists, common footguns.

## 7. Documented Strengths

Documented strengths from maintainer docs or community reports. Cite source.

## 8. Documented Weaknesses

Documented limitations from issue tracker or community reports. Cite source.

## 9. Sources

- [PulseMCP — productivity servers](https://www.pulsemcp.com/servers?q=productivity) — observed 2026-06-14
