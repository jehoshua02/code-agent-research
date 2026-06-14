# Text Generation WebUI (oobabooga)

_Last verified: 2026-06-14_

## 1. What It Is

Text Generation WebUI (oobabooga/text-generation-webui) is an AGPL-3.0 Python web interface for local LLMs. Active. Maintained by oobabooga; supports multiple backends (Transformers, llama.cpp, ExLlama) behind a unified UI.

## 2. Install

- **One-click installers:** clone the repo and run `start_windows.bat`, `start_linux.sh`, or `start_macos.sh`. The installer prompts for GPU vendor and pulls ~10 GB of PyTorch + deps.
- **Portable builds:** prebuilt CUDA, Vulkan, ROCm, and CPU-only zips on the releases page (Linux/Windows/macOS).
- **Manual (conda/pip):** Python 3.11+ (3.13 supported); Miniforge env, install PyTorch for your target, then the matching `requirements_*.txt` (NVIDIA CUDA, AMD ROCm, CPU, Apple Intel, Apple Silicon).
- **Docker:** Compose v2.17+; symlink a hardware-specific compose file (NVIDIA, AMD, Intel GPU, CPU) and `docker compose up --build`. GPU passthrough via `--gpus all`.
- **CUDA:** 12.4 or 12.8 builds.
- **ROCm (Linux):** 6.2.4 or 6.4.4. AMD on Windows is Vulkan-only (no ROCm, no ExLlama).
- **macOS:** Metal acceleration is automatic on Apple Silicon and Intel Macs via llama.cpp; GGUF Q4_K_M / Q5_K_M recommended.

## 3. Hardware Support

- **CUDA / NVIDIA:** primary path; all backends (llama.cpp, Transformers, ExLlamaV2/V3, TensorRT-LLM) and all formats available.
- **ROCm / AMD (Linux):** llama.cpp and ExLlamaV2 (EXL2, GPTQ). ExLlamaV3 has no ROCm. AMD on Windows is Vulkan + llama.cpp only.
- **Metal / Apple:** Apple Silicon and Intel Macs via llama.cpp (GGUF only).
- **CPU:** Transformers and llama.cpp CPU builds; AVX2 and AVX-only binary variants (`+cpuavx2`, `+cpuavx`). 16 GB RAM minimum recommended.
- **Multi-GPU:** NVIDIA via `accelerate` for Transformers; llama.cpp supports tensor split modes (`layer`, `row`, `tensor`, `none`).
- **Memory:** depends on backend; llama.cpp uses mmap and `--n-gpu-layers` offloading; Transformers backend supports `device_map="auto"` for CPU/disk offload.

## 4. Model Formats

Format support is backend-specific; the UI can switch backends without restarting.

| Format | Backend | Platforms |
|---|---|---|
| GGUF | llama.cpp | CUDA, ROCm Linux, Vulkan, Metal, CPU |
| EXL2 | ExLlamaV2 / ExLlamaV3 | CUDA; ExLlamaV2 also ROCm Linux |
| GPTQ | Transformers / ExLlamaV2 / AutoGPTQ | CUDA (ExLlamaV2 also ROCm Linux) |
| AWQ | Transformers | CUDA |
| safetensors FP16/BF16 | Transformers | CUDA |
| bitsandbytes 4-/8-bit (NF4, FP4, INT8) | Transformers | CUDA |
| TensorRT-LLM engines | TensorRT-LLM | CUDA |
| HQQ | HQQ loader | CUDA |

llama.cpp backend handles the full set of GGUF quantization types (Q4_K_M, Q5_K_M, Q8_0, IQ-series, etc.).

## 5. API Surface

OpenAI-compatible? Native API? Streaming? Tool calling? Embeddings?

## 6. Performance

Throughput (tok/s), latency, batch support. Cite source or note "not benchmarked".

## 7. Documented Strengths

Documented strengths from maintainer docs, benchmarks, or independent comparisons. Cite source.

## 8. Documented Weaknesses

Documented limitations from issue tracker, docs, or community reports. Cite source.

## 9. Sources

- [oobabooga/text-generation-webui](https://github.com/oobabooga/text-generation-webui) — observed 2026-06-14
