# AI Coding Assistant Comparison Guide
**May 3, 2026**

---

## 1. Executive Summary

The AI coding assistant market has matured from autocomplete novelty into a contested landscape of agentic platforms that can plan, write, debug, and ship code with minimal human intervention. As of mid-2026, fifteen notable tools span the spectrum from zero-cost open-source CLIs to $200/month enterprise IDEs, and from lightweight VS Code plugins to fully autonomous cloud agents. Consolidation is accelerating: Cognition acquired Windsurf ($250M), xAI/SpaceX agreed to acquire Cursor ($50B+), and Google absorbed the Windsurf leadership team to build Antigravity — signals that the independent IDE era may be brief.

The core divide in the market is between **interface-first tools** (IDEs and plugins that keep AI inside the editor) and **agent-first tools** (CLIs and autonomous runtimes that treat the codebase as data and the shell as the workspace). Cursor, Windsurf, Antigravity, Trae, and CodeBuddy compete for the IDE tier; Claude Code, OpenCode, Gemini CLI, Codex CLI, and Qwen Code compete for the terminal tier; Cline, Kilo, Copilot, and Augment occupy the extension/plugin tier; and Hermes Agent is a category unto itself as a persistent, self-improving agent runtime.

No single tool wins on all dimensions. Claude Code leads on SWE-bench and autonomous batch work. Copilot leads on enterprise market share and GitHub integration. Cursor leads on IDE experience and parallel agent execution. Gemini CLI leads on free-tier generosity and context window size. OpenCode leads on open-source community and provider flexibility. The choice is almost always shaped by workflow (terminal vs. IDE), model preference (locked vs. flexible), cost structure (subscription vs. pay-as-you-go), and privacy posture.

---

## 2. Tool Categories

### CLI / Terminal Agents
Tools that run in the terminal, operate on local files and shell, and are driven by natural language prompts. No persistent GUI; best for developers who live in the terminal or want headless/CI use.

- **Claude Code** (Anthropic) — reference agentic CLI; best SWE-bench scores
- **OpenCode** (Anomaly Co) — MIT, provider-agnostic, 75+ models, 154K GitHub stars
- **Gemini CLI** (Google) — Apache 2.0, 1M-token context, largest free tier
- **Codex CLI** (OpenAI) — Rust-based, Apache 2.0, tight GitHub integration
- **Qwen Code** (Alibaba) — Apache 2.0, open-weight models, fully self-hostable

### VS Code Forks (AI-native IDEs)
Standalone editors forked from VS Code with AI baked into every layer — not plugins. Full VS Code extension compatibility.

- **Cursor** (Anysphere) — deep indexing, multi-model, background cloud agents
- **Windsurf** (Cognition/Codeium) — proprietary SWE models, Flows, Codemaps
- **Google Antigravity** (Google) — three-surface agent model, browser automation native
- **Trae** (ByteDance) — aggressive free tier, SOLO mode, significant privacy concerns

### IDE Extensions / Plugins
Extensions that augment existing editors (primarily VS Code and JetBrains) without replacing them.

- **GitHub Copilot** (Microsoft/GitHub) — dominant market share, multi-model, GitHub-native
- **Cline** (Cline Bot Inc.) — Apache 2.0, model-agnostic, browser-in-the-loop
- **Kilo Code** (Kilo) — Cline/Roo fork, Orchestrator mode, 500+ models, JetBrains support
- **Augment Code** (Augment, Inc.) — enterprise-scale Context Engine, multi-repo, spec-driven agents
- **CodeBuddy** (Tencent Cloud) — full-lifecycle (design → deploy), WeChat ecosystem, China-focused

### Autonomous Agent Runtimes
Not IDE-centric; operate as long-lived agents or frameworks with persistent memory and self-improvement.

- **Hermes Agent** (Nous Research) — MIT, self-improving skills, 15+ messaging platforms, 200+ model providers

---

## 3. Comparison Matrix

