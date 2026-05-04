# Gemini CLI

## What It Is

**Gemini CLI** is an open-source, agentic AI coding assistant and terminal agent made by **Google**. It runs directly in your terminal and operates on your local files and shell, powered by Google's Gemini models.

- **Product category:** Agentic AI assistant / CLI tool
- **Maker:** Google (google-gemini org on GitHub)
- **Initial release:** June 25, 2025 (general availability)
- **Latest stable version:** v0.40.0 (April 28, 2026)
- **License:** Apache 2.0 (fully open source)
- **Pricing:**
  - **Free (Google Account / Gemini Code Assist for Individuals):** 1,000 requests/day, 60 requests/minute — no credit card required
  - **Free (Gemini API Key, unpaid):** 250 requests/day, 10 requests/minute — Flash model only
  - **Gemini Code Assist Standard:** 1,500 requests/day, 120 req/min — fixed-price subscription
  - **Gemini Code Assist Enterprise:** 2,000 requests/day, 120 req/min — seat-licensed subscription
  - **Vertex AI / Pay-as-you-go:** token-based billing; dynamic quotas; 90-day trial in Express Mode
  - Free tier data may be used for model improvement (privacy concern for teams)

---

## What It Does

### Core Capabilities

- **Reads, writes, and edits files** across a codebase — single files or multi-file refactors
- **Runs shell commands** (build, test, lint, git) and reasons about output in a ReAct (Reason + Act) loop
- **Searches codebases** using bundled ripgrep (offline-capable as of v0.40.0)
- **Queries the web** via Google Search grounding — pulls live documentation and current results into context
- **Fetches URLs** during sessions for up-to-date reference material
- **Generates code from images and PDFs** (e.g., wireframe → implementation)
- **Automates GitHub workflows** — code reviews, issue triage, PR assistance via GitHub Actions
- **Plans before acting** via Plan Mode: read-only analysis phase, trade-off discussion, user-approved plan before execution
- **Manages memory** across sessions using a 4-tier context system (global, user, project, session)
- **Agent Skills:** on-demand specialized expertise modules (security auditing, cloud deployments, migrations) injected only when needed
- **Non-interactive scripting mode:** pipe-friendly, supports JSON/streaming-JSON output for CI/CD pipelines
- **YOLO mode:** fully autonomous execution without per-step confirmation prompts

### Supported Languages and Frameworks

Gemini CLI is language-agnostic at the CLI layer. It can read, edit, and reason about any text-based source files. Google Cloud integrations (BigQuery, Cloud Run, Vertex AI) receive first-class support through official extensions.

### How It Works

1. User sends a prompt in the terminal (or pipes input non-interactively)
2. The ReAct loop runs: Gemini reasons, selects tools, executes, observes output, repeats
3. Built-in tools: file read/write, shell execution, web search, web fetch, ripgrep search
4. External capabilities added via MCP servers (local or remote)
5. Context is assembled from hierarchical GEMINI.md files (global → project → component)
6. Agent Skills extend the system prompt on-demand when a matching task is detected

---

## What It Doesn't Do

- **No native IDE integration** (VS Code agent mode is a separate preview via Gemini Code Assist, not Gemini CLI itself)
- **Requires internet** for model inference — the AI runs on Google's cloud, not locally (local Gemma routing is experimental, not full offline inference)
- **Token inefficiency** — consumes ~65% more input tokens than Claude Code on equivalent tasks (432K vs 261K observed in benchmarks), which hurts on pay-per-token plans
- **Flash model quality gap** — the free tier defaults to Flash, which "consistently lacked type hints, module-level docstrings, and input validation" compared to Pro on complex tasks
- **Reliability on multi-file refactors** — community reports of tool call errors, formatting retries, and files being overwritten requiring developer intervention
- **No Windows Clipboard image support on Linux/macOS** (Windows only feature as of v0.23.0)
- **Slower on complex tasks** — benchmarks show ~2h for a full CLI tool build vs Claude Code's ~1h 17m with fewer retries
- **Free tier privacy** — data sent via personal Google account may be used for model training; not suitable for confidential codebases without a paid plan

---

## Architecture

### Runtime Model

- **Runs locally** as a Node.js CLI process installed via npm, npx, Homebrew, MacPorts, or Anaconda
- **AI inference is cloud-side** — Gemini models run on Google infrastructure; the CLI sends prompts and receives responses over the network
- **PTY shell architecture** — handles interactive programs (vim, install scripts) without breaking sessions
- **Single Executable Application (SEA)** packaging bundles ripgrep for offline code search

### Authentication Options

| Method | Access | Notes |
|--------|--------|-------|
| Google OAuth (personal account) | 1,000 req/day, 60 req/min | Best free tier; data may train models |
| Gemini API Key (unpaid) | 250 req/day, 10 req/min | Flash only |
| Gemini API Key (paid) | Usage-based billing | Pro model access |
| Vertex AI | Dynamic/purchased quotas | Enterprise; no data training |
| Gemini Code Assist subscription | 1,500–2,000 req/day | Shared quota with VS Code extension |

### Models

- **Gemini 2.5 Pro** — primary model; 1M token context window; available on free Google account tier
- **Gemini 3 Flash** — default for unpaid API key; faster, cheaper, lower quality on complex tasks
- **Gemini 3.1 Pro Preview** — available as of v0.31.0 (February 2026)
- **Gemma (local routing)** — experimental; locally-running Gemma model used for routing decisions only, not full inference
- Model selection configurable via `--model` flag or settings

### Context Window

1,000,000 tokens with Gemini 2.5 Pro — sufficient to load entire large codebases in a single session.

