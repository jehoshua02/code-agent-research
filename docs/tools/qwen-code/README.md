# Qwen Code

## What It Is

**Qwen Code** is an open-source, agentic terminal-based coding assistant made by **Alibaba's Qwen team**. It is a CLI tool that pairs a custom agentic interface with the Qwen3-Coder family of large language models.

- **Product category:** Agentic AI coding assistant / CLI tool (with IDE extension support)
- **Maker:** Alibaba / Qwen team (QwenLM)
- **Initial release:** July 2025 (alongside Qwen3-Coder model launch)
- **License:** Apache 2.0 (fully open source)
- **GitHub:** [QwenLM/qwen-code](https://github.com/QwenLM/qwen-code) — 24,100+ stars as of May 2026

## Pricing

- The CLI itself is free and open source
- **Alibaba Cloud Coding Plan** — primary paid API path; no public per-token rates listed, managed through Model Studio / DashScope
- **Free OAuth tier** — discontinued April 15, 2026
- **Self-hosted** — run local models via Ollama or vLLM at zero API cost
- **Third-party APIs** — OpenRouter, Fireworks AI, or any OpenAI-compatible endpoint; cost depends on provider
- **OpenRouter / Fireworks AI** — pay-as-you-go, competitive rates for Qwen3-Coder-480B

## What It Does

### Core Capabilities

- **Reads, writes, and edits files** across large codebases autonomously
- **Runs shell commands** (builds, tests, git operations) and reasons about output
- **Understands entire repositories** via a native 256K token context window (extendable to 1M with YaRN extrapolation)
- **Multi-step agentic workflows:** handles sequential tasks like PR creation, rebasing, merge conflict resolution, and formatting pipelines
- **Code generation:** scaffolds APIs, features, boilerplate across dozens of languages
- **Debugging:** analyzes stack traces, identifies root causes, applies targeted fixes
- **Test generation:** produces unit tests including edge cases and boundary conditions
- **Query optimization:** suggests database indexing strategies and query rewrites
- **Documentation generation:** writes JSDoc, docstrings, README sections, and architecture flowcharts
- **GitHub integration:** reads issues, creates PRs, manages branches
- **Memory across tasks:** retains changelog context to avoid redundant operations within a session
- **Codebase explanation:** navigates and summarizes unfamiliar repositories

### Supported Languages

Qwen2.5-Coder-32B scores 65.9 on McEval across **40+ programming languages**, with explicit strength in Python, TypeScript, JavaScript, Java, C++, Rust, Go, and uncommon languages like Haskell and Racket. Qwen3-Coder extends this with a 70% code-data training ratio across 7.5T tokens.

### Modes of Operation

- **Interactive mode** — conversational terminal session (default)
- **Headless / non-interactive mode** — scriptable, CI-pipeline-friendly (disabled automatically when `CI_*` env vars are detected)
- **Skills / SubAgents** — built-in composable agentic workflows

## What It Doesn't Do

- **No production-critical security implementation** — outputs require human review; the Qwen team explicitly warns against trusting generated security code without audit
- **No replacement for formal code review** — agentic suggestions can be confident but wrong
- **Algorithm fidelity issues** — documented real-world cases where the model abandons a complex algorithm (e.g., Chudnovsky) mid-task and silently substitutes a simpler but less correct one without flagging the change
- **Debugging existing code** — community feedback consistently notes it is weaker at debugging complex pre-existing code than at generating new code
- **No native VS Code extension** — Gemini CLI (its upstream fork) has VS Code integration; Qwen Code does not, as of mid-2026
- **No mobile apps outside China** — Android and iOS apps are China-only
- **No GUI or web IDE** — CLI-first; IDE support is limited to VS Code, Zed, and JetBrains via extension wrappers (not native)
- **Context configuration pitfalls** — Ollama default context is often 2048 tokens despite 128K+ support; requires manual configuration
- **Political content censorship** — Qwen models refuse to discuss historical events or figures considered sensitive by the Chinese government; Taiwan governance questions are blocked
- **Regional API restrictions** — DashScope API unavailable in some regions (e.g., India) through official channels without workarounds
- **Rate limits** — free-tier users have hit aggressive limits; early versions had rate-limit regressions between patch releases

## Architecture

### How It Runs

| Layer | Details |
|---|---|
| **Runtime** | Node.js 20+ required |
| **Language** | TypeScript (89.6%), JavaScript, Java, Python components |
| **Installation** | `npm install -g @qwen-code/qwen-code`, Homebrew, or quick-install shell script (Linux/macOS/Windows) |
| **Config** | `.env` files or environment variables for API keys and endpoints |
| **IDE integration** | VS Code, Zed, JetBrains via extension wrappers |
| **Local inference** | Ollama or vLLM via OpenAI-compatible API endpoint |

### Origin

Qwen Code is a **fork of Google's Gemini CLI**, adapted with:
- Customized prompts optimized for Qwen3-Coder's function-calling protocol
- Enhanced output parser tuned to Qwen model response formatting
- Additional provider support beyond Google's ecosystem

### Models Used

| Model | Parameters | Context | Notes |
|---|---|---|---|
| **Qwen3-Coder-480B-A35B** | 480B total / 35B active (MoE) | 256K native / 1M YaRN | Flagship; benchmark-comparable to Claude Sonnet 4 |
| **Qwen3-Coder-Next** | 80B total / 3B active (MoE, hybrid attention) | — | Feb 2026; >70% SWE-bench Verified, 44.3% SWE-bench Pro |
| **Qwen3.6-35B-A3B** | 35B total / 3B active | — | Open-weight, efficient agentic coding |
| **Qwen2.5-Coder-32B** | 32B dense | 128K | Previous-gen; strong baseline, runs locally |
| **Qwen2.5-Coder (0.5B–32B)** | 6 sizes | varies | Full range for local deployment |

Training details (Qwen3-Coder-480B): 7.5T tokens, 70% code-focused, synthetic data cleaned and rewritten by Qwen2.5-Coder, trained with long-horizon agent RL using parallel environment execution.

### Supported Backends / Providers

- Alibaba Cloud Model Studio / DashScope (Coding Plan)
- OpenAI-compatible APIs (any)
- Anthropic API
- Google Gemini API
- OpenRouter
- Fireworks AI
- Ollama (local)
- vLLM (local)

## Key Differentiators

1. **Open-source model + open-source CLI** — both the model weights and the agentic tool are Apache 2.0. No vendor lock-in at either layer.
2. **Self-hostable end-to-end** — run Qwen2.5-Coder or Qwen3-Coder locally with Ollama/vLLM. No API dependency, no data leaving the machine.
3. **Frontier-class agentic performance at open-source pricing** — Qwen3-Coder-480B scores 69.6% on SWE-bench Verified vs. Claude Sonnet 4's 70.4%; exceeds it on Agentic Browser Use (49.9 vs. 47.4) and Agentic Tool Use (68.7 vs. 65.2).
4. **1M token effective context** — largest effective context window among open coding agents; enables true repo-scale operations.
5. **Multi-provider by design** — not locked to one API. Switch between Alibaba Cloud, OpenRouter, Fireworks, or self-hosted with one config change.
6. **Model family breadth** — 0.5B to 480B parameter range; deploy the smallest viable model for the task and cost profile.
7. **Tongyi Lingma integration** — Alibaba's enterprise IDE assistant (generated 3B+ lines of code since June 2024) uses the same underlying model family.

**Benchmark comparison (Qwen3-Coder-480B vs Claude Sonnet 4):**

| Benchmark | Qwen3-Coder-480B | Claude Sonnet 4 |
|---|---|---|
| SWE-bench Verified | 69.6% | 70.4% |
| Agentic Coding | 37.5 | 39.0 |
| Agentic Browser Use | 49.9 | 47.4 |
| Agentic Tool Use | 68.7 | 65.2 |
| McEval (40+ languages) | 65.9 (32B) | — |
| Aider (code repair) | 73.7 (32B) | — |

Qwen3-Coder-Next (3B active): >70% SWE-bench Verified, 44.3% SWE-bench Pro — competitive with models 10–20x larger.

## Ideal Use Cases

- **Privacy-sensitive organizations** — self-host models, zero data egress, full audit control
- **High-volume agentic pipelines** — self-hosted inference removes per-token cost at scale
- **Teams needing maximum customization** — fork the Apache 2.0 CLI, modify prompts, embed in internal tooling
- **Polyglot codebases** — 40+ language support with strong uncommon-language performance
- **Large monorepos** — 256K–1M token context handles repository-scale context without chunking
- **Infrastructure-conscious orgs** — run a 7B or 14B Qwen2.5-Coder locally on a single GPU for modest tasks; scale up to 480B via API for complex agentic work
- **Budget-constrained teams** — self-hosted path has near-zero marginal cost once hardware is provisioned

**Not ideal for:**
- Teams wanting a zero-config, polished out-of-box experience (steeper setup vs. Claude Code or Copilot)
- Projects requiring guaranteed algorithm correctness without human review
- Users in regions with DashScope API restrictions who don't want to use third-party providers

## Community & Ecosystem

- **GitHub stars:** 24,100+ (QwenLM/qwen-code) as of May 2026; 420+ releases
- **Model downloads:** Qwen-based coding models have surpassed **20 million downloads** globally
- **Tongyi Lingma:** Alibaba's enterprise IDE assistant powered by the same model family; 3B+ lines generated since June 2024
- **Open source status:** Both CLI (Apache 2.0) and model weights (open-weight, most variants) are publicly available on GitHub, Hugging Face, and ModelScope
- **Extensibility:**
  - Supports MCP (Model Context Protocol) for tool extensibility
  - Compatible as a backend for Claude Code and Cline (configured as alternative provider)
  - SDKs available for TypeScript, Python, Java integration
  - Skills / SubAgents system for composable workflows
- **Third-party availability:** Deployable via Together AI, OpenRouter, Fireworks AI, Ollama, vLLM
- **Forks and mirrors:** Active fork ecosystem; `kevinli1124/qwen-code` and others track upstream
- **Enterprise:** Alibaba Cloud Coding Plan provides SLA-backed API access; Together AI offers SOC 2-compliant North American hosting with 99.9% uptime SLA and batch API support

## Sources

- [QwenLM/qwen-code — GitHub](https://github.com/QwenLM/qwen-code)
- [Qwen3-Coder: Agentic Coding in the World — Qwen Blog](https://qwenlm.github.io/blog/qwen3-coder/)
- [Introducing Qwen-Code — NYU Shanghai RITS](https://rits.shanghai.nyu.edu/ai/introducing-qwen-code-alibabas-open%E2%80%91source-cli-for-agentic-coding-with-qwen3%E2%80%91coder/)
- [Alibaba Unveils Qwen3-Coder — Alibaba Cloud Blog](https://www.alibabacloud.com/blog/alibaba-unveils-cutting-edge-ai-coding-model-qwen3-coder_602399)
- [Boost Your Coding Workflow with Qwen Code — Alibaba Cloud Blog](https://www.alibabacloud.com/blog/boost-your-coding-workflow-with-qwen-code-a-practical-guide_602991)
- [Qwen Code CLI: A Guide With Examples — DataCamp](https://www.datacamp.com/tutorial/qwen-code)
- [Qwen Code is Good but Not Great — InfoWorld](https://www.infoworld.com/article/4054914/qwen-code-is-good-but-not-great.html)
- [AI CLI Tools in 2026: Claude Code vs Gemini CLI vs Qwen Code — Jahanzaib Tayyab](https://www.jahanzaibtayyab.com/blog/ai-cli-tools-comparison-2026)
- [Top AI Coding Assistants Compared — Medium / Fendy Feng](https://medium.com/@fendylike/top-ai-coding-assistants-claude-code-vs-gemini-cli-vs-cursor-vs-qwen-code-0bc759fc9d45)
- [Qwen3-Coder on Together AI](https://www.together.ai/blog/qwen-3-coder)
- [Qwen2.5-Coder Series — Qwen Blog](https://qwenlm.github.io/blog/qwen2.5-coder-family/)
- [Qwen2.5-Coder Technical Report — arXiv](https://arxiv.org/abs/2409.12186)
- [Qwen3-Coder-Next Technical Report — arXiv](https://arxiv.org/html/2603.00729v1)
