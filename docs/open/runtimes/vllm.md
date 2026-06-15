# vLLM

_Last verified: 2026-06-14_

## 1. What It Is

vLLM (vllm-project/vllm) is an Apache 2.0 Python inference engine. Active. High-throughput, memory-efficient serving via PagedAttention; OpenAI-compatible API; the de facto choice for production GPU serving of open-weight models.

## 2. Install

- **Linux (primary):** `uv pip install vllm --torch-backend=auto` (Python 3.10–3.13, wheels for `manylinux_2_35`). AMD: `uv pip install vllm --extra-index-url https://wheels.vllm.ai/rocm/`. Source build: `uv pip install -e . --torch-backend=auto`; CPU build: `VLLM_TARGET_DEVICE=cpu uv pip install . --no-build-isolation`.
- **Windows:** Not natively supported; run via WSL or community forks.
- **macOS (Apple Silicon):** Community `vllm-metal` plugin (macOS Sonoma+); no prebuilt wheels.
- **Docker:** NVIDIA `vllm/vllm-openai:latest` with `--runtime nvidia --gpus all --ipc=host`; AMD `vllm/vllm-openai-rocm` with `--device /dev/kfd --device /dev/dri`; CPU `vllm/vllm-openai-cpu:latest-{x86_64,arm64}`.
- **CUDA:** 12.9 default; 12.8 and 13.0 also supported (B200/GB200 needs ≥ 12.8). Compute capability ≥ 7.5. GCC ≥ 11.3 for source builds.
- **Quirks:** Fresh venv (conda's NCCL conflicts); set `VLLM_ENABLE_CUDA_COMPATIBILITY=1` for legacy drivers; Intel XPU needs `triton-xpu==3.7.1` and Python 3.12; AMD ROCm requires precompiled wheels or the validated Triton branch.

## 3. Hardware Support

- **NVIDIA CUDA:** Turing through Blackwell (T4, RTX 20xx–50xx, A100, L4, H100, B200/GB200). All quantization paths.
- **AMD ROCm:** Instinct MI200/MI300/MI350, Radeon RX 7900/9000, Ryzen AI MAX; ROCm ≥ 6.3 (MI350 needs 7.0+, Ryzen AI MAX 7.0.2+). Supports GGUF and FP8 W8A8; no AWQ or bitsandbytes.
- **Apple Silicon / Metal:** Via community `vllm-metal` plugin (macOS Sonoma+), FP32/FP16 only; MLX-community models recommended.
- **CPU:** x86 (AVX512F recommended), ARM AArch64 (NEON), Apple Silicon (experimental), IBM Z s390x (experimental). KV cache size via `VLLM_CPU_KVCACHE_SPACE`; thread pinning via `VLLM_CPU_OMP_THREADS_BIND`.
- **Other accelerators:** Google TPU, Intel Gaudi, Intel XPU, IBM Spyre, Huawei Ascend, Rebellions NPU, MetaX GPU (plugin ecosystem).
- **Parallelism:** Tensor parallel (`--tensor-parallel-size`), pipeline parallel (`--pipeline-parallel-size`), expert parallel (MoE), data parallel; multi-node requires Ray (`--distributed-executor-backend ray`).
- **Memory:** PagedAttention; `--gpu-memory-utilization` (default 0.92); `--cpu-offload-gb <GB>` for weight offload with `uva` or `prefetch` backends. KV cache CPU offload is a known gap in v1.

## 4. Model Formats

- **safetensors:** Default HuggingFace weight format.
- **GGUF:** Highly experimental, moved to the out-of-tree `vllm-gguf-plugin`; usage like `vllm serve repo:Q4_K_M --tokenizer <base>`. NVIDIA + AMD, not Intel/CPU.
- **AWQ:** W4A16; Turing+ NVIDIA, Intel GPU, x86 CPU. Not AMD or ARM CPU.
- **GPTQ (GPTQModel):** Volta+ NVIDIA, Intel GPU, x86 CPU.
- **FP8:** W8A8 via llm-compressor on Ada/Hopper NVIDIA and AMD; also MXFP8/MXFP4 and NVFP4.
- **bitsandbytes:** NVIDIA only (Volta–Hopper).
- **compressed-tensors (llm-compressor):** FP8 W8A8, INT4 W4A16, INT8 W4A8, INT8 W8A8 — hardware coverage varies.
- **Marlin / DeepSpeedFP / TorchAO / NVIDIA ModelOpt / AMD Quark / Intel Neural Compressor:** Additional quant backends. Online quantization and KV cache quantization also supported. Select with `--quantization`.

## 5. API Surface

Full OpenAI-compatible HTTP server (`vllm serve`): `/v1/chat/completions`, `/v1/completions`, `/v1/embeddings` (Pooling/Embed entrypoint), `/v1/models`. Also exposes Anthropic Messages API, native gRPC (`vllm.entrypoints.serve.dev.rpc`), and MCP entrypoint (`vllm.entrypoints.mcp`).

- **Tool / function calling:** `auto`, `required`, `none`, named-function `tool_choice`; parallel tool calls; streaming tool-call extraction. Per-model tool parser plugins (Llama 3.1/4, Mistral, Hermes, DeepSeek-V3, Qwen2.5, Granite, etc.). [tool_calling docs](https://docs.vllm.ai/en/latest/features/tool_calling.html).
- **Vision / multimodal:** Images (PIL/URL/base64), video (frames/URL), audio (array+rate) via `image_url`, `video_url`, `input_audio` / `audio_url` content fields on Chat Completions. [multimodal_inputs docs](https://docs.vllm.ai/en/latest/features/multimodal_inputs.html).
- **Streaming:** SSE on chat completions and completions, including mid-generation tool-call extraction.
- **Structured outputs:** xgrammar and guidance backends; JSON Schema, regex (Rust), EBNF, choices, structural tags. Via `response_format`/`extra_body` or `--structured-outputs-config.backend`. [structured_outputs docs](https://docs.vllm.ai/en/latest/features/structured_outputs.html).
- **Logprobs:** Per-token `logP` and prompt `prmpt logP`, broad hardware coverage.

## 6. Performance

Maintainers do not publish a static table of canonical figures. The [benchmarking docs](https://docs.vllm.ai/en/latest/benchmarking/) describe tooling (CLI, Parameter Sweeps, Performance Dashboard) with per-commit results pushed to a PyTorch CI dashboard.

The only fixed maintainer-authored numbers come from the [launch blog post (June 2023)](https://vllm.ai/blog/2023-06-20-vllm) on A10G/A100 with LLaMA-family models: **14×–24×** higher throughput than HF Transformers (single output), **8.5×–15×** (3 parallel); **2.2×–2.5×** over TGI (single), **3.3×–3.5×** (3 parallel); LMSYS reported up to **30×** higher throughput vs. initial HF backend (50% fewer GPUs handling ~30K req/day, peak 60K). Dashboard sample shows ~24.98–28.61 tok/s for Llama-3.1-8B-Instruct at 2048 in/out across concurrency, presented as illustrative. Prefill vs decode is measured separately by the benchmark tooling but not split out in published figures.

## 7. Documented Strengths

Documented strengths from maintainer docs, benchmarks, or independent comparisons. Cite source.

## 8. Documented Weaknesses

Documented limitations from issue tracker, docs, or community reports. Cite source.

## 9. Sources

- [vllm-project/vllm](https://github.com/vllm-project/vllm) — observed 2026-06-14
