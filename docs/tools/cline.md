# Cline

## What It Is

**Cline** is an open-source, agentic AI coding assistant that runs as a sidebar extension inside VS Code (and, as of 2026, JetBrains, Cursor, Windsurf, Zed, and Neovim). It was originally released as **Claude Dev** by developer **Saoud Rizwan** in July 2024, following Anthropic's "Build with Claude" hackathon. It was renamed to **Cline** (short for CLI + Editor) in October 2024 as it expanded beyond Claude models. Rizwan subsequently incorporated **Cline Bot Inc.**, which raised **$32M** in Seed + Series A funding (led by Emergence Capital, with Pace Capital, Y Combinator's Jared Friedman, and others).

- **Product category:** Agentic AI coding assistant / VS Code extension
- **Maker:** Cline Bot Inc. (founder: Saoud Rizwan)
- **Initial release:** July 2024 (as Claude Dev); renamed Cline October 2024
- **License:** Apache 2.0 (open source)
- **Extension ID:** `saoudrizwan.claude-dev` (unchanged since original release)
- **Pricing:**
  - Extension itself: free
  - Models: pay-as-you-go via your own API keys — no Cline markup
  - **Cline Provider:** managed pay-as-you-go inference ($0.01–$0.10 per task typical) — no API key needed
  - **Teams plan:** free through Q1 2026, then $20/user/month (first 10 seats always free)
  - **Enterprise:** custom pricing, VPC deployments, SSO/SCIM, audit logs, SLA

---

## What It Does

### Core Capabilities

Cline is a **human-in-the-loop autonomous agent** — it can plan and execute multi-step coding tasks across the full development lifecycle, requesting approval at each step.

| Capability | Details |
|---|---|
| File operations | Read, create, edit files; diffs displayed before applying |
| Terminal execution | Run shell commands in the IDE's integrated terminal; stderr parsed for auto-retry |
| Browser automation | Puppeteer-controlled Chromium: navigate, click, type, screenshot, read console logs |
| Codebase search | Regex search across workspace; symbol mapping via `list_code_definition_names` |
| Context references | `@url`, `@file`, `@folder`, `@problems` annotations pull in targeted context |
| MCP tool use | Connect to 300+ external tools/data sources via Model Context Protocol |
| Subagents | Read-only parallel research agents spawned for codebase exploration |
| Checkpoints | Shadow Git repo snapshots after each tool call; three-mode rollback (files-only, messages-only, full reset) |

### Plan/Act Mode

- **Plan mode:** Read-only reasoning phase — Cline analyzes code and proposes a strategy without modifying anything.
- **Act mode:** Execution with approval gates — each file edit and terminal command requires explicit user authorization.

Users switch between modes freely; Plan mode is safe for exploratory sessions.

### Rules Engine (`.clinerules/`)

Version-controlled markdown files in `.clinerules/` at the project root are injected into the system prompt before every interaction. Rules support YAML frontmatter with `globs` for file-scoped activation. Cline auto-imports `.cursorrules`, `.windsurfrules`, and `AGENTS.md` from other tools. Global rules (machine-wide) can be overridden per workspace.

### Safety & Approval Controls

- Per-category auto-approval: read-only ops, writes, terminal commands, browser actions, MCP calls
- Destructive operations (`rm -rf`, `DROP TABLE`, force push) always require manual approval
- **YOLO Mode:** disables all approval gates — intended for sandboxed/throwaway environments only
- **Spend limits (v3.78+):** daily/monthly caps with a dedicated UI to prevent runaway token usage

### Supported Languages / Frameworks

Cline is language-agnostic — it operates on files and runs shell commands, so it works with any language the underlying model understands. Community reports strongest results with TypeScript/JavaScript (React, Next.js, Tailwind) stacks. Works with Python, Go, Rust, Java, C#, and more.

---

## What It Doesn't Do

