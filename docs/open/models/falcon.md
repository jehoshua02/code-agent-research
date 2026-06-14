# Falcon

_Last verified: 2026-06-14_

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

- [tiiuae on HuggingFace](https://huggingface.co/tiiuae) — observed 2026-06-14