| Tool | Type | Maker | Entry Paid Price | Models | Open Source | Offline/Local | MCP Support | Agent Mode | Key Strength |
|---|---|---|---|---|---|---|---|---|---|
| **Claude Code** | CLI | Anthropic | $20/mo (Pro) | Claude only | Source-available | No | Yes (creator) | Yes | SWE-bench leader, deep shell integration |
| **OpenCode** | CLI + TUI | Anomaly Co | Free (BYOK) | 75+ providers | MIT | Via Ollama | Yes | Yes | Provider-agnostic, true OSS, LSP-aware |
| **Gemini CLI** | CLI | Google | Free (1K req/day) | Gemini family | Apache 2.0 | No (cloud inference) | Yes | Yes | Largest free tier, 1M token context |
| **Codex CLI** | CLI | OpenAI | $8/mo (Go) | GPT-5.x family | Apache 2.0 | No | Yes | Yes | GitHub-native automation, parallel agents |
| **Qwen Code** | CLI | Alibaba | Free (BYOK) | Qwen + multi-provider | Apache 2.0 | Via Ollama/vLLM | Yes | Yes | Self-hostable end-to-end, 1M token context |
| **Cursor** | VS Code fork | Anysphere | $20/mo (Pro) | Multi-provider | No | No | Yes (40-tool cap) | Yes | Codebase indexing, parallel cloud agents |
| **Windsurf** | VS Code fork | Cognition | Free / $20/mo (Pro) | SWE-1.x + multi | No | No | Yes | Yes | Proprietary SWE models, Codemaps, Flows |
| **Antigravity** | VS Code fork | Google | Free (preview) / $20/mo | Gemini + multi | No | No | Yes | Yes | Three-surface agents, browser automation |
| **Trae** | VS Code fork | ByteDance | Free / $10/mo (Pro) | Claude, GPT, Gemini | No | No | Yes | Yes | Lowest price, SOLO mode — privacy risks |
| **Copilot** | Plugin + CLI | GitHub/Microsoft | Free / $10/mo (Pro) | OpenAI + Claude + Gemini | No | No | Yes | Yes | Market leader, GitHub integration, multi-model |
| **Cline** | VS Code ext | Cline Bot Inc. | Free (BYOK) | 30+ providers | Apache 2.0 | Via Ollama | Yes (unlimited) | Yes | Transparent pricing, browser-in-the-loop |
| **Kilo Code** | VS Code/JB ext | Kilo | Free (BYOK) | 500+ models | Apache 2.0 / MIT | Via Ollama | Yes (marketplace) | Yes | Orchestrator mode, JetBrains, Memory Bank |
| **Augment Code** | Plugin + CLI | Augment, Inc. | $20/mo (Indie) | Multi-provider | No | No | Yes | Yes | Enterprise-scale Context Engine, multi-repo |
| **CodeBuddy** | Plugin + IDE + CLI | Tencent Cloud | Free / $9.95/mo (Pro) | Hunyuan + DeepSeek + multi | No | No | Yes | Yes | Full lifecycle (design→deploy), WeChat stack |
| **Hermes Agent** | Agent runtime | Nous Research | Free (self-hosted) | 200+ providers | MIT | Via local models | Yes | Yes | Self-improving skills, persistent memory |

---

## 4. Feature Deep-Dives

### Pricing & Cost Model

The market has split into three cost philosophies. **Subscription bundles** (Cursor, Windsurf, Antigravity, Trae, Copilot) charge flat monthly rates with usage caps; predictable but potentially limiting for heavy users. **BYOK / pay-as-you-go** (Claude Code API, Cline, Kilo, OpenCode, Qwen Code, Hermes) charge nothing for the tool and pass model costs through directly; cheap for light use, expensive at scale. **Managed subscriptions with credit systems** (Augment, CodeBuddy, Windsurf credits) fall in between, offering pooled budgets with per-feature metering.

Free tiers vary dramatically. Gemini CLI offers 1,000 requests/day at zero cost — the most generous in the category. Copilot Free gives 2,000 completions + 50 agent requests/month. Windsurf provides unlimited Tab autocomplete free. Trae's free tier includes Claude 3.5 Sonnet and GPT-4o at no cost. CodeBuddy offers 50 Craft credits/day free. Claude Code, Augment, and Codex require paid plans for meaningful use.

The hidden cost in all BYOK tools is frontier model API spend. Heavy Cline or Kilo users routinely spend $10–$25/day at Claude Opus or GPT-5 rates — far exceeding equivalent flat-rate subscriptions. OpenCode partially addresses this by supporting existing Copilot or ChatGPT subscriptions as authentication backends at no additional API cost.

### Model Flexibility (Single Vendor vs. Multi-Model)

Only Claude Code locks you to a single vendor (Anthropic). Every other tool offers some degree of multi-model support, though depth varies. Copilot is the most comprehensive closed-product offering: OpenAI, Anthropic, Google, and xAI models under one subscription. OpenCode, Cline, Kilo, Hermes, Qwen Code, and Codex all support 30–200+ providers including local models via Ollama.

Cursor and Windsurf offer multi-model routing but limit it to a curated set of frontier providers (Claude, GPT, Gemini, Grok, DeepSeek). Windsurf adds its proprietary SWE-1.x models as the default path, making the product less model-neutral in practice. Augment takes a model-agnostic stance — it owns the orchestration and context layer, not the models, and exposes intelligent routing (Prism) across providers.

