# GitHub Copilot

## What It Is

**Category:** AI coding assistant — IDE plugin, CLI, chat interface, and autonomous coding agent  
**Maker:** GitHub (Microsoft subsidiary)  
**Initial release:** June 2021 (Technical Preview); GA for individuals October 2022  
**Current status (May 2026):** Mature product undergoing major billing transition; new individual plan sign-ups temporarily paused as of April 20, 2026

### Pricing (pre-June 2026 usage-based transition)

| Plan | Price | Target |
|---|---|---|
| Copilot Free | $0 | Individuals; 2,000 completions + 50 chat/agent requests/month |
| Copilot Student | $0 | Verified students; 300 premium requests/month |
| Copilot Pro | $10/user/month | Individual developers |
| Copilot Pro+ | $39/user/month | Power users; 1,500 premium requests + all models |
| Copilot Business | $19/user/month | Organizations on GitHub Free/Team |
| Copilot Enterprise | $39/user/month | GitHub Enterprise Cloud; 1,000 premium requests/user |

**Billing change effective June 1, 2026:** All plans move to AI Credits (1 credit = $0.01 USD). Inline code completions and Next Edit Suggestions remain free/unlimited. Chat, agent mode, code review, and cloud agent consume credits. Pro includes $10/month in credits; Pro+ includes $39/month. Additional credits purchasable on demand.

Free for verified teachers and open source maintainers (Pro-tier access).

---

## What It Does

### Core Features

**Inline Code Completion**  
Real-time, context-aware completions as you type. Suggests single lines or entire functions. Uses a dual-model architecture for Copilot Edits: one model proposes changes, a speculative-decoding endpoint applies them fast. Does not consume AI Credits — included at all tiers.

**Next Edit Suggestions (NES)**  
Predicts the next edit location in the file after completing one, not just where your cursor is. Helps chain multi-point refactors. Also credit-free on all plans.

**Copilot Chat**  
Inline and panel chat interfaces for asking questions about code, generating code on demand, explaining errors, and refactoring. Available in VS Code, Visual Studio, JetBrains IDEs, and GitHub.com. Supports slash commands (`/explain`, `/fix`, `/tests`, `/doc`). Consumes AI credits.

**Agent Mode (IDE)**  
Autonomously plans and executes multi-step coding tasks within the IDE. Determines which files to change, makes edits across multiple files, runs terminal commands, reviews output, and iterates until done. Generally available in VS Code and JetBrains as of March 2026. Inline agent mode in preview for JetBrains as of April 2026. Supports Model Context Protocol (MCP) servers.

**Copilot Cloud Agent (formerly Coding Agent)**  
Fully autonomous background agent that works on GitHub issues independently. You assign it an issue; it researches the repo, creates an implementation plan, makes code changes on a branch, and opens a pull request for review. Runs in a sandboxed environment on GitHub's infrastructure. Available on Pro, Pro+, Business, and Enterprise plans.

**Copilot Code Review**  
AI-driven pull request review. Gathers full project context before analyzing a PR, understanding how changes relate to the broader codebase. Shipped on an agentic architecture March 5, 2026. Flags bugs, style issues, and security concerns.

**Copilot CLI**  
Reached GA February 2026. Includes Plan mode and fully autonomous Autopilot mode. Features parallel specialized sub-agents (Explore, Task, Code Review, Plan), repository memory across sessions, hooks, plugins, and a built-in GitHub MCP server.

**GitHub Spark**  
Low-code/no-code web app builder integrated with Copilot. Available on Pro+ plan.

### Supported IDEs and Surfaces

- Visual Studio Code
- Visual Studio
- JetBrains IDEs (IntelliJ, PyCharm, WebStorm, etc.)
- Vim / Neovim
- Azure Data Studio
- GitHub.com (chat, code review, cloud agent)
- GitHub Mobile
- GitHub CLI / terminal (Windows Terminal Canary)

Chat functionality currently available in VS Code, JetBrains, and Visual Studio only (not Vim/Neovim).

### Supported Languages

Works across all languages present in public GitHub repositories. Best performance in: Python, JavaScript, TypeScript, Ruby, Go, C#, C++. Also effective for SQL, Bash, Java, Rust, PHP, and many others. Quality degrades for niche or low-resource languages.

