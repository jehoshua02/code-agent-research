---
name: "Hunyuan"
maker: "Tencent"
license: "Tencent Hunyuan License"
license_category: "custom-permissive"
status: "active"
url: "https://huggingface.co/tencent"
last_verified: "2026-06-14"
variants: ["Hunyuan-0.5B", "Hunyuan-1.8B", "Hunyuan-4B", "Hunyuan-7B-Instruct", "Hunyuan-MT-7B", "Hunyuan-A13B-Pretrain", "Hunyuan-A13B-Instruct", "Hunyuan-A13B-Instruct-FP8", "Hunyuan-A13B-Instruct-GPTQ-Int4", "Hunyuan-Large-389B"]
params_total: "389B"
has_moe: true
params_active: "13B"
context_window: 262144
modalities: ["text"]
gated: false
released: "2025-06"
hardware_tiers: ["8gb", "12gb", "16gb", "24gb", "24gb+"]
best_for: ["coding", "research", "data"]
notes: "Proprietary Tencent license — not Apache 2.0; minimum 2× RTX 4090 even at Q4"
---

# Hunyuan

_Last verified: 2026-06-14_

## 0. TL;DR

Hunyuan is Tencent's open-weight model family, built around a [mixture-of-experts](../GLOSSARY.md#moe-mixture-of-experts) design where only 13B of the 80B total parameters activate per request, making it more efficient to run than its total size suggests. Pick Hunyuan if you need strong Chinese-English bilingual capability with long context (up to 256K tokens), or if you want a Tencent-backed model for reasoning and agentic tasks. The main catch is the proprietary Tencent license (not Apache 2.0) that requires careful review before commercial use, and the minimum hardware bar is high — you need at least two high-end GPUs even for compressed versions.

## 1. What It Is

Hunyuan is Tencent's open-weight family. Released under the Tencent Hunyuan License — custom proprietary terms, not Apache 2.0; has commercial-use carve-outs in some jurisdictions. MoE and dense variants targeting multilingual and Chinese-language strength.

## 2. Variants

| Name | Total / Active Params | Released | Architecture | Intended Use |
|---|---|---|---|---|
| Tencent-Hunyuan-Large | 389B / 52B | Nov 2024 | MoE | General-purpose, long-context |
| Hunyuan-A13B-Pretrain | 80B / 13B | Jun 2025 | MoE | Pre-trained base for fine-tuning |
| Hunyuan-A13B-Instruct | 80B / 13B | Jun 2025 | MoE | Reasoning, agentic, coding, math, science |
| Hunyuan-A13B-Instruct-FP8 | 80B / 13B | Jun 2025 | MoE | Same as Instruct, reduced memory |
| Hunyuan-A13B-Instruct-GPTQ-Int4 | 80B / 13B | Jun 2025 | MoE | Consumer / constrained inference |

The tencent org also hosts Hy-MT (translation) and Hy3 (299B) variants.

## 3. Context Window

- Hunyuan-Large: pre-train 256K; Instruct 128K.
- Hunyuan-A13B: **256K** native (262,144). Default `config.json` caps at 32K to prevent OOM. Full 256K requires 4× NVIDIA H20 (96 GB each) BF16. INT4 + single RTX 4090 can handle ~128K (approximate per community reports).
- Recommended runtimes: vLLM 0.8.5+ or SGLang.

## 4. Hardware Requirements

Hunyuan-A13B (80B total / 13B active). Sizes from official GGUF repo:

| Precision | Approx VRAM |
|---|---|
| Q4_0 | ~45 GB |
| Q4_K_M | ~49 GB |
| Q8_0 | ~85 GB |
| FP8 (official) | ~80 GB |
| FP16/BF16 | ~160 GB |

Min viable: 2× RTX 4090 (48 GB combined) for Q4_K_M at 32K context. Full 256K needs 4× H20 96 GB. All experts must reside in VRAM, not just active.

Hunyuan-Large (389B / 52B): no official table; FP16 ~780 GB; realistically 8× A100/H100. Not consumer-runnable without heavy quant.

## 5. Where To Get Weights

