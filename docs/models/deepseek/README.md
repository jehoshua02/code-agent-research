# DeepSeek

## What It Is

DeepSeek is a Chinese AI lab (DeepSeek-AI) that releases open-weight large language models with competitive frontier performance at dramatically lower cost than Western counterparts. The core model family covered here spans three product lines:

- **DeepSeek V3** — general-purpose instruction model, non-reasoning, fast and cheap.
- **DeepSeek R1** — reasoning model trained with reinforcement learning, comparable to OpenAI o1.
- **DeepSeek V4 Pro** — flagship MoE model released April 2026, 1.6T parameters, 1M context, hybrid reasoning modes.

All models are released under the MIT license (open-weight, commercial use allowed). Weights are publicly available on Hugging Face and ModelScope.

Version lineage of the V3/V4 series:
- **V3** (Dec 26, 2024) — original 671B MoE release.
- **V3-0324** (Mar 24, 2025) — improved post-training; AIME +19.8, LiveCodeBench +10.
- **V3.1** (Aug 21, 2025) — hybrid thinking/non-thinking mode; SWE-bench 66.0.
- **V3.2** (Dec 1, 2025) — further refinement; SWE-bench 77.2, LiveCodeBench 83.3%.
- **V4 Pro / V4 Flash** (Apr 24, 2026) — current generation; 1.6T / 284B parameters, 1M context.

R1 lineage:
- **R1** (Jan 20, 2025) — original 671B reasoning model.
- **R1-0528** (May 28, 2025) — AIME 2025 +17.5, GPQA +9.5, reduced hallucination.

## Variants

### DeepSeek V3 (671B MoE)
- **Architecture:** Mixture of Experts, 671B total / 37B active per token.
- **Training:** Pretrained on 14.8T tokens; 2.788M H800 GPU hours.
- **Key innovations:** Multi-head Latent Attention (MLA), auxiliary-loss-free load balancing, Multi-Token Prediction objective, FP8 mixed precision training.
- **Use case:** Fast, cost-efficient general coding and instruction following. The baseline for the V3.x series.

### DeepSeek V4 Flash (284B MoE)
- **Architecture:** MoE, 284B total; lighter sibling to V4 Pro.
- **Use case:** Lower-latency, lower-cost inference when V4 Pro is too expensive. Fits on a single H200 (141 GB) or 2x A100 80 GB in FP4+FP8 mixed (~158 GB).

### DeepSeek V4 Pro (1.6T MoE)
- **Architecture:** MoE, 1.6T total / 49B active per token. FP4 for MoE expert weights, FP8 for all other weights.
- **Hybrid attention:** Compressed Sparse Attention (CSA) + Heavily Compressed Attention (HCA); uses only 27% of V3.2 inference FLOPs per token; KV cache reduced to 10% of V3.2.
- **Reasoning modes:** Non-Think (fast), Think High (analytical), Think Max (maximum reasoning; requires ≥384K context).
- **Use case:** Complex software engineering, long-context agentic tasks, competitive programming.

### DeepSeek R1 (671B MoE)
- **Architecture:** Same MoE as V3 — 671B total / 37B active.
- **Training:** Reinforcement learning without supervised SFT as prerequisite (R1-Zero), then SFT + RL (R1). Extended chain-of-thought with self-verification and reflection.
- **Use case:** Math, reasoning, competitive coding, tasks that benefit from step-by-step thought.

### DeepSeek R1 Distilled Models
Smaller dense models distilled from R1 reasoning traces. Available on Ollama and Hugging Face.

| Model | Base | Size (disk) | Primary use |
|---|---|---|---|
| R1-Distill-Qwen-1.5B | Qwen-2.5 | ~1 GB | Edge / embedded |
| R1-Distill-Qwen-7B | Qwen-2.5 | ~4.7 GB | Single consumer GPU |
| R1-Distill-Qwen-14B | Qwen-2.5 | ~9 GB | Mid-range GPU |
| R1-Distill-Qwen-32B | Qwen-2.5 | ~20 GB | Single high-VRAM GPU |
| R1-Distill-Llama-8B | Llama 3.1 | ~5 GB | Single consumer GPU |
| R1-Distill-Llama-70B | Llama 3.3 | ~43 GB | Multi-GPU consumer setup |

## Pricing

