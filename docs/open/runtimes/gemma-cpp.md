# gemma.cpp

_Last verified: 2026-06-14_

## 0. TL;DR

gemma.cpp is a lightweight C++ runtime built by Google specifically for the Gemma model family — not a general-purpose LLM server. Pick it if you're deploying a Gemma model and want a minimal, well-optimized binary with no Python dependency. The hard constraint: it only runs Gemma models, so if you ever need to switch model families you'll need a different runtime entirely.

## 1. What It Is

gemma.cpp (google/gemma.cpp) is an Apache 2.0 C++ inference engine maintained by Google. Active. Lightweight standalone runtime targeting Google's Gemma model family — model-specific by design, optimized for Gemma's architecture rather than general-purpose serving.

## 2. Install

Platforms: Linux, macOS, Windows (WSL recommended for Windows; native build via Visual Studio 2022 Build Tools + Clang/LLVM). Build tools required: CMake, a Clang C++ compiler supporting C++17, and `tar`.

```sh
# Unix-like
cmake --preset make
cmake --build --preset make -j$(nproc)

# Windows (native)
cmake --preset windows
cmake --build --preset windows -j4
```

Weights are downloaded separately from [Kaggle (Gemma C++ tab)](https://www.kaggle.com/models/google/gemma-2/gemmaCpp) or Hugging Face Hub. Recommend starting with `gemma2-2b-it-sfp` checkpoint. Bazel is also supported (`bazel build -c opt --cxxopt=-std=c++20 :gemma`). See [../README.md](../README.md#4-deployment-notes) for general reader-facing deployment context.

## 3. Hardware Support

CPU-only inference via [Google Highway](https://github.com/google/highway) SIMD library (runtime ISA selection — no GPU acceleration). Supports x86 (AVX/AVX2/AVX-512), ARM (NEON), and any other CPU Highway targets. Multi-socket tensor parallelism with CCX-aware thread pool. Memory-mapped or parallel disk I/O (heuristic with user override). No CUDA/ROCm/Metal GPU support.

## 4. Model Formats

Proprietary `.sbs` format (custom forward/backward-compatible binary with embedded metadata). Supports bf16, fp32, fp64, custom fp8 (2–3 mantissa bits with tensor scaling), and NUQ (non-uniform 4-bit) quantizations. Single-file format embeds tokenizer directly (post-2025-05-06 weights or via `migrate_weights` tool). Conversion from safetensors supported (not yet open-sourced). Models: Gemma 2 (2B/9B/27B), Gemma 3, PaliGemma 2.

## 5. API Surface

Primarily a **C++ library** (`libgemma`, ~2K LoC core) and **CLI tool**, not an OpenAI-compatible server. A basic HTTP API server is included (see `API_SERVER_README.md`) exposing a **Google-protocol REST API** (not OpenAI-compatible):

- `POST /v1beta/models/gemma3-4b:generateContent` (non-streaming)
- `POST /v1beta/models/gemma3-4b:streamGenerateContent` (SSE streaming)
- `GET /v1beta/models`

**Streaming:** Supported in the C++ API ("C++ APIs with streaming for single query and batched inference") and via the HTTP server's SSE endpoint. **Vision:** Via PaliGemma 2 (image file via `--image_file`). **Tool calling, structured outputs, embeddings:** Not documented. Python bindings via pybind11; community Lua and Godot bindings exist. Sources: [README.md](https://github.com/google/gemma.cpp/blob/main/README.md), [API_SERVER_README.md](https://raw.githubusercontent.com/google/gemma.cpp/main/API_SERVER_README.md).

## 6. Performance

Not benchmarked by maintainer. No quantitative throughput, latency, or batch-size figures in README or docs. Optimization notes are qualitative: mixed-precision GEMM with runtime autotuning, 8-bit switched floating-point models described as enabling "faster inference," and a caveat that "long sequences will be slow due to the quadratic cost of attention." No prefill vs decode breakdown. Source: [README.md](https://github.com/google/gemma.cpp/blob/main/README.md).

## 7. Documented Strengths

- **Minimal footprint — ~2K LoC core, no Python:** Pure C++ with minimal dependencies; easy to embed in native applications or ship as a standalone binary without a Python runtime. Source: [README](https://github.com/google/gemma.cpp).
- **Portable CPU SIMD via Google Highway:** Runtime ISA dispatch (AVX/AVX2/AVX-512 on x86, NEON on ARM) means a single binary runs optimally on any CPU the Highway library targets. Source: [README](https://github.com/google/gemma.cpp).
- **No GPU required — runs on any CPU hardware:** Designed for resource-constrained environments where a GPU is unavailable or undesirable. Source: [README](https://github.com/google/gemma.cpp).
- **Research-friendly, transparent codebase:** Positioned as bridging the gap between deployment runtimes and research frameworks; straightforward to modify, making it suitable for architecture experimentation on Gemma models. Source: [README](https://github.com/google/gemma.cpp).

## 8. Documented Weaknesses

- **Gemma-only — no support for other model families:** Works exclusively with Gemma 2, Gemma 3, and PaliGemma 2; cannot run Llama, Mistral, Qwen, or any other architecture. Source: [README](https://github.com/google/gemma.cpp).
- **No GPU acceleration:** CPU-only inference via Highway; no CUDA, ROCm, or Metal backend. Throughput is limited by CPU memory bandwidth compared to GPU-accelerated alternatives. Source: [README](https://github.com/google/gemma.cpp).
- **Quadratic attention degrades at long sequences:** Maintainer documents explicitly: "long sequences will be slow due to the quadratic cost of attention" — practical context length is constrained despite 128K theoretical support. Source: [README](https://github.com/google/gemma.cpp).
- **Proprietary `.sbs` format with closed-source converter:** Models must be converted to gemma.cpp's format; the safetensors-to-`.sbs` converter is not yet open-sourced, creating a dependency on Google-provided tooling. Source: [README](https://github.com/google/gemma.cpp).

## 9. Sources

- [google/gemma.cpp](https://github.com/google/gemma.cpp) — observed 2026-06-14
