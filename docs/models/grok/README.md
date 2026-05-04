# Grok (xAI)

## What It Is

Grok is a family of large language models developed by xAI, Elon Musk's AI company. The family spans general-purpose frontier models (Grok-3 and successors) and a dedicated agentic coding model (Grok Code Fast 1). All models are proprietary and API-only; no open weights are released for Grok-3 or later. xAI trained Grok-3 on the Colossus supercomputer in Memphis using approximately 200,000 NVIDIA H100 GPUs — roughly 200 million GPU-hours of compute, 10x more than Grok-2.

Grok-3 was released February 19, 2025. Grok Code Fast 1 was released August 26–28, 2025 as xAI's first purpose-built agentic coding model, developed with a new architecture separate from the Grok-4 lineage.

## Variants

| Model | Type | Parameters | Use Case |
|---|---|---|---|
| Grok-3 | Dense | Undisclosed | General-purpose flagship |
| Grok-3 Mini | Dense (small) | Undisclosed | Budget reasoning, math |
| Grok-3 (Think) | Grok-3 + extended reasoning | Undisclosed | Hard reasoning, coding, math |
| Grok Code Fast 1 | MoE reasoning | ~314B (estimated) | Agentic coding, tool use |

**Grok-3** is the baseline flagship. **Grok-3 Mini** is the cheaper fast variant — surprisingly competitive on math benchmarks. **Grok-3 Think** applies extended test-time compute to Grok-3 for harder tasks. **Grok Code Fast 1** is a purpose-built coding model with a new pretraining corpus heavy on programming content and posttraining focused on real-world pull requests. It uses a mixture-of-experts architecture and exposes visible reasoning traces.

Note: Grok-4 and later variants (Grok-4 Fast, Grok-4.1 Fast, Grok-4.3) now represent xAI's frontier line. Grok-3 remains available but is no longer xAI's primary focus.

## Pricing

All prices are per million tokens via the xAI API.

| Model | Input | Output | Cached Input |
|---|---|---|---|
| Grok-3 | $3.00 | $15.00 | $0.75 |
| Grok-3 Mini | $0.30 | $0.50 | — |
| Grok Code Fast 1 | $0.20 | $1.50 | $0.02 |

Grok Code Fast 1 was available for free at launch through partner platforms. There is no open self-hosted option; all inference is through xAI's API.

## Context Window

| Model | Context Window | Notes |
|---|---|---|
| Grok-3 | 131,072 tokens (API) | xAI marketed 1M at launch; actual API limit is 131k |
| Grok-3 Mini | 131,072 tokens | Same as Grok-3 |
| Grok Code Fast 1 | 256,000 tokens | Max completion: 40,000 tokens |

The 1 million token claim for Grok-3 was a marketing figure. Official xAI API documentation and third-party evaluators confirm the enforced limit at 131,072 tokens. Grok Code Fast 1's 256k window is practical for large codebases.

## Benchmarks

### Grok-3 (released February 2025)

| Benchmark | Score | Model variant |
|---|---|---|
| AIME 2025 | 93.3% | Grok-3 Think (cons@64) |
| GPQA Diamond | 84.6% | Grok-3 Think |
| MATH | 94.4% | Grok-3 |
| HumanEval | 94.5% | Grok-3 |
| LiveCodeBench | 79.4% | Grok-3 Think |
| LiveCodeBench | 80.4% | Grok-3 Mini |
| LMArena (Chatbot Arena) | 1400+ ELO | Grok-3 (first model to break 1400) |

Grok-3 placed first on Chatbot Arena across overall, coding, math, and hard prompt categories at release. However, TechCrunch and independent reviewers questioned whether benchmark conditions matched those of competitors. Early user reports noted Grok-3 struggled with "somewhat complex coding" relative to GPT-4o and Claude 3.5 — suggesting benchmark scores may not fully predict real-world developer experience.

### Grok Code Fast 1 (released August 2025)

| Benchmark | Score | Notes |
|---|---|---|
| SWE-Bench Verified | 70.8% | xAI internal harness; full subset |
| LiveCodeBench | 65.7% | Third-party evaluation |
| GPQA Diamond | 72.7% | |
| MMLU Pro | 79.3% | |
| Artificial Analysis Intelligence Index | 29 | Above average among reasoning models in its price tier |
| Agentic Index | 46.6 | Strongest performance area |

SWE-Bench Verified at 70.8% is notable for a fast/cheap model. For reference, Claude Opus 4 scored ~72.5% and Opus 4.1 ~74.5% on the same benchmark. Grok Code Fast 1 sits competitively below frontier-tier models at a fraction of the cost.

Independent coding evaluation (16x.engineer) gave it a 7.64 average across tasks. It ranked second among open/proprietary alternatives when excluding Grok-4 and Claude Opus 4, outperforming Qwen3 Coder and Kimi K2.

## Hardware Requirements

Grok models are API-only and proprietary. xAI does not publish model weights. There are no self-hosted deployment options, no VRAM requirements, no Ollama or vLLM compatibility.

xAI's own inference infrastructure runs on NVIDIA H100 clusters (Colossus). End users need only an internet connection and an xAI API key.

## Supported Tools

### Grok Code Fast 1 — Official Launch Partners

At launch, Grok Code Fast 1 was made available for free (for a limited time) on the following platforms:

