# OLMo

_Last verified: 2026-06-14_

## 0. TL;DR

OLMo is the Allen Institute for AI's uniquely transparent open model — not only are the weights free under Apache 2.0, but the full training dataset and training code are also publicly released, making it the rare model you can fully audit and reproduce from scratch. Pick OLMo if you're doing academic research that requires complete reproducibility, studying how language models are trained, or need a model with no license restrictions and maximum openness. The main catch is that it's a research-first model, not a frontier performer: it's English-only, has a short 4K context window, and lacks tool calling or vision — newer models will outperform it on most practical tasks.

## 1. What It Is

OLMo is the Allen Institute for AI (AI2)'s fully-open model family. Weights, code, AND training data all released under Apache 2.0. Designed as a research-transparent alternative where the entire pipeline is reproducible.

## 2. Variants

OLMo 2 (current generation; "1124" denotes the November 2024 training cutoff; released January 2025):

| Name | Params | Stage | Intended Use |
|---|---|---|---|
| OLMo-2-1124-7B | 7B | Base | Research / educational base LM |
| OLMo-2-1124-7B-SFT | 7B | SFT | Supervised fine-tune stage |
| OLMo-2-1124-7B-DPO | 7B | DPO | DPO-aligned instruct |
| OLMo-2-1124-7B-Instruct | 7B | RLVR Instruct | Final instruction-following |
| OLMo-2-1124-13B | 13B | Base | Research / educational base LM |
| OLMo-2-1124-13B-SFT / DPO / Instruct | 13B | SFT / DPO / Instruct | Same stages as 7B |

Training tokens: 7B on 4T, 13B on 5T. Positioned for research / educational use.

## 3. Context Window

**4,096 tokens** native across all OLMo 2 variants — a known limitation versus contemporaries. RoPE allows community YaRN extrapolation (2x / 4x to 8K–16K), but this is unofficial and unvalidated by Ai2. No officially extended-context OLMo 2 variant exists as of mid-2026.

## 4. Hardware Requirements

No official VRAM table on model cards. Estimates from standard ~2 GB/B at FP16:

| Variant | Q4 | Q8 | FP16 |
|---|---|---|---|
| OLMo-2-7B | ~4 GB | ~7–8 GB | ~14 GB |
| OLMo-2-13B | ~7 GB | ~13–14 GB | ~26 GB |

Model cards mention 8-bit `bitsandbytes` loading. Min viable for 7B-Instruct at FP16: RTX 3090 24 GB; for 13B at FP16: A6000 48 GB or 2× RTX 3090. 64 GB system RAM for 13B partial offload.

## 5. Where To Get Weights

- HuggingFace org: https://huggingface.co/allenai
- **Gated:** no. **License:** Apache 2.0. Direct download.
- All stages (base / SFT / DPO / Instruct) publicly available. Training data and code also openly released — distinctive to OLMo.

## 6. Runtime Support

Supported by **Hugging Face Transformers** (primary, with `bitsandbytes` 8-bit loading), **vLLM** (BF16, GPTQ), and **llama.cpp** (community GGUF quants for OLMo 2 are available). **Ollama** supports OLMo 2 via GGUF. Because the architecture is a standard decoder-only transformer close to Llama, most runtimes can load it with minor config. **AWQ** is available from community sources. OLMo's focus on full openness means Ai2 publishes training code (OLMo repo on GitHub) and data (Dolma dataset), not just weights. Common formats: GGUF (Q2–Q8), GPTQ (INT4/INT8), 8-bit via bitsandbytes.

## 7. Capabilities

OLMo 2 targets general English **instruction following** (via the Instruct variant trained with SFT + DPO + RLVR), reasoning, and academic benchmarks. It is primarily a **research model** — its key differentiator is full pipeline transparency (weights + data + training code), not frontier capability. No tool/function calling schema, no vision, English-only. The 4K context window limits utility on long documents. ([OLMo 2 paper](https://arxiv.org/abs/2501.00656))

## 8. Benchmarks

Public benchmark numbers (MMLU, HumanEval, SWE-bench, GAIA, ...). Cite source.

## 9. Documented Strengths

Documented strengths from benchmarks, model card, or independent testing. Cite source.

## 10. Documented Weaknesses

Documented limitations and failure modes from benchmarks, model card, or community reports. Cite source.

## 11. Sources

- [allenai on HuggingFace](https://huggingface.co/allenai) — observed 2026-06-14
