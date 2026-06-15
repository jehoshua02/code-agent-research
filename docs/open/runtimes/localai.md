# LocalAI

_Last verified: 2026-06-14_

## 0. TL;DR

LocalAI is a Docker-based server that exposes an OpenAI-compatible API in front of many different local backends (llama.cpp, Whisper, image generation, and more), so existing code that calls OpenAI can be pointed at your own hardware with no client changes. Pick it if you want a single self-hosted endpoint that handles text, speech, and images across heterogeneous hardware. The trade-off is operational complexity — you're managing multiple backend processes and a Go routing layer, which adds surface area compared to single-purpose servers.

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

Drop-in OpenAI-compatible REST API. Confirmed endpoints:

- `/v1/chat/completions`, `/v1/completions`, `/v1/edits`, `/v1/embeddings`, `/v1/models`
- `/v1/images/generations` (Stable Diffusion via stablediffusion-ggml and Diffusers)
- `/v1/messages` (Anthropic Messages API: tool calling, multimodal, system prompts)
- `/v1/responses` (Open Responses API: background, reasoning config, parallel tools)
- Audio: STT (transcription), TTS, Realtime API (speech-to-speech over WebSocket)
- Reranker, object detection, voice activity detection

- **Tool / function calling:** Fully supported via OpenAI-compatible tools API; LocalAI parses structured tool calls out of model output. Parallel function calls (experimental). Works across llama.cpp (automatic), vLLM/vLLM Omni (needs `tool_parser`), MLX.
- **Vision (multimodal):** Vision API; llama.cpp video input listed.
- **Streaming:** SSE. Anthropic Messages path emits `message_start`, `content_block_delta`, `message_stop`. Tool streaming supported.
- **Structured outputs / grammar:** BNF grammar constraints on the llama.cpp backend via the `grammar` parameter (JSON, YAML, binary choices, arbitrary BNF). `grammar_json_functions` for grammar-based function calling; `no_grammar: true` per-request opt-out.
- **Logprobs:** Not documented.
- **Beyond OpenAI:** Anthropic API compatibility, ElevenLabs API compatibility, drop-in Ollama API (v4.2.0+), video generation, object detection, reranker, Realtime speech-to-speech.

Sources: [features](https://localai.io/features/), [openai-functions](https://localai.io/features/openai-functions/), [constrained_grammars](https://localai.io/features/constrained_grammars/).

## 6. Performance

Not benchmarked by maintainer. None of the official docs publish throughput, latency, or batch-size figures. Performance depends entirely on the chosen backend (llama.cpp, vLLM, MLX, etc.) and hardware. Source: [LocalAI README](https://github.com/mudler/LocalAI).

## 7. Documented Strengths

- **True OpenAI drop-in replacement:** Existing code calling `api.openai.com` can be redirected to `localhost` with no client-side changes; also covers Anthropic Messages, Ollama, and ElevenLabs compatible APIs. Source: [localai.io/features](https://localai.io/features/).
- **Broadest multi-modal scope among self-hosted servers:** Single endpoint covers text, embeddings, image generation, speech-to-text, TTS, video generation, object detection, and reranking — 36+ backends. Source: [localai.io/features](https://localai.io/features/).
- **Runs on CPU without GPU:** CPU path works on any x86-64/ARM64 machine; GPU is optional, not required. Source: [README](https://github.com/mudler/LocalAI).
- **Distributed inference across nodes:** Built-in peer-to-peer federation and production multi-node scaling to spread inference load beyond a single machine. Source: [localai.io/features](https://localai.io/features/).

## 8. Documented Weaknesses

- **Complex setup and backend management:** LocalAI is a routing layer over 36+ backends; users must manage backend installs individually (`local-ai backends list/install`) and write per-model YAML configs — significantly more operational surface area than single-backend servers. Source: [Ollama vs LocalAI comparison](https://hyscaler.com/insights/ollama-vs-localai-open-source-local-llm-apis/).
- **Backend install failures are a recurring issue:** Community reports document errors such as "not a valid backend: run file not found" when backends cannot install correctly. Source: [issue #7662](https://github.com/mudler/LocalAI/issues/7662).
- **Models stay resident in VRAM by default:** Once a model loads, it is not evicted when switching; VRAM exhaustion occurs when loading multiple models without explicit unloading. Source: [troubleshooting docs](https://localai.io/basics/troubleshooting/).
- **Intel GPU known hang:** Intel SYCL backend requires `mmap: false` in model YAML to avoid hangs — documented workaround rather than a fixed bug. Source: [Hardware docs](https://localai.io/).

## 9. Sources

- [mudler/LocalAI](https://github.com/mudler/LocalAI) — observed 2026-06-14