Trae and Antigravity offer Gemini and Claude as alternatives but default to their respective first-party or vendor-preferred models. CodeBuddy defaults to Tencent's Hunyuan model with Claude/GPT as switches. Gemini CLI is Google-model-first but technically accepts any API-key-backed Gemini endpoint.

### Agentic Capabilities (Autonomous Multi-Step Tasks)

All fifteen tools claim agentic capability, but execution quality and autonomy depth differ significantly. Claude Code's agentic loop is the most mature for pure coding tasks, with SWE-bench Verified scores of 87.6% (Opus 4.7) and 79.6% (Sonnet 4.6) — the highest verified scores as of May 2026. It operates as a true while-loop agent: gather context → act → verify → repeat, across dozens of tool calls without human intervention.

Cursor's background cloud agents and Windsurf's Cascade are the strongest IDE-side agentic systems, capable of running CI pipelines, full test suites, and generating preview deployments autonomously. Antigravity's three-surface model (editor + terminal + browser simultaneously) is architecturally distinctive but was still maturing as of early 2026. Augment's Intent workspace — with Coordinator/Implementor/Verifier agent hierarchy and living specifications — is the most structured multi-agent system, scoring #1 on SWE-Bench Pro.

At the lower end, Copilot's cloud agent is solid for well-scoped GitHub issue resolution but lacks the depth of Claude Code or Cursor for complex multi-file tasks. Trae's SOLO mode showed 75.2% autonomous task completion in independent tests. Hermes Agent is the only tool designed for truly long-running autonomous operation across sessions, but trades raw coding benchmark performance for persistent memory and self-improvement.

### Codebase Understanding (Indexing, Context Window, Repo-Scale)

Context window is a key differentiator. Gemini CLI and Qwen Code offer up to 1M tokens effective context — enough to load entire large codebases in a single session. Claude Code (500K on Enterprise) and Copilot Enterprise (200K) are competitive. Most other tools operate in the 128K–200K range per session.

Codebase indexing goes beyond raw context size. Cursor's three-layer pipeline (Tree-sitter AST segmentation + Turbopuffer vector DB + 7B CodeLlama reranker) retrieves semantically relevant context from repos up to ~50K files. Augment's Context Engine is the most sophisticated: a semantic knowledge graph that processes 500K+ files, understands call graphs, cross-service dependencies, and commit history — the only system explicitly built for enterprise monorepo and microservice scale.

Kilo Code, Cline, and OpenCode rely on LSP integration and file-tree scanning rather than deep vector indexing. Trae uses just-in-time scanning that degrades past ~100K lines. CodeBuddy uses vector embeddings for semantic search but doesn't publish context window limits. Hermes uses FTS5 keyword search — no semantic retrieval — which limits its ability to surface past solutions when terminology differs.

### Extensibility (MCP, Plugins, Hooks)

MCP (Model Context Protocol), created by Anthropic, has become the de facto interoperability standard. All fifteen tools support MCP to varying degrees. Claude Code is the reference implementation with the broadest hook system (27 lifecycle events). OpenCode has 40+ lifecycle hooks and a full npm-based plugin runtime. Kilo ships a first-class MCP marketplace. Cline can autonomously author new MCP servers on demand. Antigravity indexes 1,500+ MCP servers at antigravity.codes.

Beyond MCP, extensibility approaches diverge. Cursor uses `.cursorrules` project files and supports custom OpenAI-compatible endpoints. Windsurf has Cascade Hooks for reusable workflow commands. Copilot uses GitHub Marketplace extensions invokable via `@extensionname`. CodeBuddy ships an open Plugin SDK with commands, skills, and hooks. Hermes has a modular skills system following the agentskills.io open standard, adopted by 26+ platforms. Claude Code uniquely separates four orthogonal extension mechanisms: MCP, plugins, skills, and hooks — each targeting a different layer of the agent loop.

### Privacy & Data Handling

This is the starkest divide in the market. Self-hosted open-source tools (Qwen Code + local models, Hermes, OpenCode + Ollama) offer true data isolation — no code ever leaves the machine. Claude Code, Copilot Enterprise, Augment Enterprise, and Windsurf Enterprise offer contractual data-retention protections with no training on customer data. All paid-tier tools reviewed (except Trae) make explicit commitments about not training on paid-plan data.

