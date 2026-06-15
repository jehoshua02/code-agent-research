---
name: "Phi"
maker: "Microsoft"
license: "MIT"
license_category: "mit"
status: "active"
url: "https://huggingface.co/microsoft"
last_verified: "2026-06-14"
variants: ["Phi-3-mini-3.8B", "Phi-3-small-7B", "Phi-3-medium-14B", "Phi-3.5-mini-3.8B", "Phi-3.5-MoE-42B", "Phi-3.5-Vision-4.2B", "Phi-4-14B", "Phi-4-mini-3.8B", "Phi-4-multimodal-5.6B", "Phi-4-reasoning-14B", "Phi-4-reasoning-vision-15B"]
params_total: "42B"
has_moe: true
params_active: "6.6B"
context_window: 131072
modalities: ["text", "vision", "audio"]
gated: false
released: "2025-04"
hardware_tiers: ["8gb", "12gb", "16gb", "24gb", "24gb+"]
best_for: ["coding", "research", "data"]
notes: "Phi-4 has only 16K native context; family is English-first despite some multilingual support"
---

# Phi

_Last verified: 2026-06-14_

## 0. TL;DR

Phi is Microsoft's family of small language models that punch well above their weight — a 14B Phi-4 often beats much larger models on coding, math, and reasoning tasks, thanks to carefully curated synthetic training data rather than raw scale. Pick Phi if you need a capable model that runs on consumer hardware (some variants fit on a single GPU or even CPU), is MIT-licensed with zero restrictions, and excels at STEM and coding tasks. The main catch is that Phi models are English-first and the flagship Phi-4 has a shorter native context window (16K) than most peers.

## 1. What It Is

Phi is Microsoft's small-language-model family (Phi-3, Phi-4). Released under MIT license. Designed for capable performance at small parameter counts (1B–14B) via curated synthetic training data.

## 2. Variants

| Name | Total / Active Params | Released | Architecture | Intended Use |
|---|---|---|---|---|
| Phi-3-mini | 3.8B | Apr 2024 | Dense | Edge / mobile, English reasoning |
| Phi-3-small | 7B | May 2024 | Dense | Efficient mid-range |
| Phi-3-medium | 14B | May 2024 | Dense | Reasoning, math, code |
| Phi-3.5-mini | 3.8B | Aug 2024 | Dense | Multilingual, 128K context |
| Phi-3.5-MoE | 42B / 6.6B (16×3.8B, 2 active) | Aug 2024 | MoE | Cost-efficient inference |
| Phi-3.5-Vision | 4.2B | Aug 2024 | Dense + vision | Image+text, OCR, charts |
| Phi-4 | 14B | Dec 2024 | Dense | STEM reasoning, coding, math |
| Phi-4-mini | 3.8B | Feb 2025 | Dense | Edge / speed-optimized |
| Phi-4-multimodal | 5.6B | Feb 2025 | Dense + speech + vision | Speech + vision + text |
| Phi-4-reasoning | 14B | Apr 2025 | Dense | Multi-step reasoning |
| Phi-4-reasoning-vision-15B | 15B | Mar 2026 | Dense + vision | Vision-language reasoning |

## 3. Context Window

- Phi-3-mini: 4K (default) or 128K (LongRope variant).
- Phi-3-small: 8K or 128K variant.
- Phi-3-medium: 4K or 128K variant.
- Phi-3.5-mini / MoE / Vision: 128K.
- Phi-4: **16K** native (shorter than most peers).
- Phi-4-mini / multimodal: 128K.
- Phi-4-reasoning: 32K.
- Practical caveat: 128K LongRope variants degrade quality at the far end; English-first family.

## 4. Hardware Requirements

| Model | FP16 | Q8 | Q4 | Min viable GPU |
|---|---|---|---|---|
| Phi-3-mini / Phi-4-mini (3.8B) | ~7.6 GB | ~4 GB | ~2.5 GB | RTX 3060 8 GB (Q4); CPU-only viable |
| Phi-3.5-MoE (42B total) | ~84 GB | ~42 GB | ~21 GB | All experts in VRAM; Q4 fits RTX 3090/4090 |
| Phi-4 (14B) | ~28–32 GB | ~14–16 GB | ~7–8 GB | RTX 3090/4090 (Q8); RTX 4080 16 GB (Q4) |
| Phi-4-reasoning-vision-15B | ~30 GB | ~15 GB | ~8 GB | RTX 3090/4090 (Q4/Q8) |

Phi-4 (14B) at Q4 runs on ~16 GB system RAM CPU-only.

## 5. Where To Get Weights

