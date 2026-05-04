# Kilo Code

## What It Is

**Category:** Open-source agentic AI coding assistant (IDE plugin + CLI + cloud agents)
**Maker:** Kilo (kilo.ai) — independent startup
**Released:** Late 2024 (forked from Roo Code, which forked from Cline); v7.x as of May 2026
**License:** Apache-2.0 (extension); MIT (GitHub repo)
**Website:** https://kilo.ai / https://github.com/Kilo-Org/kilocode
**GitHub:** 18.9k stars, 2.5k forks, 18,857 commits, 879 open issues (as of May 2026)

Kilo Code is a VS Code/JetBrains extension and CLI tool that acts as an autonomous coding agent — it reads your codebase, plans, writes, runs, and debugs code with minimal manual intervention. It positions itself as a "superset" of Cline and Roo Code, absorbing the best of both and adding orchestration, inline autocomplete, and cross-platform sync.

## Pricing

| Component | Price | Notes |
|---|---|---|
| Kilo Code extension | Free | Open source, no subscription |
| BYOK (Bring Your Own Key) | Free | Pay your provider directly |
| Kilo Gateway (managed API) | Provider rate, 0% markup | Access 500+ models via Kilo's unified gateway |
| Kilo Pass Starter | $19/month | Up to $26.60/month in credits (40% bonus) |
| Kilo Pass Pro | $49/month | Up to $68.60/month in credits |
| Kilo Pass Expert | $199/month | Up to $278.60/month in credits |
| Teams | $15/user/month | Analytics, shared modes, centralized billing, priority support |
| Enterprise | Contact sales | SSO, audit logs, model limits, SLA |
| KiloClaw (managed cloud agents) | $9/month | Managed OpenClaw; AI inference billed separately |

Annual plans available with 50% bonus credits. Pay-as-you-go credit top-ups also available. Free-tier models exist (e.g., ByteDance Dola Seed 2.0 Pro, NVIDIA Nemotron 3 Super 120B) subject to rate limits.

## What It Does

### Agent Modes

Kilo Code ships with six built-in modes plus unlimited custom modes:

| Mode | Purpose |
|---|---|
| **Code** | Write, edit, refactor code; execute terminal commands |
| **Ask** | Answer questions without modifying files |
| **Architect** | Plan complex features; produce structured design before coding |
| **Debug** | Trace errors, read logs, propose and apply fixes |
| **Orchestrator** | Meta-agent that breaks a goal into subtasks and routes each to the right specialist mode |
| **Custom** | User-defined modes with scoped tool permissions and custom system prompts |

### Core Capabilities

- **Natural language to code** — describe a feature; the agent plans, writes, and runs it
- **Tab autocomplete** — multi-line inline suggestions aware of codebase patterns
- **Codebase indexing** — semantic search across the full repo without manual file specification
- **Context injection** — `@git-changes`, `@folder`, `@terminal`, `@file` context mentions
- **Terminal command execution** — runs shell commands, installs packages, runs tests
- **Browser automation** — launches and controls a browser for integration testing
- **Automatic error recovery** — detects test failures, retries, resumes after connectivity loss
- **Memory Bank** — stores architectural decisions and conventions in Markdown files in your repo; reconstructed at session start so context persists across sessions
- **MCP integration** — built-in Model Context Protocol marketplace; connect external tools (GitHub Issues, Figma, databases, search, domain APIs) with no custom code
- **Code review** — automated PR analysis with quality suggestions
- **Cloud agents (KiloClaw)** — run long-duration tasks without blocking local resources; integrates with Telegram, Discord, Slack; supports cron scheduling
- **Voice prompting** — natural language commands via microphone in IDE
- **Cross-device continuity** — start a task on mobile, continue in VS Code, finish in CLI; session state syncs

### Supported Languages & Frameworks