**Trae is the most significant privacy concern in this comparison.** Documented analysis shows telemetry continues after opt-out, collected data includes file contents and persistent device identifiers, data is retained 5 years post-account-closure, and terms permit using input for model training. ByteDance ownership subjects data to Chinese data laws. **Trae should not be used for proprietary code, government projects, or any work under NDA.**

Gemini CLI's free tier (personal Google account) may use data for model improvement — a lesser but real concern for confidential codebases. The paid Vertex AI path opts out of training. Google Antigravity's free preview offers no published data policy, which is concerning for sensitive work.

### Enterprise Readiness (SSO, Audit, Compliance)

Copilot Enterprise is the most enterprise-hardened product: deployed at ~90% of Fortune 500 companies, with IP indemnification, content exclusions, audit logs, and RBAC under GitHub Enterprise Cloud. Augment Enterprise leads on compliance depth for pure coding agents: SOC 2, ISO 42001, CMEK, SIEM integration, data residency, SSO/SCIM — plus the only semantic context engine that scales to enterprise monorepos.

Windsurf Enterprise offers SOC 2 + HIPAA + FedRAMP + ITAR — the broadest compliance surface in the IDE category. Cursor has SOC 2 and privacy mode but lacks HIPAA/FedRAMP. CodeBuddy offers MLPS Level 3 (Chinese standard) and national cryptographic algorithms, relevant for Chinese enterprise deployments.

Claude Code, Kilo (Enterprise tier), Cline (Enterprise plan), and Codex (Enterprise plan) all offer SSO/SCIM and audit logs at their enterprise tiers. OpenCode, Gemini CLI, Hermes, and Qwen Code have minimal or no enterprise governance features — they are developer tools, not enterprise platforms.

### Open Source vs. Proprietary

Five tools are fully or substantially open source:
- **OpenCode** (MIT) — CLI + TUI; 154K stars, fully forkable, self-hostable
- **Gemini CLI** (Apache 2.0) — Google's CLI; community contributions welcomed
- **Codex CLI** (Apache 2.0) — OpenAI's CLI layer; inference still requires OpenAI account
- **Qwen Code** (Apache 2.0) — CLI + open-weight models; truly self-hostable end-to-end
- **Hermes Agent** (MIT) — agent runtime + skills; no managed service
- **Cline** (Apache 2.0) — VS Code extension; largest OSS coding agent extension
- **Kilo Code** (Apache 2.0 / MIT) — extension; forked from Cline/Roo

Claude Code is source-available (TypeScript published March 2026) under Anthropic's commercial terms — auditable but not OSI open source.

Cursor, Windsurf, Antigravity, Trae, Copilot, Augment, and CodeBuddy are fully proprietary. The VS Code base they fork is open source, but their AI layers, indexing pipelines, and models are closed.

---

## 5. Decision Guide

**Use Claude Code when** you need the highest autonomous coding performance on complex multi-file tasks, you're comfortable with terminal-native workflows, and you don't need model flexibility. Best for teams delegating entire feature builds or large refactors.

**Use OpenCode when** you want a true open-source terminal agent with no vendor lock-in, need to switch between 75+ model providers, or want to authenticate with an existing Copilot or ChatGPT subscription. Best for privacy-conscious or model-experimenting developers.

**Use Gemini CLI when** you want a capable agentic CLI at zero cost, work heavily in GCP or Google Workspace, need a 1M-token context window for large repos, or want fully auditable Apache 2.0 tooling.

**Use Codex CLI / Codex Cloud** when your workflow is GitHub-centric and you want issue-to-PR automation, parallel async task execution, or a tool that bundles well with existing ChatGPT subscriptions.

**Use Qwen Code when** you need a fully self-hostable agentic coding CLI — both the CLI and model weights are open source, enabling zero-egress operation on your own GPU infrastructure.

**Use Cursor when** you want the most capable AI-native IDE experience, need deep codebase indexing across large repos, want parallel cloud agents running CI while you code locally, and are willing to pay $20–$60/month for best-in-class IDE tooling.

**Use Windsurf when** you want agentic autonomy in a VS Code-style editor, need compliance beyond SOC 2 (HIPAA, FedRAMP, ITAR), use multiple editors including JetBrains or Vim, or want visual codebase maps (Codemaps) to onboard to large repos faster.

**Use Google Antigravity when** your work is greenfield, you want native browser automation integrated with your IDE's agent, you're deep in the Google ecosystem, and you're willing to tolerate a product still stabilizing as of early 2026.

**Use Trae when** you're an individual developer on a tight budget working on non-proprietary personal projects, and you explicitly understand and accept the data privacy risks from ByteDance ownership.

**Use GitHub Copilot when** your organization is already on GitHub Enterprise, you want a single product covering inline completions + agent mode + cloud PR automation across VS Code, JetBrains, and Vim, or you need enterprise governance with IP indemnification.

