# Hunyuan (Tencent)

## What It Is

Hunyuan is Tencent's family of large language models, developed by the Tencent HY (Hunyuan) team. The family spans multiple generations: Hunyuan-Large (released November 2024), an open-weight MoE model that was the largest open-source Transformer-based MoE model at the time of release, and Hy3 preview (released April 22, 2026), the first model from a full ground-up rebuild of the Hunyuan architecture. Both are proprietary in training but released under the Tencent Hunyuan Community License, which permits commercial use.

The Hunyuan brand also encompasses Yuanbao (Tencent's consumer AI assistant), CodeBuddy (Tencent Cloud's coding assistant), and specialized variants for reasoning (Hunyuan-T1), speed (Hunyuan Turbo S), and vision (Hunyuan-Large-Vision). This document focuses on the two main text/code generation models: Hunyuan-Large and Hy3 preview.

## Variants

### Hunyuan-Large (Hunyuan-MoE-A52B) — November 2024

| Variant | Parameters (Total / Active) | Context | Notes |
|---|---|---|---|
| Hunyuan-A52B-Pretrain | 389B / 52B | 256K | Base pretrain model |
| Hunyuan-A52B-Instruct | 389B / 52B | 128K | Instruction-tuned |
| Hunyuan-A52B-Instruct-FP8 | 389B / 52B | 128K | Quantized for reduced memory |

Architecture: Transformer-based MoE with Grouped Query Attention (GQA) and Cross-Layer Attention (CLA). 1 shared expert + specialized experts per token. CLA reduces KV-Cache memory by ~50%.

Also known as the "Yuanbao Code Large Model" within the Tencent product ecosystem, as it powers Yuanbao's code-oriented features.

### Hy3 preview (Hunyuan 3.0) — April 22, 2026

| Property | Value |
|---|---|
| Total parameters | 295B |
| Active parameters | 21B |
| MTP speculative layer | 3.8B |
| Transformer layers | 80 (+ 1 MTP layer) |
| Expert config | 192 experts, top-8 activated |
| Attention | GQA, 64 heads, 8 KV heads, 128-dim |
| Hidden size | 4096 |
| Intermediate size | 13,312 |
| Vocabulary | 120,832 tokens |
| Context window | 256K tokens |
| Precision | BF16 |

Hy3 was rebuilt from scratch in ~90 days (training start: late January 2026; release: April 2026). It integrates fast and slow thinking in a single model, configurable per request via a `reasoning_effort` parameter.

## Pricing

### Hunyuan-Large (389B)
- Weights are open on Hugging Face under the Tencent license (free to self-host).
- Tencent Cloud API pricing is not publicly listed for Hunyuan-Large by name; the broader Hunyuan API lineup (as of 2024–2025) ranged from free (Hunyuan-lite) to ~¥0.03/1K tokens input for Hunyuan-pro. Hunyuan-Large is available via the Tencent Cloud HunyuanAPI platform — check cloud.tencent.com for current rates.

### Hy3 preview (295B)
- **Tencent Cloud TokenHub**: ¥1.2 (~$0.17) per million input tokens; ¥4 (~$0.55) per million output tokens.
- **OpenRouter**: Free tier was available at launch (April 22–May 8, 2026) at $0/M in and $0/M out. Paid tier pricing on OpenRouter not confirmed publicly.
- Weights available on Hugging Face, ModelScope, and GitCode for self-hosting at no licensing cost (Tencent Hy Community License).

## Context Window

| Model | Native Context |
|---|---|
| Hunyuan-Large Pretrain | 256K tokens |
| Hunyuan-Large Instruct | 128K tokens |
| Hy3 preview | 256K tokens (262,144 tokens as listed on OpenRouter) |

Both models use GQA and CLA for efficient long-context handling. Practical long-context performance at full 256K has not been independently benchmarked by third parties as of writing. Hy3 preview's TTFT of 3.58s (vs. median 2.18s for comparable open-weight models) suggests some latency cost at long contexts.

## Benchmarks

### Hunyuan-Large (Instruct vs. LLaMA 3.1 405B Instruct)

| Benchmark | Hunyuan-Large Instruct | LLaMA 3.1 405B Instruct |
|---|---|---|
| HumanEval | **90.0%** | 89.0% |
| MATH | **77.4%** | 73.8% |
| MMLU | **89.9%** | 87.3% |

Pretrain model scores: HumanEval 71.4% (vs. LLaMA 3.1 405B: 61.0%), MBPP 72.6% (vs. 73.4%).

Hunyuan-Large topped 15 of 19 benchmarks across English, Chinese, math, and coding at the time of release. It matched or exceeded LLaMA 3.1 405B while activating only 52B parameters.

### Hy3 preview

