# LocalAI

_Last verified: 2026-06-14_

## 1. What It Is

LocalAI (mudler/LocalAI) is an MIT-licensed Go server that mimics the OpenAI API across many local backends (llama.cpp, vLLM, GPT4All, Whisper, diffusion). Active. Lets existing OpenAI-API client code target self-hosted models without changes.

## 2. Install

Docker is the recommended path; prebuilt binaries and source builds are also available.

- **Docker images (`localai/localai`):** `latest-cpu`, `latest-gpu-nvidia-cuda-12`, `latest-gpu-nvidia-cuda-13`, `latest-gpu-hipblas` (AMD), `latest-gpu-intel` (SYCL/oneAPI), `latest-gpu-vulkan`, `latest-nvidia-l4t-arm64` (Jetson). Versioned tags follow `v<x.y.z>-gpu-...`; `-core` variants ship without Python deps for smaller llama.cpp/SD-only deployments.
- **GPU passthrough:** NVIDIA `--gpus all` (NVIDIA Container Toolkit); AMD `--device /dev/kfd --device /dev/dri`; Intel `--device /dev/dri`; Jetson `--runtime nvidia --gpus all`.
- **Prebuilt binaries:** Linux (x86-64, arm64), macOS, Windows from GitHub releases; on macOS remove the quarantine attribute. Run `./local-ai-Linux-x86_64 run`.
- **From source:** `git clone https://github.com/mudler/LocalAI && cd LocalAI` then follow `localai.io/basics/build/`.
- **Other targets:** Podman, Kubernetes.

## 3. Hardware Support

- **CPU:** Primary supported path on any x86-64 or ARM64 system.
- **NVIDIA CUDA 11/12/13:** Requires NVIDIA Container Toolkit. Drives llama.cpp (`gpu_layers`), diffusers, and vLLM backends.
- **AMD ROCm (hipblas):** ROCm ≥ 7.0.0 with `amdgpu-dkms`. Verified targets: MI100 (gfx908), MI210/250 (gfx90a), RX 6800 (gfx1030), RX 7900 (gfx1100/1101/1102), RDNA4 (gfx1200/1201).
- **Apple Silicon / Metal:** Native via llama.cpp and MLX / MLX-VLM backends (August 2025+); MLX-Distributed supports multi-Mac inference.
- **Intel GPU (SYCL/oneAPI):** Requires `--device /dev/dri`; set `mmap: false` in model YAML to avoid known hangs.
- **Vulkan:** Cross-vendor via the `latest-gpu-vulkan` image.
- **NVIDIA Jetson (ARM64):** `latest-nvidia-l4t-arm64` for Jetson Nano/Xavier NX/AGX Orin/DGX Spark.
- **Multi-GPU:** llama.cpp uses `CUDA_VISIBLE_DEVICES` / `HIP_VISIBLE_DEVICES`; vLLM/diffusers use `tensor_parallel_size: N`. Automatic model fitting across multiple GPUs supported.
- **Backend autodetection:** Override with `LOCALAI_FORCE_META_BACKEND_CAPABILITY` (`default`/`nvidia`/`amd`/`intel`).

## 4. Model Formats

LocalAI is a multi-backend server; the appropriate backend (36+ total: llama.cpp, ik_llama.cpp, vLLM, transformers, MLX/MLX-VLM, whisper.cpp, faster-whisper, stable-diffusion.cpp, diffusers, piper, kokoro, parakeet.cpp, etc.) is chosen by file format or YAML config.

- **GGUF (primary, via llama.cpp / ik_llama.cpp):** Recommended for most use cases. All standard quantization levels (Q2_K, Q4_K_S, Q4_K_M default, Q6_K, Q8_0). Wide architecture coverage (LLaMA, Mistral, Falcon, Starcoder, GPT-2, Mamba, RWKV, …). Reference: `huggingface://owner/repo/file.gguf`.
- **GGML:** Legacy, deprecated but supported.
- **safetensors / PyTorch:** HuggingFace FP16/BF16 weights via transformers, vLLM, diffusers, MLX backends. Required for vLLM and diffusers.
- **GPTQ:** NVIDIA-only via vLLM and transformers.
- **AWQ:** NVIDIA-only via vLLM.
- **Diffusion (Stable Diffusion `.ckpt`/`.safetensors`, HF diffusers pipelines):** Image and video generation.
- **Audio:** Whisper, faster-whisper, WhisperX, moonshine, voxtral (STT); piper, Kokoro, Coqui TTS, fish-speech (TTS); ACE-Step/acestep.cpp (music).
- **Model URIs:** `file://`, `huggingface://`, `ollama://`, `oci://`, remote YAML config URL, or LocalAI gallery handle (e.g., `llama-3.2-1b-instruct:q4_k_m`).

## 5. API Surface

OpenAI-compatible? Native API? Streaming? Tool calling? Embeddings?

## 6. Performance

Throughput (tok/s), latency, batch support. Cite source or note "not benchmarked".

## 7. Documented Strengths

Documented strengths from maintainer docs, benchmarks, or independent comparisons. Cite source.

## 8. Documented Weaknesses

Documented limitations from issue tracker, docs, or community reports. Cite source.

## 9. Sources

- [mudler/LocalAI](https://github.com/mudler/LocalAI) — observed 2026-06-14
