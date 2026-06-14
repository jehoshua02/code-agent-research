# llama.cpp

_Last verified: 2026-06-14_

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

OpenAI-compatible? Native API? Streaming? Tool calling? Embeddings?

## 6. Performance

Throughput (tok/s), latency, batch support. Cite source or note "not benchmarked".

## 7. Documented Strengths

Documented strengths from maintainer docs, benchmarks, or independent comparisons. Cite source.

## 8. Documented Weaknesses

Documented limitations from issue tracker, docs, or community reports. Cite source.

## 9. Sources

- [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp) — observed 2026-06-14