### Supported Frameworks

React, Angular, Vue.js, Node.js, Django, Flask, Ruby on Rails, and most major web/backend frameworks. Also assists with infrastructure-as-code (Terraform, Kubernetes manifests), database query generation, and API integration.

---

## What It Doesn't Do

**No offline mode.** Requires continuous internet access to GitHub's cloud service. No local inference option.

**Limited repository context by default.** Chat and completions are scoped to open files and the active editor session. Agent mode and cloud agent have broader repository access, but standard chat does not browse the entire repo automatically.

**Does not enforce code quality or standards.** Suggestions may omit error handling, miss security best practices, or violate project conventions. Output always requires developer review.

**Hallucinations.** May generate APIs, function signatures, or library methods that do not exist, especially when context is thin.

**Accuracy degrades on complex logic.** Reported ~45% success rate for problems requiring more than three lines of logic. More reliable for boilerplate and repetitive patterns.

**No real-time internet access in completions/chat.** Copilot's model knowledge is bounded by training cutoffs. Does not fetch live documentation or package changelogs during suggestions (only via MCP integrations that explicitly provide it).

**Cannot execute or commit code autonomously without a human review step.** Cloud agent creates PRs; it does not merge or deploy. IDE agent mode requires developer approval for terminal commands (depending on configuration).

**Usage limits.** Free plan hard cap: 2,000 completions and 50 chat/agent requests per month. Session and weekly rate limits apply across all plans. The June 2026 credit system introduces per-feature consumption costs, meaning heavy agent/chat use can exhaust monthly credits quickly.

**No write access to databases.** Generated SQL or ORM code must be manually reviewed and executed by the developer.

**Context drift in long sessions.** Does not reliably track variable types or state changes across long conversations; relevance of suggestions can degrade.

---

## Architecture

### Deployment Model

Copilot runs as a **thin IDE plugin** communicating with **GitHub's cloud inference infrastructure**. No model weights run locally. The plugin captures editor context (open files, cursor position, recent edits, language metadata) and sends it to the cloud; responses stream back.

**Cloud agent** runs in a fully sandboxed GitHub-managed environment when assigned issues, with no local component required.

**CLI** is a standalone binary with its own cloud connection and optional MCP server integration.

### Model Stack (May 2026)

Copilot supports multi-model selection. Users on paid plans can switch models in chat and agent mode. Available models:

**OpenAI:**
- GPT-4.1, GPT-5 mini, GPT-5.2, GPT-5.2-Codex, GPT-5.3-Codex, GPT-5.4, GPT-5.4 mini, GPT-5.4 nano, GPT-5.5

**Anthropic:**
- Claude Haiku 4.5, Claude Sonnet 4, Claude Sonnet 4.5, Claude Sonnet 4.6, Claude Opus 4.5, Claude Opus 4.6, Claude Opus 4.6 (fast mode, preview), Claude Opus 4.7

**Google:**
- Gemini 2.5 Pro, Gemini 3 Flash (preview), Gemini 3.1 Pro (preview)

**Other:**
- xAI Grok Code Fast 1
- Fine-tuned models: Raptor mini (GPT-5 mini base), Goldeneye (GPT-5.1-Codex base)

Default models for inline completions use lower-latency, cost-optimized variants. All default models include content filtering and public code matching (to flag verbatim licensed code reproduction).

### Copilot Edits Dual-Model Architecture

Edits use two models: a primary model that plans and proposes changes, and a speculative-decoding model that applies those changes at high speed. This reduces perceived latency for multi-file edit sessions.

### MCP Integration

Agent mode (IDE) and cloud agent support the Model Context Protocol (MCP). Pre-configured MCP servers include the GitHub MCP server (issues, PRs, repos) and Playwright (web browsing and screenshots). Custom MCP servers can be added to extend Copilot's tool access.

### Agent HQ (Announced GitHub Universe 2025)

A control plane that orchestrates third-party agents (from Anthropic, OpenAI, Google, Cognition, xAI) alongside GitHub's own agents, all accessible under a single Copilot subscription. Positions Copilot as an orchestration layer, not just a single-model tool.

