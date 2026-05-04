# Cursor

## What It Is

**Product category:** AI-native code editor (standalone IDE)
**Developer:** Anysphere, Inc. — San Francisco startup founded 2022
**Initial release:** 2023
**Latest stable:** Cursor 3.1 (April 13, 2026)
**License:** Proprietary

Cursor is a fork of Visual Studio Code with AI deeply integrated at every layer — autocomplete, inline editing, multi-file composition, and autonomous agents. It is not a plugin; it ships its own editor binary with full control over the UI, indexing pipeline, and inference routing.

**Traction (as of early 2026):**
- 2M+ total users, 1M+ paying, 1M daily active users
- $2B annualized revenue (February 2026)
- Trusted by over half the Fortune 500; ~40,000 engineers at NVIDIA
- Valuation: $29.3B (Series D, November 2025)
- Acquisition: SpaceX/xAI reportedly agreed to acquire Anysphere for $50B+ (April 2026)

---

## Pricing

| Plan | Price | Key Inclusions |
|---|---|---|
| **Hobby** | Free | Limited agent requests, limited Tab completions |
| **Pro** | $20/user/month | Extended agent limits, frontier models, MCPs, skills, hooks, cloud agents |
| **Pro+** | $60/user/month | 3x usage on all OpenAI/Claude/Gemini models |
| **Ultra** | $200/user/month | 20x usage, priority access to new features |
| **Teams** | $40/user/month | Shared chats/rules, centralized billing, usage analytics, RBAC, SAML/OIDC SSO |
| **Enterprise** | Custom | Pooled usage, invoice/PO billing, SCIM, AI code tracking API, audit logs, granular model controls |

**Bugbot (automated PR review)** is a separate add-on: $40/user/month for Pro (up to 200 PR reviews/month) or Teams (all PRs + analytics dashboard).

Student discount: free Pro year with a school email address.

---

## What It Does

### Tab (Autocomplete)

Context-aware inline completions using a custom fast model trained with online reinforcement learning (retrained every 1.5–2 hours). Predicts multi-line edits, handles brackets, and infers next actions. Powered internally by a fine-tuned Llama-3-70B using **speculative edits** — outputs the entire file with changes applied, using the original as draft tokens, achieving ~1,000 tokens/second (~13x speedup over naive generation).

### Ask Mode

Read-only exploration: ask questions about the codebase, understand structure, draft plans — without modifying files. Uses the full codebase index for context.

### Agent Mode

Fully autonomous task execution: reads files, edits across multiple files, runs terminal commands (builds, tests, linters), iterates on failures. Supports:
- **Subagents**: parallel specialized workers delegated by a parent agent for discrete subtasks (codebase research, terminal commands, parallel work streams)
- **Background agents**: long-running cloud agents that take a ticket and work for tens of minutes without occupying local resources; they can run CI/CD pipelines, full test suites, and generate preview deployments
- **Parallel execution**: `/best-of-n` command runs the same task across multiple models simultaneously in isolated worktrees
- **Automations**: scheduled or event-triggered agents; can respond to GitHub PR opens, PagerDuty alerts, Slack messages, or webhooks

### Composer 2

Multi-file planning and editing tool. Anysphere's proprietary frontier coding model released with Cursor 3 (April 2026). Uses advanced reasoning for complex refactors. Provides diff previews before applying changes. Can simultaneously edit 10+ files, generate tests, and update documentation.

### Bugbot / Fixer

Automated PR review agent. Evolved from an 8-pass pipeline to a fully agentic system that reasons over diffs, calls tools dynamically, and decides its own investigation depth. Achieves ~80% PR review resolution rate.

### Ctrl+K (Inline Edit)

Natural-language inline edits: describe a change in plain English, Cursor applies it in-place with a diff preview.

### Codebase Indexing

Three-layer retrieval:
1. **Segmentation**: Tree-sitter splits code at function/class boundaries
2. **Sync**: Merkle tree of file hashes, uploads only changed files every ~5 minutes
3. **Vector storage**: Turbopuffer serverless vector DB backed by cloud object storage
4. **Reranking**: fine-tuned 7B CodeLlama processes up to 500,000 tokens per query with blob-storage KV caching

### Supported AI Models

