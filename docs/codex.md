# OpenAI Codex (2025)

> This document covers the 2025 Codex coding agent — both the open-source CLI tool and the ChatGPT/API-based cloud agent. Not the deprecated 2021 Codex code-completion model.

---

## What It Is

**Codex** is an agentic AI coding assistant made by **OpenAI**. It ships as two related but distinct products that share models and branding:

1. **Codex CLI** — an open-source, terminal-based coding agent that runs locally on your machine.
2. **Codex (Cloud/Web/App)** — a cloud-hosted agent embedded in ChatGPT and the Codex desktop app, which runs tasks in isolated cloud sandboxes against GitHub repositories.

- **Product category:** Agentic AI coding assistant
- **Maker:** OpenAI
- **CLI initial release:** April 2025 (open-source, Apache-2.0)
- **Cloud agent initial release:** May 2025 (research preview); general availability followed in 2025
- **CLI language:** Rust (96%+ of codebase), with Python, TypeScript, and shell support

### Pricing

| Plan | Monthly Cost | Codex Access |
|------|-------------|--------------|
| Free | $0 | Basic exploration only |
| Go | $8 | Lightweight tasks |
| Plus | $20 | Multiple focused sessions/week |
| Pro 5x | $100 | 5× Plus rate limits |
| Pro 20x | $200 | 20× Plus rate limits |
| Business | Pay-as-you-go | Token-based billing per seat |
| Enterprise / Edu | Custom | Custom via sales |

Pricing shifted in April 2026 to token-based credits for Business and new Enterprise plans. Token credit rates (per 1M tokens):

| Model | Input | Cached Input | Output |
|-------|-------|-------------|--------|
| GPT-5.5 | 125 cr | 12.5 cr | 750 cr |
| GPT-5.4 | 62.5 cr | 6.25 cr | 375 cr |
| GPT-5.4-mini | 18.75 cr | 1.875 cr | 113 cr |
| GPT-5.3-Codex | 43.75 cr | 4.375 cr | 350 cr |

API key access is available across all tiers for automation at standard OpenAI API token rates.

---

## What It Does

### Core Capabilities

- **Reads, writes, and edits files** across an entire repository autonomously
- **Executes shell commands** (builds, tests, linters, git operations) and reasons about output
- **Writes and runs tests**, interprets failures, iterates until passing
- **Explains and summarizes** complex or legacy codebases
- **Reviews code** for bugs, logic errors, and edge cases with inline GitHub comments
- **Fixes bugs end-to-end:** reproduces, diagnoses, patches, verifies
- **Proposes pull requests** for review from a cloud-isolated environment
- **Parallelizes agents** — multiple tasks run concurrently via worktrees (CLI) or cloud environments (web/app)
- **Web search** during task execution (enabled by default in cloud, configurable in CLI)
- **Image input** — screenshots and design specs as task context
- **Image generation** — produces images mid-task (5–8 credits per image)
- **Subagent orchestration** — spawns specialized subagents for complex multi-step work

### Integrations

- **GitHub** — cloud agent connects to repos; auto code review via GitHub App; issue-to-PR workflows
- **Slack** — delegate tasks or ask questions directly from channels/threads
- **Linear** — triage bugs, manage releases, track team workload
- **Figma** — fetch design context as a published skill
- **Cloudflare / Vercel** — deploy web applications via skills
- **MCP (Model Context Protocol)** — extend Codex with any MCP-compatible third-party tool or data source
- **OpenAI Agents SDK** — orchestrate Codex programmatically; run CLI as an MCP server for pipeline automation

### AGENTS.md

Codex reads `AGENTS.md` files (global and per-repo) for persistent custom instructions. Precedence: global → repo root → subdirectory. This is a cross-tool standard: tools from other vendors also honor `AGENTS.md`, simplifying team workflows versus tool-specific config files.

---

## What It Doesn't Do

- **No real-time autocomplete** — it is an agentic task executor, not a keystroke-level code completion tool. Use Cursor or Copilot for inline suggestions.
- **No built-in IDE** — no editor UI. Interacts with your files from the terminal, web, or desktop app.
- **Cloud agent runs offline by default** — during task execution, internet access is disabled unless explicitly enabled; no access to external APIs or services mid-task by default.
- **No long-running background memory** — each task/thread is stateful within its run; no persistent cross-session project memory without AGENTS.md or explicit context.
- **Limited course-correction mid-task** (early releases) — the research preview lacked mid-run steering; GPT-5.3-Codex added real-time interaction without losing context.
- **No Windows-native sandbox parity** — Windows uses PowerShell sandbox or WSL2; Linux uses bubblewrap; macOS uses Seatbelt. Behaviors differ slightly across platforms.
- **Not free for production** — requires a paid ChatGPT plan or API key. The Free tier is exploration-only with severe limits.

---

## Architecture

### Codex CLI (Local)

- Written in **Rust** for speed and low overhead
- Runs locally on macOS, Linux, and Windows (native PowerShell sandbox or WSL2)
- Authentication: ChatGPT account (recommended for plan users) or raw OpenAI API key
- **Sandbox layer** enforces boundaries at the OS level:
  - macOS: Seatbelt framework
  - Linux/WSL2: `bubblewrap` user namespace isolation
  - Windows: Native PowerShell sandbox
- Three sandbox modes:
  - `read-only` — inspect files only; edits and commands require explicit approval
  - `workspace-write` (default) — read + edit within project dir + run routine commands
  - `danger-full-access` — no filesystem or network restrictions
