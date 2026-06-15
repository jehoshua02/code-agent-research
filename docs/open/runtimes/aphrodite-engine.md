# Aphrodite Engine

_Last verified: 2026-06-14_

## 0. TL;DR

Aphrodite Engine is a vLLM fork aimed at community and hobbyist GPU hosting, adding support for more [quantization](../GLOSSARY.md#quantization) formats than upstream vLLM. Pick it over vLLM if you need quantization formats vLLM doesn't support (such as GGUF or AQLM) while still getting a high-throughput OpenAI-compatible server. The catch: AGPL-3.0 license has copyleft implications for commercial use, and like vLLM it's Linux+NVIDIA-only (Windows via WSL2 only, no macOS).

## 1. What It Is

Aphrodite Engine (aphrodite-engine/aphrodite-engine) is an AGPL-3.0 Python serving engine derived from vLLM. Active. OpenAI-compatible, with quantization-format support beyond upstream vLLM; community-oriented around large-scale local hosting.

## 2. Install

- **Linux (pip):** `pip install -U aphrodite-engine` — prebuilt wheels target CUDA 12.8/12.9, Python 3.10–3.13.
- **Windows:** Via WSL2 only.
- **macOS:** Not supported.
- **Docker:** `docker run --runtime nvidia --gpus all -v ~/.cache/huggingface:/root/.cache/huggingface -p 2242:2242 --ipc=host alpindale/aphrodite-openai:latest`
- **From source:** `git clone https://github.com/PygmalionAI/aphrodite-engine && cd aphrodite-engine && uv pip install -e .` (needed for Python 3.14, non-standard CUDA, ARM64/GH200).
- **GPU:** NVIDIA with compute capability ≥ 7.0 (Volta+) and CUDA ≥ 12; NVIDIA Container Toolkit for Docker.

## 3. Hardware Support

- **CUDA / NVIDIA:** Volta (sm70), Turing (sm75), Ampere (sm80/86), Ada (sm89), Hopper (sm90); Blackwell support via NVFP4.
- **ROCm / AMD:** Supported, but quantization is limited to GPTQ, INT8, FP8, BitsAndBytes, VPTQ, Experts-INT8.
- **Metal / Apple Silicon:** Not supported.
- **CPU (x86 AVX2/AVX512, ppc64le):** Supported; only AWQ quantization works on CPU.
- **Other accelerators:** Intel XPU (limited quant), Google TPU (TPU-INT8 only), AWS Inferentia/Trainium (Neuron-Quant).
- **Multi-GPU:** Tensor parallelism for distributed inference.
- **Memory:** Defaults to 92% GPU VRAM (`--gpu-memory-utilization` configurable); FP8 E5M2 / E4M3 / INT8 KV cache quantization plus TurboQuant.

## 4. Model Formats

Loads HuggingFace safetensors and PyTorch state_dict for almost all architectures. Quantization-format breadth is the engine's main differentiator from vLLM:

- **Weight formats:** GGUF (all architectures, single or sharded), AWQ, GPTQ (2/3/4/8-bit via ExLlamaV2 kernels), EXL2 (ExLlamaV2) and ExLlamaV3, AQLM (2-bit), AutoRound, BitNet (1-bit), bitsandbytes (8-bit), QuIP# (2-bit), SqueezeLLM (4-bit), Marlin, NVIDIA ModelOpt (FP8/FPGEMM-FP8), TorchAO, VPTQ, compressed_tensors, MXFP4 (Blackwell native; Marlin on Ampere/Hopper), DeepSpeedFP, EETQ (INT8), QQQ, SmoothQuant+ (4-/8-bit), Experts-INT8 (MoE).
- **KV cache quantization:** FP8 E5M2 (CUDA 11.8+), FP8 E4M3, INT8 with calibration, TurboQuant.
- **Differentiators vs. vLLM:** EXL2/ExLlamaV2/V3, QuIP#, SqueezeLLM, AQLM, BitNet.

## 5. API Surface

OpenAI-compatible HTTP server on port 2242 (`aphrodite run <model>`), inheriting vLLM's endpoint set: `/v1/chat/completions`, `/v1/completions`, `/v1/embeddings`, `/v1/models`. The docs describe it as supporting "Text/Chat Completions, Vision, and Batch API."

- **Tool / function calling:** Supported via the OpenAI `tools` parameter (inherited from vLLM); exact per-model parser availability matches upstream.
- **Vision (multimodal):** Supported — listed explicitly in the docs alongside Chat Completions and Batch API.
- **Streaming:** SSE on chat and completion endpoints (inherited from vLLM).
- **Structured outputs:** Inherited from vLLM (xgrammar/guidance); JSON Schema, regex, EBNF via `response_format`.
- **Logprobs:** Supported (inherited from vLLM); per-token and prompt logprobs.
- **Additional samplers:** DRY, XTC, Mirostat, and other community samplers exposed as extra parameters — beyond the OpenAI-compatible surface.

Sources: [aphrodite-engine README](https://github.com/aphrodite-engine/aphrodite-engine), [docs landing page](https://aphrodite.pygmalion.chat/).

## 6. Performance

Not officially benchmarked by maintainers. No canonical tok/s, TTFT, or throughput figures are published in the README or documentation. The engine inherits vLLM's PagedAttention and continuous batching; the README emphasizes architectural features (speculative decoding with EAGLE/DFlash/MTP, MXFP4 on Blackwell, custom CUDA kernels) without numerical claims. Source: [aphrodite-engine README](https://github.com/aphrodite-engine/aphrodite-engine).

## 7. Documented Strengths

Documented strengths from maintainer docs, benchmarks, or independent comparisons. Cite source.

## 8. Documented Weaknesses

Documented limitations from issue tracker, docs, or community reports. Cite source.

## 9. Sources

- [aphrodite-engine/aphrodite-engine](https://github.com/aphrodite-engine/aphrodite-engine) — observed 2026-06-14