### MCP (Model Context Protocol)

Gemini CLI's extensibility is built on MCP. It connects to local or remote MCP servers to add tools, resources, and capabilities. The `/mcp` command manages server connections at runtime.

### GEMINI.md Context Files

Hierarchical instruction files loaded from `~/.gemini/GEMINI.md` (global) down to component-level directories. All found files are concatenated and sent with every prompt. Managed via the `/memory` command.

---

## Key Differentiators

1. **Largest free tier in the category** — 1,000 requests/day and 60 req/min at no cost; competitors offer far less or nothing
2. **Fully open source (Apache 2.0)** — code can be inspected, audited, forked, and self-hosted; no other major CLI coding agent matches this
3. **Google Search grounding** — live web search built in; Claude Code and Copilot CLI lack native search integration
4. **1M token context window** — largest in the CLI agent category; enables whole-repo loading
5. **Agent Skills system** — modular on-demand expertise injected only when relevant, keeping context lean
6. **Plan Mode** — structured read-only planning phase before any mutations; reduces unwanted side effects
7. **PTY shell** — handles truly interactive subprocesses (editors, package managers) without workarounds
8. **Pre-installed in Google Cloud Shell** — zero setup for GCP users
9. **Partner extension ecosystem** — 100+ extensions including Figma, Stripe, Snyk, Elastic, Shopify, Postman, Dynatrace
10. **Non-interactive scripting** — JSON/streaming-JSON output for pipeline automation; Claude Code is primarily interactive

---

## Ideal Use Cases

- **Solo developers and students** who want a powerful coding agent at zero cost
- **GCP-heavy teams** — native Cloud Shell integration, BigQuery, Cloud Run, Vertex AI extensions
- **Open-source projects** requiring auditable, forkable tooling
- **CI/CD automation** — non-interactive mode with JSON output fits pipeline integration
- **Prototyping and exploration** — fast iteration with Google Search grounding for live docs
- **Security-sensitive inspection** — Apache 2.0 license lets teams audit the entire call chain
- **Large monorepos** — 1M context window accommodates very large codebases without chunking
- **Multi-service workflows** — MCP extensibility connects databases, APIs, and SaaS tools in one session
- **Teams already in Google Workspace / GCP** — credential reuse, unified billing, shared quotas with Code Assist

**Not ideal for:**
- Teams needing the highest output quality on complex multi-file refactors (Claude Code outperforms here)
- Confidential codebases on the free tier (data training risk)
- Offline or air-gapped environments (cloud inference required)

---

## Community & Ecosystem

### Adoption

- **1M+ developers** using Gemini CLI within three months of extensions launch (October 2025)
- **96,000+ GitHub stars** on the main repo — one of the fastest-growing developer tool repos on GitHub
- Active issue tracker, discussion forum, and PR contributions from community

### Open Source Status

- **Apache 2.0** license — permissive; allows commercial use, modification, distribution, and sublicensing
- Community contributions accepted: bug reports, documentation, MCP server implementations, extensions
- Published changelogs, public roadmap discussions on GitHub

### Extensions Ecosystem

- **100+ extensions** in the catalog as of early 2026
- **37 official Google-built extensions** in the `gemini-cli-extensions` GitHub organization
- **Notable partner extensions:** Dynatrace, Elastic, Figma, Harness, Postman, Shopify, Snyk, Stripe, GitLab
- Extension installation: `gemini extensions install <GitHub URL or local path>`
- Each extension bundles an MCP server, a GEMINI.md playbook, optional custom commands, and excluded tools
- Community registry at `geminicli.com/extensions` ranked by GitHub stars
- **Awesome Gemini CLI** curated list at `Piebald-AI/awesome-gemini-cli`
- Building extensions: Google provides templates and a step-by-step guide; any MCP server qualifies

### Related Google Products

| Product | Relationship |
|---------|-------------|
| Gemini Code Assist | Shared quota; VS Code/JetBrains IDE counterpart |
| Google Cloud Shell | Gemini CLI pre-installed |
| Vertex AI | Enterprise auth and billing backend |
| Google AI Studio | API key source for paid access |
| ADK (Agent Development Kit) | Companion framework for building agents that Gemini CLI can call |

---

## Sources

- [Google Blog: Introducing Gemini CLI](https://blog.google/technology/developers/introducing-gemini-cli-open-source-ai-agent/)
- [GitHub: google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli)
- [Gemini CLI Quotas and Pricing](https://google-gemini.github.io/gemini-cli/docs/quota-and-pricing.html)
- [Gemini CLI Documentation](https://geminicli.com/docs/)
- [Gemini CLI v0.40.0 Changelog](https://geminicli.com/docs/changelogs/latest/)
- [Google Blog: Gemini CLI Extensions](https://blog.google/innovation-and-ai/technology/developers-tools/gemini-cli-extensions/)
- [Google Cloud Docs: Gemini CLI](https://docs.cloud.google.com/gemini/docs/codeassist/gemini-cli)
- [DataCamp: Gemini CLI vs Claude Code](https://www.datacamp.com/blog/gemini-cli-vs-claude-code)
- [CodeAnt: CLI Benchmarks 2026](https://www.codeant.ai/blogs/claude-code-cli-vs-codex-cli-vs-gemini-cli-best-ai-cli-tool-for-developers-in-2025)
- [VentureBeat: Gemini CLI Economics](https://venturebeat.com/ai/google-is-redefining-enterprise-ai-economics-with-open-source-gemini-cli-that-will-be-free-for-the-majority-of-developers)
