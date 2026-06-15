# StarCoder2

_Last verified: 2026-06-14_

## 0. TL;DR

StarCoder2 is a code-only base model from the open BigCode research project, trained on The Stack v2 dataset covering 600+ programming languages — think of it as an autocomplete engine for code, not a chat assistant. Pick StarCoder2 if you want a solid, openly-developed foundation for building a code completion or fill-in-the-middle tool, especially if you plan to fine-tune it for your specific use case. The main catch is that it has no instruction tuning out of the box (it won't respond well to plain English commands), requires accepting an OpenRAIL-M license on download, and has been largely superseded by newer code-focused models like Qwen2.5-Coder.

## 1. What It Is

StarCoder2 is the BigCode project's open-weight code model family (3B/7B/15B). Released under BigCode OpenRAIL-M license (permissive with use-based restrictions). Trained on The Stack v2 and targeted at code generation.

## 2. Variants

| Name | Params | Released | Intended Use |
|---|---|---|---|
| StarCoder2-3B | 3B | Feb 2024 | Code gen, FIM, lightweight / on-device |
| StarCoder2-7B | 7B | Feb 2024 | Code gen across 17 languages |
| StarCoder2-15B | 15B | Feb 2024 | Code gen across 600+ languages; flagship |

All three are base (non-instruct) models. They work best given code context rather than natural-language commands — bare "write a function that..." prompts under-perform without additional fine-tuning. 3B/7B trained on 3.5+ trillion tokens (The Stack v2).

## 3. Context Window

**16,384 tokens** native across all three variants, using a sliding window attention mechanism with a 4,096 dense window. Full attention is dense only inside the 4K window; the rest uses sliding/sparse patterns. No official long-context extension. Perplexity may degrade near the far edges of the 16K window.

## 4. Hardware Requirements

7B and 15B figures from the official HuggingFace model cards; 3B from standard formulas.

| Variant | Q4 | Q8 | FP16/BF16 |
|---|---|---|---|
| StarCoder2-3B | ~2.0 GB | ~3.5 GB | ~6 GB |
| StarCoder2-7B | ~4.2 GB | ~7.7 GB | ~14.6 GB |
| StarCoder2-15B | ~9.2 GB | ~16.9 GB | ~32.2 GB |

Min viable GPU: RTX 3090/4090 24 GB runs 15B at Q8. 7B at FP16 fits a 16 GB GPU (RTX 4080, A4000). 32–64 GB system RAM recommended if offloading the 15B.

## 5. Where To Get Weights

- HuggingFace org: https://huggingface.co/bigcode
- Repos: `bigcode/starcoder2-3b`, `bigcode/starcoder2-7b`, `bigcode/starcoder2-15b`.
- **Gated:** yes — must log in to HF and accept the **BigCode OpenRAIL-M v1** license before download. Self-serve, no institutional approval.
- Commercial use permitted subject to OpenRAIL-M use restrictions.

## 6. Runtime Support

Supported by **Hugging Face Transformers** (primary; model card examples use transformers + `generate`), **vLLM** (BF16 and GPTQ), **llama.cpp** (GGUF; StarCoder2 architecture supported since llama.cpp mid-2024), and **Ollama** (GGUF). **Text Generation Inference (TGI)** — Hugging Face's serving backend — is a natural fit given the BigCode/HF collaboration. Community GGUF quants (Q2–Q8) available for all three sizes; official GPTQ-Int4 quants published by BigCode. AWQ available from community. No FP8 or MLX official releases.

## 7. Capabilities

StarCoder2 is a **code-only** model with no chat / instruction tuning — it is a base model intended for code completion and **fill-in-the-middle (FIM)** (special `<fim_prefix>`, `<fim_suffix>`, `<fim_middle>` tokens). Supports **600+ programming languages** (15B) trained on The Stack v2; 7B and 3B cover at least 17 major languages. No tool/function calling, no vision, no multilingual natural language. Typically fine-tuned before deployment as a chat assistant (e.g., Starchat). ([StarCoder2 paper](https://arxiv.org/abs/2402.19173))

## 8. Benchmarks

Public benchmark numbers (MMLU, HumanEval, SWE-bench, GAIA, ...). Cite source.

## 9. Documented Strengths

Documented strengths from benchmarks, model card, or independent testing. Cite source.

## 10. Documented Weaknesses

Documented limitations and failure modes from benchmarks, model card, or community reports. Cite source.

## 11. Sources

- [bigcode on HuggingFace](https://huggingface.co/bigcode) — observed 2026-06-14