---

## Key Differentiators

**GitHub ecosystem depth.** Native integration with GitHub repositories, issues, pull requests, Actions, and Advanced Security. No other tool has equivalent depth in the GitHub workflow. For teams already on GitHub Enterprise, Copilot Enterprise is the path of least resistance.

**Multi-model, multi-provider choice.** No other mainstream coding assistant offers model switching across OpenAI, Anthropic, Google, and xAI in a single product under one subscription. This is a strategic hedge against model vendor lock-in.

**Cloud agent with GitHub-native PR workflow.** The cloud agent can take an issue and produce a PR entirely autonomously. Competing agents typically require local execution environments; Copilot's runs on GitHub's infrastructure with no setup.

**Enterprise footprint.** Deployed at ~90% of Fortune 100 companies. Centralized policy controls, IP indemnification on Business/Enterprise tiers, audit logs, and content exclusions for sensitive codebases.

**Next Edit Suggestions.** Predictive multi-point editing that moves the cursor to the next likely edit location — differentiates Copilot from pure autocomplete tools.

**Free tier with real completions.** 2,000 completions/month on the free tier is competitive with Codeium for casual use, with no credit card required.

---

## Ideal Use Cases

- **Teams already on GitHub Enterprise** — Copilot Enterprise integrates directly into the GitHub.com UI, PR review, and issue workflows with no additional tooling.
- **Organizations needing centralized AI governance** — Business/Enterprise plans offer policy controls, content filtering, and audit logs that consumer tools lack.
- **Developers who want model choice without switching tools** — Multi-model support under one subscription avoids managing multiple AI tool subscriptions.
- **Autonomous issue resolution** — Cloud agent handles well-scoped, self-contained issues (bug fixes, small features) end-to-end, freeing developers from context switching.
- **Mixed-language/framework teams** — Broad language support without per-language plugin configuration.
- **Developers new to a codebase** — Chat + code explanation features reduce onboarding friction. 80% of new GitHub developers adopt Copilot in their first week.
- **High-volume enterprise development** — Copilot is reported to generate ~46% of written code on average (up to 61% for Java), making it meaningful for productivity at scale.

Less ideal for: developers in air-gapped environments, teams with strict data residency requirements beyond what GitHub Enterprise offers, or developers who want full model control and local inference (consider Ollama-based tools instead).

---

## Community & Ecosystem

### Adoption

- ~20 million total users as of July 2025
- 4.7 million paid subscribers as of January 2026 (~75% YoY growth)
- Deployed at ~90% of Fortune 100 companies; 50,000+ organizations
- 42% market share in AI coding tools market (valued at $7.37B in 2025)
- 400% YoY user growth from early 2024 to early 2025

### Productivity Data (GitHub-reported)

- Developers report up to 55% task speed-up
- PR cycle time reduced from 9.6 days to 2.4 days (75% reduction) in some studies
- Average 46% of code written is Copilot-generated; Java developers reach 61%

### Open Source Status

Copilot itself is **not open source**. The VS Code extension's core logic is proprietary. However:
- GitHub published `copilot.vim` (the Neovim/Vim plugin) as open source
- The Language Server Protocol adapter for some integrations is open source
- GitHub has released open datasets and model cards related to Copilot research

### Extensibility

- **MCP servers:** Any MCP-compatible server can be connected to Copilot agent mode or cloud agent, extending its tool access to databases, APIs, CI systems, etc.
- **Custom agents (cloud agent):** Custom agent profiles (Markdown + YAML frontmatter) define specialized versions of the cloud agent with specific tools, instructions, and MCP configurations.
- **Copilot Extensions (GitHub Marketplace):** Third-party extensions can be invoked via `@extensionname` in Copilot Chat, integrating external services like Sentry, Datadog, Docker, and more.
- **Agent HQ:** Multi-agent orchestration layer announced at GitHub Universe 2025 enables third-party agent integration under the Copilot umbrella.

### Governance and Compliance

- IP indemnification on Business and Enterprise plans
- Content exclusions: can configure Copilot to exclude suggestions matching public code
- Audit logs and usage metrics available for org admins
- Data does not train GitHub's models when using Business/Enterprise (by default)
