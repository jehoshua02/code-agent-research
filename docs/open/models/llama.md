# Llama

_Last verified: 2026-06-14_

## 0. TL;DR

Llama is Meta's family of open-weight language models — think of them as freely downloadable AI brains you can run on your own hardware. Pick Llama if you want the broadest ecosystem support: more tutorials, tools, and community [quantizations](../GLOSSARY.md#quantization) exist for Llama than almost any other open model. The main catch is that the license restricts commercial apps with over 700 million monthly active users, and the largest models require expensive data-center GPUs (like an A100 or H100).

## 1. What It Is

Llama is Meta's open-weight model family (Llama 3.1, 3.2, 3.3, Llama 4 as of 2026). Released under the Llama Community License — permissive for most uses but with conditions (700M MAU cap, naming, AUP). General-purpose decoder-only transformers in dense and MoE variants; long context, multilingual.

## 2. Variants

| Name | Total / Active Params | Released | Architecture | Intended Use |
|---|---|---|---|---|
| Llama 3.1 8B Instruct | 8B | Jul 2024 | Dense | Multilingual chat, distillation source |
| Llama 3.1 70B Instruct | 70B | Jul 2024 | Dense | Multilingual chat, commercial deployment |
| Llama 3.1 405B Instruct | 405B | Jul 2024 | Dense | Frontier-scale chat, synthetic data generation |
| Llama 3.2 1B / 3B Instruct | 1B / 3B | Sep 2024 | Dense | On-device / mobile edge |
| Llama 3.2 11B / 90B Vision Instruct | 11B / 90B | Sep 2024 | Dense + vision | Multimodal chat, image understanding |
| Llama 3.3 70B Instruct | 70B | Dec 2024 | Dense | Improved successor to 3.1 70B |
| Llama 4 Scout 17B-16E | 109B total / 17B active | Apr 2025 | MoE (16 experts) | Multimodal, long-context (10M) |
| Llama 4 Maverick 17B-128E | 400B total / 17B active | Apr 2025 | MoE (128 experts) | Multimodal, high-capacity |

A base (pre-trained) variant exists for each Instruct model.

## 3. Context Window

- Llama 3.1 / 3.2 / 3.3: **128K tokens** native (RoPE theta 500,000).
- Llama 4 Scout: **10M tokens** native (headline figure; practical long-context throughput not widely benchmarked publicly).
- Llama 4 Maverick: **1M tokens** native.
- Practical caveat: above ~32K, KV cache memory grows substantially. vLLM/SGLang with chunked prefill recommended for long contexts.

## 4. Hardware Requirements

No official VRAM table from Meta; figures below are standard estimates (FP16 ≈ 2 GB/param, Q8 ≈ 1, Q4 ≈ 0.5) plus overhead.

| Variant | FP16/BF16 | Q8 | Q4 | Min viable GPU |
|---|---|---|---|---|
| 3.2 1B | ~2.5 GB | ~1.5 GB | ~1 GB | Mobile / consumer 4 GB |
| 8B | ~16 GB | ~8 GB | ~5 GB | RTX 3080 10 GB (Q4); RTX 3090/4090 (FP16) |
| 70B | ~140 GB | ~70 GB | ~40 GB | 1× A100 80 GB (Q4); 2× A100 80 GB (FP16) |
| 405B | ~810 GB | ~405 GB | ~200 GB | 4× A100 80 GB (Q4); 8× H100 80 GB (FP16) |
| Scout (109B total) | ~218 GB | ~109 GB | ~55 GB | Single H100 80 GB at INT4 |
| Maverick (400B total) | ~800 GB | ~400 GB | ~200 GB | Single H100 DGX host at FP8 (per Meta) |

For MoE variants, all expert weights must reside in VRAM (or be offloaded), not just active experts. CPU offload via llama.cpp viable for ≤70B with ≥64 GB system RAM (slow throughput).

## 5. Where To Get Weights

- HuggingFace org: https://huggingface.co/meta-llama
- **Gated:** yes. Every Llama 3.x / 4.x repo requires accepting the Llama Community License Agreement (name, email/org, agree to AUP). Access is auto-granted; per-repo acceptance required.
- License: Llama Community License (commercially permissive; entities with >700M MAU need explicit Meta permission).
- Weights ship as BF16; Llama 4 Maverick also ships FP8. Community GGUF quants on HF (TheBloke, bartowski).

## 6. Runtime Support

Supported by all major runtimes: **llama.cpp** (native GGUF; first-class support, name derived from Llama), **Ollama** (GGUF, wraps llama.cpp), **vLLM** (BF16/FP8/AWQ/GPTQ), **SGLang** (BF16/FP8), **Hugging Face Transformers** (BF16), **MLX** (Apple Silicon, MLX-LM). Llama 4 MoE requires vLLM ≥0.8 or SGLang for efficient expert routing. Common quant formats: GGUF (Q2–Q8, IQ variants), AWQ (INT4), GPTQ (INT4/INT8), FP8 (Llama 4 Maverick official).

## 7. Capabilities

Llama 3.1/3.2/3.3 Instruct models are trained for multilingual chat (8 languages: EN, DE, FR, IT, PT, HI, ES, TH), code generation, and **tool/function calling** via a structured `<|python_tag|>` / tool-call format. Llama 3.2 11B/90B add **vision** (image understanding). Llama 4 Scout and Maverick extend to native multimodal (image + text) and extremely long context. ([Meta Llama 3 model card](https://huggingface.co/meta-llama/Meta-Llama-3.1-8B-Instruct))

## 8. Benchmarks

Public benchmark numbers (MMLU, HumanEval, SWE-bench, GAIA, ...). Cite source.

## 9. Documented Strengths

Documented strengths from benchmarks, model card, or independent testing. Cite source.

## 10. Documented Weaknesses

Documented limitations and failure modes from benchmarks, model card, or community reports. Cite source.

## 11. Sources

- [meta-llama on HuggingFace](https://huggingface.co/meta-llama) — observed 2026-06-14