- **GitHub Copilot**
- **Cursor**
- **Cline** (VS Code plugin)
- **Windsurf**
- **Roo Code**
- **Kilo Code**
- **opencode**

xAI published integration docs for Cursor and Cline, requiring users to set the base URL to `https://api.x.ai/v1` and supply an xAI API key. The model ID is `grok-code-fast-1`.

### API Compatibility

The xAI API is OpenAI-compatible. Grok models work with the OpenAI SDK, Anthropic SDK, OpenRouter, and any OpenAI-compatible client.

### Grok-3 in Coding Tools

Grok-3 is accessible in Cursor, Cline, and any OpenAI-compatible coding tool via the xAI API. Grok-3 does not have native integrations in Copilot or Windsurf.

## Strengths

**Grok-3:**
- First model to break 1400 ELO on Chatbot Arena at release, winning all categories including coding
- Strong math and reasoning (AIME 2025: 93.3%, MATH: 94.4%)
- Competitive HumanEval and LiveCodeBench via Think variant
- Real-time web access in the Grok chatbot (X platform)
- Grok-3 Mini provides strong math at very low cost ($0.30/$0.50 per million)

**Grok Code Fast 1:**
- Purpose-built for agentic coding workflows — pretraining and posttraining on real pull requests
- SWE-Bench Verified 70.8% at $0.20/M input — exceptional price-to-performance ratio
- 256k context window suitable for large codebases
- Visible reasoning traces let developers follow and interrupt tool calls
- ~115 tokens/second throughput (above average for reasoning models)
- Prompt caching with >90% hit rates in partner workflows ($0.02/M cached)
- Proficient in TypeScript, Python, Java, Rust, C++, Go
- Optimized for tool use: grep, file editing, terminal operations
- Available in every major coding IDE/agent platform at launch

## Weaknesses

**Grok-3:**
- Context window is effectively 131k despite 1M marketing claims
- Real-world coding performance lagged behind GPT-4o and Claude 3.5 per early user reports, even with strong benchmark numbers
- Benchmark controversy: TechCrunch reported questions about whether xAI's benchmark conditions were equivalent to competitors'
- No self-hosted option; API-only
- Knowledge cutoff: November 2024
- Hallucination issues including fabricating URLs reported in early reviews

**Grok Code Fast 1:**
- No multimodal support — text only, no image input
- Reasoning overhead causes high time-to-first-token (7.09s) — unsuitable for interactive/chat workflows requiring instant responses
- Significantly verbose: generates ~66M tokens per evaluation run vs. a median of 26M, increasing costs
- Failed badly on Tailwind CSS v3 task (1/10) — suspected training gap for newer CSS frameworks
- Tends to over-grep (scans too many files before narrowing scope)
- Struggles with complex architecture documentation and theoretical CS questions
- Occasional API errors reported in Cline ("Unexpected API Response")
- Scores below Grok-4 and Claude Opus 4 on general coding quality
- Not suitable for synchronous, fast-feedback IDE chat (better for async agent loops)

## Sources

- [xAI Grok Code Fast 1 announcement](https://x.ai/news/grok-code-fast-1)
- [xAI Grok-3 Beta announcement](https://x.ai/news/grok-3)
- [xAI Models and Pricing documentation](https://docs.x.ai/developers/models)
- [xAI Use with Code Editors documentation](https://docs.x.ai/developers/advanced-api-usage/use-with-code-editors)
- [Grok Code Fast 1 — Artificial Analysis](https://artificialanalysis.ai/models/grok-code-fast-1)
- [Grok-3 — Artificial Analysis](https://artificialanalysis.ai/models/grok-3)
- [Grok Code Fast 1 coding evaluation — 16x.engineer](https://eval.16x.engineer/blog/grok-code-fast-1-coding-evaluation-results)
- [Grok Code Fast 1 — InfoQ](https://www.infoq.com/news/2025/09/xai-grok-fast1/)
- [Grok Code Fast 1 — OpenRouter](https://openrouter.ai/x-ai/grok-code-fast-1)
- [Grok Code Fast 1 review — Barnacle Goose / Medium](https://medium.com/@leucopsis/grok-code-fast-1-review-a-fast-low-cost-coder-for-agentic-work-6ef638b25c2e)
- [Grok-3 benchmark comparison — Helicone](https://www.helicone.ai/blog/grok-3-benchmark-comparison)
- [xAI Grok API pricing — mem0.ai](https://mem0.ai/blog/xai-grok-api-pricing)
- [Grok-3 model specs — Galaxy.ai](https://blog.galaxy.ai/model/grok-3)
- [Grok Code Fast 1 design analysis — Design for Online](https://designforonline.com/ai-models/xai-grok-code-fast-1/)
- [Grok Code Fast 1 — Grokipedia](https://grokipedia.com/page/Grok_Code_Fast_1)
- [Did xAI lie about Grok-3 benchmarks? — TechCrunch](https://techcrunch.com/2025/02/22/did-xai-lie-about-grok-3s-benchmarks/)
- [Colossus supercomputer — xAI](https://x.ai/colossus)
- [xAI on X — Grok Code Fast 1 launch partners](https://x.com/xai/status/1961129789944627207)
- [Grok context window — Data Studios](https://www.datastudios.org/post/grok-context-window-token-limits-memory-policy-and-2025-rules)
- [Grok Code Fast 1 — CodeGPT blog](https://www.codegpt.co/blog/xai-grok-models-comparison)
