# Granite

_Last verified: 2026-06-14_

## 0. TL;DR

Granite is IBM's open-weight model family designed with enterprise use in mind — think carefully documented training data provenance, structured tool calling, and multilingual business-task performance — all under Apache 2.0 with no download restrictions. Pick Granite if you're building enterprise software and want an IBM-backed model that's safe to deploy commercially, integrates with IBM's watsonx.ai platform, and handles 12+ languages reliably. The main catch is that Granite tops out at 8B parameters in the instruct line, so it won't match frontier-scale models on complex reasoning tasks, and there's no vision capability.

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

Sources: HuggingFace model cards ([Granite-3.3-8B-Instruct](https://huggingface.co/ibm-granite/granite-3.3-8b-instruct), [Granite-3.1-8B-Instruct](https://huggingface.co/ibm-granite/granite-3.1-8b-instruct)).

| Benchmark | Granite-3.1-8B-Instruct | Granite-3.3-8B-Instruct |
|---|---|---|
| MMLU | 65.3 | 65.5 |
| MMLU-Pro | 41.0 | — |
| GPQA | 8.3 | — |
| IFEval | 72.1 | 74.8 |
| MATH-500 | — | 69.0 |
| HumanEval (pass@1) | — | 89.7 |
| HumanEval+ | — | 86.1 |
| GSM8K | 73.8 | 80.9 |
| BBH | 34.1 | 69.1 |
| Arena-Hard | — | 57.6 |

Granite-3.3-8B HumanEval of 89.7 is competitive with Llama-3.1-8B-Instruct (85.3) and approaches Qwen-2.5-7B-Instruct (93.4). GPQA and SWE-bench were not reported for Granite-3.3.

## 9. Documented Strengths

- **Documented data provenance**: IBM explicitly lists training data sources, their licenses, and data filtering methodology — a significant differentiator for enterprise risk management. Training used ~12 trillion tokens from publicly licensed and IBM-internal synthetic data only, with no undisclosed scrapes. ([Granite-3.1-8B model card](https://huggingface.co/ibm-granite/granite-3.1-8b-instruct))
- **Strong code generation**: Granite-3.3-8B-Instruct achieves HumanEval 89.7 and HumanEval+ 86.1, outperforming Llama-3.1-8B-Instruct on both metrics despite similar parameter count. ([Granite-3.3 model card](https://huggingface.co/ibm-granite/granite-3.3-8b-instruct))
- **Apache 2.0 with commercial deployment on watsonx.ai**: Fully permissive license and enterprise-grade deployment path via IBM watsonx.ai; suitable for regulated industries that need vendor accountability. ([ibm-granite org](https://huggingface.co/ibm-granite))
- **Structured reasoning in 3.3**: Native `<think>` / `<response>` tag support for chain-of-thought reasoning, improving performance on complex tasks like MATH-500 (69.0) and BBH (69.1) relative to 3.1. ([Granite-3.3 model card](https://huggingface.co/ibm-granite/granite-3.3-8b-instruct))

## 10. Documented Weaknesses

- **Small maximum model size (8B)**: The Granite 3.x instruct line tops out at 8B parameters; for tasks requiring frontier-scale reasoning, it cannot match 70B+ open models or API-based services.
- **Low GPQA score**: Granite-3.1-8B-Instruct scores 8.3 on GPQA (graduate-level scientific reasoning), indicating weak performance on complex scientific questions. ([Granite-3.1 model card](https://huggingface.co/ibm-granite/granite-3.1-8b-instruct))
- **BBH regression in 3.1**: Granite-3.1-8B scores only 34.1 on BBH (though 3.3 improves to 69.1), suggesting the earlier generation has meaningful gaps on multi-step reasoning. ([Granite-3.1 model card](https://huggingface.co/ibm-granite/granite-3.1-8b-instruct))
- **No vision in the 3.x text line**: The Granite 3.x instruct family has no multimodal capability; IBM maintains a separate Granite Vision series, complicating deployment for mixed text/image workloads.

## 11. Sources

- [ibm-granite on HuggingFace](https://huggingface.co/ibm-granite) — observed 2026-06-14
