# KoboldCpp

_Last verified: 2026-06-14_

## 1. What It Is

KoboldCpp (LostRuins/koboldcpp) is an AGPL-3.0 single-binary inference server built on llama.cpp. Active. Bundles a web UI focused on story-writing/role-play use cases; OpenAI-compatible API; popular for hobbyist local hosting.

## 2. Install

Single prebuilt binary, no package manager. Releases at [github.com/LostRuins/koboldcpp/releases](https://github.com/LostRuins/koboldcpp/releases).

- **Windows:** `koboldcpp.exe` (CUDA 12, default), `koboldcpp-oldpc.exe` (CUDA 11 + AVX1), `koboldcpp-nocuda.exe` (CPU/Vulkan, recommended for AMD on Windows).
- **Linux (x86-64):** Same three variants — `koboldcpp-linux-x64`, `-oldpc`, `-nocuda`. `chmod +x` and run.
- **macOS (Apple Silicon):** `koboldcpp-mac-arm64` includes Metal. Intel Macs require building from source (`make LLAMA_METAL=1`).
- **AMD ROCm/HIP (Linux):** Build from source — e.g. `make LLAMA_HIPBLAS=1 GPU_TARGETS=gfx1100 -j$(nproc)` (RDNA3); RDNA2 uses `gfx1030`; RDNA4 uses `gfx1201` with `GGML_HIP_FORCE_ROCWMMA_FATTN_GFX12=1`. Experimental rolling ROCm Linux binaries also published.
- **Docker:** `hub.docker.com/r/koboldai/koboldcpp` (Ubuntu, NVIDIA/AMD passthrough; described as expert-targeted).

## 3. Hardware Support

- **CUDA (cuBLAS):** Enable with `--usecuda`. CUDA 12 default, CUDA 11 via the `oldpc` build. `--gpulayers N` controls VRAM offload.
- **ROCm/HIP (hipBLAS):** Source build with `LLAMA_HIPBLAS=1`. RDNA2 (gfx1030), RDNA3 (gfx1100), RDNA4 (gfx1201/1200).
- **Metal (Apple):** Prebuilt arm64 binary or `make LLAMA_METAL=1`. Apple Silicon (M1–M4) and Intel Macs; benefits from unified memory.
- **Vulkan:** `--usevulkan`; cross-vendor (NVIDIA, AMD, Intel) without CUDA/ROCm; recommended for AMD on Windows; in the `nocuda` builds.
- **CPU:** All builds. AVX2 default; `--noavx2` for older CPUs. OpenBLAS path removed — CPU BLAS now routed through Vulkan or CUDA.
- **Multi-GPU:** CUDA only; auto-distributes layers across detected NVIDIA GPUs; `--tensor_split 3 1` adjusts ratio.
- **Memory:** `--gpulayers N` for layer offload; `--usemmap` for memory-mapped weight loading; CPU+GPU hybrid spills unfittable layers to system RAM.

## 4. Model Formats

- **GGUF (primary):** Loaded via the bundled llama.cpp. Compatible with community GGUFs from Hugging Face (TheBloke, bartowski, etc.).
- **Architectures:** Llama, Mistral, Qwen, Gemma (incl. Gemma4), Phi, Falcon, Deepseek, and most other GGUF-supported families.
- **Legacy GGML `.bin`:** Backward compatibility maintained.
- **Quantizations:** legacy (Q4_0, Q4_1, Q5_0, Q5_1, Q8_0); K-quants (Q2_K, Q3_K_{S,M,L}, Q4_K_{S,M}, Q5_K_{S,M}, Q6_K); IQ-quants (IQ3_XXS, IQ3_S, IQ3_M, IQ4_XS); F16. Q4_K_M is the community default.
- **Not supported natively:** GPTQ, AWQ, EXL2, safetensors — must be converted to GGUF first.

## 5. API Surface

Full OpenAI-compatible API at `/v1` (e.g., `http://localhost:5001/v1`): `/v1/chat/completions`, `/v1/completions`, `/v1/embeddings` (also at `/api/extra/embeddings`), `/v1/audio/transcriptions` (Whisper).

- **Tool / function calling:** Via Chat Completions, enabled with `--jinja` and `--jinjatools`; custom instruct tags configurable via `--chatcompletionsadapter`. MCP server support noted in README.
- **Vision (multimodal):** Vision projectors loaded via `--mmproj`; image and audio inputs simultaneously; `--visionmaxres` for max image resolution. Qwen3-VL-8B, Qwen-Omni recommended.
- **Streaming:** Three modes — polled-streaming (recommended; polls `/api/extra/generate/check` every second), true SSE per-token, and deprecated pseudo-streaming.
- **Structured outputs / grammar:** GBNF grammar sampling; `json_to_gbnf.py` utility included. No explicit OpenAI-style `response_format: json_object`.
- **Logprobs:** Supported. Built-in Token Probability Viewer.
- **Native KoboldAI API at `/api/v1`** (used by KoboldAI Classic/United). Proprietary routes under `/api/extra/`. Interactive docs at running server's `/api` and at [koboldcpp_api](https://lite.koboldai.net/koboldcpp_api). Compatibility endpoints for Ollama, A1111/Forge, ComfyUI, XTTS, OpenAI Speech.

Sources: [README](https://github.com/LostRuins/koboldcpp), [Wiki](https://github.com/LostRuins/koboldcpp/wiki).

## 6. Performance

Not benchmarked by maintainer. KoboldCpp includes a `--benchmark` flag that runs a built-in benchmark and outputs CSV timing/speed (including tok/s), but no canonical throughput figures, latency numbers, or prefill-vs-decode breakdowns are published in the README, wiki, or docs. Source: [Wiki](https://github.com/LostRuins/koboldcpp/wiki).

## 7. Documented Strengths

Documented strengths from maintainer docs, benchmarks, or independent comparisons. Cite source.

## 8. Documented Weaknesses

Documented limitations from issue tracker, docs, or community reports. Cite source.

## 9. Sources

- [LostRuins/koboldcpp](https://github.com/LostRuins/koboldcpp) — observed 2026-06-14
