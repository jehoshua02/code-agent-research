# DeepSeek

_Last verified: 2026-06-14_

## 1. What It Is

DeepSeek is DeepSeek AI's open-weight family. V2 and V3 use the DeepSeek License (permissive, commercial use allowed); R1 reasoning model released MIT. DeepSeek-V3 is a 671B-total / 37B-active MoE; R1 is a reasoning-focused variant trained with RL.

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

- [deepseek-ai on HuggingFace](https://huggingface.co/deepseek-ai) — observed 2026-06-14
