# SWE-1 Family (Windsurf / Cognition AI)

## What It Is

The SWE-1 family is a series of proprietary, closed-weight AI models developed by Windsurf (formerly Codeium, now operating as Cognition AI). The family was first announced on May 15, 2025, as part of Windsurf Wave 9, marking Windsurf's entry into first-party model development after previously relying on third-party models from Anthropic, OpenAI, and Google.

Unlike general-purpose LLMs fine-tuned for coding, SWE-1 models are designed from the ground up for the full software engineering lifecycle: planning, implementation, debugging, code review, and multi-step agentic workflows. The core design philosophy is "flow awareness" — a training and inference framework that enables models to reason over long-running, multi-surface engineering tasks with incomplete or evolving state, maintaining awareness of terminals, browsers, and prior interaction history rather than treating each prompt as an isolated request.

All models are trained on real user interactions from the Windsurf editor using end-to-end reinforcement learning with a custom Cascade agent harness. The harness provides three grading mechanisms: classical unit tests, rubric-based scoring, and agentic browser-based evaluation. A "reward hardening" process prevents models from gaming reward signals.

The models are proprietary and closed — no weights are publicly released and they are not available on Hugging Face or via Ollama/vLLM.

## Variants

| Model | Role | Status |
|---|---|---|
| SWE-1 | Flagship agentic model, advanced tool-call reasoning | Released May 2025; superseded by SWE-1.5 |
| SWE-1-lite | Mid-tier variant, replaced Cascade Base, free for all users | Released May 2025 |
| SWE-1-mini | Compact high-speed model for real-time tab completions | Released May 2025 |
| SWE-1.5 | Second-generation frontier agentic model, speed-optimized | Released October 29, 2025 |
| SWE-1.6 | Third-generation frontier model, improved intelligence and model UX | Released April 2026 (preview March 2026) |

**SWE-1** was competitive with Claude 3.5 Sonnet on tool-use and multi-hop reasoning tasks at lower cost. It was the first model in the family capable of long-horizon agentic sessions.

**SWE-1-lite** replaced the prior Cascade Base model with improved quality. It was made freely available to all Windsurf users without credit limits.

**SWE-1-mini** powers passive suggestions in Windsurf Tab (inline completion), optimized for sub-second latency rather than reasoning depth.

**SWE-1.5** is a frontier-scale model with hundreds of billions of parameters, built on a strong open-source foundation model and fine-tuned via RL on real coding workflows. It is co-optimized with the Cascade agent harness and Cerebras inference infrastructure to achieve 950 tokens/second. It uses a Mixture-of-Experts (MoE) architecture. It ships with Codemaps, a codebase navigation tool, and Fast Context retrieval (approximately 10x faster than standard agentic search). SWE-1.5 Free offers the same intelligence at standard (200 tok/s) throughput for free users via a Fireworks partnership.

**SWE-1.6** is post-trained on the same pre-trained base as SWE-1.5 but with significant additional reinforcement learning compute (two orders of magnitude more than SWE-1.5 training) and a length penalty to discourage unnecessarily long reasoning trajectories. It introduces parallel tool execution, reduced looping behavior, greater reliance on built-in tools over shell commands, and structured planning (todo lists for long-horizon tasks). SWE-1.6 Fast (950 tok/s via Cerebras) is available to paying users; SWE-1.6 Free (200 tok/s via Fireworks) is available to all users.

An auxiliary model, **swe-grep**, powers the Fast Context retrieval feature for codebase search.

## Pricing

SWE-1 models do not carry traditional per-token input/output pricing when used inside Windsurf. They consume zero credits within Windsurf subscription plans — they do not count against the quota that third-party models (Claude, GPT-4, Gemini) use. This is a key differentiator: users on free and pro tiers can use SWE-1-family models without burning their credit allocation.

Windsurf subscription plans (as of mid-2026):

| Plan | Price | Notes |
|---|---|---|
| Free | $0/month | Unlimited SWE-1-family usage; 25 credits/month for third-party models |
| Pro | $15–$20/month | 500 credits/month for third-party models; SWE-1 family unlimited |
| Teams | $30–$40/user/month | Centralized billing, admin dashboard |
| Enterprise | Custom | SSO, RBAC, hybrid deployment, priority support |

For API/overage access beyond subscription limits, extra usage is priced at approximately $0.30/M input tokens and $1.50/M output tokens for SWE-1.6 (enterprise rate). Third-party overage is $0.50/M input and $2.00/M output.

SWE-1.6 was offered free for all users for the first three months following its release.

## Context Window

Context window sizes are not officially disclosed by Windsurf for any model in the SWE-1 family. Third-party reporting based on user testing and partial documentation suggests SWE-1.5 operates with a 128K token context window. No figures have been confirmed for SWE-1, SWE-1-lite, SWE-1-mini, or SWE-1.6.

