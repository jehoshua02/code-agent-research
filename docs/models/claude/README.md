# Claude

## What It Is

Claude is a proprietary large language model family developed by Anthropic. The family launched in March 2024 with the Claude 3 generation and is structured around three tiers: Haiku (fast, low-cost), Sonnet (balanced), and Opus (most capable). Anthropic is a safety-focused AI lab and all Claude models are closed-weight and accessible only via API, claude.ai, or partner platforms (AWS Bedrock, Google Vertex AI, Microsoft Foundry). The family has iterated rapidly through generations 3, 3.5, 3.7, 4, 4.1, 4.5, 4.6, and 4.7 as of early 2026.

## Variants

All variants support text and image input (vision) with text output. All support multilingual use.

### Currently Active Models

| Model | API ID | Released | Context | Max Output | Notes |
|---|---|---|---|---|---|
| Claude Opus 4.7 | `claude-opus-4-7` | April 16, 2026 | 1M tokens | 128K tokens | Most capable GA model; new tokenizer (uses 1–1.35x more tokens); xhigh effort level; 3.75MP vision |
| Claude Sonnet 4.6 | `claude-sonnet-4-6` | Feb 17, 2026 | 1M tokens | 64K tokens | Best speed/intelligence balance; extended thinking + adaptive thinking |
| Claude Haiku 4.5 | `claude-haiku-4-5-20251001` | Oct 15, 2025 | 200K tokens | 64K tokens | Fastest model; ~97 tokens/sec throughput; extended thinking |
| Claude Opus 4.6 | `claude-opus-4-6` | Feb 5, 2026 | 1M tokens | 128K tokens | Legacy; fast mode available ($30/$150/MTok) |
| Claude Sonnet 4.5 | `claude-sonnet-4-5-20250929` | Sep 29, 2025 | 200K tokens | 64K tokens | Strong coding; 1M context in beta |
| Claude Opus 4.5 | `claude-opus-4-5-20251101` | Nov 24, 2025 | 200K tokens | 64K tokens | 67% cheaper than Opus 4.1 with similar quality |
| Claude Opus 4.1 | `claude-opus-4-1-20250805` | Aug 5, 2025 | 200K tokens | 32K tokens | Production reliability focus |

### Deprecated Models (still available, migration recommended)

| Model | API ID | Released | Notes |
|---|---|---|---|
| Claude Sonnet 4 | `claude-sonnet-4-20250514` | May 22, 2025 | Retires June 15, 2026 |
| Claude Opus 4 | `claude-opus-4-20250514` | May 22, 2025 | Retires June 15, 2026 |
| Claude 3.7 Sonnet | `claude-3-7-sonnet-20250219` | Feb 24, 2025 | First hybrid reasoning model |
| Claude 3.5 Sonnet (v2) | `claude-3-5-sonnet-20241022` | Oct 22, 2024 | Added computer use |
| Claude 3.5 Haiku | `claude-3-5-haiku-20241022` | Oct 22, 2024 | — |
| Claude 3.5 Sonnet | `claude-3-5-sonnet-20240620` | June 20, 2024 | — |
| Claude 3 Haiku | `claude-3-haiku-20240307` | Mar 13, 2024 | Still available; very cheap |
| Claude 3 Sonnet | `claude-3-sonnet-20240229` | Mar 4, 2024 | Discontinued |
| Claude 3 Opus | `claude-3-opus-20240229` | Mar 4, 2024 | Deprecated |

Parameter counts are not publicly disclosed by Anthropic for any Claude model.

## Pricing

All prices in USD per million tokens (MTok). Batch API provides 50% discount across the board. Prompt caching reduces repeated input costs by up to 90%.

### Standard API Pricing

| Model | Input | Output | Batch Input | Batch Output |
|---|---|---|---|---|
| Opus 4.7 | $5 | $25 | $2.50 | $12.50 |
| Opus 4.6 | $5 | $25 | $2.50 | $12.50 |
| Opus 4.5 | $5 | $25 | $2.50 | $12.50 |
| Opus 4.1 | $15 | $75 | $7.50 | $37.50 |
| Opus 4 (deprecated) | $15 | $75 | $7.50 | $37.50 |
| Sonnet 4.6 | $3 | $15 | $1.50 | $7.50 |
| Sonnet 4.5 | $3 | $15 | $1.50 | $7.50 |
| Sonnet 4 (deprecated) | $3 | $15 | $1.50 | $7.50 |
| Sonnet 3.7 (deprecated) | $3 | $15 | $1.50 | $7.50 |
| Haiku 4.5 | $1 | $5 | $0.50 | $2.50 |
| Haiku 3.5 (deprecated) | $0.80 | $4 | $0.40 | $2.00 |
| Haiku 3 | $0.25 | $1.25 | $0.125 | $0.625 |
| Opus 3 (deprecated) | $15 | $75 | $7.50 | $37.50 |

