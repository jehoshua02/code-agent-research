# Hermes Agent

**Source:** [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) · MIT License  
**Docs:** https://hermes-agent.nousresearch.com/docs/  
**As of:** May 2026

---

## 1. What It Is

Hermes Agent is an open-source, self-improving autonomous AI agent built by **Nous Research** (the team behind the Hermes, Nomos, and Psyche model families). It is not an IDE copilot or chatbot wrapper — it is a long-lived agent runtime that persists across sessions, accumulates skills from experience, and runs on infrastructure you control.

- **Product category:** Autonomous AI agent framework / personal agent runtime
- **Made by:** Nous Research
- **Released:** February 25, 2026
- **License:** MIT (fully open-source, free)
- **Pricing:** Free. Self-hosted. Bring your own API keys. No managed service or usage limits.
- **Stars:** ~131,000 GitHub stars as of v0.12.0 (April 30, 2026) — fastest-growing agent framework of 2026

---

## 2. What It Does

### Core Concept

The central premise is a **closed learning loop**: after completing complex tasks (typically 5+ tool calls), Hermes autonomously writes structured skill documents capturing procedures, pitfalls, and verification steps. Future runs load matching skills as context. Memory compounds across sessions.

### Memory System

Three-layer memory architecture:

| Layer | Mechanism |
|---|---|
| Session recall | SQLite with FTS5 full-text search + LLM summarization |
| User modeling | Honcho dialectic user modeling (builds profile over time) |
| Skill context | Skill files injected into system prompt at agent init |

Memory persists in `MEMORY.md` and `USER.md` files; sessions stored in SQLite with lineage tracking across context compressions.

### Built-in Tools

61 registered tools across 52 toolsets, including:
- Web search, extraction, browsing, vision
- Image generation, text-to-speech
- File operations, terminal commands
- Subagent spawning (parallel workstreams)
- MCP (Model Context Protocol) integration
- Scheduled automations via built-in cron

### Skills System