- HuggingFace org: https://huggingface.co/microsoft
- **Gated:** no. All Phi-3, Phi-3.5, Phi-4 variants are MIT-licensed and download directly.
- Phi-4 initially released on Azure AI Foundry (Dec 2024), open-sourced under MIT on HF Jan 2025.
- Also available via Azure AI Foundry and ONNX Runtime (on-device).

## 6. Runtime Support

Supported by **Hugging Face Transformers**, **vLLM** (BF16, AWQ, GPTQ), **llama.cpp** (GGUF), **Ollama** (GGUF), and **MLX** (Apple Silicon). Microsoft also ships Phi models via **ONNX Runtime** and **DirectML** for on-device/edge deployment (Windows AI platform). Phi-3.5-MoE requires vLLM or SGLang for expert routing. Phi-4-multimodal requires a runtime with speech+vision preprocessing (transformers or Azure AI). Common quant formats: GGUF (Q2–Q8), AWQ (INT4), GPTQ (INT4/INT8), INT4 via ONNX.

## 7. Capabilities

Phi models are optimized for **STEM reasoning, coding, and math** at small parameter counts, leveraging curated synthetic training data rather than raw scale. Phi-3.5-Vision and Phi-4-multimodal add **vision** (image understanding, OCR, chart reading) and speech respectively. **Tool/function calling** is supported in Phi-3/3.5/4 Instruct variants via a structured prompt format. Phi-3.5-mini and Phi-4-mini support 128K context for long-document tasks. Primarily English-first; Phi-3.5-mini adds multilingual coverage across ~20 languages. ([Phi-4 technical report](https://arxiv.org/abs/2412.08905))

## 8. Benchmarks

Numbers for Phi-4 (14B Instruct) on the simple-evals framework, from the Phi-4 Technical Report (Dec 2024). ([arXiv:2412.08905](https://arxiv.org/abs/2412.08905))

| Benchmark | Phi-4 14B | Qwen2.5-14B | GPT-4o (reference) |
|---|---|---|---|
| MMLU | 84.8 | 79.9 | 88.1 |
| MMLU-Pro | 70.4 | 63.2 | 73.0 |
| GPQA | 56.1 | 42.9 | 50.6 |
| MATH | 80.4 | 75.6 | 74.6 |
| HumanEval | 82.6 | 72.1 | 90.6 |
| IFEval | 63.0 | 78.7 | 84.8 |

## 9. Documented Strengths

- **STEM and math at 14B**: Phi-4 scores MATH 80.4 and GPQA 56.1, exceeding GPT-4o (74.6 and 50.6 respectively) at 1/70th the parameter count. ([Phi-4 Technical Report, Dec 2024](https://arxiv.org/abs/2412.08905))
- **Consumer hardware deployment**: 14B at Q4 fits ~7–8 GB VRAM or 16 GB RAM CPU-only — unique for a model with frontier-competitive STEM scores. ([Phi-4 Technical Report, Dec 2024](https://arxiv.org/abs/2412.08905))
- **MIT license, no gating**: Download and use commercially with zero restrictions, unlike many comparable-quality models. ([microsoft/phi-4 on HuggingFace](https://huggingface.co/microsoft/phi-4))
- **Synthetic data efficiency**: Achieves strong benchmarks via curated synthetic training data rather than raw scale — explicitly outperforms its GPT-4o teacher on GPQA and MATH. ([Phi-4 Technical Report, Dec 2024](https://arxiv.org/abs/2412.08905))

## 10. Documented Weaknesses

- **Instruction following (IFEval 63.0)**: Phi-4 scores notably lower on IFEval (63.0) than same-size peers like Qwen2.5-14B (78.7) — the report explicitly notes struggles with "specific formatting requirements" and "strict tabular formats." ([Phi-4 Technical Report, Dec 2024](https://arxiv.org/abs/2412.08905))
- **Factual hallucinations**: Model size limits factual coverage; the report flags "hallucinations around factual knowledge, particularly with plausible names." ([Phi-4 Technical Report, Dec 2024](https://arxiv.org/abs/2412.08905))
- **Short native context window**: Phi-4 has only 16K native context, well below the 128K common in competing 14B-class models. ([Phi-4 Technical Report, Dec 2024](https://arxiv.org/abs/2412.08905))
- **Verbosity**: The model "tends to give long elaborate answers even for simple problems," noted as a known usability limitation in the technical report. ([Phi-4 Technical Report, Dec 2024](https://arxiv.org/abs/2412.08905))

## 11. Sources

- [microsoft on HuggingFace](https://huggingface.co/microsoft) — observed 2026-06-14
