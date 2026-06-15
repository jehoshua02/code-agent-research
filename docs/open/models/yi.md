# Yi

_Last verified: 2026-06-14_

## 0. TL;DR

Yi is a Chinese AI lab's (01.AI) open-weight model family focused on strong English and Chinese bilingual capability, with models ranging from a lightweight 6B up to a capable 34B — all under the permissive Apache 2.0 license. Pick Yi if you need a well-established bilingual model with no download restrictions and good consumer-hardware compatibility, especially for Chinese-language tasks. The main catch is that the Yi family is now somewhat dated — newer families like Qwen3 or Llama 3 have largely surpassed it — and Yi Chat models lack a native tool-calling format.

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

Numbers for Yi base models (5-shot MMLU, 8-shot GSM8K, 4-shot MATH, 0-shot HumanEval) from the Yi technical report (Mar 2024). ([arXiv:2403.04652](https://arxiv.org/abs/2403.04652)) Yi-1.5 scores are not officially published in a separate table; the 01-AI README notes Yi-1.5 improves on Yi across "reasoning, coding, math."

| Benchmark | Yi-6B | Yi-34B |
|---|---|---|
| MMLU (5-shot) | 63.2 | 76.3 |
| CMMLU (5-shot) | 75.5 | 83.7 |
| GSM8K (8-shot) | 32.5 | 67.2 |
| MATH (4-shot) | 4.6 | 14.4 |
| HumanEval (pass@1) | 15.9 | 23.2 |

Yi-34B-Chat AlpacaEval win rate: 94.08 (vs. GPT-4 baseline). ([arXiv:2403.04652](https://arxiv.org/abs/2403.04652))

## 9. Documented Strengths

- **Chinese-English bilingual**: Yi-34B CMMLU 83.7 is one of the strongest results among open models at launch (Nov 2023) for Chinese language understanding. ([Yi technical report, Mar 2024](https://arxiv.org/abs/2403.04652))
- **Apache 2.0, no gating**: Fully open download with no access form or usage cap — simpler to deploy in organizational contexts than Llama or Gemma 1–3.
- **200K long-context variant**: Yi-34B-200K extends to 200,000-token context via position interpolation, useful for very long document analysis. ([Yi technical report, Mar 2024](https://arxiv.org/abs/2403.04652))
- **Human preference (Chat)**: Yi-34B-Chat achieves a 94.08 AlpacaEval win rate, indicating strong instruction-following quality for a base-34B model at launch. ([Yi technical report, Mar 2024](https://arxiv.org/abs/2403.04652))

## 10. Documented Weaknesses

- **Math and code lag**: The technical report explicitly acknowledges "discernible disparities...particularly in tasks related to mathematics and coding" — Yi-34B MATH 14.4 is far below contemporaries like Qwen2.5-72B or DeepSeek-R1. ([Yi technical report, Mar 2024](https://arxiv.org/abs/2403.04652))
- **No native tool-calling format**: Yi-Chat models lack a structured function-call schema; tool use requires prompt engineering rather than a native runtime format.
- **Superseded by newer models**: As of mid-2025, Qwen3 and Llama 3.x outperform Yi-1.5 at all size classes on general benchmarks; 01.AI's newer work (Yi-Lightning, etc.) is closed-source.
- **Long-context coherence degradation**: Community reports note that the 200K context models degrade in quality beyond ~32K tokens in practice. ([Yi technical report, Mar 2024](https://arxiv.org/abs/2403.04652))

## 11. Sources

- [01-ai on HuggingFace](https://huggingface.co/01-ai) — observed 2026-06-14
