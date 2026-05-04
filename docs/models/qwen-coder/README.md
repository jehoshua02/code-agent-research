# Qwen Coder

## What It Is

The Qwen Coder family is a series of code-specialized large language models developed by Alibaba's Qwen team. It spans two major generations:

**Qwen2.5-Coder** (released November 2024): Dense models ranging from 0.5B to 32B parameters, pretrained on 5.5 trillion tokens with a heavy code focus. Built on the Qwen2.5 architecture. Most variants are Apache 2.0 licensed (3B is Qwen Research license only). These are the current self-hosting workhorses.

**Qwen3-Coder** (released 2025–2026): Mixture-of-Experts (MoE) models targeting agentic software engineering at scale. Includes three distinct models: Qwen3-Coder-480B-A35B (flagship, July 2025), Qwen3-Coder-30B-A3B (mid-tier, July 2025), and Qwen3-Coder-Next (efficiency-focused, February 2026). All Apache 2.0 licensed. Trained with long-horizon reinforcement learning (Agent RL) on 20,000 parallel cloud environments. Designed for multi-turn tool use, repository-scale reasoning, and CLI/IDE agent integration.

Alibaba also released **Qwen Code**, an open-source CLI agent (forked from Gemini CLI) purpose-built for Qwen3-Coder, comparable to Claude Code in function.

## Variants

### Qwen2.5-Coder

| Model | Params | Context | License |
|---|---|---|---|
| Qwen2.5-Coder-0.5B | 0.49B | 32K | Apache 2.0 |
| Qwen2.5-Coder-1.5B | 1.54B | 32K | Apache 2.0 |
| Qwen2.5-Coder-3B | 3.09B | 32K | Qwen Research |
| Qwen2.5-Coder-7B | 7.61B | 128K | Apache 2.0 |
| Qwen2.5-Coder-14B | 14.7B | 128K | Apache 2.0 |
| Qwen2.5-Coder-32B | 32.5B | 128K | Apache 2.0 |

Each size ships in both base and instruct variants. The 32B-Instruct is the primary self-hosting choice for serious coding work, competitive with GPT-4o on multiple benchmarks at the time of release.

### Qwen3-Coder

| Model | Total / Active Params | Experts | Context | Released |
|---|---|---|---|---|
| Qwen3-Coder-30B-A3B | 30.5B / 3.3B | 128 (8 active) | 256K | Jul 2025 |
| Qwen3-Coder-480B-A35B | 480B / 35B | 160 (8 active) | 256K | Jul 2025 |
| Qwen3-Coder-Next | 80B / 3B | 512 (10 active) | 256K | Feb 2026 |

Quantized variants (FP8) are available for 480B and Coder-Next on Hugging Face. GGUF variants available via Unsloth.

**Qwen3-Coder-Next** uses a novel hybrid architecture (Gated DeltaNet + Gated Attention + MoE), a fundamentally different design from standard transformer MoE. 48 layers; 12 blocks of pattern `(3 x DeltaNet-MoE → 1 x Attention-MoE)`. Only 3B parameters active per token while achieving competitive results with much larger models.

**Qwen3-Coder-480B-A35B** is the maximum capability open model. Context extendable to 1M tokens via YaRN. Non-thinking mode only (no `<think>` blocks).

All Qwen3-Coder models support 358 programming languages and are non-thinking (inference-time reasoning is not built in, unlike Qwen3 base).

## Pricing

### Qwen2.5-Coder (Alibaba Cloud / DashScope, Chinese Mainland)

| Model | Input ($/1M) | Output ($/1M) |
|---|---|---|
| qwen2.5-coder-7b | $0.144 | $0.287 |
| qwen2.5-coder-14b | $0.287 | $0.861 |
| qwen2.5-coder-32b | $0.287 | $0.861 |
| qwen2.5-coder-3b | Free (limited time) | Free |
| qwen2.5-coder-0.5b / 1.5b | Free (limited time) | Free |

### Qwen3-Coder (Alibaba Cloud, International/Singapore — tiered by context length)

**qwen3-coder-plus** (maps to 480B-A35B):

| Context Tier | Input ($/1M) | Output ($/1M) |
|---|---|---|
| 0–32K tokens | $1.00 | $5.00 |
| 32K–128K tokens | $1.80 | $9.00 |
| 128K–256K tokens | $3.00 | $15.00 |
| 256K–1M tokens | $6.00 | $60.00 |

**qwen3-coder-flash** (maps to 30B-A3B):

| Context Tier | Input ($/1M) | Output ($/1M) |
|---|---|---|
| 0–32K tokens | $0.30 | $1.50 |
| 32K–128K tokens | $0.50 | $2.50 |
| 128K–256K tokens | $0.80 | $4.00 |
| 256K–1M tokens | $1.60 | $9.60 |

