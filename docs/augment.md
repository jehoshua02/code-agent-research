# Augment Code

## What It Is

**Augment Code** is an agentic AI coding platform built for professional engineering teams working on large, complex codebases. It positions itself as "The Software Agent Company."

- **Product category:** AI coding agent platform (IDE agents, CLI agent, desktop workspace, code review bot)
- **Maker:** Augment, Inc. (Palo Alto, CA)
- **Founded:** 2022 by Igor Ostrovsky (ex-Microsoft) and Guy Gur-Ari (ex-Google Research); executive team includes CEO Scott Dietzen (ex-CEO of Pure Storage) and Dion Almaer (ex-Google, Shopify)
- **Launch:** Emerged from stealth April 24, 2024 with $252M raised (Series B); flagship extension first shipped late 2023 in private access
- **Investors:** Eric Schmidt, Index Ventures, Sutter Hill Ventures, Lightspeed, Meritech Capital, Innovation Endeavors; near-unicorn at ~$977M post-money valuation
- **Pricing:**
  - **Indie:** $20/month — 40,000 credits/month, 1 user
  - **Standard:** $60/month per developer — 130,000 credits/month, up to 20 users
  - **Max:** $200/month per developer — 450,000 credits/month, up to 20 users
  - **Enterprise:** Custom pricing — unlimited users, custom credits, CMEK, data residency, audit trails, SIEM, SSO/SCIM
  - **Top-up:** $15 per 24,000 credits on all paid plans (expire 12 months after purchase)
  - Credits pool at the team level. No AI training on paid plan data. No free tier.

---

## What It Does

### Core Capabilities

- **Context Engine:** Semantically indexes entire codebases — code, dependencies, commit history, documentation, issues — into a real-time knowledge graph. Processes 50,000+ files/minute and has scaled to 1M+ file repositories. Retrieves only relevant context rather than dumping entire codebases into prompts.
- **IDE Agents (VS Code & JetBrains):** Natural language → multi-step task plans → multi-file edits and PRs. Supports persistent memories and task lists. Agents understand cross-file and cross-service relationships.
- **Auggie CLI:** Terminal-based coding agent (`auggie` command). Operates autonomously in the terminal with the same Context Engine backing.
- **Intent Workspace (macOS, public beta):** Spec-driven multi-agent desktop environment. A Coordinator agent drafts a living specification, decomposes it into tasks, and delegates to parallel Implementor agents in waves. A Verifier agent checks implementation against the spec before PR creation. Supports BYOA (Bring Your Own Agent): Claude Code, Codex, and OpenCode can run inside Intent alongside Auggie.
- **Code Review Bot:** GitHub-integrated PR reviewer that catches bugs and style mismatches; provides one-click fixes in the IDE. Generates PR summaries and inline comments.
- **Chat & Agents:** Conversational interface available across IDE and CLI surfaces for Q&A, exploration, and task delegation.
- **MCP & Native Tools:** Exposes the Context Engine as an MCP server. Native integrations with GitHub, Linear, and Notion. MCP support for stdio, SSE, and HTTP transports, enabling connection to arbitrary external tools and data sources.
- **Slack Integration:** Available on Standard and above.

### Supported Languages and Frameworks

No official language restriction stated. The Context Engine performs semantic indexing across polyglot repositories. Supports cross-repository and cross-service (microservice) context. Works with any language readable by VS Code or JetBrains.

### Benchmarks

- Ranked #1 on SWE-Bench Pro Leaderboard (51.80% vs next-best 50.21%)
- 70% win rate over GitHub Copilot in head-to-head blind study on the Elasticsearch repository; agents outperformed humans in code reuse (+18.2) and completeness (+14.8)

---

## What It Doesn't Do

- **No programmatic SDK:** Unlike Claude Code's Agent SDK (Python/TypeScript), there is no API to build custom subagents or orchestrate Augment agents programmatically.
- **Intent is Mac-only:** Windows and Linux support is explicitly "no plan" as of May 2026.
- **No per-prompt cost visibility:** Analytics show aggregate credit usage but not per-operation cost breakdown.
- **No reasoning effort control:** Cannot tune reasoning depth on reasoning models; no cost/performance lever like Claude Code's `--thinking` budget.
- **Credit ceiling introduces cost uncertainty:** Unlike Cursor's flat-rate unlimited model, unpredictable credit consumption (simple task ~293 credits; complex ~4,261+ credits) can lead to unexpected overage costs.
- **No offline/local model support:** Fully cloud-dependent. No on-premise LLM option.
- **Stability complaints:** User reports document crash-on-task, HTTP 400 errors on simple prompts, and hallucinated APIs — though severity varies by version.
- **Memory limitations:** Context window for ongoing tasks is bounded; persistent state requires explicit "Augment memories," and agents can repeat mistakes across long sessions.

---

## Architecture

### How It Runs

| Surface | Type |
|---|---|
| VS Code extension | IDE plugin (local extension, cloud inference) |
| JetBrains plugin | IDE plugin (local extension, cloud inference) |
| Auggie CLI | Local CLI binary (`auggie`), cloud inference |
| Intent | macOS native desktop app (public beta), cloud inference |
| Code Review bot | Cloud service, GitHub App |
| Context Engine MCP | Cloud MCP server, accessible by third-party agents |

