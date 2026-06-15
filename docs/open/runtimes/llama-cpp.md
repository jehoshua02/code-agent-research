---
name: "llama.cpp"
maker: "ggml-org"
license: "MIT"
license_category: "mit"
status: "active"
url: "https://github.com/ggml-org/llama.cpp"
last_verified: "2026-06-14"
language: "C++"
platforms: ["linux", "macos", "windows"]
gpu_backends: ["cuda", "rocm", "metal", "cpu", "vulkan", "sycl"]
api_openai_compat: true
supports_mcp: "none"
formats: ["gguf"]
notes: "Upstream of Ollama, KoboldCpp, and llamafile; GGUF is the sole inference format."
---

# llama.cpp

_Last verified: 2026-06-14_

## 0. TL;DR

llama.cpp is a C/C++ library that runs LLMs locally using [GGUF](../GLOSSARY.md#quantization)-format model files, on anything from a MacBook GPU to a Linux CUDA server. Pick it if you want low-level control, broad hardware support, or are building a tool that embeds model inference directly. The catch is that it's a library and CLI, not a polished app — you'll need to build from source or wire up bindings yourself; many people use a friendlier wrapper like Ollama instead.

## 1. What It Is

llama.cpp (ggml-org/llama.cpp) is an MIT-licensed C/C++ inference framework. Active. Runs LLMs efficiently on CPU and GPU (CUDA, Metal, ROCm, Vulkan) using the GGUF format; the upstream of many derived runtimes (Ollama, KoboldCpp, llamafile).

## 2. Install

**Platforms:** Linux (x86-64, ARM64, s390x; experimental RISC-V), macOS (Apple Silicon + Intel), Windows (x64, ARM64; Visual Studio 2022 C++ tools), Android (ARM64), iOS (xcframework).

**Build from source (CMake):**

```bash
cmake -B build
cmake --build build --config Release
```

Backend flags (combinable): `-DGGML_CUDA=ON` (NVIDIA; CUDA Toolkit required), `-DGGML_HIP=ON -DGPU_TARGETS=gfx1030` (AMD ROCm), `-DGGML_VULKAN=ON`, `-DGGML_SYCL=ON` (Intel GPU), `-DGGML_MUSA=ON` (Moore Threads), `-DGGML_CANN=on` (Ascend NPU), `-DGGML_WEBGPU=ON`. Metal is **on by default** on macOS (disable with `-DGGML_METAL=OFF`). CPU BLAS: `-DGGML_BLAS=ON -DGGML_BLAS_VENDOR=OpenBLAS|Intel10_64lp|...`; ZenDNN for AMD EPYC.

**Prebuilt binaries:** GitHub releases ship per-platform variants — macOS arm64 (CPU+Metal), Linux x64 (CPU, Vulkan, ROCm 7.2, OpenVINO, SYCL), Windows x64 (CPU, CUDA 12.4/13.3, Vulkan, SYCL, HIP). Package managers: `brew install llama.cpp`, `winget install llama.cpp`, Nix.

**Python bindings (llama-cpp-python):** `pip install llama-cpp-python`. GPU variants via `CMAKE_ARGS="-DGGML_CUDA=on"`, etc., or prebuilt wheels at `https://abetlen.github.io/llama-cpp-python/whl/{cpu,cu121,cu130,metal,rocm72,vulkan}`. Wheels require Python 3.10–3.12; CUDA wheels need compute capability ≥ 6.0.

## 3. Hardware Support

- **CUDA / NVIDIA:** Compute capability ≥ 6.0 (Pascal+) for wheels; custom builds via `-DCMAKE_CUDA_ARCHITECTURES`. Unified memory via `GGML_CUDA_ENABLE_UNIFIED_MEMORY=1`; multi-GPU P2P via `GGML_CUDA_P2P`. Device selection through `CUDA_VISIBLE_DEVICES`.
- **AMD ROCm/HIP:** `-DGGML_HIP=ON -DGPU_TARGETS=<gfx>`; `HSA_OVERRIDE_GFX_VERSION` overrides unsupported targets; `HIP_VISIBLE_DEVICES` for selection.
- **Apple Metal:** On by default on macOS; targets Apple Silicon (M1–M4) and Metal-capable Intel Macs. Accelerate framework provides CPU BLAS.
- **CPU:** AVX/AVX2/AVX-512/AMX (x86), NEON+KleidiAI (ARM), experimental RVV (RISC-V). BLAS via OpenBLAS, BLIS, Intel oneMKL, Accelerate, ZenDNN.
- **Vulkan:** Cross-platform any GPU with Vulkan 1.2+ drivers.
- **Other:** SYCL (Intel GPU), MUSA (Moore Threads), CANN (Ascend NPU), OpenCL, OpenVINO, WebGPU, IBM zDNN.
- **Multi-GPU:** Multiple backends can be built simultaneously; runtime `--device` / `--list-devices` selection.
- **Memory mapping:** mmap is default (disable with `--no-mmap`).
- **Layer offload:** `-ngl <N>` controls GPU layers; hybrid CPU+GPU when model exceeds VRAM.

## 4. Model Formats

GGUF is the sole inference format (replaces deprecated GGML). Other source formats (HuggingFace safetensors, PyTorch `.bin`) must be converted via `convert_hf_to_gguf.py`. Models can be pulled directly from Hugging Face via `llama-cli -hf <user>/<repo>`.

Quantization (precision F32/F16/BF16, plus integer):

- **Legacy:** Q4_0, Q4_1, Q5_0, Q5_1, Q8_0.
- **K-quants (recommended):** Q2_K, Q3_K_{S,M,L}, Q4_K_{S,M}, Q5_K_{S,M}, Q6_K. Q4_K_M is the common general-purpose default.
- **IQ-quants (importance-matrix):** IQ1_S, IQ2_XXS, IQ2_XS, IQ3_S/M, IQ4_NL/XS — best quality-per-bit at very low bit widths.

Tools: `llama-quantize` (with optional `--imatrix`), `llama-gguf-split` for sharding.

## 5. API Surface

`llama-server` exposes OpenAI-compatible endpoints: `POST /v1/chat/completions`, `POST /v1/completions`, `POST /v1/embeddings`. The docs caveat: "no strong claims of compatibility with OpenAI API spec is being made, in our experience it suffices to support many apps."

- **Tool / function calling:** Via `--jinja` flag — "Function calling / tool use for ~any model" using the standard `tools` parameter and automatic tool-call parsing.
- **Vision / multimodal:** Experimental — `/v1/chat/completions` accepts `image_url`, `input_audio`, `input_video` content parts (base64 or remote URL).
- **Streaming:** SSE via the `stream` parameter.
- **Structured outputs:** `response_format` for plain or schema-constrained JSON; `grammar` parameter for GBNF grammar files; `json_schema` for schema-constrained sampling.
- **Logprobs:** Via `n_probs` on the native `/completion` endpoint (top-N token probabilities).
- **Native endpoints:** `POST /completion`, `POST /embedding`, `POST /reranking`, `POST /infill` (code prefix/suffix), `GET /slots`, `GET /metrics` (Prometheus).

Source: [tools/server/README.md](https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md).

## 6. Performance

No canonical benchmark suite. The README ships a single illustrative `llama-bench` output (Qwen2 1.5B Q4_0, Metal+BLAS): prefill `pp512` ≈ 5765 tok/s, decode `tg128` ≈ 198 tok/s — a format example for the tool, not a maintainer-published reference. The server docs mention continuous batching, parallel decoding (up to 4 concurrent requests with 4096-token context), and speculative decoding but give no associated numbers. Prefill and decode are reported separately by `llama-bench` (pp* vs tg* tests). Source: [README](https://github.com/ggml-org/llama.cpp).

## 7. Documented Strengths

- **Broadest hardware reach of any GGUF runtime**: Single codebase supports Metal, CUDA, ROCm/HIP, Vulkan, SYCL, OpenCL, WebGPU, and CPU (x86/ARM/RISC-V/Z) — documented in the [ggml-org/llama.cpp README](https://github.com/ggml-org/llama.cpp).
- **Q4_K_M throughput vs FP16 CPU baseline**: Independent benchmarks on Llama-3.1-8B show 47.9 tok/s with Q4_K_M (4.8 bits/weight), an ~18× improvement over the FP16 CPU baseline, with >90% RAM reduction. ([arxiv 2601.14277](https://arxiv.org/html/2601.14277v1))
- **Zero-dependency CPU inference**: Runs on bare CPU with no GPU drivers; suitable for air-gapped, embedded, and mobile (Android/iOS) targets where other runtimes cannot be installed. ([README](https://github.com/ggml-org/llama.cpp))
- **Upstream of the ecosystem**: Ollama, KoboldCpp, and llamafile are all wrappers around llama.cpp, making it the de facto reference implementation for GGUF inference. ([ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp))

## 8. Documented Weaknesses

- **Multimodal is explicitly "experimental"**: Server docs mark `image_url`, `input_audio`, and `input_video` support as experimental; flash attention is disabled for multimodal projectors on several backends. ([tools/server/README.md](https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md))
- **Vulkan backend shows negative scaling on MoE models at small batch sizes**: throughput drops at batch sizes 2–3, reported in weekly GitHub issue trackers (Nov 2025). ([Buttondown weekly report Nov 2025](https://buttondown.com/weekly-project-news/archive/weekly-github-report-for-llamacpp-november-03/))
- **Low multi-request throughput compared to production servers**: llama-server's continuous batching supports a modest 4 parallel slots by default and lacks the scheduler-level optimizations of vLLM/TGI; llama_server is also reported 5–10% slower than llama_cli per token. ([community reports](https://github.com/ggml-org/llama.cpp/discussions/4167))
- **No native Python package** — all GPU builds require environment-specific compile flags or pre-built wheel variants (`CMAKE_ARGS="-DGGML_CUDA=on"`), adding friction for Python-first workflows. ([llama-cpp-python docs](https://github.com/abetlen/llama-cpp-python))

## 9. Sources

- [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp) — observed 2026-06-14