### Qwen3-Coder (OpenRouter — third-party pricing)

| Model | Input ($/1M) | Output ($/1M) |
|---|---|---|
| Qwen3-Coder-480B-A35B | $0.22 | $1.80 |
| Qwen3-Coder-480B-A35B (free tier) | $0.00 | $0.00 |
| Qwen3-Coder-30B-A3B | $0.07 | $0.27 |
| Qwen3-Coder-Next | $0.12 | $0.80 |

All models are open-weight and can be self-hosted at compute cost only.

## Context Window

| Model Family | Native | Extended |
|---|---|---|
| Qwen2.5-Coder 0.5B–3B | 32K | — |
| Qwen2.5-Coder 7B–32B | 128K | — |
| Qwen3-Coder (all variants) | 256K (262,144 tokens) | 1M via YaRN |

Qwen3-Coder's 256K native context covers approximately 393 A4 pages or a large monorepo. The 1M YaRN extension is available but comes with quality caveats at extreme lengths. "Lost in the middle" degradation is present at very large context depths, consistent with current transformer limitations.

## Benchmarks

### Qwen2.5-Coder-32B-Instruct

| Benchmark | Score | Notes |
|---|---|---|
| Aider | 73.7 | Comparable to GPT-4o |
| McEval | 65.9 | Best open-source; 40+ languages |
| MdEval | 75.2 | Best open-source; multi-language repair |
| HumanEval | 92.7 | Code generation pass@1 |
| MBPP | 90.2 | Code generation pass@1 |
| Humaneval-Infilling | SOTA | Code completion |
| CrossCodeEval | SOTA | Repository-level completion |
| EvalPlus, LiveCodeBench, BigCodeBench | Best open-source at release | Outperformed DS-Coder-33B |

### Qwen3-Coder-480B-A35B-Instruct

| Benchmark | Score | Notes |
|---|---|---|
| SWE-Bench Verified | 69.6% | Best open-source at release |
| SWE-Bench Pro | 38.7% | — |
| TerminalBench 2.0 | 23.9% | — |
| EvasionBench | 78.16% | — |

Claimed comparable to Claude Sonnet 4 on agentic coding tasks at release.

### Qwen3-Coder-Next (80B total / 3B active)

| Benchmark | Score | Notes |
|---|---|---|
| SWE-Bench Verified (SWE-Agent) | 70.6% | Surpasses 480B on this scaffold |
| SWE-Bench Verified (MiniSWE-Agent) | 71.1% | — |
| SWE-Bench Verified (OpenHands) | 71.3% | — |
| SWE-Bench Pro | 44.3% | Above DeepSeek-V3.2 (40.9%) |
| SWE-Bench Multilingual | 62.8% | Near DeepSeek-V3.2 (62.3%) |
| TerminalBench 2.0 | 34.2–36.2% | — |
| EvalPlus | 86.56% | — |
| CRUXEval | 95.88% | — |
| Codeforces | 2100 rating | Competitive programming |
| MMLU | 87.73% | General knowledge |
| GPQA | 74.49% | Graduate-level science |

Qwen3-Coder-Next (3B active) outperforms models with 10–20x more active parameters on SWE-Bench. At release, frontier closed models were: Claude 4 ~77.2%, GPT-5 ~74.9%, Gemini 2.5 ~73.1%. Claude Opus 4.5 scored 80.9%.

Tool calling robustness: 92.7% accuracy across 5 IDE/CLI scaffolds tested on 21 distinct tool chat templates (versus competitors at 49.3%–93.7%).

## Hardware Requirements

### Qwen2.5-Coder

| Model | Q4 VRAM | Q8 VRAM | FP16 VRAM | Min GPU |
|---|---|---|---|---|
| 0.5B | ~0.5GB | ~0.7GB | ~1GB | Any modern GPU |
| 1.5B | ~1.2GB | ~2GB | ~3GB | RTX 3060 8GB |
| 3B | ~2.5GB | ~4GB | ~6GB | RTX 3060 8GB |
| 7B | ~4.2GB | ~7–8GB | ~14–17GB | RTX 3060 12GB (Q4) |
| 14B | ~9GB | ~15GB | ~28GB | RTX 3090 (Q4) |
| 32B | ~20GB | ~34GB | ~64GB | RTX 3090/4090 (Q4), dual-GPU (FP16) |

The 32B Q4_K_M model fits on a single 24GB GPU (RTX 3090/4090) with ~4GB headroom for up to 16K context. Q4 is the minimum recommended for code tasks; below Q4 produces measurable syntax errors. Q8 on Mac M-series (48GB+) delivers near-FP16 quality.

Deployment: Ollama, vLLM, SGLang, LM Studio, llama.cpp all supported.

### Qwen3-Coder-480B-A35B

