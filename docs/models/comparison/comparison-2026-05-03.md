# AI Model Comparison Guide for Coding

**May 3, 2026**

---

## 1. Executive Summary

The AI coding model landscape in mid-2026 is defined by two distinct tiers: proprietary frontier models that lead on real-world benchmarks, and open-weight models that have closed most of the gap at a fraction of the cost. Claude Opus 4.7 (87.6% SWE-bench Verified) and GPT-5.5 (88.7%) trade the top spot on real-world software engineering tasks, with Gemini 3.1 Pro (80.6%) and DeepSeek V4 Pro (80.6%) close behind. The once-clear lead of closed models has narrowed dramatically: open-weight Qwen3-Coder-Next achieves 71% SWE-bench at ~3B active parameters, and DeepSeek V4 Pro at 80.6% matches Gemini 3.1 Pro while being fully self-hostable — albeit at cluster scale.

Cost dynamics have shifted just as quickly. DeepSeek V4 Pro's API at $0.435/$0.87 per million tokens is roughly 7x cheaper than Claude Sonnet 4.6 and 10x cheaper than Claude Opus 4.7 on output tokens. Qwen3-Coder-480B is available on OpenRouter at $0.22/$1.80 per million tokens — open-weight, Apache 2.0, and capable of near-frontier agentic coding. For teams that can tolerate API latency and don't need raw SWE-bench-topping accuracy, open-weight and Chinese-lab models offer exceptional value.

A third category has emerged: IDE-native models. Windsurf's SWE-1 family is purpose-built for the software engineering lifecycle — not general LLMs adapted for code — and runs at 950 tokens/second on Cerebras hardware, making agentic tasks complete in under 5 seconds. Grok Code Fast 1 similarly targets agentic workflows at $0.20/$1.50 per million tokens with a 256K context window. The model choice is increasingly inseparable from the IDE and agent scaffold choice: the same underlying capability can produce dramatically different results depending on how the model is wired into the development environment.

---

## 2. Model Categories

### Proprietary Frontier (General-Purpose)

Models developed by large Western AI labs, API-only, no self-hosting, highest capability ceiling.

- **Claude** (Anthropic) — Opus 4.7, Sonnet 4.6, Haiku 4.5
- **GPT** (OpenAI) — GPT-5.5, GPT-5.3-Codex, o3
- **Gemini** (Google DeepMind) — Gemini 3.1 Pro, Gemini 3 Flash

### Open-Weight Frontier (Chinese Labs)

Full model weights released under permissive licenses; API available but self-hosting is the key differentiator.

- **DeepSeek** (DeepSeek-AI) — V4 Pro, V4 Flash, R1
- **Qwen Coder** (Alibaba) — Qwen3-Coder-480B, Qwen3-Coder-Next, Qwen2.5-Coder-32B
- **Hunyuan** (Tencent) — Hy3 preview, Hunyuan-Large

### Open-Weight General-Purpose

Broad open-weight models competitive on coding, best as fine-tuning bases.

- **Llama** (Meta) — Llama 4 Scout, Maverick, Llama 3.3 70B

### Code-Specialized / IDE-Native

Models purpose-built for software engineering workflows, not adapted from general LLMs.

- **SWE-1** (Windsurf / Cognition AI) — SWE-1.6, SWE-1.5, SWE-1-lite
- **Grok Code Fast 1** (xAI) — agentic coding MoE, purpose-built posttraining on real PRs

### Reasoning Models

Models with extended chain-of-thought training, optimized for math and hard logic.

- **DeepSeek R1 / R1-0528** — open-weight, MIT license
- **OpenAI o3** — proprietary; superseded by GPT-5.4 as default
- **Grok-3 Think** — extended reasoning variant of Grok-3

---

## 3. Comparison Matrix