All inference is cloud-side. No local model execution. The Context Engine runs as a cloud service that continuously indexes connected repositories.

### Models Available

Augment supports user-selectable models billed at different credit rates:

| Model | Relative Credit Cost |
|---|---|
| Claude Haiku 4.5 | ~30% of Sonnet baseline |
| GPT-5.4 | ~72% of Sonnet baseline |
| Kimi K2.6 (Moonshot AI) | ~50% of Sonnet baseline |
| GPT-5.1 | ~75% of Sonnet baseline |
| Gemini 3.1 Pro | ~92% of Sonnet baseline |
| Claude Sonnet 4.5 / 4.6 | Baseline (1×) |
| GPT-5.2 | ~133% of Sonnet baseline |
| GPT-5.5 | ~143% of Sonnet baseline |
| Claude Opus 4.5 / 4.6 / 4.7 | ~167% of Sonnet baseline |

**Intelligent routing options:**
- **Prism (Claude + Gemini):** Routes between Opus 4.7, Sonnet 4.6, and Gemini 3.0 Flash; averages 20–30% cheaper than frontier models.
- **Prism (GPT + Kimi):** Routes between GPT-5.5, GPT-5.4, and Kimi K2.6.

Augment does not expose its own proprietary model; it is a model-agnostic orchestration layer on top of third-party frontier models plus its own Context Engine retrieval.

### Context Engine Internals

- Semantic knowledge graph (not simple vector RAG or grep)
- Understands file relationships, call graphs, cross-service dependencies, not just keyword co-occurrence
- Ingests: source code, dependencies, commit history, issue trackers, docs, architectural patterns
- Permission-aware retrieval: respects repo access controls
- Actively compresses context — reports like "4,456 sources → 682 relevant" for a single query
- Exposed externally via MCP server (`auggie-context-mcp`)

---

## Key Differentiators

1. **Enterprise-scale context:** Processes 500,000+ files, multi-repo, multi-service codebases. Competitors (Cursor: ~50K files, Copilot: single-repo window) fall short at this scale.
2. **Cross-service reasoning:** Understands service boundaries, shared telemetry, circuit-breaker patterns across microservice architectures. Can make coordinated changes across multiple services in a single task.
3. **Intent's spec-driven multi-agent orchestration:** Living specification as single source of truth; Coordinator/Implementor/Verifier agent hierarchy; resumable sessions; unique in the market as of 2026.
4. **BYOA interoperability:** Intent lets teams run Claude Code, Codex, or OpenCode inside Augment's workspace — non-exclusive, composable.
5. **Model-agnostic:** Single subscription unlocks Claude, GPT, Gemini, Kimi — user picks model per task. Intelligent routing for cost optimization.
6. **SWE-Bench Pro #1:** Claims highest benchmark score for agentic coding as of 2026.
7. **Enterprise security posture:** SOC 2, ISO 42001, CMEK, SIEM, data residency, SSO/SCIM on Enterprise tier; no AI training on customer data on any paid plan.

---

## Ideal Use Cases

- **Large enterprise codebases:** 100K–1M+ files, polyglot, multi-repo setups where other tools fail to surface relevant context.
- **Microservice architectures:** Tasks requiring coordinated changes across multiple services (integration tests, shared telemetry updates, API contract changes).
- **Teams already on JetBrains:** Augment is one of the few agentic tools with first-class JetBrains support (IntelliJ, PyCharm, etc.).
- **Spec-driven development (Intent):** Projects where architectural alignment across parallel agents matters; large features decomposed across multiple devs or agents.
- **Code review at scale:** Organizations wanting automated PR review that understands codebase conventions, not just syntax.
- **Teams wanting model flexibility:** Organizations that want to route tasks to the cheapest or most capable model without changing tools.
- **Security-conscious enterprises:** Teams that need CMEK, data residency, audit logs, and training opt-out guarantees.

Not ideal for: solo developers on small projects (credit cost model disadvantages low-volume users vs. flat-rate tools), Windows/Linux users who want the Intent workspace, or teams wanting a programmable agent SDK.

---

## Community & Ecosystem

- **Closed-source product:** The core platform (Context Engine, IDE extensions, Intent, CLI) is proprietary.
- **Open protocol participation:** Augment exposes and consumes MCP (Model Context Protocol), enabling integration with third-party tooling.
- **Community MCP server:** [`aj47/auggie-context-mcp`](https://github.com/aj47/auggie-context-mcp) — open-source community project exposing the Context Engine as an MCP server for use with other agents.
- **Adoption:** Enterprise clients include MongoDB, Spotify, Snyk, Webflow. Revenue reported at $20M ARR with 156-person team (as of 2025).
- **Marketplace presence:** Available on VS Code Marketplace and JetBrains Plugin Marketplace.
- **No public API / agent SDK:** Extensibility is via MCP integrations only; no programmable surface for building on top of Augment agents.
- **BYOA policy:** Supports external agents (Claude Code, Codex, OpenCode) running inside Intent, making Augment additive rather than exclusive.
- **GitHub App:** Code review bot installs as a standard GitHub App.
