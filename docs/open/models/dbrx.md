# DBRX

_Last verified: 2026-06-14_

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

Which runtimes load it (ollama, vllm, llama.cpp, transformers, ...). Quantization formats available (GGUF, AWQ, GPTQ, FP8, ...).

## 7. Capabilities

Tool use, function calling, vision, code, languages, etc. What it's trained for.

## 8. Benchmarks

Public benchmark numbers (MMLU, HumanEval, SWE-bench, GAIA, ...). Cite source.

## 9. Documented Strengths

Documented strengths from benchmarks, model card, or independent testing. Cite source.

## 10. Documented Weaknesses

Documented limitations and failure modes from benchmarks, model card, or community reports. Cite source.

## 11. Sources

- [databricks/dbrx-instruct on HuggingFace](https://huggingface.co/databricks/dbrx-instruct) — observed 2026-06-14