- HuggingFace org: https://huggingface.co/tencent
- **Gated:** no HF access gate; publicly downloadable.
- License: Tencent's proprietary "tencent-hunyuan-a13b" license (not Apache 2.0). Review LICENSE at github.com/Tencent-Hunyuan/Hunyuan-A13B before commercial use.

## 6. Runtime Support

Primary recommended runtimes are **vLLM** (≥0.8.5) and **SGLang** for MoE expert routing at scale. **Hugging Face Transformers** is supported for smaller quants and experimentation. **llama.cpp** supports GGUF quants (official GGUF repo published by Tencent for Hunyuan-A13B). **Ollama** can load community GGUF variants. Official quantizations shipped: **FP8** (Hunyuan-A13B-Instruct-FP8) and **GPTQ-Int4** (Hunyuan-A13B-Instruct-GPTQ-Int4). GGUF (Q4_0, Q4_K_M, Q8_0) available from the Tencent GGUF repo.

## 7. Capabilities

Hunyuan-A13B-Instruct targets **reasoning** (multi-step math, science, code), **agentic behavior**, and long-context tasks (up to 256K tokens). Strong **Chinese and English** bilingual capability is a primary design goal, with some multilingual coverage. **Tool/function calling** is supported in the Instruct variant per the Tencent model card. No vision in the text-focused A13B; Tencent maintains separate Hunyuan-Vision and Hunyuan-Video models. ([Hunyuan-A13B model card](https://huggingface.co/tencent/Hunyuan-A13B-Instruct))

## 8. Benchmarks

Numbers from the official Hunyuan-A13B GitHub repository (Tencent, Jun 2025). Base model unless noted. ([github.com/Tencent-Hunyuan/Hunyuan-A13B](https://github.com/Tencent-Hunyuan/Hunyuan-A13B))

| Benchmark | Hunyuan-A13B Base | Hunyuan-A13B-Instruct |
|---|---|---|
| MMLU | 88.17 | — |
| MMLU-Pro | 67.23 | — |
| GPQA | 49.12 | — |
| MATH | 72.35 | — |
| GSM8K | 91.83 | — |
| EvalPlus | 78.64 | — |
| AIME 2024 | — | 87.3 |
| AIME 2025 | — | 76.8 |

## 9. Documented Strengths

- **Math reasoning at MoE efficiency**: Instruct scores AIME 2024 87.3 with only 13B active parameters — competitive with much larger dense models. ([Hunyuan-A13B GitHub, Jun 2025](https://github.com/Tencent-Hunyuan/Hunyuan-A13B))
- **Chinese-English bilingual**: Primary design goal; CMATH 91.17 reflects strong Chinese mathematical reasoning alongside English MMLU 88.17. ([Hunyuan-A13B GitHub, Jun 2025](https://github.com/Tencent-Hunyuan/Hunyuan-A13B))
- **Long context**: Native 256K context window (262,144 tokens), one of the longest among open-weight models in its class. ([Hunyuan-A13B model card](https://huggingface.co/tencent/Hunyuan-A13B-Instruct))
- **Official quantizations**: Tencent ships FP8 and GPTQ-Int4 variants alongside GGUF Q4/Q8, reducing the barrier to deployment on consumer clusters.

## 10. Documented Weaknesses

- **NLU and text-creation gaps**: Community evaluation finds performance gaps in ComplexNLU (61.2) and creative/text-generation tasks compared to competing models at similar active-parameter counts. ([Hunyuan-A13B GitHub, Jun 2025](https://github.com/Tencent-Hunyuan/Hunyuan-A13B))
- **High minimum hardware bar**: Q4_K_M still requires ~49 GB VRAM (2× RTX 4090); the 80B total expert weight must all reside in memory despite only 13B active per token.
- **Proprietary license**: Tencent's custom license is not Apache 2.0 and has commercial-use restrictions in some jurisdictions — requires legal review before production deployment. ([Hunyuan-A13B LICENSE](https://github.com/Tencent-Hunyuan/Hunyuan-A13B))
- **Limited third-party validation**: Relatively new model (Jun 2025) with fewer independent community benchmarks than Llama or Qwen families.

## 11. Sources

- [tencent on HuggingFace](https://huggingface.co/tencent) — observed 2026-06-14