All prices per 1M tokens at the DeepSeek API (deepseek.com). V4 Pro is currently at 75% discount until 2026-05-31.

| Model | Input (cache miss) | Input (cache hit) | Output |
|---|---|---|---|
| V4 Flash (deepseek-v4-flash) | $0.14 | $0.0028 | $0.28 |
| V4 Pro (deepseek-v4-pro) | $0.435 | $0.003625 | $0.87 |

Legacy V3 / R1 prices via third-party providers (OpenRouter, DeepInfra, etc.) typically range from $0.14–$0.55 input and $0.28–$2.19 output depending on model and provider. DeepSeek's own API is consistently 5–10x cheaper than comparable closed-source models (GPT-4o, Claude Sonnet).

For coding tool integrations using the API directly (via Continue / Cline in VS Code), community estimates put usage costs at roughly $2–5/month at 500 completions per day.

Self-hosted deployment eliminates per-token cost but requires significant upfront GPU infrastructure (see Hardware Requirements).

## Context Window

| Model | Native Context | Output Limit |
|---|---|---|
| V3 / V3.x series | 128K tokens | 8K tokens |
| R1 / R1-0528 | 128K tokens (671B); 128K (distills, except 70B at 160K) | 16K tokens |
| V4 Flash | 1M tokens | 384K tokens |
| V4 Pro | 1M tokens | 384K tokens |

V4 Pro Think Max mode requires a minimum context of 384K to operate at full reasoning depth. The 1M context is native — not extended via YaRN or sliding window.

DeepSeek V3 original achieves near-perfect retrieval on Needle in a Haystack across the full 128K window.

## Benchmarks

### Coding

| Benchmark | V3 (Dec 2024) | V3.2 (Dec 2025) | R1 | R1-0528 | V4 Pro |
|---|---|---|---|---|---|
| HumanEval (Pass@1) | 82.6% | ~95%+ | — | — | 76.8% (base) |
| LiveCodeBench (Pass@1) | 37.6% | 83.3% | 65.9% | — | 93.5% |
| Codeforces Rating | 51.6th pct | — | 2029 | — | 3206 |
| SWE-bench Verified | 42.0% | 77.2% | — | — | 80.6% |
| Terminal-Bench 2.0 | — | — | — | — | 67.9% |

### Reasoning & General

| Benchmark | V3 | R1 | R1-0528 | V4 Pro |
|---|---|---|---|---|
| AIME 2024 (Pass@1) | 39.2% | 79.8% | — | — |
| AIME 2025 (Pass@1) | — | 70.0% | 87.5% | — |
| MATH-500 | 90.2% | 97.3% | — | — |
| MMLU | 88.5% | 90.8% | — | — |
| GPQA Diamond | 59.1% | 71.5% | 81.0% | 90.1% |
| MMLU-Pro | — | — | — | 87.5% |

### Distilled model highlights

| Model | LiveCodeBench | MATH-500 | AIME 2024 |
|---|---|---|---|
| R1-Distill-Qwen-7B | 37.6 | 92.8% | 55.5% |
| R1-Distill-Qwen-32B | 1691 Elo (CF) | — | beats o1-mini |
| R1-Distill-Llama-70B | 57.5 | 94.5% | 86.7% |

**Context:** R1 matches OpenAI o1 on math, code, and reasoning. V4 Pro at LiveCodeBench 93.5 and Codeforces 3206 exceeds Gemini 3.1 Pro High. V3 at release was strongest open-weight non-reasoning model on coding benchmarks; V3.2 extended that lead significantly.

## Hardware Requirements

### DeepSeek V3 / V3.x (671B MoE)

The MoE architecture means only 37B parameters are active per token, reducing inference compute — but all expert weights must still reside in memory.

| Quantization | VRAM needed | Minimum setup |
|---|---|---|
| FP16/BF16 (full) | ~1.34 TB | Cluster only |
| Q4_K_M | ~380–400 GB total (VRAM + RAM with offloading) | 4–8x A100 80GB or CPU offload with 400GB combined |
| Q4 with CPU offload | ~24 GB VRAM + 376 GB RAM | 1x RTX 4090 + 512 GB system RAM (very slow) |

For production quality inference: 8x A100 80GB (tensor parallel) is the minimum practical GPU cluster.

