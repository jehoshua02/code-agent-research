# Granite

_Last verified: 2026-06-14_

## 1. What It Is

Granite is IBM's open-weight family. Released under Apache 2.0. Enterprise-oriented general-purpose, code, time-series, and embedding models with attention to data provenance and licensing transparency.

## 2. Variants

**Granite 3.1** (Dec 18, 2024):

| Name | Total / Active Params | Architecture | Intended Use |
|---|---|---|---|
| Granite-3.1-1B-A400M-Instruct | 1.3B / 400M | MoE | Lightweight instruction following |
| Granite-3.1-2B-Instruct | 2.5B | Dense | General assistant |
| Granite-3.1-3B-A800M-Instruct | 3.3B / 800M | MoE | Efficient instruction following |
| Granite-3.1-8B-Instruct | 8.1B | Dense | General assistant |

**Granite 3.3** (Apr 16, 2025):

| Name | Params | Architecture | Intended Use |
|---|---|---|---|
| Granite-3.3-2B-Instruct | 2B | Dense | Reasoning, instruction following |
| Granite-3.3-8B-Instruct | 8B | Dense | Enterprise assistant; structured reasoning via `<think>` / `<response>` tags |

Both generations support 12+ languages (en, de, es, fr, ja, pt, ar, cs, it, ko, nl, zh).

## 3. Context Window

All Granite 3.1 and 3.3 models: **128K tokens** native. Practical caveat: at 128K, KV cache for the 8B at FP16 can require 32–40 GB on top of weights — full 128K realistically needs an A100 80 GB or H100. Shorter contexts (8K–32K) fit a single 24 GB GPU.

## 4. Hardware Requirements

No official VRAM table in model cards; estimates from standard scaling.

| Variant | Q4 | Q8 | FP16/BF16 |
|---|---|---|---|
| Granite-3.x-2B | ~1.5 GB | ~2.5 GB | ~5 GB |
| Granite-3.x-8B | ~5 GB | ~9 GB | ~16 GB |

Min viable for 8B at FP16: RTX 3080/4070 Ti 16 GB. Q4: RTX 3060 12 GB, or even 3050 8 GB with headroom. 16–32 GB system RAM for CPU offload.

## 5. Where To Get Weights

- HuggingFace org: https://huggingface.co/ibm-granite
- **Gated:** no. **License:** Apache 2.0. Direct download.

## 6. Runtime Support

Supported by **Hugging Face Transformers** (primary; IBM publishes examples using transformers), **vLLM** (BF16, AWQ, GPTQ), **llama.cpp** (community GGUF quants), and **Ollama** (GGUF). IBM also deploys Granite via **watsonx.ai** (their enterprise AI platform). **SGLang** supports the standard dense sizes. MoE variants (3.1-1B-A400M, 3.1-3B-A800M) work with vLLM's MoE routing. Common quant formats: GGUF (Q2–Q8), GPTQ (INT4/INT8), AWQ (community sources). IBM ships official GGUF and quantized variants in the `ibm-granite` HF org.

## 7. Capabilities

Granite 3.x models are trained for **enterprise instruction following** in 12+ languages (EN, DE, ES, FR, JA, PT, AR, CS, IT, KO, NL, ZH), with emphasis on safe and reliable outputs suitable for business contexts. **Tool/function calling** is natively supported — model cards document a structured tool-call format. **Code generation** is a strength (separate Granite-Code models exist; the 3.x instruct line also handles code). Granite-3.3 adds structured reasoning via `<think>` / `<response>` tags. No vision in the 3.x text line; IBM maintains separate Granite Guardian (safety) and Granite Vision models. ([Granite 3.3 model card](https://huggingface.co/ibm-granite/granite-3.3-8b-instruct))

## 8. Benchmarks

Public benchmark numbers (MMLU, HumanEval, SWE-bench, GAIA, ...). Cite source.

## 9. Documented Strengths

Documented strengths from benchmarks, model card, or independent testing. Cite source.

## 10. Documented Weaknesses

Documented limitations and failure modes from benchmarks, model card, or community reports. Cite source.

## 11. Sources

- [ibm-granite on HuggingFace](https://huggingface.co/ibm-granite) — observed 2026-06-14
