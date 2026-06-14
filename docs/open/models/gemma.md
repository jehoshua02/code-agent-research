# Gemma

_Last verified: 2026-06-14_

## 1. What It Is

Gemma is Google's open-weight family (Gemma 2, Gemma 3). Released under Gemma Terms of Use — permissive for most uses but with prohibited-use restrictions; not strictly OSI-open. Derived from Gemini research, intended for responsible open development.

## 2. Variants

| Name | Params | Released | Architecture | License | Intended Use |
|---|---|---|---|---|---|
| Gemma 1 (2B / 7B) | 2B / 7B | Feb 2024 | Dense | Gemma | Text gen, research; English |
| Gemma 2 (2B / 9B / 27B) | 2.6B / 9B / 27B | Jun–Jul 2024 | Dense (interleaved attention) | Gemma | General text; English |
| Gemma 3 (1B) | 1B | Mar 2025 | Dense | Gemma | Lightweight; text-only |
| Gemma 3 (4B / 12B / 27B) | 4B / 12B / 27B | Mar 2025 | Dense + vision | Gemma | Multimodal, 140+ languages |
| Gemma 4 (E2B / E4B) | ~2B / ~4B effective | Apr 2026 | MoE-based | Apache 2.0 | Edge, multimodal |
| Gemma 4 (26B A4B) | 26B / ~4B | Apr 2026 | MoE | Apache 2.0 | Vision, audio, reasoning |
| Gemma 4 (31B) | 31B | Apr 2026 | Dense + multimodal | Apache 2.0 | Flagship; text+image+audio |

## 3. Context Window

- Gemma 1: 8K.
- Gemma 2 (all sizes): **8,192** native; uses interleaved sliding-window (4K) + global (8K) attention. Effective long-range retrieval often limited to ~4K.
- Gemma 3 1B: 32K.
- Gemma 3 4B / 12B / 27B: **128K** input, 8K output max. Images encode to 256 tokens each at 896×896.
- Gemma 4 E2B / E4B: 128K.
- Gemma 4 26B / 31B: 256K.

## 4. Hardware Requirements

| Model | FP16/BF16 | Q8 | Q4 | Min viable GPU |
|---|---|---|---|---|
| Gemma 3 1B | ~2 GB | ~1 GB | ~0.6 GB | Any modern GPU / CPU |
| Gemma 2 2B | ~5 GB | ~2.6 GB | ~1.4 GB | Any 4 GB+ GPU |
| Gemma 3 4B | ~8 GB | ~4 GB | ~2.2 GB | RTX 3060 8 GB |
| Gemma 2 9B | ~18 GB | ~9 GB | ~5.7 GB | RTX 3090 (FP16); 3060 12 GB (Q8); RTX 2070 (Q4) |
| Gemma 3 12B | ~24 GB | ~12.6 GB | ~6.7 GB | RTX 4090 (FP16 at limit); 3060 12 GB (Q8) |
| Gemma 2 / 3 27B | ~54 GB | ~27 GB | ~15 GB | 2× A100 40 GB (FP16); RTX 4090 24 GB (Q4) |

Native weights are BF16. Community GGUF via bartowski; also via Ollama.

## 5. Where To Get Weights

- HuggingFace org: https://huggingface.co/google
- **Gated:** yes for Gemma 1 / 2 / 3 — must accept Gemma Terms of Use on HF (instant grant; no manual review).
- **Gemma 4:** Apache 2.0 — no gating. Significant policy shift from earlier generations.
- Also on Google AI Studio, Vertex AI Model Garden, Kaggle, Ollama.
- Instruct variants labeled `-it`; base variants labeled `-pt` (or unlabeled).

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

- [google/gemma collection on HuggingFace](https://huggingface.co/google) — observed 2026-06-14
