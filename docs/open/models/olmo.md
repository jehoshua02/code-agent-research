# OLMo

_Last verified: 2026-06-14_

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

- [allenai on HuggingFace](https://huggingface.co/allenai) — observed 2026-06-14