| Model Family | Maker | Top Variant | SWE-bench Verified | Context Window | Open Weight | Self-Hostable | API Cost Input/Output ($/1M) |
|---|---|---|---|---|---|---|---|
| Claude | Anthropic | Opus 4.7 | 87.6% | 1M | No | No | $5 / $25 |
| GPT | OpenAI | GPT-5.5 | 88.7% | 922K | No | No | $5 / $30 |
| Gemini | Google | Gemini 3.1 Pro | 80.6% | 1M | No | No | $2 / $12 |
| DeepSeek | DeepSeek-AI | V4 Pro | 80.6% | 1M | Yes | Yes (cluster) | $0.44 / $0.87 |
| Grok | xAI | Grok Code Fast 1 | 70.8% | 256K | No | No | $0.20 / $1.50 |
| Hunyuan | Tencent | Hy3 preview | 74.4% | 256K | Yes | Yes (cluster) | $0.17 / $0.55 |
| Llama | Meta | Llama 4 Maverick | ~43% (LCB) | 1M | Yes | Yes | $0.17 / $0.60 |
| Qwen Coder | Alibaba | Qwen3-Coder-Next | ~71% | 256K | Yes | Yes | $0.12 / $0.80 |
| SWE-1 | Windsurf | SWE-1.6 | N/A* | ~128K | No | No | $0 (in Windsurf) |

*SWE-1 uses SWE-bench Pro (731 tasks) instead of SWE-bench Verified. SWE-1.5 scored 40.08% on SWE-bench Pro vs. Claude Sonnet 4.5's 43.60%. SWE-bench Pro and Verified are not directly comparable.

Notes: Llama 4 SWE-bench Verified not officially reported; LiveCodeBench (LCB) score of 43.4 used as proxy. DeepSeek R1 excluded from top variant since V4 Pro supersedes it on coding. Grok Code Fast 1 pricing is $0.20/$1.50 at standard rate.

---

## 4. Key Factors for Choosing a Model

### Benchmark Performance

SWE-bench Verified is the most meaningful coding benchmark — models must identify root causes, write fixes, and pass existing tests on real GitHub issues. As of May 2026:

- **GPT-5.5**: 88.7% — highest reported
- **Claude Opus 4.7**: 87.6% — highest generally available
- **Gemini 3.1 Pro / DeepSeek V4 Pro**: 80.6% — tied for third
- **Hy3 preview**: 74.4%
- **Qwen3-Coder-Next**: ~71%
- **Grok Code Fast 1**: 70.8%

HumanEval is largely saturated (frontier models 90%+) and not useful for differentiation. LiveCodeBench measures competitive-programming style problems and correlates with algorithmic ability more than real-world engineering. SWE-bench Pro (Scale AI, 731 tasks) is harder than Verified and better predicts multi-file agentic performance; only SWE-1 and a few others report it.

Benchmark scores are scaffold-dependent. Windsurf's SWE-bench Pro scores use their own Cascade harness; an independent analysis found the harness alone contributes ~11 percentage points. Always prefer apples-to-apples comparisons using the same agent framework.

### Cost

Cost varies by two orders of magnitude across the landscape. Key reference points per million tokens (input/output):

- Cheapest API: DeepSeek V4 Flash ($0.14/$0.28), Llama 3.1 8B via DeepInfra ($0.02/$0.02)
- Mid-range value: Gemini 3 Flash ($0.50/$3.00), Qwen3-Coder-Next ($0.12/$0.80)
- Frontier-tier: Claude Opus 4.7 ($5/$25), GPT-5.5 ($5/$30)
- Self-hosted: compute cost only; at scale, open-weight models beat all API pricing

For agentic coding loops with many tool calls, output token cost dominates. At $25/M output (Claude Opus), a 100K-token agentic session costs $2.50. The same session on DeepSeek V4 Pro ($0.87/M) costs $0.087. At 10,000 sessions/month, this is $25,000 vs. $870 — a 30x difference.

SWE-1 models are free within Windsurf subscriptions ($0 credits), making them effectively the cheapest option for teams already using Windsurf.

### Context Window

| Window Size | Models |
|---|---|
| 1M tokens | Claude Opus 4.7, Claude Sonnet 4.6, GPT-5.5, Gemini 3.1 Pro, DeepSeek V4 Pro/Flash |
| 256K tokens | Qwen3-Coder series, Hy3 preview, Hunyuan-Large (pretrain) |
| 128K tokens | GPT-5, o3, Llama 3.x, DeepSeek V3/R1, Hunyuan-Large (instruct), SWE-1.5 (est.) |
| 10M tokens | Llama 4 Scout (open-weight; instruct-tuning extension; quality caveats at extremes) |