### Prompt Caching

Cache writes cost 1.25x base input (5-minute TTL) or 2x base input (1-hour TTL). Cache reads cost 0.1x base input. As of March 13, 2026, there are no long-context surcharges; 900K-token requests cost the same per-token rate as 9K-token requests on models with 1M context.

### Other Cost Factors

- **Fast mode** (Opus 4.6 only): $30/$150 per MTok input/output (6x premium, significantly lower latency)
- **Web search** (server-side tool): $10 per 1,000 searches, plus token costs
- **Code execution**: 1,550 free hours/month per org; $0.05/hour/container beyond that
- **Data residency** (US-only routing): 1.1x multiplier on all token costs
- **Claude Managed Agents**: $0.08/session-hour, plus standard token costs
- No self-hosted option; no open weights released

### Consumer Plans

- **Free**: Access to claude.ai with usage limits
- **Pro**: $20/month individual; priority access, higher limits
- **Team**: $30/user/month; team collaboration features
- **Enterprise**: Custom pricing; volume discounts, custom rate limits

## Context Window

| Model Generation | Context Window | Max Output |
|---|---|---|
| Claude 3 (Haiku/Sonnet/Opus) | 200K tokens | Varies |
| Claude 3.5 Sonnet / Haiku | 200K tokens | 8K tokens |
| Claude 3.7 Sonnet | 200K tokens | 128K tokens |
| Claude Sonnet 4 / Opus 4 | 200K tokens | 64K / 32K tokens |
| Haiku 4.5 | 200K tokens | 64K tokens |
| Sonnet 4.5 / Opus 4.1 | 200K tokens | 64K / 32K tokens |
| Opus 4.5 | 200K tokens | 64K tokens |
| Opus 4.6 / Sonnet 4.6 | **1M tokens** | 128K / 64K tokens |
| Opus 4.7 | **1M tokens** | 128K tokens |

1M-token context (~750K words / ~3.4M unicode characters for Sonnet 4.6; ~555K words / ~2.5M unicode characters for Opus 4.7 due to new tokenizer) became generally available in February 2026. Previously only available in beta or for select customers.

Practical limit note: While the API accepts 1M tokens, very long contexts can degrade coherence and attention on specific content. Prompt caching is recommended for large, stable context blocks.

## Benchmarks

Claude models are proprietary so parameter counts and architecture are not published. Benchmarks below are from Anthropic announcements and third-party evaluations.

### SWE-bench Verified (real-world software engineering — higher is better)

SWE-bench Verified is the most relevant benchmark for coding tool use. Models must reproduce a bug, identify the root cause, write a fix, and pass existing tests on real GitHub issues.

| Model | SWE-bench Verified | Notes |
|---|---|---|
| Claude Opus 4.7 | 87.6% | April 2026; 13% lift over Opus 4.6 on 93-task internal benchmark |
| Claude Opus 4.6 | 80.8% | — |
| Claude Sonnet 4.6 | 79.6% | +2.4 pts over Sonnet 4.5 |
| Claude Haiku 4.5 | 73.3% | Strong for its tier |
| Claude Sonnet 4.5 | 77.2% | — |
| Claude Opus 4 / Sonnet 4 | ~72.5% / ~72.7% | May 2025 launch; led at time of release |
| Claude 3.7 Sonnet | 70.3% | With custom scaffold; 63.7% pass@1 |
| Claude 3.5 Sonnet (v2) | 49.0% | Oct 2024; led all public models at release |
| Claude 3.5 Sonnet (v1) | 33.4% | June 2024 |
| Claude 3 Opus | ~38% | Measured in internal agentic coding eval |

### CursorBench (coding inside Cursor IDE)

| Model | CursorBench |
|---|---|
| Claude Opus 4.7 | 70% |
| Claude Opus 4.6 | 58% |

### HumanEval (function-level code generation — largely saturated at frontier)

