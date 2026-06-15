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

Public benchmark numbers (MMLU, HumanEval, SWE-bench, GAIA, ...). Cite source.

## 9. Documented Strengths

Documented strengths from benchmarks, model card, or independent testing. Cite source.

## 10. Documented Weaknesses

Documented limitations and failure modes from benchmarks, model card, or community reports. Cite source.

## 11. Sources

- [databricks/dbrx-instruct on HuggingFace](https://huggingface.co/databricks/dbrx-instruct) — observed 2026-06-14