Skills are portable files following the [agentskills.io](https://agentskills.io) open standard (SKILL.md format, adopted by 26+ platforms including Claude, Codex, Gemini CLI, Cursor, GitHub Copilot). v0.10.0 ships with **118 bundled, human-reviewed skills**. Users accumulate custom skills over time. Community skills via the ecosystem (no centralized marketplace yet).

### Multi-Platform Messaging

15+ messaging platform adapters via a unified gateway process:
- Telegram, Discord, Slack, WhatsApp, Signal, Matrix, Email, CLI
- Slash command dispatch, user authorization, background maintenance hooks

### Automation

- Built-in cron scheduler (natural language scheduling)
- Spawn isolated subagents for parallel workstreams
- Batch processing and trajectory export for RL training (Atropos integration)
- Programmatic tool calling via `execute_code` to collapse multi-step pipelines

### Coding-Specific Capabilities

- Terminal-native: reads errors, analyzes code, suggests fixes in real time
- Debug, run scripts, modify files from the terminal without switching tools
- ACP (Agent Communication Protocol) entry point for IDE integration
- Trajectory export for model training pipelines
- Code review skill bundled (`skills/software-development/requesting-code-review/`)

---

## 3. What It Doesn't Do

- **No native Windows support.** Requires WSL2.
- **No managed/cloud service.** No hosted version; you provision and operate your own infrastructure.
- **No semantic memory search.** FTS5 keyword indexing only — if a past solution used different terminology, it won't surface. Embedding-based retrieval is absent.
- **No skill quality enforcement.** Auto-generated skills are not reviewed; users accumulate mediocre or incorrect skills over time.
- **High meta-cognition cost.** Skill extraction, memory nudges, and user modeling each require LLM calls. On expensive frontier models, overhead cost can exceed task cost.
- **No compliance features.** No signed skill provenance, no audit trails, no approval workflows, no GDPR-compliant data erasure for user profiling.
- **Weaker at pure coding benchmarks than specialized tools.** For focused software engineering tasks (writing, debugging, refactoring), Cursor, Windsurf, and Claude Code outperform Hermes on SWE-bench class tasks.
- **Android/Termux limitations.** Full `.[all]` extra incompatible; uses curated `.[termux]` subset with manual install path.

---

## 4. Architecture

### Runtime

Python 88.2%, TypeScript 8.4%. Core orchestration engine: `AIAgent` in `run_agent.py` — a synchronous loop serving all entry points (CLI, gateway, ACP, batch).

### Entry Points

| Entry point | Description |
|---|---|
| CLI | Interactive TUI with multiline editing, slash-command autocomplete, streaming tool output |
| Gateway | Long-running process with 20 platform adapters (messaging platforms) |
| ACP | IDE integration layer |
| Batch | Trajectory generation for research/training |

All entry points channel through the same `AIAgent` class; platform-specific logic is isolated at entry points.

### Terminal Backends (7)

`local` · `Docker` · `SSH` · `Daytona` · `Modal` · `Singularity` · `Vercel Sandbox`

### Provider Resolution

18+ model providers with OAuth flows and credential pooling. Switch with `hermes model` — no code changes:
- Nous Portal, OpenRouter (200+ models), OpenAI, NVIDIA NIM, Xiaomi MiMo, z.ai/GLM, Kimi/Moonshot, MiniMax, Hugging Face, custom OpenAI-compatible endpoints

Not locked to any model family (despite the name; the Hermes model family from Nous is one option, not a requirement).

### Data Layer

- SQLite + FTS5 for session storage with atomic writes
- Pluggable memory providers (`plugins/memory/`); one active at a time
- Skills discovered from: `~/.hermes/plugins/`, `.hermes/plugins/`, pip entry points

### Prompt System

`prompt_builder.py` assembles: SOUL.md (personality) + memory artifacts + skills + context files + model-specific instructions. `prompt_caching.py` applies Anthropic-style cache breakpoints. `context_compressor.py` summarizes earlier turns when context exceeds thresholds. System prompt is stable mid-conversation (no surprise drift).

### Deployment

Self-hosted on Linux, macOS, WSL2, or Android/Termux. One-line installer:
```sh
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
```
Runs cheaply on serverless (Modal, Daytona) when idle.

---

## 5. Key Differentiators

| Feature | Hermes Agent | Claude Code | OpenClaw |
|---|---|---|---|
| Persistent memory | Yes — FTS5 + LLM summarization | Auto-memory (CLAUDE.md notes) | File-based (MEMORY.md, static) |
| Self-improving skills | Yes — autonomous post-task creation | No | No (ClawHub marketplace, manual) |
| Model flexibility | 200+ models, 18+ providers | Anthropic only | Multi-provider |
| Runs between sessions | Yes — long-lived daemon | No — ephemeral sessions | Partial |
| Messaging integrations | 15+ platforms | None | Telegram, Discord, Slack, WhatsApp, Signal |
| IDE integration | ACP layer | VS Code, JetBrains native | Limited |
| Open source | MIT | No | No |
| Coding benchmark strength | Moderate | High (SWE-bench ~70–75%) | Moderate |

**The defining differentiator:** The autonomous learning loop. No other agent framework auto-creates, auto-improves, and auto-retrieves procedural skills from its own execution history. Combined with vendor-agnostic model support and true server-resident operation, Hermes occupies a category distinct from session-based coding assistants.

---

## 6. Ideal Use Cases

- **Developers who context-switch frequently** — Hermes remembers project quirks, past solutions, and individual working style without re-briefing each session.
- **Automation workflows** — scheduled reports, nightly backups, multi-step pipelines across messaging platforms.
- **Research & ML teams** — batch trajectory generation, RL training integration (Atropos), multi-agent orchestration.
- **Self-hosted / privacy-conscious setups** — no data leaves your infrastructure; full control over credentials and storage.
- **Multi-channel teams** — one agent reachable via Slack, Telegram, CLI simultaneously with consistent memory.
- **Long-running personal assistants** — the agent compounds capability over weeks/months; best ROI on tasks done repeatedly.

**Not ideal for:** teams needing compliance/audit trails, pure coding benchmark performance, Windows-native workflows, or zero-ops managed service.

---

## 7. Community & Ecosystem

### Adoption

- 131,000 GitHub stars (v0.12.0, April 30, 2026) — reached 110k in ~10 weeks from launch
- 19,900 forks, 142+ contributors
- Fastest-growing agent framework of 2026 by star velocity

### Open Source

MIT license. 88 public GitHub repositories in the NousResearch org. Community forks and companion projects active.

### Companion Projects

| Project | Description |
|---|---|
| [hermes-webui](https://github.com/nesquena/hermes-webui) | Lightweight dark-themed web UI with CLI parity |
| [hermes-workspace](https://github.com/outsourc-e/hermes-workspace) | Native web workspace: chat, terminal, memory, skills, inspector |
| [awesome-hermes-agent](https://github.com/0xNyk/awesome-hermes-agent) | Curated list of skills, tools, integrations |
| [hermes-optimization-guide](https://github.com/OnlyTerp/hermes-optimization-guide) | Setup, migration, LightRAG, Telegram, skill creation guide |
| [hermes-agent-docs](https://github.com/mudrii/hermes-agent-docs) | Community-maintained comprehensive docs (v0.2.0+) |
| SwarmClaw | Third-party multi-agent orchestration bridging Hermes, OpenClaw, Claude Code |

### Skills Ecosystem

Skills use the [agentskills.io](https://agentskills.io) open standard (SKILL.md files). The standard is adopted by 26+ platforms. 118 bundled skills ship with Hermes. No centralized skill registry has emerged yet — community distribution is informal (GitHub, awesome-hermes-agent list).

### Model Ecosystem

Built by the team behind the [Hermes model family](https://huggingface.co/NousResearch) (fine-tuned open-weight models optimized for tool use and instruction following). These models are recommended but optional — any OpenAI-compatible endpoint works.

### Security

Zero agent-specific CVEs to date (compared to competitor OpenClaw which disclosed 9 CVEs in 4 days in March 2026, including CVSS 9.9). Known risk area: credential exposure on host systems when running with broad filesystem access.

---

## Sources

- [NousResearch/hermes-agent (GitHub)](https://github.com/NousResearch/hermes-agent)
- [Hermes Agent Official Docs](https://hermes-agent.nousresearch.com/docs/)
- [Hermes Agent Architecture Docs](https://hermes-agent.nousresearch.com/docs/developer-guide/architecture)
- [Hermes Agent Homepage (Nous Research)](https://hermes-agent.nousresearch.com/)
- [Hermes Agent Homepage (hermesagent.agency)](https://hermesagent.agency/)
- [Hermes Agent on OpenRouter](https://openrouter.ai/apps/hermes-agent)
- [Hermes Agent Review — Krzysztof Słomka (Medium)](https://kisztof.medium.com/hermes-agent-review-nous-researchs-self-improving-ai-agent-e72bc244435a)
- [Hermes Agent Review — Kristopher Dunham (Medium)](https://medium.com/@creativeaininja/hermes-agent-the-open-source-ai-agent-that-actually-remembers-what-it-learned-yesterday-278441cd1870)
- [I Switched from OpenClaw to Hermes Agent (Medium)](https://medium.com/@sathishkraju/i-switched-from-openclaw-to-hermes-agent-heres-what-nobody-told-me-5f33a746b6ca)
- [Hermes Agent vs Claude Code vs OpenClaw (utilo.io)](https://utilo.io/en/home/blog/hermes-vs-claude-code-vs-openclaw-2026)
- [Hermes Agent vs OpenClaw (kanaries.net)](https://docs.kanaries.net/articles/hermes-agent-vs-openclaw)
- [Hermes Agent: A Self-Improving AI Agent That Runs Anywhere (dev.to)](https://dev.to/arshtechpro/hermes-agent-a-self-improving-ai-agent-that-runs-anywhere-2b7d)
- [What Is Hermes Agent? (MindStudio)](https://www.mindstudio.ai/blog/what-is-hermes-agent-openclaw-alternative)
- [agentskills.io](https://agentskills.io/home)
- [awesome-hermes-agent (GitHub)](https://github.com/0xNyk/awesome-hermes-agent)