Cursor routes across multiple frontier models. Current options include:
- **Claude Opus 4.7** — deep refactors, architecture, complex debugging
- **GPT-5.5** — broad-purpose coding
- **Gemini 2.5 Pro** — 1M+ token context window tasks
- **DeepSeek V4 Pro** — near-frontier reasoning at ~1/10th the cost
- **Grok Code** — xAI model
- **cursor-small** — fast, lightweight local-style completions
- **Custom OpenAI-compatible endpoints** — self-hosted or third-party models

Model selection is per-request or set as a default. Users can switch mid-session.

### Other Capabilities

- **Mission Control**: window management for multiple agent tabs in side-by-side or grid layout
- **MCP (Model Context Protocol)**: integrations with GitHub, PostgreSQL, Linear, Notion, Playwright; 40-tool ceiling per session
- **Slack integration** for team collaboration
- **GitHub PR review** integration
- **`.cursorrules`**: project-level AI behavior configuration file
- **`.cursorignore`**: exclude files/dirs from indexing (analogous to `.gitignore`)
- **CLI / terminal mode**: run Cursor agents from the terminal

### Language & Framework Support

- **Excellent**: Python, JavaScript, TypeScript
- **Good**: Java, C++, Rust, Go
- **Moderate**: PHP, and most other mainstream languages (inherits VS Code language server support)
- Framework-agnostic; understands React, Next.js, Django, Rails, etc. through codebase indexing

---

## What It Doesn't Do

| Limitation | Detail |
|---|---|
| **Cannot run fully offline** | Cloud inference required; no fully local execution path |
| **Large files degrade** | Files over ~5,000 lines significantly slow Cursor down |
| **Monorepo limits** | Repos >50,000 files can cause planning hangs and rate-limit errors (NGHTTP2_ENHANCE_YOUR_CALM); requires `.cursorignore` tuning |
| **Context degradation** | Long sessions cause reasoning degradation; agents can enter loops repeating irrelevant changes |
| **MCP ceiling** | Hard limit of 40 MCP tools per session |
| **No architectural judgment** | Cannot replace human decisions on system design, trade-offs, security posture |
| **Complex bug detection** | Struggles with subtle bugs in large, deeply coupled codebases |
| **Multi-IDE coverage** | Works only in the Cursor editor; no JetBrains, Xcode, Neovim, or other IDE support |
| **No built-in file restrictions** | No native way to prevent agents from accessing specific files beyond OS-level permissions |
| **Unpredictable costs** | Usage-based tiers make monthly spend hard to predict for heavy users |

### Known Security Issues

- CVE-2025-54135, CVE-2025-54136: MCP-related remote code execution (patched in v2.5)
- CVE-2025-59944: case-sensitivity bypass for file protection (patched)
- Workspace Trust disabled by design — risk when opening untrusted repos
- Agent terminal access creates a prompt injection attack surface
- `.env` files and SSH keys on disk can be inadvertently included in agent context

---

## Architecture

### Editor Layer

- **Base**: VS Code fork written in TypeScript
- **Platforms**: Windows, macOS, Linux
- Full control over editor internals; AI capabilities are not plugins but native editor features

### Inference Layer

- Cloud-based inference via Anysphere's backend
- Model router fronts multiple providers (Anthropic, OpenAI, Google, xAI, DeepSeek)
- Speculative decoding for completions: fine-tuned Llama-3-70B at ~1,000 tokens/sec
- Tab RL model: online reinforcement learning, retrained every 1.5–2 hours

### Indexing Layer

- Tree-sitter AST segmentation at function/class boundaries
- Turbopuffer vector DB for semantic retrieval
- 7B CodeLlama reranker; up to 500K tokens per query
- Merkle tree sync: only changed files uploaded, ~5-minute cadence

### Cloud Agent Layer

- Sandboxed isolated environments on Anysphere infrastructure
- Supports CI/CD execution, test suites, preview deployments
- Event-driven triggers: GitHub webhooks, PagerDuty, Slack

### Privacy Mode

When enabled:
- Zero Data Retention terms enforced with all model providers
- File paths encrypted segment-by-segment client-side; plaintext fetched only at inference time for the specific lines needed
- Code not retained after fulfilling a request
- SOC 2 certified

---

## Key Differentiators