Ollama supports V3 (via GGUF quantized variants). vLLM supports V3 with `--cpu-offload-gb` flag for partial offloading. SGLang is also commonly used.

Minimum system RAM for CPU offloading: 256 GB+. Storage: 400 GB NVMe for Q4 weights.

### DeepSeek R1 (671B MoE)

Same architecture as V3 — identical full-model VRAM requirements.

**Distilled models** are dense (not MoE) and practical on consumer hardware:

| Model | Q4 VRAM | Q8 VRAM | FP16 VRAM | Example GPU |
|---|---|---|---|---|
| 7B | ~4 GB | ~7 GB | ~14 GB | RTX 3060 (12 GB) |
| 14B | ~8 GB | ~14 GB | ~28 GB | RTX 3080 (10 GB) at Q4 |
| 32B | ~18 GB | ~34 GB | ~64 GB | RTX 4090 (24 GB) at Q4 |
| 70B | ~40 GB | ~70 GB | ~140 GB | 2x RTX 3090 at Q4 |

Q4_K_M is recommended for best quality-to-size ratio. Q8 is near-lossless when VRAM permits.

### DeepSeek V4 Pro (1.6T MoE)

Official weights are ~862 GB in FP4+FP8 mixed precision. This is cluster-class only.

| Config | Precision | Notes |
|---|---|---|
| 8x H100 80 GB (NVLink) | FP8 | Minimum viable production setup |
| 8x H200 or DGX H100 | FP4+FP8 | Recommended |
| Community Q4 (forthcoming) | Q4 | ~800+ GB VRAM still needed |

Requirements: 1 TB+ system RAM, 2 TB NVMe storage, NVLink + InfiniBand interconnect.

**V4 Pro is not practical for individual self-hosting.** Use the API. Consider V4 Flash if self-hosting is required — it fits on a single H200 or 2x A100 80 GB (~158 GB in FP4+FP8).

## Supported Tools

DeepSeek models (V3, R1, V4 Pro) are accessible across all major coding tools via OpenAI-compatible APIs:

| Tool | Integration method |
|---|---|
| **Cursor IDE** | API key in settings; V3 and R1 supported natively |
| **Continue (VS Code)** | DeepSeek provider built-in; all models supported |
| **Cline (VS Code)** | OpenAI-compatible endpoint; V3, R1, V4 Pro |
| **Aider** | `--model deepseek/deepseek-chat` flag |
| **Open WebUI** | Ollama backend for distilled models; API for full models |
| **Ollama** | `ollama pull deepseek-r1` (distilled variants); V3 via GGUF |
| **vLLM** | Full model serving with tensor parallelism and CPU offload |
| **SGLang** | Optimized for DeepSeek MoE inference, lower TTFT |
| **Claude Code** | Via MCP DeepSeek server or OpenAI-compatible proxy |

DeepSeek's API is OpenAI API-compatible (same `/v1/chat/completions` interface), so any tool that accepts a custom base URL can use it with minimal configuration.

V4 Pro is also available through third-party inference providers: DeepInfra, Novita, Fireworks AI, NVIDIA NIM.

## Strengths

- **Coding performance per dollar** — V3 and V4 Pro consistently top coding benchmarks among open-weight models. At API prices 5–10x cheaper than GPT-4o or Claude Sonnet, they are the strongest value for coding workloads.
- **Open weights** — MIT license allows full local deployment, fine-tuning, and commercial use with no restrictions.
- **MoE efficiency** — 37B–49B active parameters means inference cost scales with active compute, not total parameter count. V4 Pro uses 27% of V3.2 FLOPs per token.
- **1M context (V4)** — Native 1M token window without approximation; practical for large codebase ingestion.
- **Reasoning depth (R1 / V4 Pro Think Max)** — R1 matches o1 on math and competitive programming. V4 Pro Think Max with Codeforces 3206 and SWE-bench 80.6% leads open-weight models.
- **Distilled models** — R1 distills run reasoning-class performance on consumer hardware (7B–70B). R1-Distill-Qwen-32B beats o1-mini on multiple benchmarks.
- **Rapid iteration** — DeepSeek has shipped major model updates every 2–3 months since late 2024.
- **Self-hosting feasibility for distills** — R1 14B–32B distills run well on a single RTX 4090, making private local deployment accessible.
- **OpenAI-compatible API** — Zero-friction integration with existing tooling.

