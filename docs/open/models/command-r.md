# Command R

_Last verified: 2026-06-14_

## 1. What It Is

Command R / Command R+ / Command A are Cohere's open-weight families. Released under CC-BY-NC 4.0 (non-commercial; commercial use requires a Cohere license). Optimized for retrieval-augmented generation and tool use; multilingual.

## 2. Variants

| Name | Params | Released | Intended Use |
|---|---|---|---|
| Command R v0.1 (`c4ai-command-r-v01`) | 35B | Mar 2024 | RAG, tool use, long-context |
| Command R 08-2024 | 32B | Aug 2024 | Updated RAG, multilingual (23 languages) |
| Command R+ v0.1 | 104B | Mar 2024 | Advanced reasoning, RAG, multi-step tools |
| Command R+ 08-2024 | 104B | Aug 2024 | Updated; grounded generation, citations |
| Command R7B (`c4ai-command-r7b-12-2024`) | 7B | Dec 2024 | Lightweight enterprise; reasoning, RAG, code |
| Command A (`c4ai-command-a-03-2025`) | 111B | Mar 2025 | Agentic tasks; deployable on 2 GPUs |

Note: Command R was 35B in v0.1 but 32B in 08-2024 (Cohere reduced size between releases).

## 3. Context Window

- Command R v0.1 / 08-2024 / R+ / R7B: **128K** tokens.
- Command A: **256K** native; HF default config caps at 128K — manual change required for full 256K.
- Practical caveat: grounded-generation prompts add overhead; effective RAG context often ≤100K in practice.

## 4. Hardware Requirements

| Model | FP16 | Q8 | Q4 | Min viable GPU |
|---|---|---|---|---|
| Command R7B (7B) | ~14 GB | ~7 GB | ~4 GB | RTX 3060 12 GB |
| Command R 08-2024 (32B) | ~64 GB | ~32 GB | ~16 GB | RTX 4090 24 GB (Q4); A100 80 GB (FP16) |
| Command R+ (104B) | ~208 GB | ~104 GB | ~52 GB | 2× RTX 4090 or A100 80 GB (Q4); 3× A100 80 GB (FP16) |
| Command A (111B) | ~222 GB | ~111 GB | ~56 GB | 2× A100 80 GB (per model card); FP16 needs 3+ A100 80 GB |

CPU offload viable via llama.cpp; 64 GB RAM recommended for R+ partial offload.

## 5. Where To Get Weights

- HuggingFace org: https://huggingface.co/CohereForAI
- **Gated:** no HF access gates; publicly downloadable. Use is subject to Cohere Labs' Acceptable Use Policy.
- License: **CC-BY-NC** (Creative Commons Attribution-NonCommercial). Commercial use requires a separate Cohere license agreement.

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

- [CohereForAI on HuggingFace](https://huggingface.co/CohereForAI) — observed 2026-06-14
