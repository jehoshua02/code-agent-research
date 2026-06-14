# Phi

_Last verified: 2026-06-14_

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

- [microsoft on HuggingFace](https://huggingface.co/microsoft) — observed 2026-06-14
