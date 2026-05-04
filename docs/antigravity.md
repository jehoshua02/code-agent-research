# Google Antigravity

## What It Is

**Product category:** Agent-first IDE / agentic development platform.

**Maker:** Google (developed with involvement from Google DeepMind). Evidence in the codebase suggests it incorporated technology from Windsurf ("Cascade" references found); Google acquired Windsurf's leadership team and ~40 engineers in a reported $2.4B deal, then shipped Antigravity separately.

**Released:** November 18, 2025, announced alongside Gemini 3. Public preview download went live November 20, 2025. Current version: 1.23.2 (as of April 2026).

**Pricing:**
- Free during public preview with "generous rate limits" (exact limits not documented)
- AI Pro: $20/month
- AI Ultra: $249.99/month
- On-demand credits: $25 per 2,500 credits
- Credit-to-token conversion is not publicly documented — a recurring user complaint
- In early 2026, quota refresh rates quietly degraded from ~5-hour cycles to weekly resets for some tiers, triggering significant community backlash
- Google suspended accounts using Antigravity quotas with unauthorized third-party agent tools (e.g., OpenClaw, OpenCode)

---

## What It Does

### Core concept

Antigravity is built around *missions* and *agents*, not files and autocomplete. Instead of helping you write code line by line, you assign tasks to autonomous agents that plan, execute, and verify multi-step work across three integrated surfaces: the editor, a terminal, and an embedded browser.

### Key capabilities

**Three-surface agent execution**
Agents operate simultaneously across the editor (code changes), terminal (running builds, tests, servers), and browser (visual verification, E2E testing). A single agent can scaffold a feature, start a dev server, open the browser, verify the UI, and fix failures — without pausing for input.

**Agent Manager (Manager View)**
A separate application window functioning as mission control. Spawn and monitor multiple agents in parallel across different workspaces. Each agent tracks its own task state, artifacts, and verification status asynchronously.

**Artifacts system**
Instead of raw logs or diffs, agents produce human-readable deliverables: task lists, implementation plans, screenshots, and browser recordings. Verification is at-a-glance rather than parse-the-output.

**Editor View**
Standard VS Code-style editing with tab completions, inline commands, and an integrated agent sidebar. Familiar for existing VS Code / Cursor users.

**Four agent modes**
1. Agent-Driven — full autonomy, minimal interruption
2. Agent-Assisted — agent pauses at key checkpoints for review
3. Review-Driven — human approves each step
4. Custom Configuration — mix-and-match per task

**Knowledge Base**
Agents can persist useful context and code snippets across sessions to improve future task performance within the same project.

**Deep Think mode**
Extended reasoning for complex problems using higher-capability models.

**MCP (Model Context Protocol) support**
Built-in MCP server management. Popular integrations include GitHub, Slack, Google Drive, Jupyter, File System, and SSH servers. Configured via the Agent pane.

**Image generation**
Agents can generate required assets inline (demonstrated in a game-clone test producing sprites on demand).

### Supported languages/frameworks

No explicit whitelist — inherited from VS Code's extension ecosystem. Works on any codebase VS Code handles. Tested publicly on Next.js, Supabase, Python, and standard web stacks. Performance degrades on codebases with non-standard patterns or homegrown frameworks.

### Benchmarks (per Google/third-party claims)

