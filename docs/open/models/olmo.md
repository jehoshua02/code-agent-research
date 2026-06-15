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

Scores for the fully post-trained Instruct variants. Source: HuggingFace model cards ([7B-Instruct](https://huggingface.co/allenai/OLMo-2-1124-7B-Instruct), [13B-Instruct](https://huggingface.co/allenai/OLMo-2-1124-13B-Instruct)).

| Benchmark | OLMo-2-7B-Instruct | OLMo-2-13B-Instruct |
|---|---|---|
| MMLU | 61.3 | 68.5 |
| GSM8K | 85.1 | 87.4 |
| MATH | 32.5 | 39.2 |
| IFEval | 72.3 | 82.6 |
| BBH | 46.6 | 58.8 |
| DROP | 60.5 | 71.5 |
| AlpacaEval | 29.1 | 39.5 |
| TruthfulQA | 56.5 | 64.3 |

The 7B-Instruct outperforms Gemma-2-9B-it and Mistral-Nemo-Instruct on the Ai2 aggregate metric; the 13B-Instruct is competitive with Qwen-2.5-14B-Instruct. HumanEval, GPQA, and SWE-bench were not reported.

## 9. Documented Strengths

- **Fully open pipeline — weights, data, and training code**: OLMo 2 is one of the only models where the complete pretraining dataset (Dolma), model architecture, and training scripts are all publicly released under Apache 2.0, enabling genuine scientific reproducibility — a major differentiator for academic research. ([OLMo 2 paper](https://arxiv.org/abs/2501.00656), [Ai2](https://huggingface.co/allenai))
- **Competitive instruction-following for its size**: OLMo-2-7B-Instruct scores 72.3 on IFEval and 85.1 on GSM8K, outperforming similarly-sized open models like Gemma-2-9B-it and Mistral-Nemo-Instruct on Ai2's aggregate evaluation suite. ([HuggingFace model card](https://huggingface.co/allenai/OLMo-2-1124-7B-Instruct))
- **Apache 2.0 license**: No use-based restrictions — suitable for commercial deployment, fine-tuning, and redistribution without negotiating a separate license. ([allenai/OLMo-2-1124-7B-Instruct](https://huggingface.co/allenai/OLMo-2-1124-7B-Instruct))
- **Multi-stage training released**: All intermediate checkpoints (SFT, DPO, RLVR) are publicly available, making OLMo 2 valuable for alignment research and studying the effect of each post-training stage. ([HuggingFace allenai org](https://huggingface.co/allenai))

## 10. Documented Weaknesses

- **4K context window**: All OLMo 2 variants have a 4,096-token native context, significantly shorter than contemporaries (Llama 3 at 128K, Qwen 2.5 at 128K), limiting usefulness on long documents and multi-turn conversations. ([OLMo 2 paper](https://arxiv.org/abs/2501.00656))
- **English-only**: OLMo 2 was trained exclusively on English data; multilingual tasks are unsupported and performance on non-English text is undefined. ([HuggingFace model card](https://huggingface.co/allenai/OLMo-2-1124-7B-Instruct))
- **Trails frontier open models on reasoning**: OLMo-2-7B-Instruct MATH score (32.5) and BBH (46.6) lag behind Llama-3.1-8B-Instruct and Qwen-2.5-7B-Instruct; it is a research-transparency model, not a capability leader. ([HuggingFace model card](https://huggingface.co/allenai/OLMo-2-1124-7B-Instruct))
- **No tool calling or vision**: No structured function-calling schema and no multimodal support; unsuitable as a drop-in for agentic or image-understanding tasks.

## 11. Sources

- [allenai on HuggingFace](https://huggingface.co/allenai) — observed 2026-06-14
