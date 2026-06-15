# Hermes

_Last verified: 2026-06-14_

## 0. TL;DR

Hermes is Nous Research's series of fine-tuned models built on top of base models like Llama 3.1, specifically sharpened for tool calling, structured outputs, and multi-step agentic workflows — it's what you get when you take a capable base model and train it intensively to reliably follow JSON and XML schemas when calling functions. Pick Hermes if you're building an AI agent that needs to call tools or APIs reliably and you want a community-developed model with a well-documented calling format. The main catch is that the license is inherited from the base model (Llama's 700M MAU cap applies), training was at 8K context so quality may degrade on very long inputs despite the 128K window, and no vision support exists.

## 1. What It Is

Hermes is Nous Research's open-weight series of fine-tuned models. Licenses inherit from the base model used for each Hermes variant (e.g., Llama-based Hermes inherits Llama Community License; Qwen-based inherits Apache 2.0). Tuned for tool use, function calling, and chat quality.

## 2. Variants

Hermes 3 (Nous Research, fine-tuned from Llama 3.1; released Aug 15, 2024):

| Name | Base Model | Params | Intended Use |
|---|---|---|---|
| Hermes-3-Llama-3.1-8B | Llama 3.1 8B | 8B | Generalist assistant, function calling, agentic |
| Hermes-3-Llama-3.1-70B | Llama 3.1 70B | 70B | High-capability generalist, structured outputs, reasoning |
| Hermes-3-Llama-3.1-405B | Llama 3.1 405B | 405B | Maximum-capability generalist (community quantized) |

All variants tuned for function calling, XML structured outputs, scratchpad / internal-monologue agentic workflows, roleplay, code, multi-turn chat. Training used 8,192-token sequence packing. GGUF quants at `NousResearch/Hermes-3-Llama-3.1-{8B,70B}-GGUF`; FP8 via NeuralMagic.

## 3. Context Window

**131,072 tokens (128K)** native for all sizes (inherited from Llama 3.1). Practical caveat: training was at 8K sequence length, so quality may degrade above ~32K versus models explicitly long-context trained. KV cache at 128K is prohibitively large on most hardware for 70B and 405B.

## 4. Hardware Requirements

Standard formula estimates (no official VRAM table on model cards):

| Variant | Q4 | Q8 | FP16 |
|---|---|---|---|
| Hermes-3-8B | ~5 GB | ~9 GB | ~16 GB |
| Hermes-3-70B | ~40 GB | ~75 GB | ~140 GB |
| Hermes-3-405B | ~230 GB | ~405 GB | ~810 GB |

Min viable: 8B FP16 on RTX 3080/4070 Ti 16 GB; 70B Q4 on 2× RTX 4090 (~48 GB) or 1× A100 80 GB. GGUF Q4 builds available for both 8B and 70B (llama.cpp).

## 5. Where To Get Weights

- HuggingFace org: https://huggingface.co/NousResearch
- **Gated:** no HF gate on Nous's side. However, since these are fine-tunes of **Meta Llama 3.1**, the Llama 3.1 Community License applies (commercial use above 700M MAU needs separate Meta agreement).
- GGUF quant repos same terms, no additional gating.

## 6. Runtime Support

As Llama 3.1 fine-tunes, Hermes 3 runs on every runtime that supports Llama 3.1: **llama.cpp** (GGUF; Nous publishes official GGUF repos for 8B and 70B), **Ollama** (GGUF), **vLLM** (BF16, FP8 via NeuralMagic/llm-compressor), **SGLang**, **Hugging Face Transformers**, and **MLX** (Apple Silicon). FP8 quantized variants are available from NeuralMagic (`neuralmagic/Hermes-3-Llama-3.1-*-FP8`). Community AWQ and GPTQ quants exist for 8B and 70B. The 405B is only practical via community GGUF Q2–Q4 with aggressive offloading.

## 7. Capabilities

Hermes 3 is purpose-built for **tool use and function calling** using both a JSON schema tool format and an XML-based structured output format (`<tool_call>` / `<tool_response>`). It supports **agentic workflows** with internal monologue / scratchpad thinking (Hermes introduced the `<scratchpad>` pattern widely adopted in the community). Code generation, multi-turn reasoning, and roleplay are also training targets. Inherits Llama 3.1's 8-language multilingual training but is not specifically optimized for it. No vision. ([Hermes 3 technical report](https://nousresearch.com/hermes3/))

## 8. Benchmarks

Public benchmark numbers (MMLU, HumanEval, SWE-bench, GAIA, ...). Cite source.

## 9. Documented Strengths

Documented strengths from benchmarks, model card, or independent testing. Cite source.

## 10. Documented Weaknesses

Documented limitations and failure modes from benchmarks, model card, or community reports. Cite source.

## 11. Sources

- [NousResearch on HuggingFace](https://huggingface.co/NousResearch) — observed 2026-06-14
