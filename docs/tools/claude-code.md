# Claude Code

## What It Is

**Claude Code** is an agentic, terminal-native coding assistant made by **Anthropic**. It is a command-line interface (CLI) tool — not primarily an IDE plugin — that runs on your local machine (or Anthropic-managed VMs) and operates on your local files and shell environment through natural language commands.

- **Product category:** Agentic coding assistant / AI coding agent
- **Maker:** Anthropic PBC
- **Released:** Research preview February 2025; General Availability (GA) May 2025 (alongside Claude 4 models)
- **Source availability:** TypeScript source made public March 31, 2026 on GitHub at [anthropics/claude-code](https://github.com/anthropics/claude-code); proprietary license (Anthropic Commercial Terms of Service, not OSI open source)

### Pricing Model

| Plan | Price | Claude Code Access | Token Window (5-hr rolling) |
|---|---|---|---|
| Free | $0 | No | — |
| Pro | $20/month | Yes | ~44,000 tokens |
| Max 5x | $100/month | Yes | ~88,000 tokens |
| Max 20x | $200/month | Yes | ~220,000 tokens |
| Team Standard | $20/seat/month (min 5) | Premium seats only | 200K context |
| Team Premium | $100/seat/month | Yes | 5x vs Standard |
| Enterprise | Custom | Yes | 500K context window |

**API pay-as-you-go (Sonnet 4.6):** $3/MTok input (≤200K), $15/MTok output (≤200K); 50% batch discount. Prompt cache reads: $0.30/MTok.

Notable: In April 2026, Anthropic briefly removed Claude Code from the $20 Pro plan, then reversed within 24 hours. Pro access remains as of May 2026.

---

## What It Does

### Core Capabilities

Claude Code operates as an **agentic loop**: gather context → take action → verify results → repeat. It chains dozens of tool calls autonomously, course-correcting based on output.

**Built-in tool categories:**

| Category | Capabilities |
|---|---|
| File operations | Read, edit, create, rename, reorganize files |
| Search | Glob patterns, regex content search, codebase exploration |
| Execution | Run shell commands, tests, servers, git operations |
| Web | Search the web, fetch documentation, look up error messages |
| Code intelligence | Type errors, warnings, jump-to-definition, find references (via plugins) |
| Orchestration | Spawn subagents, checkpoint/rewind, fork sessions |

### Agentic Features

- **Autonomous multi-step execution:** Diagnoses bugs, writes failing tests, edits code, re-runs tests, commits — all without hand-holding
- **Multi-file context:** Sees and edits across your entire project, not just the current file
- **Session persistence:** Conversations stored as append-only JSONL in `~/.claude/projects/`; sessions can be resumed (`--continue`), forked (`/branch`), or rewound (Esc×2 checkpoints)
- **Parallel sessions:** Git worktrees enable multiple simultaneous Claude Code instances on isolated branches
- **Subagents:** Delegate subtasks to isolated agent contexts; only summaries return to parent, preventing context bloat
- **Compaction pipeline:** Five-layer automatic context management (budget reduction → snip → microcompact → context collapse → auto-compact model summary)
- **Memory:** `CLAUDE.md` (user-written, persistent) + auto memory (model-generated patterns, per worktree)
- **Hooks:** 27 lifecycle event types (PreToolUse, PostToolUse, PermissionRequest, ConfigChange, etc.) for policy enforcement and automation
- **Plan mode:** Read-only exploration with user-approved plan before any execution

### Supported Languages and Frameworks

Claude Code reads and writes code in any language the underlying Claude models understand — which includes all major languages (Python, TypeScript/JavaScript, Go, Rust, Java, C/C++, Ruby, PHP, Swift, Kotlin, etc.) and frameworks. No explicit per-language configuration required.

### Interfaces

Claude Code runs through multiple surfaces (same underlying agentic loop everywhere):

- Terminal (primary)
- Desktop app
- VS Code and JetBrains IDE extensions
- claude.ai/code (browser)
- Remote Control (browser UI controlling local execution)
- Slack integration
- GitHub Actions / CI-CD pipelines
- iOS app (added October 2025)

---

## What It Doesn't Do

- **No inline autocomplete:** Does not provide real-time keystroke-level completions like GitHub Copilot or Cursor's tab-complete. Operates on discrete tasks, not continuous typing assistance.
- **No visual diff/UI:** No graphical diff viewer; all interaction is terminal/text-based unless using IDE extensions.
- **No model flexibility:** Locked to Anthropic's Claude models. Cannot swap in GPT-5, Gemini, or local models mid-session (unlike Cursor, which supports multi-provider model switching).
- **No free tier:** Requires a paid subscription ($20+/month) or API key; no free access to Claude Code functionality.
- **Context window limits:** Large files or long sessions can exhaust the context window; compaction may lose early instructions. Single tool outputs too large to summarize cause a "thrashing" error.
- **No persistent remote state:** Each new session starts with a fresh context window; cross-session memory is limited to CLAUDE.md and auto memory.
- **Slower for simple completions:** 45–90 seconds for large file refactoring vs. faster alternatives for routine tasks. Not optimized for quick one-liner suggestions.
- **No audit of MCP servers:** Anthropic does not vet third-party MCP servers; users assume trust risk.
- **Irreversible external actions:** Checkpoints cover file changes only; database writes, API calls, and deployments cannot be rolled back through Claude Code.
- **Permission restoration on resume:** Session-scoped permission decisions are not restored on session resume by design — intentional but can surprise users.

---

## Architecture

### Execution Model

Claude Code is described in research as a **simple while-loop reactive agent**: ~1.6% AI decision logic, ~98.4% deterministic operational harness. All entry points (CLI, SDK, IDE) converge on one `queryLoop()` function.

**Three execution environments:**

| Environment | Where Code Runs | Use Case |
|---|---|---|
| Local | Your machine | Default; full access to local files and tools |
| Cloud | Anthropic-managed VMs | Offload tasks; work on remote repos |
| Remote Control | Your machine, via browser | Web UI with local execution |

### Models

| Model | Used For | Plan |
|---|---|---|
| Claude Opus 4.7 | Complex architecture, hard reasoning | Max, Team Premium |
| Claude Sonnet 4.6 | Most coding tasks | Pro, Team Standard, Enterprise, API |

Switch models with `/model` during a session or `claude --model <name>` at startup.

### Permission System

Seven graduated permission modes:

1. **plan** — read-only; user approves plan before execution
2. **default** — approves most operations interactively
3. **acceptEdits** — auto-approves file edits; asks for commands
4. **auto** — ML classifier evaluates actions (Team/Enterprise; research preview)
5. **dontAsk** — no prompts; deny rules still enforce
6. **bypassPermissions** — minimal prompting; for isolated VMs/test environments
7. **bubble** — internal subagent escalation to parent terminal

Deny rules always override allow rules, even more-specific allows. Users approve ~93% of prompts in practice, which informed the ML-classifier auto mode design.

### Safety Layers (7 independent)

1. Tool pre-filtering (deny before model sees tools)
2. Deny-first rule evaluation
3. Permission mode constraints
4. ML-based auto-mode classifier
5. Shell sandboxing (macOS: Seatbelt; Linux/WSL2: bubblewrap)
6. Permission non-restoration on resume
7. Hook-based interception

### Context Management

Context window holds: conversation history, file contents, command outputs, CLAUDE.md, auto memory, loaded skills, MCP tool names, system instructions. Five-layer compaction pipeline runs sequentially before costlier operations engage.

### Storage

Sessions stored as append-only JSONL under `~/.claude/projects/`. File snapshots (checkpoints) stored separately per session. Design prioritizes auditability over query power.

---

## Key Differentiators

1. **Best-in-class benchmark performance:** Claude Opus 4.7 scores 87.6% on SWE-bench Verified (up from 80.8% for Opus 4.6); Claude Sonnet 4.6 at 79.6%. As of May 2026, top of verified leaderboard.

2. **Autonomous multi-file agent:** Designed for delegated, end-to-end task completion across large codebases — not file-scoped inline assistance. Handles entire feature builds, large-scale refactors, and cross-module debugging independently.

3. **Deep shell integration:** Native terminal tool; can run any command the developer can, use any CLI tool, interact with git, manage builds, and control system state — not sandboxed to a subset of shell.

4. **Principled safety architecture:** Layered permission system, OS-level sandboxing, ML classifier, and hook-based governance combine to let the agent act autonomously while preserving human control at escalation points.

5. **Extensibility depth:** Four orthogonal extension mechanisms (MCP, plugins, skills, hooks) each target a different layer of the loop with different context costs. Not a single plugin API.

6. **MCP ecosystem leadership:** Anthropic created the Model Context Protocol (MCP); Claude Code is the reference implementation. Broad ecosystem of MCP servers (GitHub, Postgres, Slack, Supabase, Filesystem, Memory, etc.).

7. **Subagent isolation:** Delegated tasks run in fully isolated context windows; only text summaries return to parent. Prevents context pollution on long-running compound tasks.

8. **Conversational iteration:** No need for perfect prompts. Task can be refined mid-execution; Claude adjusts without restarting.

vs. Cursor: Claude Code wins on autonomous batch operations and multi-file refactoring; Cursor wins on real-time inline completions, visual diff UI, and multi-model flexibility.

vs. GitHub Copilot: Claude Code wins on complex debugging, refactoring, and multi-file comprehension (61% prefer Claude Code for these tasks per surveys); Copilot wins on routine code completion speed and enterprise seat adoption at scale.

vs. OpenAI Codex CLI: Claude Code achieves 67% win rate in blind code quality evaluations; Codex CLI runs in network-disabled cloud containers for strong isolation.

---

## Ideal Use Cases

Claude Code is the right tool when:

- **Large-scale refactors:** Renaming across many files, updating API interfaces, migrating frameworks — tasks requiring consistent changes across dozens of files.
- **Autonomous feature builds:** "Implement OAuth2 login" end-to-end — research, plan, write tests, implement, verify, commit.
- **Complex debugging:** Multi-file, multi-layer bugs where tracing requires reading many files and running many commands iteratively.
- **Codebase exploration:** Understanding an unfamiliar repo — architecture, patterns, dependencies — via natural language questions.
- **CI/CD and automation:** Headless operation in GitHub Actions, scripted batch tasks, automated PR generation.
- **Documentation generation:** Code review and documentation for entire codebases with full context.
- **Teams that want terminal-native flow:** Developers who live in the terminal and want an agent that fits that workflow without switching to a GUI.

Less ideal when:
- You primarily want fast, keystroke-level autocomplete while actively typing
- You need multi-provider model flexibility per task
- Budget is constrained (heavy use runs $100–200+/month)
- Large enterprise with existing Copilot rollout (enterprise seat switching cost is high)

---

## Community & Ecosystem

### Adoption (as of early 2026)

- **46%** of developers rated Claude Code their most-loved coding tool (Pragmatic Engineer Survey, 15,000 developers, Feb 2026); Cursor at 19%, Copilot at 9%
- **71%** of developers using AI agents specifically use Claude Code
- **75%** startup adoption rate (highest among small companies)
- **~135,000** GitHub commits authored by Claude Code per day (~4% of all public GitHub commits)
- **22,000+** GitHub stars on the anthropics/claude-code repo
- **$2.5B** annualized revenue run rate (early 2026); reached $1B ARR in 6 months (fastest in AI coding market history)
- Represents ~13% of Anthropic's $19B ARR

### Open Source Status

- Source code (TypeScript) made public March 31, 2026
- License: Anthropic Commercial Terms of Service — source-available, not OSI open source
- Forkable and auditable; commercial use requires Anthropic agreement
- The underlying Claude models are closed/proprietary

### Extensibility Mechanisms

| Mechanism | Purpose | Context Cost |
|---|---|---|
| **MCP servers** | External tool, data, API integration via Model Context Protocol | Per-tool definitions; deferred/on-demand |
| **Plugins** | Package and distribute bundles of MCP servers, skills, hooks | Varies |
| **Skills** | Inject domain-specific instructions into the agent loop | Loaded on-demand; low until invoked |
| **Hooks** | Intercept 27 lifecycle events for policy, auditing, automation | Minimal |

**MCP transports:** stdio (local subprocess), HTTP with OAuth 2.1 (remote; preferred), SSE (deprecated).

**Built-in subagents:** Explore, Plan, and a general-purpose agent with configurable tool allowlists and permission modes.

**Settings scoping:** Organization policy → project `.claude/settings.json` → user `~/.claude/settings.json`. Deny rules propagate and cannot be overridden by inner scopes.

### Notable MCP Server Ecosystem

GitHub, Postgres, Slack, Supabase, Git, Filesystem, Fetch, Memory — plus community-contributed servers tracked in the official MCP registry.

### Claude for Open Source

Anthropic runs a program ([claude.com/contact-sales/claude-for-oss](https://claude.com/contact-sales/claude-for-oss)) offering Claude access to qualifying open-source projects.