| Feature | Cursor | GitHub Copilot | Windsurf |
|---|---|---|---|
| **Architecture** | VS Code fork (native AI) | Plugin (VS Code, JetBrains, etc.) | VS Code fork |
| **Codebase indexing** | Deep (Tree-sitter + vector DB) | Shallow | Moderate |
| **Agent autonomy** | High (subagents, background, cloud) | Moderate (Coding Agent) | High (Cascade) |
| **Multi-IDE support** | No (Cursor only) | Yes (broadest coverage) | No (Windsurf only) |
| **Parallel agents** | Yes (`/best-of-n`, worktrees) | No | No |
| **Event-driven automations** | Yes (webhooks, GitHub, Slack) | Limited | No |
| **Bring-your-own-model** | Yes (OpenAI-compatible endpoints) | No | Limited |
| **Code acceptance rate** | ~72% (reported) | ~55% (reported) | ~65% (reported) |
| **Tab completion latency** | Fast | Fast | Fastest (<150ms) |
| **Team controls** | Strong (RBAC, SSO, analytics) | Strong (enterprise-grade) | Basic |
| **Price (entry paid)** | $20/month | $10/month (individual) | $15/month |

**Cursor's strongest differentiators:**
1. **Codebase-as-context**: the indexing pipeline gives every suggestion awareness of the full repo, not just open files
2. **Background + cloud agents**: the only IDE with agents that run in the cloud on real infrastructure while you keep coding locally
3. **Parallel task execution**: `/best-of-n` and worktrees allow truly parallel agent runs; no competitor matches this
4. **Event-driven automations**: respond to GitHub PRs, CI alerts, or Slack without a human in the loop
5. **Model flexibility**: swap between Claude, GPT, Gemini, DeepSeek, or self-hosted models per task

---

## Ideal Use Cases

- **Large codebase navigation and refactoring**: deep indexing makes it uniquely capable on repos where other tools lose context
- **Multi-file feature development**: Composer 2 handles coordinated changes across many files in a single prompt
- **Autonomous background tasks**: running tests, fixing CI failures, or handling GitHub issues without blocking the developer
- **Teams that need control**: RBAC, SSO, privacy mode, and audit logs make it viable for regulated environments
- **Polyglot projects**: model-switching allows matching the right model to the right language or task
- **Developers who want to stay in an IDE**: unlike terminal agents (Claude Code), Cursor keeps AI inside the editor workflow

Less suitable for: engineers who need JetBrains or Xcode support, fully offline/air-gapped environments, or cost-sensitive individuals doing light AI usage (Copilot Individual at $10/month may suffice).

---

## Community & Ecosystem

- **Open source status**: Proprietary. The VS Code base is open-source (MIT), but Cursor's AI layers, indexing pipeline, and models are closed.
- **Extension compatibility**: inherits the full VS Code extension marketplace; existing VS Code extensions install without modification
- **MCP ecosystem**: growing library of one-click MCP integrations (GitHub, Linear, Notion, PostgreSQL, Playwright, and more)
- **`.cursorrules`**: a community-driven convention for project-specific AI behavior; hundreds of shared templates exist on GitHub
- **Community forum**: active at forum.cursor.com
- **Changelog**: actively maintained at cursor.com/changelog; frequent releases (multiple per month in 2025–2026)
- **Funding & backing**: Andreessen Horowitz, Thrive Capital, Coatue, Google, Nvidia, OpenAI — broad institutional support
- **Acquisition status**: pending xAI/SpaceX acquisition (announced April 2026); future open-source posture unknown

---

## Sources

- [Cursor Pricing](https://cursor.com/pricing)
- [Cursor Homepage](https://cursor.com/)
- [Cursor Wikipedia](https://en.wikipedia.org/wiki/Cursor_(code_editor))
- [Cursor IDE Complete Guide 2026 — Codersera](https://codersera.com/blog/cursor-ide-complete-guide-2026/)
- [How Cursor Actually Works — Data Science Collective](https://medium.com/data-science-collective/how-cursor-actually-works-c0702d5d91a9)
- [Cursor AI — daily.dev](https://daily.dev/blog/cursor-ai-everything-you-should-know-about-the-new-ai-code-editor-in-one-place)
- [Cursor vs Windsurf vs GitHub Copilot — Builder.io](https://www.builder.io/blog/cursor-vs-windsurf-vs-github-copilot)
- [Cursor Security](https://cursor.com/security)
- [Cursor Security Risks — TrueFoundry](https://www.truefoundry.com/blog/cursor-security)