| Quantization | Model Size | Minimum Setup |
|---|---|---|
| FP16 | ~960GB | Cloud/enterprise cluster |
| FP8 | ~250GB | Multiple H100s |
| Q4_K_M | ~290GB | Mac Studio M4 512GB or 12–13x RTX 4090 |
| Q4_K_XL (Unsloth) | ~276GB | 12–13x RTX 3090/4090 or 3x RTX 6000 96GB |
| Q3_K_L | ~115GB | 24GB GPU + 128GB+ system RAM (MoE offload) |
| Q2_K_XL (Unsloth) | ~180GB | Mac M2 Ultra 192GB |

MoE offloading (via llama.cpp/KTransformers) allows running on a single 24GB GPU + 128GB RAM at ~5 tokens/sec with 4K context. Requires `transformers>=4.51.0`.

### Qwen3-Coder-Next (80B total / 3B active)

| Quantization | Model Size | Setup | Speed |
|---|---|---|---|
| IQ2_XXS | ~22.3GB | 24GB GPU + 64GB RAM | Noticeable degradation |
| IQ3_M | ~34.8GB | 32GB GPU + 32GB RAM | Slight dip vs Q4 |
| Q4_K_M | ~48.2GB | RTX 5090 + 64GB DDR5 RAM | 38–48 tok/s — recommended |
| Q8_0 | ~80.1GB | RTX PRO 6000 96GB | 52–64 tok/s, identical to BF16 |

The RTX 5090 (32GB, ~$2,000) + 64GB DDR5 is the sweet spot for local deployment. RTX PRO 5000 72GB (~$5,500) runs full Q4_K_M without offload at 45–55 tok/s. MoE sparse activation means idle experts can be paged to system RAM, making the 80B total size more tractable than it appears.

Deployment frameworks: SGLang v0.5.8+, vLLM v0.15.0+, Ollama, LM Studio, MLX-LM, llama.cpp, KTransformers.

### Qwen3-Coder-30B-A3B

Single RTX 4090 (24GB) is viable at Q4. ~18–22GB at Q4_K_M with 3.3B active parameters.

## Supported Tools

**Official / first-party:**
- **Qwen Code** — Alibaba's open-source CLI agent (forked from Gemini CLI), purpose-built for Qwen3-Coder with custom tool parsers and function-calling protocol. Comparable to Claude Code in scope.
- **SGLang** and **vLLM** — primary serving backends with native support for Qwen3-Coder's custom function-call format (requires updated tool parsers in both).

**Third-party integrations:**
- **Cline** (VS Code extension) — documented first-class integration via OpenAI-compatible API
- **Claude Code** — usable via OpenAI-compatible proxy/router pointing to local or hosted Qwen3-Coder endpoint
- **Cursor**, **Copilot**, **OpenCode**, **Gemini CLI** — accessible via API routing tools (e.g., 9router, OpenRouter)
- **Ollama** — official library support (`ollama pull qwen3-coder`, `ollama pull qwen2.5-coder`)
- **LM Studio** — official support for all GGUF variants
- **MLX-LM** — Apple Silicon inference

Qwen3-Coder ships a "specially designed function call format." Tool calling requires SGLang or vLLM with updated parsers; older versions fail. For Qwen2.5-Coder, standard OpenAI function-call format applies.

## Strengths

- **Efficiency at scale**: Qwen3-Coder-Next achieves frontier-competitive SWE-Bench scores (70–71%) with only 3B active parameters. Dramatically lower inference cost than parameter-equivalent dense models.
- **Agentic tool-use robustness**: 92.7% tool-call accuracy across 21 distinct scaffolds — engineered for real CLI/IDE agent workflows, not just benchmark prompts. Trained with long-horizon RL on real software engineering tasks.
- **Open weights + permissive licensing**: All Qwen3-Coder models and most Qwen2.5-Coder models are Apache 2.0 — commercially usable, fully self-hostable, no usage restrictions.
- **Broad language coverage**: 358 coding languages supported (Qwen3-Coder); 40+ languages on multi-language benchmarks (Qwen2.5-Coder McEval/MdEval SOTA).
- **Flexible size ladder**: 0.5B to 480B with consistent API, enabling edge deployment through to enterprise scale from one model family.
- **Long context**: 256K native (Qwen3-Coder), extendable to 1M via YaRN — sufficient for large repository ingestion.
- **Strong code completion**: Qwen2.5-Coder achieved SOTA on Humaneval-Infilling, CrossCodeEval, CrossCodeLongEval, RepoEval, SAFIM — specifically relevant for IDE autocomplete use cases.
- **Self-hosting on consumer hardware**: Qwen2.5-Coder-32B at Q4 fits a single RTX 4090 (24GB). Qwen3-Coder-Next Q4_K_M runs on a single RTX 5090 at interactive speeds.