| Model | HumanEval |
|---|---|
| Claude Opus 4.7 | ~95% |
| Claude 3.5 Sonnet (v1) | 92.0% |
| Claude 3.5 Sonnet (v1, internal) | 64% (agentic eval) |

Note: HumanEval is effectively saturated for frontier models (most score 90%+). SWE-bench Verified is more discriminating for real-world coding tasks.

### TAU-bench (agentic tool use)

| Model | Retail | Airline |
|---|---|---|
| Claude 3.7 Sonnet | 81.2% | 58.4% |
| Claude 3.5 Sonnet (v2) | 69.2% | 46.0% |

### Knowledge and Reasoning

| Model | MMLU | GPQA Diamond |
|---|---|---|
| Claude 3.5 Sonnet (v1) | Top-tier (exact score not published by Anthropic) | Beat Claude 3 Opus |
| Claude 3 Opus | Led peers at launch (March 2024) | — |

Reliable knowledge cutoffs: Opus 4.7: Jan 2026; Sonnet 4.6: Aug 2025; Haiku 4.5: Feb 2025.

## Hardware Requirements

Claude models are proprietary and not available for self-hosting. There are no official weights to download, no Ollama support, and no vLLM compatibility for Claude models directly.

**API access only.** Hardware requirements for end users are limited to what is needed to call the REST API:
- Any machine with an internet connection and HTTP client
- Typical developer laptop is fully sufficient
- No GPU required on the client side

For teams routing Claude through Claude Code, Cursor, or similar tools, latency is primarily determined by Anthropic's infrastructure, not client hardware.

**Note on open-weight alternatives:** Anthropic has consistently stated it does not plan to release open weights for Claude. Developers seeking self-hosted alternatives with comparable coding ability typically use Qwen 2.5 Coder 72B (requires ~40GB VRAM at Q4) or DeepSeek Coder V3 (requires multi-GPU or high-RAM systems). These do not match current Claude performance on SWE-bench.

## Supported Tools

Claude models are the backbone of a wide range of coding tools and platforms.

### First-Party

| Tool | Model(s) Used | Notes |
|---|---|---|
| **Claude Code** (Anthropic CLI) | Sonnet 4.6 default; Opus 4.7 available | Official agentic coding CLI; supports /ultrareview command |
| **claude.ai** | All current models | Web and mobile interface |

### Third-Party Coding Assistants (Claude models available)

| Tool | Claude Support | Notes |
|---|---|---|
| **Cursor** | Opus 4.7, Sonnet 4.6, Haiku 4.5 | BYOK (bring your own key) + subscription; claude consistently rated best for complex refactors |
| **Windsurf** | Sonnet 4.6, Haiku 4.5 | Partial BYOM support |
| **Cline** | All via API key | Full BYOM; popular Claude Code alternative in VS Code |
| **Continue** | All via API key | Full BYOM; VS Code + JetBrains |
| **Aider** | All via API key | Full BYOM; terminal-based coding agent |
| **GitHub Copilot** | Sonnet 4.5+ | Curated model selection; Claude available alongside GPT and Gemini |
| **Amazon Q Developer** | Claude on Bedrock | Via Bedrock integration |

### API Platforms

Available via: Anthropic direct API, AWS Bedrock, Google Vertex AI, Microsoft Azure Foundry.

Claude Code and Anthropic's Managed Agents offering do not support BYOM — they use Anthropic's hosted models only.

## Strengths

**Real-world coding (SWE-bench leadership):** Claude models consistently lead or near-lead on SWE-bench Verified, the most practice-relevant coding benchmark. Claude Opus 4.7 at 87.6% is the highest score of any generally available model as of May 2026. Preferred by Cursor, Windsurf, and the broader coding-tool ecosystem.

**Instruction following:** Claude is notably reliable at adhering to long, complex system prompts. Production systems with multi-constraint system prompts (e.g., 2,000-word prompts with 15+ rules) see consistently fewer constraint violations than GPT or Gemini.

**Extended thinking / hybrid reasoning:** Starting with Claude 3.7 Sonnet (Feb 2025), Claude introduced visible extended thinking — the model works through problems step-by-step in a way developers can observe and budget. This materially improves math, physics, and complex debugging tasks. Continued through all Claude 4 generations.