- Three approval policies:
  - `untrusted` — prompt before non-trusted commands
  - `on-request` — operate within sandbox freely; escalate when exceeding boundaries
  - `never` — fully autonomous, no prompts
- Configured via `config.toml` and `AGENTS.md`; model switchable at runtime with `/model`
- Can expose itself as an **MCP server** for orchestration via the Agents SDK

### Codex Cloud Agent

- Each task runs in an **isolated, ephemeral container** managed by OpenAI
- Repository is preloaded into the container from a connected GitHub account
- **Two-phase runtime:**
  1. Setup phase — network-enabled; installs dependencies via user-provided setup script
  2. Agent phase — network disabled by default; agent reads/writes code, runs tests
- Internet access can be enabled per-environment for tasks requiring it
- The agent cannot access the host machine, other repos, or unrelated data
- Output surfaces: ChatGPT web, Codex desktop app (macOS), GitHub App, Slack, Linear

### Codex Desktop App (macOS)

- Native macOS app for managing multiple parallel agent threads
- Built-in **git worktree** support — agents work on isolated branches simultaneously
- Designed for human oversight of long-running tasks with real-time status updates
- Supports **background computer use** — agent can see, click, and type on your Mac

### Models

| Model | Role |
|-------|------|
| **gpt-5.5** | Default (newest); flagship for complex coding + research + computer use |
| **gpt-5.4** | High-capability general coding + agentic workflows |
| **gpt-5.4-mini** | Fast, cheap; good for subagents and routine tasks |
| **gpt-5.3-codex** | Specialized coding model; leads Terminal-Bench 2.0 at 77.3% |
| **gpt-5.3-codex-spark** | Research preview; near-instant real-time iteration (Pro only) |
| **gpt-5.2** | Previous-gen fallback |

The original **codex-1** model (released May 2025) was a version of OpenAI o3 fine-tuned with reinforcement learning on real-world coding tasks to match human PR style. Subsequent versions (GPT-5.x-Codex) build on this foundation.

---

## Key Differentiators

- **GitHub-native automation** — the GitHub App enables genuine issue-to-PR automation with inline code review comments that find real bugs. The tightest GitHub integration among terminal agents.
- **AGENTS.md standard** — promotes a cross-tool instruction format, not proprietary like Claude's `CLAUDE.md`. Reduces overhead for teams using multiple agents.
- **Parallel agents out of the box** — both CLI (via worktrees) and cloud (via parallel sandboxes) support concurrent agent execution natively.
- **Open-source CLI (Apache-2.0)** — fork, modify, self-host the CLI itself. Only OpenAI inference requires an account.
- **Bundled value** — ChatGPT plan includes Codex, image generation, video tools, and ChatGPT access. Not just a coding subscription.
- **Cost efficiency** — GPT-5.3-Codex costs roughly half of Claude Sonnet at comparable quality; Pro users rarely hit usage ceilings.
- **Runs as MCP server** — the CLI can be invoked programmatically via the Agents SDK for pipeline automation and CI/CD integration.
- **Cross-platform** — macOS, Linux, Windows; web; IDE extension; mobile (via ChatGPT). Single agent across all surfaces.
- **Speed** — GPT-5.3-Codex runs at 240+ tokens/second (claimed 2.5× faster than Claude Opus). GPT-5.3-Codex is 25% faster than GPT-5.2-Codex.

---

## Ideal Use Cases

- **Async, long-horizon tasks** — fire off a task (write this feature, fix this bug) and review the PR later. Especially powerful with cloud agent + GitHub.
- **Parallel workstreams** — run multiple independent tasks simultaneously without context-switching. Best-in-class for this pattern.
- **GitHub-centric teams** — issue-to-fix-to-PR automation with real code review saves significant review time.
- **Budget-conscious teams** — superior token economics vs. Claude Code on comparable tasks; plan bundles ChatGPT access.
- **Teams using multiple agents** — AGENTS.md shared instructions work across Codex CLI, other compliant tools, reducing config duplication.
- **CI/CD and automation pipelines** — orchestrate via Agents SDK or MCP server mode for headless, scriptable workflows.
- **Legacy codebase triage** — code understanding mode explains unfamiliar codebases without requiring full context dumps.
- **Design-to-code workflows** — Figma MCP integration makes it viable for design-spec-driven development.

Not ideal for: real-time autocomplete while typing, deep IDE UI integration, or teams requiring fully on-premises/air-gapped execution.

---

## Community & Ecosystem

- **GitHub stars:** ~79,800 (as of April 2026)
- **Forks:** ~11,500
- **npm downloads:** ~14.5M/month
- **Weekly active users:** ~3M (as of April 2026)
- **Latest CLI release:** v0.128.0 (April 30, 2026); releases are frequent (weekly cadence)
- **Open issues:** ~3,300 — active but backlog is large
- **License:** Apache-2.0 — permissive for commercial and private use

### Extensibility

- **MCP** — plug in any Model Context Protocol server to extend Codex with external tools and data
- **Skills** — OpenAI publishes first-party skills (Figma, Linear, Vercel, Cloudflare, image generation, document export); community-built skills available
- **Agents SDK** — programmatic orchestration; compose Codex into larger multi-agent pipelines
- **Plugins** — CLI plugin system for custom commands and integrations
- **AGENTS.md** — repo-level and global instruction files; supports hierarchy and subdirectory overrides

### Standards Participation

OpenAI participates in the AAIF (Agentic AI Foundation) and promotes AGENTS.md as an open cross-tool standard. MCP was co-developed with Anthropic and is broadly adopted, making Codex interoperable with the wider agent ecosystem.