## Weaknesses

- **Hallucination** — V3.x models have documented hallucination on factual and math queries. V3.2-Speciale was pulled from LMArena after hallucinating arithmetic. V4 Pro has a 94% hallucination rate on AA-Omniscience (almost always answers rather than abstaining).
- **Political censorship (R1)** — R1 systematically refuses politically sensitive queries related to China (Tiananmen Square, etc.), with inconsistent behavior across languages. Self-hosted versions can bypass this but the default API enforces it.
- **Safety/security risks (R1)** — Third-party research (Cisco, HiddenLayer) found R1 has weak safety guardrails: 100% attack success rate in some harmful prompt evaluations, 11x more likely to generate harmful content than o1, 4x more likely to produce insecure code.
- **Full-model self-hosting is impractical** — V3 requires a 8-GPU cluster; V4 Pro requires a full DGX node. Not viable for individuals or small teams.
- **Long-context extraction** — Despite the large context windows, V3.x has documented weaknesses in accurate retrieval from very long contexts.
- **Tool use ceiling (V3 series)** — V3 shows strong pass@1 on tool use benchmarks but weaker pass@3, suggesting it has not been RL'd to its ceiling on agentic tasks. V4 Pro addresses this significantly.
- **R1 reasoning token cost** — R1's CoT reasoning generates large numbers of tokens (often 1K–5K before the answer), increasing latency and API cost significantly versus a non-reasoning model.
- **Language mixing** — Earlier V3.x versions occasionally mixed Chinese and English in outputs. Partially addressed in V3.1-Terminus.
- **Data privacy concerns** — Using the DeepSeek API sends data to servers in China. Organizations with data residency or compliance requirements should self-host or use third-party inference providers.

## Sources

- [DeepSeek API Pricing Docs](https://api-docs.deepseek.com/quick_start/pricing)
- [DeepSeek API Changelog](https://api-docs.deepseek.com/updates)
- [DeepSeek-V3 GitHub](https://github.com/deepseek-ai/DeepSeek-V3)
- [DeepSeek-V3 Technical Report (arXiv)](https://arxiv.org/pdf/2412.19437)
- [DeepSeek-R1 GitHub](https://github.com/deepseek-ai/DeepSeek-R1)
- [DeepSeek-V4-Pro Hugging Face](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)
- [DeepSeek-V3.2 arXiv paper](https://arxiv.org/html/2512.02556v1)
- [DeepInfra: DeepSeek V4 Pro Overview](https://deepinfra.com/blog/deepseek-v4-pro-model-overview)
- [BentoML: Complete Guide to DeepSeek Models](https://www.bentoml.com/blog/the-complete-guide-to-deepseek-models-from-v3-to-r1-and-beyond)
- [Artificial Analysis: DeepSeek V3](https://artificialanalysis.ai/models/deepseek-v3)
- [WaveSpeedAI: DeepSeek V4 GPU Requirements](https://wavespeed.ai/blog/posts/deepseek-v4-gpu-vram-requirements/)
- [Lushbinary: DeepSeek V4 Self-Hosting Guide](https://lushbinary.com/blog/deepseek-v4-self-hosting-guide-vllm-hardware-deployment/)
- [WillItRunAI: DeepSeek R1 VRAM Guide](https://willitrunai.com/blog/deepseek-r1-vram-requirements-guide)
- [Cisco: Security Risk in DeepSeek R1](https://blogs.cisco.com/security/evaluating-security-risk-in-deepseek-and-other-frontier-reasoning-models)
- [DataCamp: DeepSeek R1 Distilled Models](https://www.datacamp.com/blog/deepseek-r1)
- [Fireworks AI: DeepSeek R1 Deep Dive](https://fireworks.ai/blog/deepseek-r1-deepdive)
- [OpenRouter: DeepSeek V3.2](https://openrouter.ai/deepseek/deepseek-v3.2)
- [DeepSeek MCP + Claude Code (Composio)](https://composio.dev/toolkits/deepseek/framework/claude-code)
- [Freedeepseekapi: DeepSeek Cursor/VS Code Integration](https://freedeepseekapi.com/blog/deepseek-coding-cursor-vscode-integration)
- [R1dacted: Censorship in DeepSeek R1 (arXiv)](https://arxiv.org/html/2505.12625v1)
