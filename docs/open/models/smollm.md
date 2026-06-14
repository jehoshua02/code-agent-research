# SmolLM

_Last verified: 2026-06-14_

## 1. What It Is

SmolLM is HuggingFace's small-model family (135M–1.7B). Released under Apache 2.0. Designed for on-device and constrained-hardware deployment, trained on the SmolLM-Corpus.

## 2. Variants

SmolLM2 (released Feb 4, 2025; HuggingFaceTB org):

| Name | Params | Context | Intended Use |
|---|---|---|---|
| SmolLM2-135M (+ Instruct) | 135M | 2K | Ultra-lightweight on-device |
| SmolLM2-360M (+ Instruct) | 360M | 2K | On-device language tasks |
| SmolLM2-1.7B (+ Instruct) | 1.7B | 8K | Lightweight general-purpose; rewriting, summarization, function calling |

All trained on 11 trillion tokens in BF16. Successor to SmolLM v1 with improvements in instruction following, knowledge, reasoning, and math.

## 3. Context Window

- **135M / 360M:** 2,048 tokens.
- **1.7B:** 8,192 tokens (extended from 2K via continued training with RoPE base 130,000).
- No official extended-context variants; the 135M / 360M are too small for meaningful RoPE extrapolation.

## 4. Hardware Requirements

Designed for on-device / edge deployment.

| Variant | Q4 | Q8 | FP16/BF16 |
|---|---|---|---|
| SmolLM2-135M | ~0.1 GB | ~0.15 GB | ~0.27 GB |
| SmolLM2-360M | ~0.2 GB | ~0.4 GB | ~0.72 GB |
| SmolLM2-1.7B | ~1.1 GB | ~1.9 GB | ~3.4 GB |

Even the 1.7B FP16 fits ~3.4 GB — runnable on integrated graphics (Intel Arc, Apple M-series) or a laptop GPU. Min viable for 1.7B FP16: RTX 3050 4 GB. 8 GB system RAM enough for CPU inference of any variant.

## 5. Where To Get Weights

- HuggingFace org: https://huggingface.co/HuggingFaceTB
- **Gated:** no. **License:** Apache 2.0. Direct download.

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

- [HuggingFaceTB/SmolLM2 on HuggingFace](https://huggingface.co/HuggingFaceTB) — observed 2026-06-14
