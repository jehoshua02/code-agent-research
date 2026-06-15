---
name: "DBRX"
maker: "Databricks"
license: "Databricks Open Model License"
license_category: "custom-permissive"
status: "borderline"
url: "https://huggingface.co/databricks"
last_verified: "2026-06-14"
variants: ["DBRX-Base", "DBRX-Instruct"]
params_total: "132B"
has_moe: true
params_active: "36B"
context_window: 32768
modalities: ["text"]
gated: true
released: "2024-03"
hardware_tiers: ["24gb+"]
best_for: ["coding"]
notes: "No updates since March 2024; largely superseded by Llama 3 and Qwen 2.5 class models"
---

# DBRX

_Last verified: 2026-06-14_

## 0. TL;DR

DBRX is Databricks' single open-weight model — a 132B [mixture-of-experts](../GLOSSARY.md#moe-mixture-of-experts) model that activates only 36B parameters per request, released in March 2024 as a competitive alternative to GPT-3.5 for code and general chat. Pick DBRX if you're already in the Databricks ecosystem (MLflow, Mosaic AI Model Serving) and want a commercially-licensed model with good coding performance. The main catch is that DBRX is now dated — the model has seen no updates since launch, lacks tool calling and multilingual support, and requires at least two A100 80 GB GPUs even at INT4 compression.

## 1. What It Is

DBRX is Databricks (Mosaic AI)'s open-weight model. Released March 2024 under the Databricks Open Model License. 132B-total / 36B-active MoE; HuggingFace repos may be gated requiring license acceptance.

## 2. Variants

| Name | Total / Active Params | Released | Intended Use |
|---|---|---|---|
| DBRX Base | 132B / 36B | Mar 27, 2024 | Pre-trained base; general-purpose |
| DBRX Instruct | 132B / 36B | Mar 27, 2024 | Few-turn instruction following, chat |

Architecture: fine-grained MoE — 16 experts per layer, 4 active per token (16-choose-4 = 1820 combinations). Uses RoPE, GLU, and GQA. Trained on 12T tokens of text + code. No smaller or larger DBRX variants exist.

## 3. Context Window

**32,768 tokens** (32K) native. No official extended-context variant. At 32K with 132B total params, memory pressure is substantial even on multi-GPU.

## 4. Hardware Requirements

| Precision | VRAM Required |
|---|---|
| BF16 | ~264 GB (8× A100 80 GB minimum) |
| Q8 | ~132 GB |
| Q4 | ~66–70 GB (≈ 2× A100 80 GB, or 4× RTX 4090 24 GB) |

All 132B params must be in memory (not just active 36B). CPU offload impractical at usable speed; full CPU offload would need ≥256 GB system RAM.

## 5. Where To Get Weights

- HuggingFace: https://huggingface.co/databricks (repos `dbrx-base`, `dbrx-instruct`)
- **Gated:** yes — must log in to HF and accept the **Databricks Open Model License** and **Databricks Open Model Acceptable Use Policy** before download. Self-serve acceptance.
- Commercial use permitted under the Databricks Open Model License.

## 6. Runtime Support

Supported by **Hugging Face Transformers** (primary; model card examples use transformers), **vLLM** (BF16, GPTQ; expert routing supported), and **llama.cpp** (GGUF; the fine-grained MoE architecture was added to llama.cpp in 2024). **Ollama** supports community GGUF quants. Databricks' own **MLflow** and **Mosaic AI Model Serving** are the intended production paths. Due to the 132B total weight requirement, consumer-grade runtimes require heavy quantization. Common quant formats: GGUF (Q2–Q8 community), GPTQ (INT4); no official FP8 or AWQ release. The 4-expert-per-token routing is compatible with vLLM's MoE backend.

## 7. Capabilities