No language restrictions — works on any text-based language the underlying model can handle. The agent reads file trees, parses code, and runs any shell command, so language support is model-dependent, not tool-dependent. Practically covers all mainstream languages (TypeScript, Python, Go, Rust, Java, C#, C/C++, Ruby, PHP, etc.) and any framework.

### How It Works

1. User sends a prompt in the IDE panel or CLI.
2. The agent (or Orchestrator) selects a mode and a model.
3. The agent reads the codebase (file tree, semantic search, terminal output, browser state).
4. It generates a plan, then iteratively writes/edits files, runs commands, reads output, and self-corrects.
5. It pauses for approval on destructive actions (configurable; "auto-accept" available for CI/CD).
6. Results surface as diffs in the IDE or committed PRs via cloud agents.

All prompts and model selections are visible to the user — no black-box routing unless the gateway "Auto" mode is used.

## What It Doesn't Do

- **No native Zed or Vim/Neovim support** — only VS Code, JetBrains, and CLI
- **CLI is newer and less mature** than Cline CLI 2.0; some CLI edge cases are rougher
- **Browser automation is weaker** than Cline's Computer Use implementation for end-to-end testing
- **Orchestrator loops** — can get stuck in refinement cycles on ambiguous tasks; requires clear success criteria in prompts
- **Autocomplete quality complaints** — some Reddit users report inline autocomplete is "subpar" versus GitHub Copilot or Supermaven
- **No auto-model selection by default** — users must choose a model manually (gateway "Auto" routes, but it is opt-in)
- **Cost opacity for new users** — easy to underestimate API costs when using premium models at high volume without a Kilo Pass budget cap
- **No fine-tuning** — cannot train or fine-tune models on your codebase
- **JetBrains rendering issues** — JCEF (Chromium Embedded Framework) must be enabled; some Android Studio and older JetBrains versions have panel rendering failures
- **Smaller community than Cline** — 18.9k GitHub stars vs. Cline's 58k+; fewer community tutorials and third-party MCP servers
- **Fork controversy** — built on Cline/Roo Code foundations; critics note heavy ad spend vs. upstream contributions

## Architecture

### Execution Surfaces

| Surface | Description |
|---|---|
| VS Code extension | Primary interface; panel-based chat + inline autocomplete |
| JetBrains plugin | IntelliJ, PyCharm, WebStorm; requires JCEF |
| CLI (`@kilocode/cli`) | `npm install -g @kilocode/cli`; `--auto` flag for CI/CD pipelines |
| Cloud agents (KiloClaw) | Managed remote execution; no Docker/SSH required; Slack/Discord/Telegram bots |
| Web (app builder) | Prototype and deploy from a browser interface |

### Model Support

- **500+ models** from 60+ providers via the Kilo AI Gateway
- **BYOK** — bring your own API keys for Anthropic, OpenAI, Google, xAI, DeepSeek, Mistral, etc.
- **Local models** — Ollama and LM Studio supported for on-device/private inference
- **Gateway providers include:** Anthropic, OpenAI, Google, xAI, DeepSeek, Moonshot AI, MiniMax, ByteDance, NVIDIA, Arcee AI, Qwen, Z.ai, and others
- **Exclusive:** "Grok Code Fast" (optimized coding variant from xAI, available via Kilo partnership)
- **Smart routing** — optional "Auto" gateway mode routes to best-fit provider per task without code changes

### Primary Language

TypeScript (91.7% of the codebase). Built on a fork of OpenCode, enhanced for the Kilo platform.

### MCP (Model Context Protocol)

Kilo has a first-class MCP marketplace (`github.com/Kilo-Org/kilo-marketplace`) with curated Skills, MCP servers, and custom Modes. Skills are self-contained capability packages with repeatable workflows. MCP servers connect external services (Figma, GitHub Issues, databases, web search) so the agent can act on real-world context without leaving the IDE.

## Key Differentiators

| Feature | Kilo Code | Cline | Roo Code |
|---|---|---|---|
| Orchestrator mode | Yes (multi-agent routing) | No (Plan/Act only) | No |
| Inline autocomplete | Yes | No | No |
| Memory Bank | Yes (persistent Markdown context) | No | No |
| JetBrains support | Yes | Teams plan only | No |
| Cross-platform sync | Yes (mobile → IDE → CLI) | No | No |
| Models | 500+ / 0% markup | 311+ via gateway | Gateway-dependent |
| Teams pricing | $15/user/month | $20/user/month | N/A |
| Cloud agents | Yes (KiloClaw + Slack/Discord bots) | No | No |
| Code review (PR analysis) | Yes | No | No |
| Voice prompting | Yes | No | No |
| License | Apache-2.0 / MIT | Apache-2.0 | Apache-2.0 |

**"Superset" positioning:** Kilo explicitly forked Roo Code (itself a Cline fork) and merged the best features of both: Roo's temperature control, i18n (14+ languages), per-mode tool selection; Cline's MCP Marketplace, zero-config setup, task notifications. Then added Orchestrator, inline autocomplete, Memory Bank, and cloud execution.

**Pricing transparency:** Zero markup on model tokens is the clearest differentiator vs. Cursor and Windsurf, which bundle model access into subscription tiers with usage caps.

## Ideal Use Cases

- **Complex multi-file features** — Orchestrator mode plans, codes, and debugs across many files autonomously
- **JetBrains users** — the only open-source agent with native JetBrains support
- **Teams needing persistent context** — Memory Bank prevents repeated re-explanation of architecture across sessions
- **Cost-sensitive power users** — BYOK or 0%-markup gateway; no subscription required for occasional heavy use
- **CI/CD and background tasks** — CLI `--auto` flag and KiloClaw cloud agents run tasks headlessly on a schedule
- **Slack-first workflows** — KiloClaw ships code from a Slack message without opening an IDE
- **Model experimenters** — switching between 500+ models in one interface without managing multiple API integrations
- **Privacy-first teams** — local model support via Ollama/LM Studio keeps code off external servers

## Community & Ecosystem

- **2.3M+ users** (per kilo.ai)
- **30T+ tokens processed**
- **18.9k GitHub stars**, 2.5k forks (May 2026); active — 879 open issues, 256 open PRs, v7.2.31 released April 29, 2026
- **#1 Open Source Product of the Month** (Product Hunt)
- Used by developers at Meta, Amazon, Airbnb, PayPal, Square, Red Hat (per kilo.ai)
- **Open source:** Apache-2.0 / MIT — full code transparency, community contributions welcome
- **Marketplace:** `github.com/Kilo-Org/kilo-marketplace` — community Skills, MCP servers, custom Modes
- **Internationalization:** 14+ languages in the UI
- **Reciprocal sharing philosophy:** Kilo's stated goal is to push merged upstream features back into the open-source ecosystem
- **Forum/discussion:** GitHub Discussions (330+ threads), active Discord
- **Criticism:** Smaller community vs. Cline (58k stars); perceived as marketing-heavy relative to core upstream contribution; autocomplete quality trails dedicated autocomplete tools like Supermaven

## Sources

Sources were integrated during research but not individually tracked.

*Sources: kilo.ai, github.com/Kilo-Org/kilocode, kilo.ai/pricing, kilo.ai/cline, kilo.ai/docs, blog.kilo.ai, morphllm.com, producthunt.com — researched May 2026*