1M context is now available from multiple providers at no pricing premium (Claude, Gemini, DeepSeek V4). Gemini 3.1 Pro and 3 Flash add a 2x surcharge for prompts over 200K tokens. Practical advice: use prompt caching for large stable context blocks; coherence and attention quality degrades before the hard token limit.

### Speed (Tokens/sec, TTFT)

Speed matters most in interactive IDE use and tight agentic loops.

| Model | Throughput | TTFT Notes |
|---|---|---|
| SWE-1.5 / SWE-1.6 (Cerebras) | ~950 tok/s | Sub-second for short responses |
| Gemini 2.5 Flash | ~232 tok/s | Among fastest API models |
| Gemini 3 Flash | ~183 tok/s | Fast and frontier-capable |
| Claude Haiku 4.5 | ~97 tok/s | Fastest Claude model |
| Grok Code Fast 1 | ~115 tok/s | High TTFT (7s) for reasoning |
| Hunyuan-Large BF16 | ~75 tok/s (self-hosted) | — |
| Claude Sonnet 4.6 | ~53 tok/s (est.) | — |
| Hy3 preview | — | TTFT 3.58s (above median) |

Reasoning models (R1, o3, Grok-3 Think) have high TTFT because they generate chain-of-thought tokens before the answer. This is unsuitable for interactive autocomplete but acceptable for batch or async agent tasks.

### Open Weight vs. Proprietary

Open-weight means you can download, self-host, fine-tune, and inspect model weights. Proprietary models are API-only.

Open-weight advantages: full data control, no API dependency, fine-tuning potential, cost elimination at scale, air-gapped deployment.

Open-weight disadvantages: significant infrastructure burden for large models, no SLA, self-managed updates.

Truly permissive open-weight models (Apache 2.0): Qwen3-Coder series, Qwen2.5-Coder (most), DeepSeek V3/R1/V4 (MIT).

Restricted open-weight: Llama (Meta Community License; 700M MAU cap; EU restriction on multimodal Llama 4; "Built with Llama" attribution required). Hunyuan (Tencent Hy Community License; commercial use permitted but terms differ from Apache 2.0).

Closed-weight: Claude, GPT, Gemini, Grok, SWE-1.

### Hardware Requirements for Self-Hosting

See the Self-Hosting Guide (Section 6) for detailed VRAM tables. Summary:

- **Single consumer GPU (RTX 4090, 24GB)**: Qwen2.5-Coder-32B (Q4), Qwen3-Coder-30B-A3B (Q4), DeepSeek R1-Distill-Qwen-32B, Llama 3.3 70B (Q4 with dual GPUs)
- **Single workstation GPU (RTX 5090 / PRO 6000)**: Qwen3-Coder-Next (Q4), Llama 4 Scout (Q8)
- **Small cluster (4–8x A100/H100)**: DeepSeek V3/R1 (671B), Hunyuan-Large, DeepSeek V4 Flash, Llama 3.1 405B
- **Large cluster (8x H100+ / DGX)**: DeepSeek V4 Pro (1.6T), Hy3 preview, Qwen3-Coder-480B

### Privacy and Data Handling

Proprietary API models send prompts to third-party servers. Key considerations:

- **Claude**: Anthropic servers (US). Data residency (US-only routing) available at 1.1x price. Enterprise plans with BAA available.
- **GPT**: OpenAI servers (US). Enterprise tier with zero data retention available.
- **Gemini**: Google servers. Vertex AI provides enterprise data handling with no training use of your data.
- **DeepSeek API**: Servers in China. Organizations with data residency or compliance requirements should self-host or use third-party inference providers (DeepInfra, Fireworks) that host the weights outside China.
- **Grok**: xAI servers (US). Standard API TOS applies.
- **Open-weight (self-hosted)**: Full data control. No data leaves your infrastructure.

### Tool Compatibility

Most models support OpenAI-compatible APIs, making integration straightforward. Key distinctions:

