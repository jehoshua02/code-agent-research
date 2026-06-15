# DeepSeek

_Last verified: 2026-06-14_

## 1. What It Is

DeepSeek is DeepSeek AI's open-weight family. V2 and V3 use the DeepSeek License (permissive, commercial use allowed); R1 reasoning model released MIT. DeepSeek-V3 is a 671B-total / 37B-active MoE; R1 is a reasoning-focused variant trained with RL.

## 2. Variants

| Name | Total / Active Params | Released | Architecture | Intended Use |
|---|---|---|---|---|
| DeepSeek-V2 | 236B / 21B | May 2024 | MoE | General chat / coding, economical inference |
| DeepSeek-V2.5 | 236B / 21B | Sep 2024 | MoE | Merged general + coding update |
| DeepSeek-V3 | 671B / 37B | Dec 2024 | MoE | General chat, coding, math, reasoning |
| DeepSeek-V3-0324 | 685B / ~37B | Mar 2025 | MoE | Updated V3 |
| DeepSeek-R1 | 671B / 37B | Jan 2025 | MoE | Chain-of-thought reasoning |
| DeepSeek-R1-0528 | 685B / ~37B | May 2025 | MoE | Improved R1; function calling |
| R1-Distill-Qwen-1.5B / 7B / 14B / 32B | 1.5B / 7B / 14B / 32B | Jan 2025 | Dense (Qwen2.5 base) | Accessible reasoning |
| R1-Distill-Llama-8B / 70B | 8B / 70B | Jan 2025 | Dense (Llama 3 base) | Accessible reasoning |

## 3. Context Window

- V2, V3, V3-0324, R1, R1-0528: **128K tokens** native.
- R1-Distill variants: 128K (inherited from Qwen2.5 / Llama 3 bases).
- Practical caveats: model cards explicitly note limited HuggingFace Transformers support for full V3/R1 — vLLM, SGLang, and LMDeploy recommended. At 128K, KV cache management dominates; practical context often capped at 32K–64K in small clusters.

## 4. Hardware Requirements

No official per-quantization table. DeepSeek ships native FP8 for V3/R1.

| Variant | FP16/BF16 | Q8 | Q4 | Min viable config |
|---|---|---|---|---|
| R1-Distill-Qwen-7B | ~14 GB | ~7 GB | ~4.5 GB | RTX 3080 (Q4), RTX 3090 (Q8) |
| R1-Distill-Llama-8B | ~16 GB | ~8 GB | ~5 GB | RTX 3080 (Q4); 3090/4090 (FP16) |
| R1-Distill-Qwen-14B | ~28 GB | ~14 GB | ~8 GB | RTX 4090 (Q4); 2× RTX 3090 (FP16) |
| R1-Distill-Qwen-32B | ~64 GB | ~32 GB | ~18 GB | 2× RTX 4090 (Q4/Q8); A100 80 GB (FP16) |
| R1-Distill-Llama-70B | ~140 GB | ~70 GB | ~40 GB | 1× A100 80 GB (Q4); 2× A100 80 GB (FP16) |
| V3 / R1 (671B MoE) | ~1340 GB | ~670 GB | ~336 GB | Native FP8 ~336 GB → 4× H100 80 GB / 8× A100 40 GB |

All 671B weights must reside in VRAM (or be offloaded) despite only 37B active per token. Community GGUF Q4 quants can run the full 671B with ~200 GB VRAM + fast NVMe offload, or ~360 GB RAM CPU-only (very slow).

## 5. Where To Get Weights

- HuggingFace org: https://huggingface.co/deepseek-ai
- **Gated:** no — direct download via `huggingface-cli` or URL, no auth required.
- Licenses: code/inference scripts under MIT; weights under the DeepSeek Model License (commercial use and derivatives permitted, distillation allowed). R1 distill variants are MIT.
- Official FP8 weights live in the primary repos; community GGUF quants on separate HF repos.

## 6. Runtime Support

Full-size V3/R1 (671B MoE) are best served by **vLLM** (≥0.6, with FP8 and expert-parallel support) or **SGLang** (recommended in model cards); **LMDeploy** also supported. **llama.cpp** supports GGUF quants of all sizes including the 671B (CPU/GPU offload). **Ollama** wraps llama.cpp and ships community GGUF quants. R1-Distill variants run on **Hugging Face Transformers** without special handling. **MLX** supports distill sizes on Apple Silicon. Formats: FP8 (official V3/R1), GGUF (Q2–Q8), AWQ and GPTQ available for distill variants.

## 7. Capabilities

DeepSeek-V3 and R1 target **code generation**, math reasoning, and general instruction following; R1 specifically emphasizes chain-of-thought reasoning trained via reinforcement learning without supervised reasoning labels. **Tool/function calling** was added in R1-0528 (May 2025); earlier V3/R1 had limited or no official function-call support. No vision capability in the main V3/R1 family; DeepSeek-VL2 is a separate multimodal line. Strong English and Chinese; limited other language coverage. ([DeepSeek-R1 paper, Jan 2025](https://arxiv.org/abs/2501.12948))

## 8. Benchmarks

Public benchmark numbers (MMLU, HumanEval, SWE-bench, GAIA, ...). Cite source.

## 9. Documented Strengths

Documented strengths from benchmarks, model card, or independent testing. Cite source.

## 10. Documented Weaknesses

Documented limitations and failure modes from benchmarks, model card, or community reports. Cite source.

## 11. Sources

- [deepseek-ai on HuggingFace](https://huggingface.co/deepseek-ai) — observed 2026-06-14