- **No inline completions:** Cline is a task-level agent, not a tab-complete or ghost-text tool. It does not compete with Copilot's inline suggestion mode.
- **No GUI outside VS Code sidebar:** All interaction is through the chat panel; there is no standalone app (CLI preview exists for macOS/Linux only as of v3.81).
- **Browser automation model-locked:** The `browser_action` tool requires Claude Sonnet 3.5+ for reliable visual reasoning; other models degrade significantly.
- **Large file cap:** A 300KB file read limit can cause HTTP 413 errors even with models that have 1M+ token context windows (tracked in GitHub Issue #8236).
- **Context degradation:** Accuracy drops after ~15–20 conversation turns in long sessions. The `/newtask` command mitigates this by distilling progress into a fresh context window.
- **No native Git UI:** Cline can run `git` commands in the terminal, but does not expose a visual Git workflow; relies on VS Code's built-in source control.
- **No team shared memory:** Each session is independent; there is no persistent project memory across team members without external MCP tooling.
- **No refusal to act:** YOLO Mode aside, Cline still requires human approval for destructive ops, which creates overhead in high-throughput automated pipelines.
- **Approval fatigue:** Broad multi-file changes accumulate many approval prompts, which some users find disruptive.
- **Cost unpredictability:** Without a flat-rate subscription option, budgeting is difficult. Typical active development sessions cost $10–$25/day at frontier model rates.

---

## Architecture

### Extension Host

Cline runs in VS Code's **extension host process** (separate from the main UI process), giving it full access to the VS Code API: open editors, workspace file system, integrated terminal, and the webview panel for its chat UI. The codebase is ~98% TypeScript.

### Tool Loop

Cline implements a standard **ReAct-style agent loop**:

1. User submits a task
2. Cline sends task + context to the configured LLM API
3. Model responds with a tool call (read file, write file, run command, etc.)
4. Cline executes the tool (after user approval if required) and feeds results back
5. Loop continues until task is complete or the model signals done

Each tool invocation commits a checkpoint to an internal shadow Git repo.

### APIs Called

- **LLM provider APIs** (selected by user): Anthropic Claude, OpenAI, Google Gemini, AWS Bedrock, Azure OpenAI, OpenRouter, DeepSeek, Mistral, Groq, Together, SambaNova, xAI Grok, Cerebras — or any OpenAI-compatible endpoint
- **Local model runtimes:** Ollama, LM Studio (via OpenAI-compatible API)
- **VS Code Extension API:** file system, terminal, webview, workspace state
- **Puppeteer/Chromium:** browser automation (bundled)
- **MCP servers:** stdio (local processes) or SSE (remote HTTP endpoints)

### Supported Models (Key Examples)

| Provider | Models |
|---|---|
| Anthropic | Claude Sonnet 4.7, Claude Opus 4.7, Claude Haiku 3.5 |
| OpenAI | GPT-5.5, GPT-4o, o3-mini |
| Google | Gemini 2.5 Pro, Gemini 2.5 Flash |
| Local | Any Ollama/LM Studio model |
| Cline Provider | Managed inference (no key needed) |

Browser automation and visual reasoning are **only reliable with Claude Sonnet 3.5 or later**.

---

## Key Differentiators

1. **Model agnosticism:** 30+ providers, zero vendor lock-in. Switch models between tasks.
2. **Full tool access, no caps:** Unlimited MCP tools (vs. Cursor's 40-tool cap). Cline can also *generate* new MCP servers on demand ("add a tool" triggers Cline to write, install, and configure the MCP server itself).
3. **Transparent pricing:** You pay provider rates directly — no subscription markup, no token throttling to protect margins.
4. **Shadow Git checkpoints:** Fine-grained rollback at every tool invocation, independent of project Git history.
5. **Browser-in-the-loop:** Agent can verify its own UI work by navigating the live app in a headless browser — not just static analysis.
6. **Rules as code:** `.clinerules/` files are version-controlled, file-scoped, and composable — coding standards travel with the repo.
7. **Open source (Apache 2.0):** Auditable, forkable, self-hostable. Roo Code is the most prominent fork.
8. **No IDE switch required:** Remains a sidebar in standard VS Code, preserving existing editor setup, keybindings, and extensions.

---

## Ideal Use Cases

- **Feature implementation:** Well-scoped tasks (new API endpoint, component, test suite) where multi-file coordination is needed.
- **Refactoring at scale:** Coordinated renaming, restructuring, or migrating patterns across many files.
- **Debugging:** Terminal-driven investigation + browser verification loop — run tests, read errors, apply fixes, repeat.
- **Greenfield projects:** Scaffolding from scratch where the agent can freely create the file structure.
- **Teams with model preferences:** Organizations that want to use Bedrock, Azure, or local models for compliance or cost reasons — Cline imposes no constraint.
- **MCP-heavy workflows:** Teams that have invested in MCP tooling (databases, issue trackers, observability) and want the agent to use them natively.
- **Open-source contributors:** Apache 2.0 license means teams can fork, audit, and extend without licensing concerns.

**Less ideal for:**
- Inline/tab-complete suggestions (use Copilot or Supermaven instead)
- Fully headless/CI automation (use Claude Code CLI or Aider)
- Teams that need predictable flat-rate billing
- Heavy Vim/Emacs users (no native plugin)

---

## Community & Ecosystem

### Adoption

- **5M+ installs** on VS Code Marketplace (as of 2026)
- **61,300+ GitHub stars** (`cline/cline`)
- **251+ releases** (v3.82.0 as of May 1, 2026)
- Enterprise users include Samsung, Salesforce, Oracle, Amazon, Microsoft (reported on cline.bot)

### Open Source

- License: Apache 2.0
- Contributions accepted via GitHub PRs
- Notable fork: **Roo Code** (formerly Roo Cline) — adds Ask/Code/Architect modes, targets sysadmin/CLI use cases

### MCP Ecosystem

- Built-in **MCP Marketplace** for browsing and installing servers from within the IDE
- Configuration via `cline_mcp_settings.json` (stdio and SSE transports)
- Per-server: enable/disable toggle, timeout (30s–1h), env vars, `alwaysAllow` tool lists
- Common integrations: PostgreSQL, MongoDB, SQLite, GitHub Issues, Linear, Jira, Sentry, Datadog, semantic code search
- Cline can **author new MCP servers** autonomously when asked

### Funding & Trajectory

- **$32M raised** (Seed + Series A, July 2025): Emergence Capital (lead), Pace Capital, 1984 Ventures, Essence VC, Cox Exponential, angel investors including Jared Friedman (YC), Eric Simons (Bolt.new), Logan Kilpatrick, Addy Osmani, Theo Browne
- Trajectory: expanding from VS Code extension toward enterprise platform (Teams product, JetBrains, CLI)

### Extensibility Summary

| Surface | Mechanism |
|---|---|
| Custom instructions | `.clinerules/` markdown files with glob-scoped activation |
| External tools/data | MCP servers (stdio or SSE) |
| Model selection | Any of 30+ providers or local runtime |
| Forking/self-hosting | Apache 2.0 — full source available |
| CI/headless | Preview CLI for macOS/Linux (Windows on roadmap) |
