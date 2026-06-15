# Yi

_Last verified: 2026-06-14_

## 1. What It Is

Yi is 01.AI's open-weight family. Modern checkpoints released under Apache 2.0 (earlier under a custom Yi license). General-purpose models with bilingual English/Chinese strength.

## 2. Variants

| Name | Params | Released | Intended Use |
|---|---|---|---|
| Yi-6B / 6B-Chat | 6B | Nov 2023 | Lightweight base / chat |
| Yi-9B / 9B-200K | 9B | 2024 | Mid-size general / long-context |
| Yi-34B / 34B-Chat | 34B | Nov 2023 | General base / chat |
| Yi-34B-200K | 34B | Nov 2023 | Long-document (200K context) |
| Yi-34B-Chat-4bits / 8bits | 34B | Nov 2023 | Quantized chat for consumer HW |
| Yi-1.5-6B / 9B / 34B (+ Chat) | 6B / 9B / 34B | May 2024 | Improved continued-pretrain; reasoning, code, math |
| Yi-Coder family | <10B | Sep 2024 | Code generation |
| Yi-VL (6B / 34B) | 6B / 34B | Jan 2024 | Vision-language multimodal |

## 3. Context Window

- Yi v1 base / chat (34B / 6B): **4K** native.
- Yi-200K variants (34B / 9B / 6B): extended to **200K** via position interpolation.
- Yi-1.5: 4K default; 16K / 32K variants for 9B / 34B (named accordingly).
- Practical caveat: community reports note degraded coherence beyond ~32K on the original 200K models.

## 4. Hardware Requirements

Estimates from standard formulas (no official 01.AI table).

| Model | FP16 | Q8 | Q4 | Min viable GPU |
|---|---|---|---|---|
| Yi-6B | ~12 GB | ~6 GB | ~4 GB | RTX 3060 12 GB (Q4); 3080 (Q8) |
| Yi-9B | ~18 GB | ~9 GB | ~5 GB | RTX 3060 12 GB (Q4/Q8); 3090 (FP16) |
| Yi-34B | ~68 GB | ~34 GB | ~17 GB | RTX 4090 24 GB (Q4); 2× A100 40 GB (FP16) |

CPU offload viable; 32 GB system RAM recommended for 34B partial offload.

## 5. Where To Get Weights

- HuggingFace org: https://huggingface.co/01-ai
- **Gated:** no — direct download, no auth required.
- License: **Apache 2.0** for all Yi and Yi-1.5 series.

## 6. Runtime Support

Supported by **Hugging Face Transformers** (all sizes), **vLLM** (BF16, AWQ, GPTQ), **llama.cpp** (GGUF, community quants via TheBloke and bartowski), and **Ollama** (GGUF). **SGLang** and **MLX** support the standard sizes. Yi-VL requires a runtime with vision preprocessing (transformers with vision extras). Official GPTQ-Int4 and GPTQ-Int8 quants shipped for Yi-34B-Chat; community GGUF covers Q2–Q8 for all sizes. AWQ is available from community sources.

## 7. Capabilities

Yi and Yi-1.5 are bilingual **English and Chinese** general-purpose models trained for instruction following, coding (Yi-Coder), math, and reasoning. Yi-VL (6B / 34B) adds **vision-language** capability (image understanding). Yi-Chat models support basic instruction following but do not have an official structured **tool/function calling** format — users typically prompt-engineer tool use rather than using a native schema. Yi-1.5 improved reasoning and math over the original Yi through continued pretraining. ([Yi technical report](https://arxiv.org/abs/2403.04652))

## 8. Benchmarks

Public benchmark numbers (MMLU, HumanEval, SWE-bench, GAIA, ...). Cite source.

## 9. Documented Strengths

Documented strengths from benchmarks, model card, or independent testing. Cite source.

## 10. Documented Weaknesses

Documented limitations and failure modes from benchmarks, model card, or community reports. Cite source.

## 11. Sources

- [01-ai on HuggingFace](https://huggingface.co/01-ai) — observed 2026-06-14