The Cascade agent harness uses a context window indicator within the editor to show current context usage. The models support full-file awareness and multi-file context within Windsurf's agentic sessions.

## Benchmarks

Windsurf uses **SWE-Bench Pro** (Scale AI, 731 diverse agentic coding tasks across multiple languages and codebases) as the primary benchmark rather than the more commonly cited SWE-Bench Verified. Windsurf stopped reporting standard SWE-Bench numbers in 2024, preferring SWE-Bench Pro as more reflective of real-world engineering difficulty.

### SWE-Bench Pro (731 tasks)

| Model | Score | Notes |
|---|---|---|
| Claude Sonnet 4.5 | 43.60% | General-purpose frontier model |
| **SWE-1.5** | **40.08%** | 14x faster than Sonnet 4.5 at time of release |
| GPT-5 High | 36.30% | General-purpose frontier model |

SWE-1.6 improved on SWE-1.5's SWE-Bench Pro score by more than 10 percentage points (relative), achieved while post-training on the same pre-trained base. The absolute SWE-1.6 score is not publicly disclosed.

### Qualitative Comparisons

- **SWE-1** (May 2025): Competitive with Claude 3.5 Sonnet on tool-call reasoning, multi-hop reasoning, and planning. Described as superior to open-weight and mid-sized alternatives for software engineering tasks. Did not match the absolute latest frontier models.
- **SWE-1.5** (October 2025): Near-frontier performance at 13x the speed of Claude Sonnet 4.5 and 6x the speed of Claude Haiku 4.5. Tasks completing in under 5 seconds vs. 20–30 seconds for traditional frontier models.
- **SWE-1.6** (April 2026): Comparable benchmark performance to SWE-1.6 Preview (>10% gain over SWE-1.5), with additional gains in agent behavior quality (fewer wasted turns, more parallel tool use).

Windsurf's custom Cascade agent harness provides a significant benchmark advantage. Independent analysis found the harness design alone contributed approximately 11 percentage points of advantage over a neutral harness (e.g., Claude Code), meaning raw model capability numbers are partially harness-dependent.

## Hardware Requirements

The SWE-1 family is proprietary cloud-only inference. No weights are released. Self-hosting is not possible.

Windsurf operates its own inference infrastructure:
- SWE-1.5 and SWE-1.6 run on Cerebras WSE-3 hardware (900,000 AI cores) for high-speed paid-tier inference (950 tok/s).
- Free-tier inference runs at 200 tok/s via a Fireworks AI partnership.
- Training for SWE-1.5 used thousands of GB200 NVL72 chips. SWE-1.6 training used two orders of magnitude more compute than SWE-1.5.

There are no VRAM requirements, quantization options, or Ollama/vLLM compatibility considerations because the models cannot be run locally.

## Supported Tools

The SWE-1 family is exclusively available through Windsurf's own ecosystem. It is not integrated into any third-party tools.

**Available in:**
- Windsurf IDE (VS Code-based editor) — primary access point
- Windsurf's Cascade agentic assistant (multi-file editing, terminal commands, browser integration, multi-step planning)
- Windsurf Tab (inline completions powered by SWE-1-mini)
- Devin for Terminal (SWE-1.6 listed as available frontier model for background terminal agents)

**Not available in:**
- Cursor
- GitHub Copilot
- Claude Code
- Any OpenAI-compatible API endpoint for external use
- Any self-hosted or local inference setup

Windsurf is built on VS Code, so existing VS Code extensions and keybindings carry over, but the SWE-1 models themselves are Windsurf-exclusive.

## Strengths

**Speed.** SWE-1.5 and SWE-1.6 run at 950 tok/s on Cerebras hardware — 13–14x faster than Claude Sonnet at the time of release. This makes agentic tasks that previously took 20–30 seconds complete in under 5 seconds, dramatically improving iteration speed in long coding sessions.

**Cost efficiency.** SWE-1 family models are free (zero credits) within Windsurf subscriptions, unlike frontier models from Anthropic, OpenAI, and Google which consume credits. For teams running heavy agentic workloads, this dramatically reduces effective per-session cost.

**Software engineering specialization.** Unlike general-purpose models adapted for coding, SWE-1 models are trained exclusively on software engineering tasks with real-world Windsurf editor data. Flow awareness enables reasoning over partially completed sessions, mid-task state changes, and multi-surface context (terminal, browser, editor simultaneously).

**Agent harness co-optimization.** The model, inference stack, and agent harness are trained and tuned together as a unified system rather than treating the model as a drop-in replacement. This produces more reliable tool-calling, fewer error loops, and better multi-turn coherence compared to general models used in coding IDEs.