- SWE-bench Verified: 76.2%
- Terminal-Bench 2.0: 54.2%
- Next.js + Supabase feature completion: 42s (vs. Cursor's 68s in one comparison)
- 94% refactoring accuracy vs. 78% for Cursor 2.0 (source: index.dev, methodology unverified)
- 40% faster codebase navigation on 100k+ line repos vs. Cursor 2.0

---

## What It Doesn't Do

- **No Git Worktrees support** — explicitly missing as of early 2026
- **No arrow key navigation** in file explorer
- **Broken extension support** in some modes (e.g., Svelte extension broken at launch)
- **No transparent quota documentation** — users cannot determine credit burn rates in advance
- **No offline/local model support** — all inference runs on Google's servers; data residency is entirely cloud-side
- **No enterprise-grade governance** — agent permission scoping, audit trails for regulated industries, and RBAC are still forming
- **Weak on legacy codebases** — agents misinterpret custom validation libraries and homegrown frameworks; requires supervision and rework
- **No support for third-party agent tools** against Antigravity quotas — ToS violation; accounts have been suspended for this
- **Stability** — as of early 2026: non-functional buttons, disappearing UI elements, broken syntax highlighting in some modes, significant battery drain from the embedded Chrome instance, input lag during agent processing
- **Compliance-heavy verticals** — artifacts improve auditability but governance frameworks for HIPAA/SOC2/etc. remain underdeveloped

---

## Architecture

**Foundation:** A heavily modified fork of Visual Studio Code. Settings, extensions, keybindings, and themes import from VS Code or Cursor. Some code references suggest possible derivation from Windsurf (another VS Code fork).

**Three integrated surfaces:**
1. **Editor** — VS Code-style text editing with agent sidebar
2. **Browser** — embedded Chromium instance with Agent Control mode for automated testing and visual verification
3. **Terminal** — shell access agents use to run builds, tests, and servers

**Agent Manager:** Separate window (not a panel) for parallel multi-agent orchestration across workspaces.

**Models:**
| Model | Role |
|---|---|
| Gemini 3.1 Pro | Primary default; 1M-token context window |
| Gemini 3 Flash | Faster/cheaper fallback |
| Claude Sonnet 4.6 | Switchable within sessions |
| Claude Opus 4.6 | Available; reportedly throttled in practice |
| GPT-OSS-120B | Open-source variant option |

**Deployment:** Fully cloud-inference. The IDE runs locally (macOS, Windows, Linux); all model calls go to Google's servers.

**System requirements:**
- Windows: 64-bit, Windows 10+
- macOS: Monterey 12+
- Linux: 64-bit, glibc 2.28+, glibcxx 3.4.25+

**Security note:** A prompt injection vulnerability in the `find_by_name` tool (bypassing Strict Mode via insufficient input sanitization) was patched in April 2026.

---

## Key Differentiators

**vs. Cursor:**
- Three-surface agent model vs. editor-only interface
- Parallel multi-agent orchestration (no equivalent in Cursor)
- Built-in browser automation native to the IDE
- Artifacts instead of raw diffs/logs
- Claimed benchmark wins (methodology not independently verified at scale)

**vs. GitHub Copilot:**
- Autonomous multi-step execution vs. autocomplete suggestions
- Copilot integrates into existing editors; Antigravity is a standalone IDE
- Agents run builds and tests; Copilot does not

**vs. Windsurf:**
- Ships with higher benchmark scores on SWE-bench and Terminal-Bench
- Multi-agent parallel orchestration not present in Windsurf
- Free tier during preview; Windsurf charges from the start

**Unique claims:**
- Only AI IDE with built-in browser automation (as of launch)
- Only AI IDE with native multi-agent parallel orchestration
- Free at point of use during preview (no other major IDE matched this)

---

## Ideal Use Cases

**Best fit:**
- Greenfield projects with well-defined requirements — agents excel at scaffolding and boilerplate
- CRUD endpoints, database initialization, routing setup
- UI/UX iteration — visual browser verification loop is uniquely strong here
- Background maintenance tasks — run a bug fix or refactor in one workspace while developing in another
- Prototyping and side projects where stability is not blocking
- Teams already in the Google ecosystem (Workspace, GCP, AI Studio)

**Poor fit:**
- Deadline-critical production work — too unstable as of early 2026
- Legacy codebases with custom patterns and non-standard conventions
- Compliance-sensitive industries (healthcare, finance) without custom governance overlay
- Teams requiring on-premises or private cloud inference
- Workflows requiring third-party agent tool integrations (ToS risk)

---

## Community & Ecosystem

**Adoption:** Rapid uptake during free preview; exact user count not published. Significant traction on Product Hunt and developer forums. The free model drove broad experimentation.

**Open source status:** Proprietary. Built on the open-source VS Code base but Antigravity itself is closed-source. Post-preview licensing terms not yet announced.

**Extension compatibility:** Full VS Code extension marketplace compatibility. Existing extensions import cleanly.

**MCP ecosystem:** 1,500+ MCP servers indexed at antigravity.codes. Community-maintained rules, workflows, and agent skill collections. Popular servers: GitHub, Slack, Google Drive, Jupyter, File System, SSH.

**Community tools:** Third-party open-source projects have emerged to bridge Antigravity auth to other agent CLIs (e.g., `opencode-antigravity-auth` on GitHub), though use of these against Antigravity rate limits violates ToS.

**AI Studio integration (2026):** Google merged its AI Studio prototyping playground with Antigravity, creating a pipeline: design prompts in the browser → hand off to Antigravity agents to build the full app.

**Forum:** Google AI Developers Forum hosts an active Antigravity subforum. Performance and quota complaints have been sustained since January 2026.

**Antigravity Codes:** Community hub (antigravity.codes) aggregating 1,500+ MCP servers, 500+ rules/workflows, and agent skill collections usable across Antigravity, Cursor, and Windsurf.

---

## Sources

- [Google Developers Blog — Build with Google Antigravity](https://developers.googleblog.com/build-with-google-antigravity-our-new-agentic-development-platform/)
- [Google Antigravity — Wikipedia](https://en.wikipedia.org/wiki/Google_Antigravity)
- [An Honest Review of Google Antigravity — DEV Community](https://dev.to/fabianfrankwerner/an-honest-review-of-google-antigravity-4g6f)
- [Users protest as Google Antigravity price floats upward — The Register](https://www.theregister.com/2026/03/12/users_protest_as_google_antigravity/)
- [Google Antigravity: The Agentic IDE Changing Development Work — index.dev](https://www.index.dev/blog/google-antigravity-agentic-ide)
- [Google Antigravity falls to Earth under compute burden — The Register](https://www.theregister.com/2026/02/23/google_antigravity_compute_burden/)
- [Google Patches Antigravity IDE Flaw — The Hacker News](https://thehackernews.com/2026/04/google-patches-antigravity-ide-flaw.html)
- [Antigravity Codes — MCP Servers & Workflows](https://antigravity.codes/)
- [Google Antigravity Restriction — AI CERTs News](https://www.aicerts.ai/news/google-antigravity-restriction-what-developers-need-to-know/)
- [Google AntiGravity Pricing 2026 — Vibe Coding App](https://vibecoding.app/blog/google-antigravity-pricing-2026)