## Weaknesses

- **Non-thinking mode only**: Qwen3-Coder models do not support chain-of-thought `<think>` blocks unlike Qwen3 base models. This limits performance on problems that benefit from extended reasoning.
- **Below frontier closed models**: On SWE-Bench Verified, Qwen3-Coder-Next tops at ~71% versus Claude 4 ~77%, GPT-5 ~74%, Claude Opus 4.5 ~81%. The gap matters for the hardest agentic tasks.
- **Self-hosting 480B is expensive**: The flagship model requires substantial infrastructure (250GB+ VRAM at FP8) that is out of reach for most teams without cloud compute. Single-GPU 480B inference is extremely slow (~5 tok/s).
- **Custom tool-call format requires updated frameworks**: Qwen3-Coder's function-calling breaks with older versions of vLLM/SGLang. Integration into arbitrary OpenAI-compatible pipelines requires verification.
- **Context quality degradation**: "Lost in the middle" issues at extreme context lengths (approaching 256K) are present, consistent with industry-wide limitations. Quality at 1M via YaRN is unverified for production.
- **Quantization sensitivity for code**: Below Q4 (e.g., Q2/Q3), code-specific tasks degrade faster than general language tasks — increased syntax errors and logic failures. Q4 is the practical floor.
- **Qwen2.5-Coder behind 2025/2026 frontier**: As of early 2026, Qwen2.5-Coder-32B is a solid baseline but clearly below Qwen3-Coder and frontier closed models on agentic benchmarks.
- **Security/alignment**: Related Qwen2.5 family models have documented jailbreak vulnerabilities (e.g., "Grandma jailbreak"). Code models in particular should be deployed with output sandboxing in agent contexts.
- **English-centric training**: Aggressive quantization compounds quality gaps in non-English codebases.

## Sources

- [Qwen2.5-Coder Series Blog](https://qwenlm.github.io/blog/qwen2.5-coder-family/) — official model announcement with benchmark details
- [Qwen2.5-Coder Technical Report (arXiv:2409.12186)](https://arxiv.org/abs/2409.12186) — full technical paper
- [Qwen3-Coder Blog (480B-A35B)](https://qwenlm.github.io/blog/qwen3-coder/) — official 480B announcement
- [Qwen3-Coder-Next Blog](https://qwen.ai/blog?id=qwen3-coder-next) — official Coder-Next announcement
- [Qwen3-Coder-Next Technical Report (arXiv:2603.00729)](https://arxiv.org/html/2603.00729v1) — full technical paper
- [Qwen3 Technical Report (arXiv:2505.09388)](https://arxiv.org/pdf/2505.09388) — Qwen3 base model paper
- [QwenLM/Qwen3-Coder GitHub](https://github.com/QwenLM/Qwen3-Coder) — model variants, deployment guides
- [Qwen/Qwen3-Coder-480B-A35B-Instruct (Hugging Face)](https://huggingface.co/Qwen/Qwen3-Coder-480B-A35B-Instruct) — model card and architecture
- [Qwen/Qwen3-Coder-Next (Hugging Face)](https://huggingface.co/Qwen/Qwen3-Coder-Next) — model card
- [Alibaba Cloud Model Studio Pricing](https://www.alibabacloud.com/help/en/model-studio/model-pricing) — official API pricing
- [OpenRouter: Qwen3-Coder-480B](https://openrouter.ai/qwen/qwen3-coder) — third-party pricing and providers
- [OpenRouter: Qwen3-Coder-Next](https://openrouter.ai/qwen/qwen3-coder-next) — third-party pricing
- [Artificial Analysis: Qwen3-Coder-480B](https://artificialanalysis.ai/models/qwen3-coder-480b-a35b-instruct) — independent performance analysis
- [Qwen3-Coder-Next Hardware Guide (Compute Market)](https://www.compute-market.com/blog/qwen-3-coder-next-local-hardware-guide-2026) — VRAM requirements
- [Qwen3-Coder-480B VRAM Guide (Novita)](https://blogs.novita.ai/qwen3-coder-480b-a35b-vram-how-much-memory-do-you-need/) — VRAM requirements
- [Qwen2.5-Coder-32B Hardware Guide (CraftRigs)](https://craftrigs.com/guides/qwen-2-5-coder-32b-hardware-guide/) — VRAM requirements
- [Qwen2.5-Coder-7B VRAM (RunAIatHome)](https://www.runaiathome.com/model/qwen2.5-coder-7b/) — 7B VRAM requirements
- [Ollama Qwen3-Coder](https://ollama.com/library/qwen3-coder) — Ollama library listing
- [Unsloth Qwen3-Coder-Next GGUF](https://huggingface.co/unsloth/Qwen3-Coder-Next-GGUF) — quantized GGUF variants