**Codemaps and Fast Context.** SWE-1.5+ ships with codebase navigation tooling approximately 10x faster than standard agentic search, practically useful for large codebases.

**Improving model UX (SWE-1.6).** SWE-1.6 reduced "overthinking," unnecessary unit test execution, repeated reasoning loops, and sequential tool calls in favor of parallel execution. This reduces turn count and user intervention for common coding tasks.

## Weaknesses

**No public weights or self-hosting.** The models are fully proprietary and cloud-only. Teams with data residency requirements, security constraints, or air-gapped environments cannot use them.

**Undisclosed context window.** Windsurf does not officially publish context window sizes, making it difficult to plan for large codebase analysis or predict truncation behavior. The 128K figure for SWE-1.5 is from third-party reporting only.

**Windsurf lock-in.** SWE-1 models are only accessible through Windsurf's IDE and agent system. There is no API for external integration. Users who prefer Cursor, Claude Code, Neovim, or other editors cannot access these models.

**Raw accuracy below frontier.** On SWE-Bench Pro, SWE-1.5 scores 40.08% versus Claude Sonnet 4.5's 43.60% — a 3.5-point gap. For tasks where accuracy matters more than speed (complex refactors, novel architecture decisions), frontier general-purpose models may produce better results.

**Limited to Windsurf ecosystem.** No third-party integrations (CI/CD pipelines, custom tooling, external orchestration) can call the models directly. All access is mediated through Windsurf's Cascade harness.

**Benchmark harness dependency.** Windsurf's SWE-Bench Pro scores are achieved using their own Cascade harness, which provides a measurable advantage over neutral harnesses. Reported scores are not directly comparable to scores from other providers using different agent frameworks.

**Early-stage limitations (SWE-1).** The original SWE-1 showed inconsistent performance on complex or unfamiliar existing codebases, tool-calling failures leading to error loops, and reduced robustness compared to mature frontier models. Some of these were addressed in SWE-1.5 and SWE-1.6.

## Sources

- [Windsurf Launches SWE-1: A Frontier AI Model Family Built for the Full Software Engineering Lifecycle (BusinessWire, May 15, 2025)](https://www.businesswire.com/news/home/20250515138505/en/Windsurf-Launches-SWE-1-A-Frontier-AI-Model-Family-Built-for-the-Full-Software-Engineering-Lifecycle)
- [SWE-1: Our First Frontier Models (Windsurf Blog)](https://windsurf.com/blog/windsurf-wave-9-swe-1)
- [Introducing SWE-1.5: Our Fast Agent Model (Windsurf / Cognition Blog)](https://windsurf.com/blog/swe-1-5)
- [Cognition: Introducing SWE-1.5: Our Fast Agent Model](https://cognition.ai/blog/swe-1-5)
- [Cognition: An Early Preview of SWE-1.6 and Research Update](https://cognition.ai/blog/swe-1-6-preview)
- [Cognition: Introducing SWE 1.6: Improving Model UX](https://cognition.ai/blog/swe-1-6)
- [AI Models — Windsurf Docs](https://docs.windsurf.com/windsurf/models)
- [Windsurf Next Changelogs](https://windsurf.com/changelog/windsurf-next)
- [Windsurf Launches SWE-1 Family of Models for Software Engineering (InfoQ)](https://www.infoq.com/news/2025/05/windsurf-swe-models/)
- [Windsurf Wave 13 introduces the new SWE-1.5 model and Git worktrees (Neowin)](https://www.neowin.net/news/windsurf-wave-13-introduces-the-new-swe-15-model-and-git-worktrees/)
- [Is SWE-1.5 the Fastest AI Agent? Let's find out (APIdog)](https://apidog.com/blog/swe-1-5/)
- [Windsurf SWE-1.5: AI Coding Model Guide for Agencies (Digital Applied)](https://www.digitalapplied.com/blog/windsurf-swe-1-5-fast-ai-coding-guide)
- [New Windsurf SWE-1 AI Models Fully Tested (Geeky Gadgets)](https://www.geeky-gadgets.com/windsurf-swe1-vs-swe1-light-comparison/)
- [Windsurf Launches SWE-1: AI Models Built for the Entire Software Engineering Process (DevOps.com)](https://devops.com/windsurf-launches-swe-1-ai-models-built-for-the-entire-software-engineering-process/)
- [Windsurf Launches SWE-1: A Frontier AI Model Family for End-to-End Software Engineering (MarkTechPost)](https://www.marktechpost.com/2025/05/16/windsurf-launches-swe-1-a-frontier-ai-model-family-for-end-to-end-software-engineering/)
- [SWE-Bench Pro Leaderboard — BenchLM.ai](https://benchlm.ai/benchmarks/swePro)
- [SWE-Bench Pro Leaderboard — Scale AI](https://labs.scale.com/leaderboard/swe_bench_pro_public)
