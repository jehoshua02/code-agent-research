---
name: "Browser Control"
license_category: "apache-2.0"
status: "active"
url: "https://github.com/microsoft/playwright-mcp"
last_verified: "2026-06-14"
transport: "stdio"
has_anthropic_reference: false
auth: "none"
best_for: ["research", "automation", "data"]
notes: "Dominant implementation is Microsoft's playwright-mcp; supports HTTP transport via --port flag."
---

# Browser Control

_Last verified: 2026-06-14_

## 0. TL;DR

A browser-control [MCP](../GLOSSARY.md#mcp-model-context-protocol) server gives an agent a real browser it can navigate, click, type into, and take screenshots of — for sites where plain HTTP fetching won't work because the page requires JavaScript or user interaction. Use one when the agent needs to log in to a service, fill out a form, or scrape a single-page application. The main catch: browser sessions are slow and resource-heavy, and interactive flows are fragile if page layout changes.

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

- **Handles JavaScript-rendered apps**: unlike plain HTTP fetch, a real browser engine executes JavaScript fully, making SPAs, React/Next.js apps, and dynamically loaded content accessible to agents ([microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp)).
- **Accessibility-tree element selection**: Microsoft's `playwright-mcp` exposes the browser's accessibility tree as a structured snapshot, letting agents target elements by ARIA role and label rather than brittle CSS selectors — significantly improving click reliability across page redesigns.
- **Full interactive flow support**: agents can fill forms, click through multi-step OAuth flows, handle file uploads, and respond to modal dialogs — operations that no fetch-only server can perform.
- **Screenshot feedback loop**: screenshot tools let a multimodal model visually verify page state before acting, enabling error recovery (e.g., detecting a CAPTCHA or unexpected redirect) mid-task.

## 8. Documented Weaknesses

- **Brittle CSS selector dependency**: despite accessibility-tree alternatives, many community servers default to CSS or XPath selectors that break when page markup changes, requiring frequent selector maintenance ([playwright-mcp issues](https://github.com/microsoft/playwright-mcp/issues)).
- **Heavy resource use**: a full Chromium instance consumes 200–500 MB of RAM per session; running multiple parallel browser-control agents on a single host exhausts memory quickly and is impractical without container orchestration.
- **Slow tool-call latency**: page navigation, DOM stabilization, and screenshot capture add 0.5–5 s per tool call — fine for single-step tasks but expensive in multi-step agentic loops where tens of interactions are needed.
- **Session state management complexity**: persistent browser profiles carry authentication across sessions, which aids re-use but creates credential-leak risk; ephemeral profiles lose login state between runs, forcing the agent to re-authenticate on every task.

## 9. Sources

- [PulseMCP — browser automation servers](https://www.pulsemcp.com/servers?q=browser) — observed 2026-06-14
