# Gemma

_Last verified: 2026-06-14_

## 0. TL;DR

Gemma is Google's open-weight model family built on the same research as Gemini, covering tiny 1B edge models all the way up to a capable 31B multimodal flagship that handles text, images, and audio. Pick Gemma if you want a Google-pedigree model with broad runtime support (including Google's own tools and TPUs), strong multilingual coverage (140+ languages in Gemma 3+), and — with Gemma 4 — a fully Apache 2.0 licensed model. The catch is that Gemma 1–3 require accepting a terms-of-use agreement before downloading, and the license is not strictly open-source, which can cause friction in some organizational contexts.

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

Supported by **Hugging Face Transformers**, **vLLM** (BF16, AWQ, GPTQ), **llama.cpp** (GGUF), **Ollama** (GGUF), **SGLang**, and **MLX** (Apple Silicon via MLX-LM). Google also maintains **gemma.cpp** — a lightweight C++ inference runtime specifically for the Gemma family, analogous to llama.cpp. JAX/Keras on TPU is supported for training and inference via Google AI Platform. Common quant formats: GGUF (Q2–Q8), AWQ (INT4), GPTQ (INT4/INT8); FP8 available for larger Gemma 4 sizes on H100.

## 7. Capabilities

Gemma 3 (4B–27B) supports **vision** (image understanding via SigLIP encoder), 140+ languages, and **function/tool calling** in the Instruct variants via a structured `<start_of_turn>` format. Gemma 2 is text-only and primarily English/multilingual-European; Gemma 3 extended multilingual significantly. Gemma 4 adds audio understanding alongside vision and text. Code generation and reasoning are core training targets across all sizes; the 27B and Gemma 4 31B are competitive with much larger dense models. ([Gemma 3 technical report](https://arxiv.org/abs/2503.19786))

## 8. Benchmarks

Numbers for Gemma 3 Instruct variants from the Gemma 3 Technical Report (Mar 2025). ([arXiv:2503.19786](https://arxiv.org/abs/2503.19786))

| Benchmark | Gemma 3 1B-IT | Gemma 3 4B-IT | Gemma 3 12B-IT | Gemma 3 27B-IT |
|---|---|---|---|---|
| MMLU | 38.8 | 58.1 | 71.9 | 76.9 |
| MMLU-Pro | 14.7 | 43.6 | 60.6 | 67.5 |
| HumanEval | 41.5 | 71.3 | 85.4 | 87.8 |
| MATH | 48.0 | 75.6 | 83.8 | 89.0 |
| IFEval | 80.2 | 90.2 | 88.9 | 90.4 |
| GPQA Diamond | 19.2 | 30.8 | 40.9 | 42.4 |

## 9. Documented Strengths

- **Strong instruction following (IFEval)**: The 4B and 27B models both score ~90 on IFEval — among the best for their respective size classes, surpassing much larger models. ([Gemma 3 Technical Report, Mar 2025](https://arxiv.org/abs/2503.19786))
- **Math at all sizes**: 27B-IT scores MATH 89.0 and even the 4B-IT reaches 75.6 — notable given the size. ([Gemma 3 Technical Report, Mar 2025](https://arxiv.org/abs/2503.19786))
- **Multilingual breadth**: Gemma 3 (4B–27B) supports 140+ languages, broadening Google's open-weight reach well beyond European languages. ([Gemma 3 Technical Report, Mar 2025](https://arxiv.org/abs/2503.19786))
- **Vision integration**: Native 128K context with SigLIP vision encoder enables image + text understanding at all non-1B sizes, with Pan & Scan for non-square images. ([Gemma 3 Technical Report, Mar 2025](https://arxiv.org/abs/2503.19786))

## 10. Documented Weaknesses

- **GPQA lags reasoning-specialized models**: 27B-IT scores 42.4 on GPQA Diamond, far below DeepSeek-R1 (71.5) and Phi-4 (56.1, at the same parameter count). ([Gemma 3 Technical Report, Mar 2025](https://arxiv.org/abs/2503.19786))
- **Long-context degradation**: The technical report states models "rapidly degrade" beyond 128K tokens; the 5:1 local-to-global attention ratio reduces KV cache cost but limits far-context reasoning. ([Gemma 3 Technical Report, Mar 2025](https://arxiv.org/abs/2503.19786))
- **Fixed vision encoder resolution**: The frozen 896×896 SigLIP encoder introduces artifacts on non-square images; Pan & Scan mitigates this but adds inference overhead. ([Gemma 3 Technical Report, Mar 2025](https://arxiv.org/abs/2503.19786))
- **Gating for Gemma 1–3**: Accepting the Gemma Terms of Use is required before downloading weights — not strictly open-source per OSI, which can block certain organizational deployments.

## 11. Sources

- [google/gemma collection on HuggingFace](https://huggingface.co/google) — observed 2026-06-14
