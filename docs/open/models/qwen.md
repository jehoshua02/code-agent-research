# Qwen

_Last verified: 2026-06-14_

## 1. What It Is

Qwen is Alibaba's open-weight model family. Qwen2.5 and Qwen3 lines released under Apache 2.0 (most checkpoints). General-purpose models with strong multilingual support, math/coding-specific variants (Qwen-Coder, Qwen-Math), and dense + MoE architectures.

## 2. Variants

Each variant: name, total params (and active for MoE), release date, intended use case. One row per variant.

## 3. Context Window

Native context length. Extended context options (YaRN, etc.). Practical limits.

## 4. Hardware Requirements

VRAM at Q4 / Q8 / FP16. Minimum viable GPU. Recommended setup. System RAM if offload is relevant.

## 5. Where To Get Weights

Distribution channels (HuggingFace, official site, mirrors). Gated? License acceptance required? Account needed?

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

- [Qwen on HuggingFace](https://huggingface.co/Qwen) — observed 2026-06-14