**Long output generation:** Claude 3.7 Sonnet and all Claude 4 models support 64K–128K output tokens per request (with Batch API supporting up to 300K on Opus 4.6/4.7 and Sonnet 4.6). This enables full-file rewrites and large code generation tasks in a single call.

**Large context handling:** 1M token context window (GA since Feb 2026) with no long-context pricing premium. Useful for loading entire codebases, long conversation histories, or large documentation sets.

**Agentic reliability:** Claude 4 generation is 65% less likely to use shortcuts or workarounds in agentic coding tasks compared to Claude 3.x. Parallel tool execution and enhanced memory across sessions available in Claude 4.5+.

**Prose quality:** Consistently rated highest for natural, human-like writing — relevant for docstrings, commit messages, code comments, and technical documentation generation.

**Price/performance (Haiku 4.5):** At $1/$5/MTok with 73.3% SWE-bench, Haiku 4.5 offers frontier-class coding capability at sub-frontier pricing. ~97 tokens/sec throughput is 83% faster than Sonnet 4.6.

## Weaknesses

**No self-hosting / no open weights:** All Claude models are API-only. Teams with data-sovereignty requirements, air-gapped environments, or tight cost constraints cannot run Claude locally. No Ollama, no vLLM, no quantization.

**Tokenizer overhead (Opus 4.7):** Opus 4.7 uses a new tokenizer that consumes 1–1.35x more tokens than Opus 4.6 for the same input text. This effectively increases cost for fixed workloads, partially offsetting the unchanged nominal price.

**Competitive programming / algorithmic reasoning:** Gemini models lead LiveCodeBench for competitive programming (algorithmic, Olympiad-style problems). Claude's edge is on real-world software engineering, not competitive coding puzzles.

**Creative task performance:** Some evals find GPT models slightly stronger on open-ended creative tasks. Claude's instruction-following optimization may produce more conservative or constrained outputs when unconstrained creativity is desired.

**Haiku 4.5 context ceiling:** At 200K tokens (vs. 1M for Sonnet 4.6 and Opus 4.6/4.7), Haiku 4.5 cannot handle the largest codebase-scale contexts without chunking.

**Cost at scale for Opus tier:** At $25/MTok output, Opus models are expensive for high-volume production use. Teams doing millions of coding completions per day will find Sonnet 4.6 or Haiku 4.5 necessary for cost control.

**No Haiku 4.6/4.7:** As of May 2026, the Haiku tier has not been updated past 4.5. Haiku 4.5 lacks adaptive thinking and has a smaller context window than the Sonnet/Opus tier.

## Sources

- [Anthropic Models Overview](https://platform.claude.com/docs/en/about-claude/models/overview)
- [Anthropic Pricing Page](https://platform.claude.com/docs/en/about-claude/pricing)
- [Introducing Claude 3 Family (March 2024)](https://www.anthropic.com/news/claude-3-family)
- [Introducing Claude 3.5 Sonnet (June 2024)](https://www.anthropic.com/news/claude-3-5-sonnet)
- [Computer Use & Claude 3.5 Sonnet v2 (Oct 2024)](https://www.anthropic.com/news/3-5-models-and-computer-use)
- [Claude 3.7 Sonnet and Claude Code (Feb 2025)](https://www.anthropic.com/news/claude-3-7-sonnet)
- [Introducing Claude 4 (May 2025)](https://www.anthropic.com/news/claude-4)
- [Introducing Claude Opus 4.7 (April 2026)](https://www.anthropic.com/news/claude-opus-4-7)
- [Claude (language model) - Wikipedia](https://en.wikipedia.org/wiki/Claude_(language_model))
- [Every Claude Model: From Claude 3 to Mythos Preview — claudefa.st](https://claudefa.st/blog/models)
- [Claude Haiku 4.5 Stats — llm-stats.com](https://llm-stats.com/models/claude-haiku-4-5-20251001)
- [Claude Opus 4.7 Benchmarks — Vellum](https://www.vellum.ai/blog/claude-opus-4-7-benchmarks-explained)
- [Cursor vs Claude Code vs GitHub Copilot 2026 — NxCode](https://www.nxcode.io/resources/news/cursor-vs-claude-code-vs-github-copilot-2026-ultimate-comparison)
- [Claude vs Gemini 2026 — tech-insider.org](https://tech-insider.org/claude-vs-gemini-2026/)
- [SWE-bench Leaderboard — benchlm.ai](https://benchlm.ai/coding)
