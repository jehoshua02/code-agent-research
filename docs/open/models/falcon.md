# Falcon

_Last verified: 2026-06-14_

## 0. TL;DR

Falcon is the UAE's Technology Innovation Institute open-weight model family, notable for its newer Falcon-H1 line that uses a hybrid architecture blending traditional attention with a state-space model to handle very long contexts (up to 256K tokens) more efficiently. Pick Falcon if you want an Apache 2.0 model with genuinely long-context capability, or if geopolitical/lab diversity in your model stack matters to you. The main catch is that Falcon lacks any built-in tool/function calling and no vision support, and the older Falcon 1 series is severely limited to 2K context — effectively obsolete for most modern tasks.

## 1. What It Is

Falcon is TII (UAE Technology Innovation Institute)'s open-weight family. Older Falcon-180B/40B under TII Falcon License; Falcon3 and newer under Apache 2.0. Multilingual general-purpose models.

## 2. Variants

| Name | Params | Released | Architecture | License | Intended Use |
|---|---|---|---|---|---|
| Falcon-7B / 7B-Instruct | 7B | Mar 2023 | Dense | Apache 2.0 | General base / chat |
| Falcon-40B / 40B-Instruct | 40B | Mar 2023 | Dense | Apache 2.0 | General base / chat |
| Falcon-180B / 180B-Chat | 180B | Sep 2023 | Dense | TII Falcon License | Flagship; research use |
| Falcon3-1B / 3B / 7B / 10B (Base + Instruct) | 1B–10B | Dec 2024 | Dense | Apache 2.0 | Reasoning, code, multilingual (EN/FR/ES/PT) |
| Falcon-H1-0.5B / 1.5B / 3B / 7B / 34B | 0.5B–34B | May 2025 | Hybrid SSM + Attention | Apache 2.0 | Long-context, multilingual |
| Falcon-H1R-7B | 7B | Jan 2026 | Hybrid | Apache 2.0 | Reasoning-focused H1 variant |

## 3. Context Window

- Falcon 1 (7B / 40B / 180B): **2K** (2,048 tokens) — significant limitation.
- Falcon 3 (1B–10B): **32K** (32,768).
- Falcon H1 (all sizes): **256K** (262,144) via hybrid SSM+Attention.
- Falcon H1R-7B: 256K.
- Practical caveat: Falcon 1's 2K limit cannot be easily extended post-hoc; H1's 256K is native but generation speed degrades at very long contexts.

## 4. Hardware Requirements

Falcon 1 series (official 40B/180B sources; 7B from standard formulas):

| Model | Q4 | Q8 | FP16 | Notes |
|---|---|---|---|---|
| Falcon-7B | ~4–6 GB | ~8 GB | ~15 GB | RTX 3060 12 GB viable Q4/Q8 |
| Falcon-40B | ~19–22 GB | ~40 GB | ~77–80 GB | RTX 4090 (Q4); A100 80 GB (FP16) |
| Falcon-180B | ~90 GB | ~180 GB | ~400 GB | 8× A100 40 GB (Q4); 5× A100 80 GB (FP16) |

Falcon 3 and H1 (representative; standard formula, no official table):

| Model | Q4 | Q8 | FP16 |
|---|---|---|---|
| Falcon3-10B | ~6 GB | ~10 GB | ~20 GB |
| Falcon-H1-7B | ~4 GB | ~7 GB | ~14 GB |
| Falcon-H1-34B | ~17 GB | ~34 GB | ~68 GB |

GGUF and GPTQ variants for H1 via tiiuae and community repos.

## 5. Where To Get Weights

- HuggingFace org: https://huggingface.co/tiiuae
- **Gated:** Falcon-180B requires accepting an AUP on HF before download. Falcon 1 (7B / 40B), Falcon 3, Falcon H1 are not gated.
- Licenses: Falcon-7B / 40B / Falcon 3 / Falcon H1 under **Apache 2.0**. Falcon-180B under custom TII Falcon License (Apache-2.0-based + extra restrictions).

## 6. Runtime Support

Falcon 1/3 are widely supported by **Hugging Face Transformers**, **vLLM** (BF16, AWQ, GPTQ), **llama.cpp** (GGUF via community), and **Ollama** (GGUF). **Falcon-H1** (hybrid SSM+Attention) requires Transformers ≥4.51 with Mamba/SSM kernel support; vLLM added H1 support alongside the launch. GGUF and GPTQ quants for H1 are published by tiiuae on HF. **SGLang** and **MLX** support varies — Falcon 1/3 are broadly compatible; H1's hybrid architecture may need runtime-specific patches. Quant formats: GGUF (Q2–Q8), GPTQ (INT4/INT8), AWQ (community), FP8 (H1 server variants).

## 7. Capabilities

Falcon 1 models (7B/40B/180B) target general English instruction following; 2K context limits their utility for long tasks. Falcon 3 adds **reasoning, code, and multilingual** coverage (EN, FR, ES, PT) with 32K context. Falcon-H1 targets **long-context** tasks (up to 256K) using a hybrid SSM+Attention architecture for efficient memory use; the H1R-7B variant adds reasoning focus. No vision capability in any Falcon variant; no official structured **tool/function calling** schema — function use requires prompt engineering. ([Falcon-H1 announcement](https://huggingface.co/blog/falcon-h1))

## 8. Benchmarks

Public benchmark numbers (MMLU, HumanEval, SWE-bench, GAIA, ...). Cite source.

## 9. Documented Strengths

Documented strengths from benchmarks, model card, or independent testing. Cite source.

## 10. Documented Weaknesses

Documented limitations and failure modes from benchmarks, model card, or community reports. Cite source.

## 11. Sources

- [tiiuae on HuggingFace](https://huggingface.co/tiiuae) — observed 2026-06-14
