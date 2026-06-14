# Mistral

_Last verified: 2026-06-14_

## 1. What It Is

Mistral is Mistral AI's open-weight family. Smaller models (Mistral 7B, Mixtral 8x7B/8x22B, Mistral Small, Codestral Mamba) under Apache 2.0; flagship Mistral Large under Mistral Research License (non-commercial unless licensed). Dense and MoE architectures.

## 2. Variants

| Name | Total / Active Params | Released | Architecture | License | Intended Use |
|---|---|---|---|---|---|
| Mistral-7B-Instruct v0.3 | 7B | May 2024 | Dense | Apache 2.0 | General chat, function calling |
| Mixtral-8x7B-Instruct | 47B / ~13B | Dec 2023 | MoE | Apache 2.0 | General chat |
| Mixtral-8x22B-Instruct | 141B / 39B | Apr 2024 | MoE | Apache 2.0 | Reasoning, coding, multilingual |
| Mistral-NeMo-Instruct-2407 | 12B | Jul 2024 | Dense (w/ NVIDIA) | Apache 2.0 | Drop-in mid-size, multilingual |
| Mistral-Large-Instruct-2407 | 123B | Jul 2024 | Dense | Mistral Research License (NC) | Complex reasoning |
| Codestral-22B v0.1 | 22B | May 2024 | Dense | MNLP-0.1 (non-prod) | Code, 80+ languages, FIM |
| Mistral-Small-3.1 | 24B | Mar 2025 | Dense multimodal | Apache 2.0 | Multimodal, agentic |
| Mistral-Large-3 | 675B / 41B | Dec 2025 | MoE | Apache 2.0 | Frontier reasoning, agentic, multimodal |

## 3. Context Window

- Mistral-7B v0.3: 32,768.
- Mixtral-8x7B: 32,768.
- Mixtral-8x22B: ~65,536 (64K).
- Mistral NeMo 12B: 128K (trained with FP8 quant awareness).
- Mistral Large 2 (2407): 128K.
- Codestral-22B v0.1: 32K.
- Mistral Small 3.1: 128K.
- Mistral Large 3: 256K.
- Practical caveat: KV-cache VRAM grows fast above 32K; vLLM / `mistral-inference` with paged attention recommended.

## 4. Hardware Requirements

| Model | FP16 | Q8 | Q4 | Min viable GPU |
|---|---|---|---|---|
| Mistral-7B | ~14 GB | ~7.5 GB | ~4 GB | RTX 3060 12 GB (Q4); 3090 (FP16) |
| Mixtral-8x7B | ~94 GB | ~47 GB | ~27 GB | 2× RTX 3090/4090 (Q4); 4× A100 (FP16) |
| Mixtral-8x22B | ~282 GB | ~141 GB | ~70 GB | 3–4× 24 GB (Q4); 8× A100 80 GB (FP16) |
| Mistral NeMo 12B | ~24 GB | ~12 GB | ~6.5 GB | RTX 3060 12 GB (Q4); 3090 (Q8) |
| Mistral Large 2 (123B) | ~246 GB | ~123 GB | ~62 GB | Multi-GPU cluster |
| Codestral-22B | ~44 GB | ~22 GB | ~12 GB | RTX 3090/4090 (Q4/Q8) |
| Mistral Small 3.1 (24B) | ~48 GB | ~24 GB | ~13 GB | RTX 3090/4090 (Q4/Q8) |
| Mistral Large 3 (675B MoE) | ~1350 GB | ~675 GB | ~338 GB | 8–16× H100 80 GB at Q4 |

System RAM for CPU offload: roughly 2× model size at chosen precision.

## 5. Where To Get Weights

- HuggingFace org: https://huggingface.co/mistralai
- **Gated:** no for Apache 2.0 models (Mistral 7B, Mixtral, NeMo, Small 3.1, Large 3). Yes for Codestral-22B v0.1 (MNLP-0.1, non-commercial) and Mistral-Large-Instruct-2407 (Mistral Research License, non-commercial) — must accept on HF.
- Codestral 2 (Apr 2026) was relicensed to Apache 2.0.
- Also on Mistral's La Plateforme, AWS, Azure, GCP.

## 6. Runtime Support

Supported by **vLLM** (BF16, FP8, AWQ, GPTQ), **SGLang**, **Hugging Face Transformers**, **llama.cpp** (GGUF), and **Ollama** (GGUF). Mistral also ships `mistral-inference`, their own lightweight reference server. MoE models (Mixtral, Mistral Large 3) need vLLM ≥0.5 or SGLang for expert routing. **MLX** supports smaller sizes (7B, 12B, 24B) on Apple Silicon. Common quant formats: GGUF (Q2–Q8), AWQ (INT4), GPTQ (INT4/INT8), FP8 (NeMo 12B and Large 3).

## 7. Capabilities

Mistral Instruct models are trained for general instruction following and **function/tool calling** via a structured `[TOOL_CALLS]` format (introduced in Mistral-7B v0.3 and Mixtral). Codestral specializes in code generation with fill-in-the-middle (FIM) across 80+ programming languages. Mistral Small 3.1 and Large 3 add **vision** (image understanding) and stronger agentic behavior. Strong multilingual support across European languages (EN, FR, DE, ES, IT, PT, RU); Mixtral-8x22B and NeMo 12B especially strong on multilingual tasks. ([Mistral function calling docs](https://docs.mistral.ai/capabilities/function_calling/))

## 8. Benchmarks

Public benchmark numbers (MMLU, HumanEval, SWE-bench, GAIA, ...). Cite source.

## 9. Documented Strengths

Documented strengths from benchmarks, model card, or independent testing. Cite source.

## 10. Documented Weaknesses

Documented limitations and failure modes from benchmarks, model card, or community reports. Cite source.

## 11. Sources

- [mistralai on HuggingFace](https://huggingface.co/mistralai) — observed 2026-06-14