DBRX Instruct targets **general English chat and instruction following**, with emphasis on **code generation** (trained on 12T tokens including substantial code data). Benchmarks at launch showed competitiveness with Mixtral-8x7B and GPT-3.5 on coding (HumanEval) and reasoning. No tool/function calling schema is officially documented — function use requires prompt engineering. No vision capability. No multilingual design goal; primarily English. No official smaller or updated variants have been released post-launch. ([DBRX blog post](https://www.databricks.com/blog/introducing-dbrx-new-state-art-open-llm))

## 8. Benchmarks

All scores are for DBRX Instruct. Source: Databricks launch blog ([databricks.com/blog/introducing-dbrx-new-state-art-open-llm](https://www.databricks.com/blog/introducing-dbrx-new-state-art-open-llm)). The HuggingFace model repo is gated (requires license acceptance); scores from the blog are the primary public source.

| Benchmark | DBRX Instruct | Notable Comparison |
|---|---|---|
| MMLU | 73.7% | GPT-3.5: 70.0% |
| HumanEval (pass@1) | 70.1% | CodeLlama-70B: 67.8%; Grok-1: 63.2% |
| GSM8K | 66.9% | Grok-1: 62.9% |
| MT-Bench (corrected) | 8.39 | Gemini 1.0 Pro: 8.23 |
| HellaSwag | 89.0% | GPT-3.5: 85.5% |
| HF Open LLM Leaderboard | 74.5% | Mixtral-8x7B-Instruct: 72.7% |
| Databricks Model Gauntlet | 66.8% | Mixtral-8x7B-Instruct: 60.7% |

GPQA, MATH, IFEval, and SWE-bench scores were not reported. These benchmarks reflect March 2024 results; the model has not been updated since.

## 9. Documented Strengths

- **Strong code generation at launch**: HumanEval 70.1% outperformed CodeLlama-70B (67.8%) and Grok-1 (63.2%) at the time of release in March 2024 — notable given DBRX activates only 36B parameters per token. ([Databricks blog](https://www.databricks.com/blog/introducing-dbrx-new-state-art-open-llm))
- **Fine-grained MoE efficiency**: The 16-expert, 4-active architecture (16-choose-4 = 1,820 routing combinations) enables diverse expert specialization with better per-token efficiency than coarser MoE designs; matched or exceeded Mixtral-8x7B at higher active-parameter count. ([Databricks blog](https://www.databricks.com/blog/introducing-dbrx-new-state-art-open-llm))
- **Databricks / MLflow integration**: Native deployment path via Mosaic AI Model Serving and MLflow, making it a low-friction choice for teams already in the Databricks platform.
- **32K context with competitive RAG**: HotPotQA RAG accuracy 55.0% outperforms GPT-3.5 Turbo 53.0%; a practical advantage for Databricks-based data pipelines. ([Databricks blog](https://www.databricks.com/blog/introducing-dbrx-new-state-art-open-llm))

## 10. Documented Weaknesses

- **No model updates since March 2024**: DBRX has received no architectural updates, fine-tune releases, or extended-context variants; it has been substantially surpassed by Llama 3.1 70B/405B, Qwen 2.5, and other models released later in 2024.
- **Very high hardware floor**: Even at INT4, DBRX requires ~66 GB VRAM (two A100 80 GB GPUs) because all 132B parameters must reside in memory — the active-36B figure does not reduce the memory footprint. ([DBRX model card / Databricks blog](https://www.databricks.com/blog/introducing-dbrx-new-state-art-open-llm))
- **No tool calling or multilingual support**: No officially documented function-calling format; primarily English; neither was added post-launch.
- **Long-context underperformance**: The blog notes DBRX "underperforms" GPT-4 Turbo on 16K and 32K context benchmarks despite having the window size, suggesting degraded quality at long ranges. ([Databricks blog](https://www.databricks.com/blog/introducing-dbrx-new-state-art-open-llm))

## 11. Sources

- [databricks/dbrx-instruct on HuggingFace](https://huggingface.co/databricks/dbrx-instruct) — observed 2026-06-14