- **Claude**: Native integrations in Cursor, Windsurf, Cline, Aider, GitHub Copilot, Amazon Q. Also on AWS Bedrock, Google Vertex, Azure Foundry.
- **GPT**: Native integrations in GitHub Copilot, Cursor, Windsurf, OpenAI Codex CLI. Most tools assume GPT as default.
- **Gemini**: Native in Gemini CLI, Gemini Code Assist, Google Antigravity IDE, GitHub Copilot.
- **DeepSeek**: OpenAI-compatible API. Works in Cursor, Continue, Cline, Aider with base URL change. Available on OpenRouter, DeepInfra, Fireworks.
- **Qwen Coder**: Ollama (all sizes), vLLM, SGLang. Qwen3-Coder uses a custom function-call format requiring updated vLLM/SGLang parsers. Qwen Code CLI is Alibaba's first-party agent.
- **Llama**: Ollama, vLLM, llama.cpp, LM Studio, Continue.dev, Tabby. GitHub Copilot offered Llama 3.1 405B as selectable model.
- **SWE-1**: Windsurf IDE only. No external API. Not available in Cursor, Claude Code, or any other tool.
- **Grok Code Fast 1**: OpenAI-compatible (xAI API). Available in GitHub Copilot, Cursor, Cline, Windsurf, Roo Code at launch.

### Reasoning Capability

Extended reasoning (chain-of-thought, thinking mode) improves performance on complex multi-step problems: algorithm design, debugging subtle logic errors, math-heavy engineering tasks.

Models with built-in reasoning / thinking modes:
- **Claude**: Extended thinking on Opus 4.7, Sonnet 4.6, Haiku 4.5; adaptive thinking on Sonnet 4.6
- **GPT**: o3 series (RL-trained reasoning); GPT-5.x thinking mode; adjustable effort levels
- **Gemini**: Native thinking on 2.5 Pro, 2.5 Flash, 3 Flash, 3.1 Pro
- **DeepSeek R1**: Deep chain-of-thought via RL; R1 matches o1 on AIME/math
- **DeepSeek V4 Pro**: Non-Think, Think High, Think Max modes; Think Max requires ≥384K context
- **Grok-3 Think**: Extended reasoning variant
- **Hy3 preview**: Configurable `reasoning_effort` (no_think / low / high)

Models without built-in reasoning: Qwen3-Coder (no `<think>` blocks), Llama 4 (no native reasoning mode), SWE-1 (RL on engineering tasks but no user-visible CoT).

Reasoning models trade latency for accuracy. For interactive use, non-thinking mode or lightweight thinking is preferred. For complex, async agentic tasks, deep reasoning pays off.

### Code Specialization

Some models are purpose-built for code; others are general-purpose models with strong coding ability.

**Code-specialized** (trained primarily or exclusively on code/software engineering data):
- Qwen Coder series — pretrained on 5.5T tokens code-heavy corpus; trained with Agent RL on 20,000 parallel cloud environments
- Grok Code Fast 1 — separate pretraining corpus heavy on programming; posttraining on real pull requests
- SWE-1 family — trained exclusively on software engineering tasks using real Windsurf editor data

**General-purpose with strong coding** (full general training, competitive on code):
- Claude, GPT-5.x, Gemini 3.x, DeepSeek V4 Pro, Llama 4

**Key implication**: Code-specialized models tend to have stronger tool-call reliability, better handling of diffs/patches, and more robust multi-turn repo-editing behavior. General-purpose frontier models may perform better on code that requires broad reasoning, novel API usage, or domain knowledge outside the code itself.

---

## 5. Head-to-Head Comparisons

### Claude Opus 4.7 vs. GPT-5.5

