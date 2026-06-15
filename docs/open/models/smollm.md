---
name: "SmolLM"
maker: "HuggingFace"
license: "Apache-2.0"
license_category: "apache-2.0"
status: "active"
url: "https://huggingface.co/HuggingFaceTB"
last_verified: "2026-06-14"
variants: ["SmolLM2-135M", "SmolLM2-135M-Instruct", "SmolLM2-360M", "SmolLM2-360M-Instruct", "SmolLM2-1.7B", "SmolLM2-1.7B-Instruct"]
params_total: "1.7B"
has_moe: false
context_window: 8192
modalities: ["text"]
gated: false
released: "2025-02"
hardware_tiers: ["8gb"]
best_for: ["automation"]
notes: "English-only; 135M/360M are too small for instruction following; designed for on-device edge deployment"
---

# SmolLM

_Last verified: 2026-06-14_

## 0. TL;DR

SmolLM is HuggingFace's family of tiny language models (135M to 1.7B parameters) designed to run on phones, laptops, and edge devices — the entire 1.7B model at full precision fits in about 3.4 GB of memory. Pick SmolLM if you need a privacy-preserving AI that runs entirely on-device with zero cloud dependency, and your task is simple: text rewriting, summarization, or short Q&A in English. The main catch is that these models are English-only, lack vision, and the two smallest sizes (135M, 360M) are too limited for anything beyond simple classification or text manipulation.

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

Supported by **Hugging Face Transformers** (primary, with standard `generate` API), **llama.cpp** (GGUF; all sizes including 135M), **Ollama** (GGUF), and **MLX** (Apple Silicon, excellent fit given the tiny sizes). Also deployable via **ONNX Runtime** (HuggingFace publishes ONNX exports) for browser/mobile targets. **vLLM** works but is overkill for these sizes; batch serving of SmolLM makes more sense with Transformers + TGI. Common quant formats: GGUF (Q2–Q8), ONNX (INT4/INT8), bitsandbytes 4-bit/8-bit.

## 7. Capabilities

SmolLM2-Instruct models target **on-device text tasks**: rewriting, summarization, short question answering, and light **function/tool calling** (1.7B Instruct). English-only; the small parameter count limits multilingual and complex reasoning quality. No vision. The 135M and 360M are suitable only for constrained classification or short-form generation; the 1.7B is the only variant capable of meaningful instruction following. Designed for privacy-preserving local inference rather than frontier task performance. ([SmolLM2 blog](https://huggingface.co/blog/smollm2))

## 8. Benchmarks

Scores are for the 1.7B size (the only variant capable of meaningful instruction following). Source: HuggingFace model card ([SmolLM2-1.7B-Instruct](https://huggingface.co/HuggingFaceTB/SmolLM2-1.7B-Instruct)). MMLU, HumanEval, MATH, and SWE-bench not reported; these benchmarks are designed for much larger models and are not appropriate for the 135M–1.7B range.

| Benchmark | SmolLM2-1.7B-Instruct | Llama-1B-Instruct | Qwen2.5-1.5B-Instruct |
|---|---|---|---|
| IFEval | 56.7 | 53.5 | 47.4 |
| MT-Bench | 6.13 | 5.48 | 6.52 |
| GSM8K (5-shot) | 48.2 | 26.8 | 42.8 |
| BBH (3-shot) | 32.2 | 27.6 | 35.3 |
| HellaSwag | 66.1 | 56.1 | 60.9 |
| ARC (Average) | 51.7 | 41.6 | 46.2 |
| MMLU-Pro (base, MCF) | 19.4 | 11.7 | 13.7 |

SmolLM2-1.7B-Instruct leads Llama-1B-Instruct on all reported metrics and leads Qwen2.5-1.5B-Instruct on IFEval and GSM8K, though Qwen2.5-1.5B-Instruct wins on MT-Bench and BBH.

## 9. Documented Strengths

- **Exceptional hardware efficiency**: The 1.7B model at FP16 requires only ~3.4 GB VRAM, fitting on integrated graphics and Apple Silicon unified memory; the 135M variant runs in 270 MB, enabling true browser and microcontroller inference. ([HuggingFace model card](https://huggingface.co/HuggingFaceTB/SmolLM2-1.7B-Instruct))
- **Best-in-class IFEval at ≤2B**: SmolLM2-1.7B-Instruct scores 56.7 on IFEval, outperforming both Llama-1B-Instruct (53.5) and Qwen2.5-1.5B-Instruct (47.4) on instruction adherence — the task most relevant to on-device assistant use cases. ([HuggingFace model card](https://huggingface.co/HuggingFaceTB/SmolLM2-1.7B-Instruct))
- **Apache 2.0 + ONNX exports**: Fully permissive license and official ONNX exports enable deployment in browsers (WebAssembly), Android, and iOS without licensing concerns. ([HuggingFaceTB org](https://huggingface.co/HuggingFaceTB))
- **11T-token pretraining for the size class**: Trained on significantly more tokens (11T) than the model size would suggest necessary, giving it strong knowledge density relative to its parameter count. ([SmolLM2 blog](https://huggingface.co/blog/smollm2))

## 10. Documented Weaknesses

- **135M and 360M are too small for instruction following**: Only the 1.7B variant produces meaningful instruction-following outputs; the two smaller sizes are suitable only for narrow classification or constrained template-filling tasks. ([SmolLM2 blog](https://huggingface.co/blog/smollm2))
- **English-only**: No multilingual support across any SmolLM2 variant; unsuitable for non-English tasks. ([HuggingFace model card](https://huggingface.co/HuggingFaceTB/SmolLM2-1.7B-Instruct))
- **2K context for 135M/360M**: The two smallest variants have only 2,048-token context, limiting them to single short documents or brief conversations.
- **Well behind larger models on reasoning**: BBH 32.2 and GSM8K 48.2 for the 1.7B-Instruct lag far behind 7B+ models; complex multi-step reasoning is not a reliable capability at this scale.

## 11. Sources

- [HuggingFaceTB/SmolLM2 on HuggingFace](https://huggingface.co/HuggingFaceTB) — observed 2026-06-14
