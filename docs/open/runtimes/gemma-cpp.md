# gemma.cpp

_Last verified: 2026-06-14_

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

Documented strengths from maintainer docs, benchmarks, or independent comparisons. Cite source.

## 8. Documented Weaknesses

Documented limitations from issue tracker, docs, or community reports. Cite source.

## 9. Sources

- [google/gemma.cpp](https://github.com/google/gemma.cpp) — observed 2026-06-14
