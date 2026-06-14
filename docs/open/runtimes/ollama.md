# Ollama

_Last verified: 2026-06-14_

## 1. What It Is

Ollama (ollama/ollama) is an MIT-licensed Go runtime that wraps llama.cpp with a friendlier install and model-library experience. Active. Provides a local OpenAI-compatible API; the most common entry point for local model use.

## 2. Install

- **macOS** (14 Sonoma+, Apple Silicon or Intel): `brew install ollama` or the `Ollama.dmg`.
- **Linux** (Ubuntu/Debian/Fedora/Arch, amd64/arm64): `curl -fsSL https://ollama.com/install.sh | sh`.
- **Windows** (x86-64, ARM64): `OllamaSetup.exe` from the download page, or `irm https://ollama.com/install.ps1 | iex`.
- **Docker:** `ollama/ollama` on Docker Hub; CPU image runs as `docker run -p 11434:11434 ollama/ollama`; NVIDIA uses `--gpus=all` (needs NVIDIA Container Toolkit); AMD uses the `:rocm` tag with `--device /dev/kfd --device /dev/dri`.
- **GPU drivers:** NVIDIA driver ≥ 531 (≥ 570 for compute cap 5.0–6.2); ROCm v7 on Linux (AMD); macOS Metal is built in. Ollama bundles its own CUDA libraries — no separate CUDA Toolkit install required.

## 3. Hardware Support

- **NVIDIA CUDA:** Compute capability ≥ 5.0; supports Blackwell (sm12.x), Hopper (sm9.0), Ada (sm8.9), Ampere, Turing, Pascal, Maxwell. NVIDIA Jetson (JetPack 5 R35, JetPack 6 R36) supported.
- **AMD ROCm:** Linux — RX 9000/7000/6000/5000, AI PRO, Radeon PRO W, Ryzen AI, Instinct MI. Windows — limited to RX 7000/6000 and pro W cards. `HSA_OVERRIDE_GFX_VERSION` and `ROCR_VISIBLE_DEVICES` for unsupported/multi-GPU control.
- **Apple Metal:** M1/M2/M3/M4 via Metal; also uses MLX engine for safetensors on Apple Silicon.
- **Vulkan:** Fallback on Windows/Linux for Intel GPUs and unsupported AMD; toggle via `OLLAMA_VULKAN=0` and `GGML_VK_VISIBLE_DEVICES`.
- **CPU:** Automatic fallback; force with `CUDA_VISIBLE_DEVICES=-1` / `ROCR_VISIBLE_DEVICES=-1`.
- **Multi-GPU:** NVIDIA via `CUDA_VISIBLE_DEVICES`, AMD via `ROCR_VISIBLE_DEVICES`. Mixed-vendor (NVIDIA + AMD simultaneously) is not reliably supported.
- **Memory mapping:** GGUF mmap-loaded by default for fast startup and lower RAM footprint.

## 4. Model Formats

- **GGUF (primary):** Models in the Ollama library are pre-converted; import local GGUF via `FROM ./model.gguf` in a Modelfile. Supports GGUF v1/v2/v3.
- **Modelfile:** Dockerfile-style config — `FROM`, `PARAMETER`, `TEMPLATE`, `SYSTEM`, `ADAPTER` (LoRA in safetensors or GGUF), `LICENSE`, `MESSAGE`, `REQUIRES`.
- **Import sources:** safetensors and PyTorch weights are accepted as import sources and converted to GGUF internally (Llama 2/3/3.1/3.2, Mistral, Mixtral, Gemma 1/2, Phi3).
- **Quantization:** library default is Q4_K_M. All llama.cpp quant types available via `ollama create my-model --quantize <type>`: `f32`, `f16`, `bf16`, `q8_0`, `q5_K_M`, `q4_K_M` (default), `q4_K_S`, `q3_K_{S,M,L}`, `q2_K`, `iq1_s`, `iq2_xxs`, `tq1_0`, etc.

## 5. API Surface

OpenAI-compatible? Native API? Streaming? Tool calling? Embeddings?

## 6. Performance

Throughput (tok/s), latency, batch support. Cite source or note "not benchmarked".

## 7. Documented Strengths

Documented strengths from maintainer docs, benchmarks, or independent comparisons. Cite source.

## 8. Documented Weaknesses

Documented limitations from issue tracker, docs, or community reports. Cite source.

## 9. Sources

- [ollama/ollama](https://github.com/ollama/ollama) — observed 2026-06-14