**Use Cline when** you want a VS Code extension that gives the full agentic loop without leaving your editor, need browser-in-the-loop verification, want unlimited MCP tools with no caps, and prefer transparent BYOK pricing with Apache 2.0 auditable code.

**Use Kilo Code when** you need an open-source VS Code/JetBrains agent with an Orchestrator mode for complex multi-agent routing, persistent Memory Bank for long-running projects, and access to 500+ models through a zero-markup gateway.

**Use Augment Code when** you're working on an enterprise-scale codebase (100K–1M+ files), need multi-repo or microservice-aware context, want spec-driven multi-agent orchestration via Intent, or need the deepest enterprise security posture (CMEK, data residency, SIEM).

**Use CodeBuddy when** you're building for the Tencent/WeChat ecosystem, need MLPS Level 3 compliance for Chinese enterprise deployments, or want a single product covering design-to-deploy without tool switching — especially for teams already on Tencent Cloud.

**Use Hermes Agent when** you want a persistent, self-improving autonomous agent that compounds knowledge over weeks and months, need to reach it across 15+ messaging platforms, or want to build RL training pipelines from agent trajectories. Not for teams that need compliance or pure coding benchmark performance.

---

## 6. What They All Share

Across all fifteen tools, the following capabilities are now table stakes:

- **Multi-file editing**: every tool can plan and apply coordinated changes across multiple files in a single task
- **Shell/terminal execution**: all agents can run build commands, tests, linters, and git operations, then reason about the output
- **MCP support**: Model Context Protocol is supported by every tool in this comparison
- **Plan-before-act mode**: all tools offer some form of read-only analysis phase before making changes
- **Natural language interface**: describe a task in plain English; the tool handles decomposition and execution
- **Context file conventions**: all tools support some variant of project-level instruction files (CLAUDE.md, AGENTS.md, GEMINI.md, .clinerules, .cursorrules, windsurf_rules, AGENTS.md)
- **Session-level undo or rollback**: all tools provide some mechanism to revert agent changes
- **Non-interactive / headless operation**: all tools can run in CI/CD pipelines or scripted contexts
- **Multi-language support**: all tools work across Python, TypeScript, Go, Rust, Java, and most mainstream languages

---

## 7. What None of Them Do Well (Yet)

**Cross-session project memory without manual setup.** Most tools treat each session as a blank slate. CLAUDE.md, AGENTS.md, and similar files require manual curation. Only Hermes Agent builds memory automatically from task execution, and its FTS5 retrieval is limited. Augment's Context Engine is the closest to automatic cross-session understanding, but it indexes code, not the conversational history of decisions made.

**Architecture-level judgment.** Tools can implement a feature you specify, but none reliably evaluate trade-offs between competing architectural approaches, flag long-term maintainability risks, or push back on fundamentally bad design decisions. They execute intent, they don't challenge it.

**Guaranteed algorithm correctness.** Qwen Code has documented cases of silently substituting simpler but incorrect algorithms. Claude Code, Copilot, and Cursor all produce code that looks correct and compiles but contains logic errors in complex domains. Human review remains mandatory for security-critical, financial, or safety-critical code.

**True offline / air-gapped operation.** Every tool that provides useful AI inference requires a network call — to Anthropic, OpenAI, Google, or a self-hosted endpoint that itself requires infrastructure. Qwen Code + local Ollama is the closest to genuine air-gap capability, but setup complexity is significant and model quality at local-runnable sizes lags frontier models substantially.

**Multi-agent coordination across tool boundaries.** While Augment's BYOA feature and Hermes's subagent spawning gesture toward this, there is no mature standard for Claude Code, Cursor, and Copilot agents collaborating on the same task. Agent HQ (Copilot) is nascent. Real cross-tool orchestration requires bespoke glue code.

**Long-horizon planning across calendar time.** All agentic tools are session-scoped or task-scoped. None track a multi-week feature's progress, maintain awareness of external project management state (sprint goals, team capacity), or autonomously reschedule work in response to changing priorities. Hermes Agent is the closest with its scheduling and long-lived daemon model, but it does not integrate with project management tools in a meaningful planning loop.

**Cost transparency.** Token costs, credit consumption rates, and per-operation pricing are opaque or inconsistently documented across most tools. Windsurf's credit-to-token conversion is undocumented. Augment's per-operation credit variance (293 credits simple vs. 4,261+ credits complex) makes budgeting difficult. Only Cline and Kilo in BYOK mode offer full transparency because costs are exactly what the underlying API charges.
