# Browser Control

_Last verified: 2026-06-14_

## 1. What It Is

MCP servers in this category drive a headless browser (Playwright, Puppeteer, or Chrome DevTools Protocol) to navigate, click, and extract content. Agents need them for sites that require JavaScript rendering or interactive flows. Notable community: playwright-mcp, puppeteer-based servers, chrome-devtools-mcp.

## 2. Capability

Exposes a headless (or headed) browser that the agent can drive programmatically. Tools vary by underlying engine but commonly include:

- **navigate** — load a URL in the browser
- **screenshot** — capture the current page as an image
- **click** — click an element identified by selector or coordinates
- **type** / **fill** — type text into an input field
- **evaluate** / **execute_js** — run arbitrary JavaScript in the page context
- **get_content** / **extract_text** — return the page's text or HTML content
- **wait_for** — wait for a selector, URL change, or network idle
- **new_page** / **close_page** — manage browser tabs or pages

Some servers (e.g., microsoft/playwright-mcp) also expose accessibility-tree–based element selection in addition to CSS selectors.

## 3. Install

The dominant implementation is Microsoft's official Playwright MCP server (Node.js):

```
npx @playwright/mcp@latest
```

Community Puppeteer-based servers follow the same npx pattern. Playwright browsers are auto-downloaded by Playwright on first run.

**Host vs container:** Headed browser on a system without a display requires `DISPLAY` to be set (Linux/X11) or using a headless config. For isolated, reproducible environments, run the server inside a container with Xvfb or use the `--headless` flag. The `--port` flag switches to HTTP transport for running in a container with the client connecting over the network.

## 4. Transport

stdio by default (the server is spawned as a child process). When launched with `--port <N>`, the server listens on HTTP (streamable HTTP / SSE), enabling use from remote clients or when the browser process cannot be a child of the MCP host.

## 5. Auth

No credential-based auth for the MCP protocol layer itself. The browser session may inherit cookies, localStorage, or credentials from a persistent profile directory if one is configured. No API keys are required to run the server.

## 6. Security Considerations

**Cookie and credential exposure** is the highest-impact risk. If the browser session is configured with a persistent profile directory (or the user has previously logged in during the same session), the agent has access to stored cookies, session tokens, and any autofill credentials for every site visited. A prompt-injected instruction can silently exfiltrate these by navigating to an attacker-controlled URL with cookies appended as query parameters.

**Persisted login state leakage** is a variant: even without explicit credential storage, OAuth tokens or SSO session cookies obtained during an agent-driven login flow persist in the browser profile and may be reused across sessions or by subsequent agents sharing the same profile directory.

**Arbitrary JavaScript execution** via `evaluate` / `execute_js` gives the agent (or a prompt-injecting page) direct DOM and network access within the browser context — equivalent to a persistent XSS with exfiltration capability.

**Headed-mode sandbox escape** is a risk specific to non-headless configurations: a headed browser running on a display server can interact with other windows (screen capture, keylogging via `xdotool`) and is not isolated from the desktop environment.

**Prompt injection via page content** is structurally unavoidable: the agent reads page text and can be manipulated by content on any page it visits.

**Mitigation:** use an ephemeral, isolated browser profile for each session (no persistent profile dir); prefer headless mode in a container; block network egress to internal IP ranges; never configure stored passwords or OAuth apps in an agent-controlled browser profile.

## 7. Documented Strengths

Documented strengths from maintainer docs or community reports. Cite source.

## 8. Documented Weaknesses

Documented limitations from issue tracker or community reports. Cite source.

## 9. Sources

- [PulseMCP — browser automation servers](https://www.pulsemcp.com/servers?q=browser) — observed 2026-06-14