The two highest-scoring models on SWE-bench Verified (87.6% vs. 88.7%) are effectively peers on real-world coding. GPT-5.5 has a slight benchmark edge and a larger context window (922K input vs. 1M for Claude, though Claude's full 1M is usable at standard pricing). Claude has a meaningful advantage on instruction following in complex system prompts, long output generation (128K output tokens), and is rated higher by Cursor and Windsurf users for complex refactors. GPT-5.5 at $30/M output is 20% pricier than Claude Opus 4.7 ($25/M output). For most teams, Claude Opus 4.7 is the safer default for heavy coding; GPT-5.5 via Codex CLI is stronger for long-horizon agentic tasks built on OpenAI's infrastructure.

### Gemini 3.1 Pro vs. Claude Sonnet 4.6

Both score within one point on SWE-bench Verified (80.6% vs. 79.6%). Gemini 3.1 Pro is cheaper ($2/$12 vs. $3/$15 per million tokens) and faster (~183 tok/s via Gemini 3 Flash). Claude Sonnet 4.6 has better instruction-following scores and broader IDE integration. Gemini 3 Flash is the more relevant competitor to Sonnet 4.6 in practice: at 78% SWE-bench, $0.50/$3.00 per million tokens, and 183 tok/s, it undercuts Sonnet on both cost and speed while matching it on accuracy. Choose Gemini 3 Flash for cost-sensitive agentic loops; choose Claude Sonnet 4.6 for complex, instruction-heavy workflows.

### Qwen3-Coder vs. DeepSeek for Self-Hosting

Both are MIT/Apache 2.0 open-weight models from Chinese AI labs with strong coding focus. At small scale, Qwen3-Coder wins: Qwen2.5-Coder-32B runs on a single RTX 4090 (24GB, Q4); Qwen3-Coder-Next runs on a single RTX 5090 (32GB, Q4) at 38–48 tok/s with 71% SWE-bench Verified. DeepSeek's comparable capability lives in V3.2 (77.2% SWE-bench) which requires an 8-GPU cluster. For teams with a single high-end GPU, Qwen3-Coder-Next is the best self-hosted coding model available. At cluster scale, DeepSeek V4 Pro (80.6%) edges out Qwen3-Coder-480B (69.6%) and adds native 1M context.

### Grok Code Fast 1 vs. SWE-1 (Budget Agentic Coding)

Both target the budget-conscious agentic coding segment at low cost. Grok Code Fast 1 at $0.20/$1.50 per million tokens is accessible via any OpenAI-compatible client; SWE-1 models are free within Windsurf but locked to that IDE. Grok Code Fast 1 at 70.8% SWE-bench Verified slightly edges SWE-1.5 on raw accuracy benchmarks, but SWE-1.6 at 950 tok/s and purpose-built flow awareness is a better experience inside the Windsurf IDE. Choose Grok Code Fast 1 if you want tool-agnostic cheap agentic coding across Cursor, Cline, etc.; choose SWE-1.6 if you're willing to commit to Windsurf.

### Llama 4 Maverick vs. Hunyuan Hy3 (Open-Weight Mid-Tier)

Hy3 preview significantly outperforms Llama 4 Maverick on coding benchmarks: 74.4% SWE-bench Verified vs. Llama 4's ~43% LiveCodeBench (SWE-bench not officially reported for Llama 4). Both are open-weight; Hy3 requires ~4x A100 80GB for clean BF16 inference while Llama 4 Maverick fits on a single A100 80GB at Q8. Llama 4's key strength is its ecosystem: Ollama, vLLM, llama.cpp all support it natively, and it has the largest open-weight fine-tuning community. Hy3's key strength is raw coding performance and Chinese-language capability. For coding-first self-hosting in English, Hy3 wins on performance; Llama wins on ecosystem and approachability.

### DeepSeek R1 vs. OpenAI o3 (Reasoning Models for Coding)

DeepSeek R1 at 71B MoE (37B active) matches o1 on AIME math and competitive programming, is MIT licensed, and self-hostable (at cluster scale). Its R1-0528 update (87.5% AIME 2025) further narrows the gap with o3 (which achieves 71.7% SWE-bench). R1's weaknesses: political censorship on the API version, documented weak safety guardrails, and high reasoning-token cost. o3 is safer, better integrated into the OpenAI ecosystem, and has more predictable behavior. At $2/$8 per million tokens (post-March 2026 price cut), o3 is now competitively priced against R1's API. For open/self-hosted reasoning use, R1 (or R1 distills) is the answer; for production API reasoning, o3 is preferable.

---

## 6. Self-Hosting Guide

### Which Models Can Be Self-Hosted

| Model | License | Weights Available | Minimum Practical Setup |
|---|---|---|---|
| DeepSeek V4 Flash (284B) | MIT | Yes (HuggingFace) | 2x A100 80GB (~158GB FP4+FP8) |
| DeepSeek V4 Pro (1.6T) | MIT | Yes (HuggingFace) | 8x H100 80GB (NVLink) |
| DeepSeek V3.2 (671B) | MIT | Yes | 8x A100 80GB (Q4 + CPU offload) |
| DeepSeek R1 (671B) | MIT | Yes | 8x A100 80GB (same as V3) |
| DeepSeek R1 Distill 7B–70B | MIT | Yes | RTX 3060 12GB (7B, Q4) to 2x RTX 3090 (70B, Q4) |
| Qwen2.5-Coder-32B | Apache 2.0 | Yes | RTX 4090 24GB (Q4) |
| Qwen3-Coder-30B-A3B | Apache 2.0 | Yes | RTX 4090 24GB (Q4) |
| Qwen3-Coder-Next (80B/3B active) | Apache 2.0 | Yes | RTX 5090 32GB + 64GB DDR5 RAM (Q4) |
| Qwen3-Coder-480B-A35B | Apache 2.0 | Yes | ~12x RTX 4090 (Q4) or 3x RTX 6000 96GB |
| Llama 3.3 70B | Meta Community | Yes | 2x RTX 3090 (Q4) |
| Llama 4 Scout (109B/17B active) | Meta Community | Yes | Single H100 (FP16) or RTX 4090 (Q4) |
| Llama 4 Maverick (400B/17B active) | Meta Community | Yes | 4x H100 recommended; RTX 4090 at Q4 (tight) |
| Hunyuan-Large (389B/52B active) | Tencent Hy | Yes | 8x H20 (FP8) or 16x H20 (BF16) |
| Hy3 preview (295B/21B active) | Tencent Hy | Yes | 4x A100 80GB recommended; ~$10–16/day |

Not self-hostable: Claude, GPT (flagship), Gemini, Grok, SWE-1.

Note: Meta Llama Community License restricts commercial use above 700M MAU and prohibits EU deployment of Llama 4 multimodal variants.

### Recommended Inference Stacks

- **Ollama**: Simplest for local use. Supports all Llama variants, Qwen2.5-Coder, DeepSeek R1 distills, Qwen3-Coder. One-command setup. Best for individual developers.
- **vLLM**: Production multi-GPU serving. Full support for Qwen3-Coder (with updated parsers), Llama 4, DeepSeek V3/R1, Hunyuan-Large. Preferred for team deployments.
- **SGLang**: Optimized for DeepSeek MoE inference, lower TTFT. Day-0 support for Hy3.
- **llama.cpp**: CPU/quantized inference, cross-platform. Slowest but most portable.
- **LM Studio**: GUI-based local inference for individuals. Good for Qwen2.5-Coder and Llama 3.x.

### Quality Tradeoffs at Quantization Levels

| Quantization | Quality vs. FP16 | Notes |
|---|---|---|
| Q8 | Near-lossless | Preferred when VRAM allows |
| Q4_K_M | Small degradation on general tasks; acceptable for code | Practical floor for most use |
| Q3 | Noticeable degradation | Acceptable only for edge/resource-constrained use |
| Q2 | Significant degradation | Code tasks degrade faster; increased syntax errors |

For code-specific tasks, quality degrades faster below Q4 than for general language tasks. Q4_K_M is the minimum recommended quantization for coding workloads.

### Hardware Cost Reference (US Cloud Pricing)

| GPU | VRAM | On-Demand (est.) | Notes |
|---|---|---|---|
| RTX 4090 | 24GB | ~$0.40–0.60/hr (Lambda) | Single-GPU max for consumer models |
| A100 80GB | 80GB | ~$2.50/hr | Standard production GPU |
| H100 80GB | 80GB | ~$3.50–4.00/hr | Fastest H100 variant |
| H200 141GB | 141GB | ~$5.00/hr | Fits DeepSeek V4 Flash alone |

For DeepSeek V4 Pro at 8x H100: ~$28–32/hr cloud cost. Self-owned H100 cluster amortizes in ~18 months at this usage rate vs. DeepSeek API.

---

## 7. What to Pick

**Claude Opus 4.7**: Use when you need the highest SWE-bench accuracy for complex agentic coding, work in the Claude Code / Cursor ecosystem, and cost is secondary to quality. Best for complex multi-file refactors and long-output generation.

**Claude Sonnet 4.6**: Use as the daily driver for professional coding — balanced speed, cost ($3/$15/M), and 79.6% SWE-bench. Default for Claude Code CLI. Best when you want frontier-class coding without Opus pricing.

**Claude Haiku 4.5**: Use for high-volume, low-latency tasks (autocomplete, quick fixes, CI/CD helpers). At $1/$5/M and 97 tok/s, it offers 73.3% SWE-bench at budget pricing.

**GPT-5.5**: Use when working in the OpenAI/GitHub Copilot/Codex CLI ecosystem, or when you need the absolute highest benchmark score and OpenAI's tool-calling ecosystem.

**GPT-5.3-Codex**: Use for long-horizon agentic coding with OpenAI's Codex platform — purpose-built for PR creation, multi-hour loops, and project-scale refactors.

**o3**: Use for hard algorithmic problems, competitive programming, and math-heavy engineering tasks where extra reasoning time is acceptable. Not for interactive autocomplete.

**Gemini 3 Flash**: Use when cost and speed matter as much as accuracy — 78% SWE-bench at $0.50/$3.00/M and 183 tok/s. Best value among proprietary frontier models.

**Gemini 3.1 Pro**: Use for multimodal coding tasks (screenshot to code, video walkthrough analysis), Google Cloud ecosystem integration, or when you want competitive SWE-bench at lower price than Claude Opus.

**DeepSeek V4 Pro**: Use when you want near-frontier coding performance (80.6% SWE-bench) at dramatically lower cost — especially via API for non-China-sensitive workflows. Also use for competitive programming (Codeforces 3206) and hard math.

**DeepSeek R1 / Distills**: Use for math-intensive tasks, algorithm design, and reasoning-heavy debugging where chain-of-thought helps. Distills (7B–70B) enable reasoning-class performance on consumer hardware.

**Grok Code Fast 1**: Use for cost-sensitive agentic coding in Cursor, Cline, or other OpenAI-compatible tools. At $0.20/$1.50/M with 70.8% SWE-bench, it's the cheapest proprietary model near the 70% threshold.

**Hunyuan Hy3 preview**: Use for Chinese-language codebases, Tencent Cloud / WeChat integration, or when you want an open-weight model with 74.4% SWE-bench self-hostable on 4x A100 80GB.

**Llama 4 Scout**: Use when you need an open-weight model deployable on a single H100 with extreme context (10M tokens for instruct). Best for long-document and retrieval tasks; coding performance is mid-tier.

**Llama 3.3 70B**: Use as the fine-tuning base for custom coding models. The ecosystem (Ollama, vLLM, llama.cpp, Unsloth, LlamaFactory) is the most mature of any open-weight model. At Q4 on dual RTX 3090, it's a practical workhorse.

**Qwen2.5-Coder-32B**: Use for self-hosted code completion on a single RTX 4090 (24GB). Best open-weight model for IDE autocomplete and repo-level completion (SOTA on CrossCodeEval). Practical floor for serious self-hosted coding.

**Qwen3-Coder-Next**: Use when you want near-frontier agentic coding (71% SWE-bench) self-hosted on a single RTX 5090 with only 3B active parameters. Best open-weight model per watt at its tier. Requires updated vLLM/SGLang for tool calls.

**Qwen3-Coder-480B**: Use for maximum open-weight agentic coding capability (69.6% SWE-bench) when you have cluster infrastructure. Via OpenRouter at $0.22/$1.80/M, it's a strong API option before committing to self-hosting.

**SWE-1.6**: Use when you're committed to the Windsurf IDE and want the fastest agentic experience (950 tok/s) at zero credit cost within your subscription. Best for iteration-speed-sensitive workflows where accuracy can be slightly below frontier.
