# LM Studio

_Last verified: 2026-06-14_

## 1. What It Is

LM Studio is a closed-source, proprietary desktop app from Element Labs. Free-to-use, available on macOS, Windows, and Linux. Included in the survey because it is self-hosted and free, but it is not open-source. GUI for discovering, downloading, and running local models, with an OpenAI-compatible local server.

## 2. Install

- **macOS:** Apple Silicon only (M1/M2/M3/M4), macOS 14.0+. Intel Macs not supported.
- **Windows:** x64 (AVX2 required) and ARM64 (Snapdragon X Elite).
- **Linux:** AppImage for x64 and ARM64. Ubuntu 20.04+ recommended.
- Download from [lmstudio.ai/download](https://lmstudio.ai/download); no package manager. A headless `llmster` daemon variant is available for server/CI use.
- **System minimums:** 16 GB RAM recommended (8 GB possible for small models), 4 GB VRAM minimum on Windows, ~8 GB recommended for 7B models.
- **GPU drivers:** NVIDIA ≥ 545 with CUDA 12.3+; AMD on Linux needs ROCm ≥ 5.6; AMD on Windows uses Vulkan (no ROCm install); Apple Silicon needs no extra drivers.

## 3. Hardware Support

- **NVIDIA CUDA:** Primary GPU path on Windows/Linux. Runtime labelled "CUDA 12 llama.cpp".
- **AMD ROCm (Linux):** ROCm llama.cpp runtime; tested on RX 6000/7000 (RDNA3 may need `HSA_OVERRIDE_GFX_VERSION=11.0.0`); AMD 9000 series added recently.
- **AMD Vulkan (Windows):** Default AMD path on Windows; no ROCm needed.
- **Vulkan:** Cross-vendor; also covers Intel Arc.
- **Apple Metal:** macOS default via Apple's MLX framework + Metal; unified memory pools RAM/VRAM.
- **CPU:** Fallback on all platforms; AVX2 required on x64. Roughly 4 tok/s vs ~35 tok/s with GPU.
- **Multi-GPU (v0.4.15+):** Priority-order mode (fastest GPU first, overflow to others) or tensor parallelism (model sharded across GPUs).
- **Memory features:** Cross-conversation KV cache reuse; pre-load RAM/VRAM estimation; context size directly affects KV cache VRAM.

## 4. Model Formats

- **GGUF (primary, all platforms):** Loaded via bundled llama.cpp; downloaded from Hugging Face through LM Studio's UI or by local file path.
- **MLX (Apple Silicon only):** Loaded via Apple's MLX framework; can coexist with GGUF in the same session; vision-language models via `mlx-vlm`; structured JSON via `outlines`.
- **safetensors:** Recognized but not a primary runtime format.
- **`model.yaml` open standard:** Abstracts over GGUF/MLX variants in a unified model entry.
- **Quantizations (GGUF):** BF16/F16, Q8_0, Q6_K, Q5_K_M, Q4_K_M (default), Q4_K_S/Q4_0, Q3_K_*, Q2_K, IQ4_XS, IQ3_*. Quant variants surfaced in the download UI.

## 5. API Surface

OpenAI-compatible? Native API? Streaming? Tool calling? Embeddings?

## 6. Performance

Throughput (tok/s), latency, batch support. Cite source or note "not benchmarked".

## 7. Documented Strengths

Documented strengths from maintainer docs, benchmarks, or independent comparisons. Cite source.

## 8. Documented Weaknesses

Documented limitations from issue tracker, docs, or community reports. Cite source.

## 9. Sources

- [LM Studio website](https://lmstudio.ai) — observed 2026-06-14
