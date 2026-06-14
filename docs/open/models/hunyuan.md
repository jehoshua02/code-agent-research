# Hunyuan

_Last verified: 2026-06-14_

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

Public benchmark numbers (MMLU, HumanEval, SWE-bench, GAIA, ...). Cite source.

## 9. Documented Strengths

Documented strengths from benchmarks, model card, or independent testing. Cite source.

## 10. Documented Weaknesses

Documented limitations and failure modes from benchmarks, model card, or community reports. Cite source.

## 11. Sources

- [tencent on HuggingFace](https://huggingface.co/tencent) — observed 2026-06-14
