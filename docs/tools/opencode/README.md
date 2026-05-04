# OpenCode

## What It Is

**OpenCode** is an open-source, agentic AI coding assistant built for the terminal, with additional desktop and IDE interfaces.

- **Product category:** Agentic AI coding assistant / CLI + TUI + desktop app
- **Maker:** Anomaly Co (Jay V and Frank Wang, co-founders; also Dax Raad and Adam Elmore). Previously built SST (Serverless Stack), a Y Combinator–backed open-source cloud framework.
- **Initial release:** June 19, 2025
- **Repository:** [github.com/anomalyco/opencode](https://github.com/anomalyco/opencode) — 154K+ stars, 17.8K+ forks, 784+ releases as of May 2026

## Pricing

- **Free (BYOK):** Use your own API keys for any supported provider. No sign-up required.
- **Free (subscriptions):** Authenticate with existing GitHub Copilot or ChatGPT Plus/Pro accounts.
- **OpenCode Zen (paid):** Hosted, curated model offering. Team-tested and benchmarked models. Pricing not publicly listed; subscription-based. This is the primary revenue source.
- **Self-hostable:** Fully open source (MIT license). Run entirely on your own infrastructure.

## What It Does

### Core Capabilities

- **Agentic loop:** Reads files, executes shell commands, edits code, and iterates until the task is complete — not just autocomplete.
- **Multi-file editing:** Understands imports and cross-file relationships; makes coordinated changes across the codebase.
- **Plan mode:** Analyze and plan before touching any files. Toggle between Plan (read-only, ask before acting) and Build (full permissions) with the Tab key.
- **Undo/redo:** `/undo` and `/redo` commands revert or restore agent changes within a session.
- **LSP integration:** Automatically connects to the project's Language Server. The AI sees type information, function signatures, import paths, and live diagnostics — same data as the IDE. Supported LSPs include TypeScript, Python, Go, Rust, Java, C# (Roslyn), Kotlin, and any other language with an LSP server.
- **Multi-session:** Run multiple parallel agents on the same project simultaneously.
- **Session sharing:** Generate shareable conversation links via `/share` for collaboration or debugging.
- **Image input:** Drag-and-drop images into the TUI for visual context (screenshots, diagrams).
- **Web search/fetch:** Built-in tools for agents to search the web and fetch URLs.
- **GitHub Actions integration:** `opencode github install` sets up a workflow; `opencode github run` executes an agent in CI.
- **Non-interactive mode:** `opencode run "<prompt>"` runs headless — scriptable in pipelines.
- **Headless server:** `opencode serve` and `opencode web` expose an API and web interface for remote control or mobile access.
- **Stats tracking:** `opencode stats` shows token usage and cost per session.
- **Fuzzy file search:** `@` key in the TUI opens fuzzy search to add file context to prompts.
- **Session compaction:** Automatically compresses context to preserve recent turns verbatim, extending effective context window.
- **Project initialization:** `/init` creates an `AGENTS.md` file with project-specific instructions for agents.

### Supported Languages / Frameworks

Any language with an LSP server is first-class. Explicitly supported: TypeScript, JavaScript, Python, Go, Rust, Java, C#, Kotlin. The AI itself is language-agnostic beyond LSP availability.

## What It Doesn't Do

- **No inline autocomplete:** OpenCode operates at the task level, not keystroke-by-keystroke. It does not provide real-time inline suggestions like Copilot or Cursor.
- **No built-in git integration:** No automatic commits, diff views, or PR creation within the tool. Undo/redo is session-scoped, not git-based — rolling back mid-task mistakes is manual.
- **No proprietary IDE:** It is not a full IDE. Windows native experience is less polished than Linux/macOS; WSL is the recommended path on Windows.
- **No code hosting or syncing:** Does not store or sync code. Shareable links are conversation transcripts, not code.
- **Context limits:** Large codebases can hit model context windows. Handling is not always transparent about what the agent can or cannot "see."
- **Documentation lag:** Docs are still catching up with the rapid release cadence. Some behaviors require reading source or GitHub issues.
- **API cost exposure:** Heavy BYOK usage can exceed the cost of a flat-rate subscription (e.g., Copilot). No built-in spend caps per session.
- **No built-in code review UI:** No diff visualization, approval flows, or PR review interface.

## Architecture

### How It Runs

| Mode | Description |
|------|-------------|
| **TUI (terminal UI)** | Primary interface. Full-screen terminal app built with Bubble Tea (Go). Native, not a web wrapper. |
| **Desktop app** | Electron-based. Available for macOS, Windows (beta), Linux (beta). |
| **IDE extension** | Available for VS Code, JetBrains, and others. Embeds the agent alongside your editor. |
| **Headless server** | `opencode serve` / `opencode web` — exposes HTTP API for remote or mobile clients. |
| **Non-interactive CLI** | `opencode run` — pipe-friendly, scriptable, CI-compatible. |
| **Client/server split** | TUI attaches to a backend server via `opencode attach`, enabling remote-drive from mobile. |

### Tech Stack

- **Primary language:** TypeScript (60.5%), with Rust for performance-critical components, CSS, Astro (docs site)
- **UI framework:** Bubble Tea (Go-based TUI) — earlier versions; current TypeScript rewrite uses a custom TUI layer
- **Database:** SQLite (session persistence)
- **Plugin runtime:** Bun (JavaScript/TypeScript plugins, npm packages auto-installed)

### Models Supported

75+ LLM providers via [models.dev](https://models.dev) (maintained by the OpenCode team). Notable providers:

- **Anthropic:** Claude 3.5 Sonnet, Claude 3 Opus, Claude Haiku, and variants
- **OpenAI:** GPT-4o, GPT-4 Turbo, o1, o3
- **Google:** Gemini 1.5 Pro/Flash, Gemini 2.0
- **Local:** Ollama (any locally-run model)
- **Others:** AWS Bedrock, Azure OpenAI, Groq, Fireworks, Together AI, OpenRouter, DeepSeek, Mistral, NVIDIA, LLM Gateway
- **Subscription login:** GitHub Copilot and ChatGPT Plus/Pro (OAuth)
- **OpenCode Zen:** Curated hosted models, team-tested and benchmarked

### Agent System

Two built-in primary agents:

| Agent | Tools | Default use |
|-------|-------|-------------|
| **Build** | All tools (read, edit, bash, glob, grep, web) | Default; full development work |
| **Plan** | Read-only; edits/bash set to `ask` | Planning and analysis without side effects |

Two built-in subagents (invokable via `@mentions`):

| Subagent | Tools | Purpose |
|----------|-------|---------|
| **General** | Full access | Multi-step tasks |
| **Explore** | Read-only | Codebase exploration |

Custom agents defined via markdown files in `.opencode/agents/` or `~/.config/opencode/agents/`. The filename becomes the agent name (e.g., `review.md` → `@review`).

### Plugin System

- Plugins are JavaScript/TypeScript modules placed in `.opencode/plugins/` or `~/.config/opencode/plugins/`, or loaded from npm.
- **40+ lifecycle hooks** across 19 event categories: session, file, message, tool, LSP, permission, TUI, shell, and more.
- Plugin context provides access to `project`, `directory`, `worktree`, `client`, and Bun's shell API (`$`).
- Type-safe via `@opencode-ai/plugin` TypeScript package.
- Use cases: notifications, custom tool creation, env var injection, session compaction customization.

### MCP (Model Context Protocol)

- Supports local (stdio) and remote (HTTP/SSE) MCP servers.
- OAuth 2.0 auto-handling: detects 401 responses, initiates Dynamic Client Registration (RFC 7591), stores tokens in `~/.local/share/opencode/mcp-auth.json`.
- MCP tools are first-class: available to agents alongside built-in tools, configurable per-agent with glob patterns.
- Built-in examples: Sentry (error tracking), Context7 (docs search), Grep by Vercel.

## Key Differentiators

1. **Provider-agnostic by design.** 75+ LLM providers. The team's explicit stance: "OpenCode is not an AI product. It's a product designed to use AI." No lock-in to any model.
2. **Use existing subscriptions.** Log in with GitHub Copilot or ChatGPT Plus — no additional API cost if you already subscribe.
3. **True open source (MIT).** Inspect, fork, self-host. 500+ contributors, 11K+ commits. Community-driven development.
4. **Privacy-first.** No code or context data stored by OpenCode. When using local models via Ollama, zero data leaves your machine.
5. **LSP-aware agents.** The AI sees live diagnostics, types, and signatures — not just raw text. Comparable to what an IDE exposes to the developer.
6. **Multi-agent parallelism.** Run multiple agents on the same project simultaneously — rare among terminal-based tools.
7. **models.dev.** Maintains a public database of LLM providers and models, used internally and by the broader community.
8. **Zero-friction onboarding.** No sign-up, no credit card required to start. Works immediately with an API key.
9. **Client/server architecture.** Headless server mode enables remote control — including from mobile — not common in CLI tools.

## Ideal Use Cases

- **Terminal-native developers** who live in the shell and don't want to switch to a GUI IDE for AI assistance.
- **Multi-model experimenters** who want to switch between Claude, GPT, Gemini, and local models on the same project.
- **Privacy-sensitive environments** where code cannot leave the machine (local models via Ollama, no OpenCode data retention).
- **Large-scale refactoring** across many files — agentic loop with full file access outperforms autocomplete tools.
- **CI/CD pipelines** — `opencode run` enables scriptable, non-interactive agent execution in GitHub Actions or other CI.
- **Legacy codebase onboarding** — Explore agent + LSP integration for rapid codebase comprehension.
- **Test generation and documentation** — task-level agent can match existing patterns and cover large surface areas.
- **Teams using Cloudflare, SST, or similar infrastructure** — first-class integrations and community tooling in these ecosystems.
- **Organizations wanting to self-host** — MIT license, full source available, no dependency on OpenCode servers if using BYOK.

## Community & Ecosystem

- **GitHub:** 154K+ stars, 17.8K+ forks, 500+ contributors, 784+ releases (as of May 2026). One of the fastest-growing OSS coding agents ever.
- **Adoption:** 650,000 monthly active users (achieved within 5 months of launch); 2.5 million monthly developers by early 2026.
- **License:** MIT — fully open source, commercially usable.
- **Funding/business:** Bootstrapped + Y Combinator (via SST). Revenue from OpenCode Zen subscriptions, reportedly "several million dollars annualized."
- **Ecosystem:**
  - [awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) — curated list of plugins, themes, agents, and resources.
  - npm-based plugin ecosystem; plugins auto-installed via Bun.
  - Community-contributed agents, themes, and MCP integrations.
  - 19+ language localizations for documentation.
- **Release cadence:** Extremely rapid — 16 releases in 16 days observed in April–May 2026. Active, frequent iteration.
- **Notable users:** Cloudflare (confirmed enterprise adoption).
- **Legal/controversy:** An "OpenCode vs Anthropic" debate emerged in 2026 over open vs. closed AI coding tools, reflecting the project's growing influence in the ecosystem.
- **Comparison community:** Strong HackerNews presence; frequently benchmarked against Claude Code, Aider, Cursor, and Goose.

## Sources

Sources were integrated during research but not individually tracked.