| Benchmark | Score | Notes |
|---|---|---|
| SWE-bench Verified | 74.4% | Up from Hy2's 53.0%; above GLM-5 (72.9%) and Kimi-K2.5 (72.9%); below Claude Opus 4.6 (~80%) |
| Terminal-Bench 2.0 | 54.4% | Agent coding tasks |
| MBPP-plus | 78.71% | 3-shot |
| LiveCodeBench-v6 | 34.86% | 1-shot |
| CRUXEval-I | 71.19% | 3-shot |
| GPQA Diamond | 87.2% | Graduate-level reasoning |
| GSM8K | 95.37% | 4-shot |
| MATH | 76.28% | 4-shot |
| MMLU | 87.42% | 5-shot |
| BrowseComp | 67.1% | Web search agent |

Hy3 preview's SWE-bench jump of 40% over Hy2 is the headline coding improvement. On AutoCodeBench (Tencent's own multi-language code benchmark covering 20 languages and 3,920 problems), Hunyuan models showed competitive results but no single model dominated across all problem types.

## Hardware Requirements

### Hunyuan-Large (389B / 52B active)
- **BF16 inference**: 16× H20 GPUs (minimum)
- **Int8/FP8 quantized inference**: 8× H20 GPUs (minimum)
- **LoRA fine-tuning**: 8× H20 GPUs minimum
- **Full fine-tuning**: 32× H20 GPUs minimum
- Inference throughput at batch size 4, 2048 input tokens: ~75 tokens/s (BF16), ~74 tokens/s (FP8)
- **Ollama**: Not officially supported. A community GitHub issue (#7503) tracks a request; no model file exists in the Ollama library as of writing.
- **vLLM**: Supported (open-sourced by Tencent).

### Hy3 preview (295B / 21B active, ~590GB BF16 weights)
- **Minimum (Q4 GGUF)**: ~80GB VRAM + 256GB RAM CPU offload; 700GB NVMe storage
- **Recommended (BF16, 4-way TP)**: 4× A100 80GB (320GB VRAM), 384GB RAM, 1TB NVMe, CUDA 12.4+
- **Production (BF16, 8-way TP)**: 8× H100 80GB or 8× H200 141GB, 512GB RAM, 1.5TB NVMe, CUDA 12.6+
- **Cost estimate**: ~$10–16/day on 4× A100 80GB
- **vLLM**: Supported with `--tensor-parallel-size 8`, MTP speculative decoding (`--speculative-config.method mtp`), tool-call parser (`--tool-call-parser hy_v3`), reasoning parser (`--reasoning-parser hy_v3`)
- **SGLang**: Day-0 support with EAGLE speculative sampling
- **Ollama**: No official support at launch; community GGUF builds expected within weeks of release
- **Quantization**: AngelSlim W4A16 quants available to reduce VRAM; LLaMA-Factory for fine-tuning with DeepSpeed ZeRO

## Supported Tools

### CodeBuddy (Primary Tencent Coding Tool)
CodeBuddy is Tencent Cloud's full-stack AI programming assistant, powered by Hunyuan (and optionally DeepSeek V3). It is the primary deployment surface for Hunyuan coding capabilities.

- **Forms**: Plugin (VS Code, JetBrains series, WeChat Developer Tools), IDE (CodeBuddy IDE — a standalone Cursor-like product), CLI
- **IDE support**: 15+ IDEs including VS Code, IntelliJ IDEA, PyCharm, WebStorm, GoLand, Rider; WeChat Developer Tools
- **Language support**: 200+ programming languages and frameworks
- **Features**: Code completion, intelligent code review, design-to-code conversion, bug diagnosis, performance optimization, MCP protocol support
- **Hy3 integration**: After Hy3 preview integration, CodeBuddy reduced first-token latency by 54%, cut end-to-end task duration by 47%, and achieved 99.99%+ task success rates
- **Usage**: Over 50% of Tencent's internal engineers use CodeBuddy; reported 40% coding time reduction; AI-generated code accounts for over 50% of output
- **Availability**: Free for individuals; enterprise plans via Tencent Cloud

### Other Tencent Products Using Hunyuan
- **Yuanbao**: Tencent's consumer AI assistant (yuanbao.tencent.com) — primary Hunyuan chat interface
- **WorkBuddy**: Enterprise productivity assistant
- **ima**: Knowledge management tool
- **QQ, QQ Browser, Tencent Docs, Tencent LearnShare**: All integrated Hy3 preview

### Third-Party API Access
- **OpenRouter**: `tencent/hy3-preview` (Hy3 preview available; Hunyuan-Large not listed)
- **Tencent Cloud TokenHub**: Direct API for both models

### Self-Hosting Frameworks
- vLLM, SGLang (both supported for Hy3)
- vLLM (supported for Hunyuan-Large)
- Compatible with OpenAI-compatible API format

## Strengths

- **Efficient MoE architecture**: Both models activate a fraction of total parameters per forward pass (52B/389B for Hunyuan-Large; 21B/295B for Hy3), making inference cheaper than dense models of equivalent quality.
- **Strong coding performance**: Hunyuan-Large Instruct scored 90.0% on HumanEval (edging LLaMA 3.1 405B). Hy3 preview hit 74.4% on SWE-bench Verified, a 40% jump over Hy2.
- **Long context**: 256K native context on both pretrain/Hy3 variants; CLA and GQA reduce KV-Cache memory by ~50%.
- **Chinese language**: Best-in-class Chinese capability; top CEVAL scores; tuned specifically for Chinese developer workflows in CodeBuddy.
- **Configurable reasoning**: Hy3 supports `no_think`, `low`, and `high` reasoning effort modes, enabling cost/quality tradeoffs at inference time.
- **MTP speculative decoding**: Hy3's 3.8B MTP layer provides 1.5–2× decode speedup on Hopper-class GPUs.
- **Open weights**: Both models freely downloadable with commercial-friendly licenses.
- **Production integration**: Hy3 deployed across all major Tencent products; proven at Tencent's internal scale.

## Weaknesses

- **Massive hardware footprint**: Hunyuan-Large requires 8–16× H20s; Hy3 preview requires ~590GB VRAM at BF16. Neither model is accessible on consumer hardware without aggressive quantization and CPU offloading.
- **No Ollama support**: Neither model has official Ollama integration, limiting accessibility for local development workflows common in the developer community.
- **Tool-call error recovery**: Hy3 preview officially acknowledges weak error recovery during tool calls and sensitivity to inference hyperparameters as known limitations.
- **Verbosity**: Hy3 is notably verbose — it generated 120M tokens during the Artificial Analysis evaluation vs. an average of 42M for comparable models. This inflates output token costs and latency.
- **High TTFT**: Hy3 reasoning mode has a time-to-first-token of 3.58s (median for comparable open-weight models: 2.18s).
- **LiveCodeBench gap**: Hy3's LiveCodeBench-v6 score of 34.86% (1-shot) is notably lower than its SWE-bench result, suggesting stronger agent-level task performance than raw code generation on competitive programming tasks.
- **Tencent ecosystem lock-in for best UX**: CodeBuddy and Yuanbao integration is seamless, but third-party tool support (Cursor, Claude Code, GitHub Copilot) is absent or requires manual API configuration.
- **Western availability**: Tencent Cloud pricing and registration can be friction-heavy for non-Chinese developers; documentation exists primarily in Chinese with partial English translations.
- **Hunyuan-Large context limitation**: The Instruct model caps at 128K (vs. 256K for the pretrain), limiting production long-context use without special configuration.

## Sources

- [Hunyuan-Large paper (arXiv:2411.02265)](https://arxiv.org/abs/2411.02265)
- [Tencent-Hunyuan-Large GitHub repo](https://github.com/Tencent-Hunyuan/Tencent-Hunyuan-Large)
- [tencent/Tencent-Hunyuan-Large — Hugging Face](https://huggingface.co/tencent/Tencent-Hunyuan-Large)
- [Hy3-preview GitHub repo](https://github.com/Tencent-Hunyuan/Hy3-preview)
- [tencent/Hy3-preview — Hugging Face](https://huggingface.co/tencent/Hy3-preview)
- [Hy3 preview vLLM recipes](https://recipes.vllm.ai/tencent/Hy3-preview)
- [Tencent official Hy3 announcement](https://www.tencent.com/en-us/articles/2202320.html)
- [Hy3 preview Clore.ai deployment guide](https://docs.clore.ai/guides/language-models/hy3-preview)
- [Hy3-preview — Artificial Analysis](https://artificialanalysis.ai/models/hy3)
- [Hy3-preview — OpenRouter](https://openrouter.ai/tencent/hy3-preview:free)
- [Tencent Hy3 AI Model: 40% Efficiency Gain — The Outpost](https://theoutpost.ai/news-story/tencent-launches-hy3-ai-model-with-40-efficiency-gain-and-real-world-product-integration-25687/)
- [CodeBuddy documentation](https://www.codebuddy.ai/docs/ide/Introduction)
- [CodeBuddy review — Skywork AI](https://skywork.ai/blog/tencent-codebuddy-a-new-kind-of-ai-coding-partner/)
- [AutoCodeBench paper (arXiv:2508.09101)](https://arxiv.org/html/2508.09101v1)
- [Hunyuan-Large outshines open competitors — DeepLearning.AI The Batch](https://www.deeplearning.ai/the-batch/hunyuan-large-outshines-open-competitors-with-high-benchmark-scores/)
- [Tencent Hy3 open-sourced at 74.4% SWE-bench — Business Analytics](https://businessanalytics.substack.com/p/tencent-open-sources-hy3-at-744)
- [Tencent Cloud price announcement — Futunn](https://news.futunn.com/en/post/69947199/tencent-cloud-officially-announced-a-price-increase-for-its-hunyuan)
