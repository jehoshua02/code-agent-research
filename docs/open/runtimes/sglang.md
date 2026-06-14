# SGLang

_Last verified: 2026-06-14_

## 1. What It Is

SGLang (sgl-project/sglang) is an Apache 2.0 Python serving engine. Active. Combines a high-performance backend with a structured-generation frontend language; competitive with vLLM on throughput, with built-in support for constrained outputs.

## 2. Install

- **Linux (primary):** `uv pip install sglang` (manylinux wheels, glibc ≥ 2.34, x86-64 and aarch64). Extras: `sglang[all]`, `[diffusion]`, `[ray]`, `[tracing]`, `[http2]`, `[fastokens]`, `[checkpoint-engine]`, `[runai]`. For CUDA 12.9: install PyTorch 2.11 from `https://download.pytorch.org/whl/cu129` and the kernel from `https://docs.sglang.ai/whl/cu129/`.
- **Docker:** `lmsysorg/sglang:latest` (CUDA 12.9), `-runtime` (smaller production), `-cu130-runtime` (Blackwell B300/GB300), `dev-cu12`, `nightly`. Requires `--shm-size 32g`.
- **macOS (Apple Silicon):** Experimental MLX backend, Python 3.11 only; roadmap target 2026 Q1.
- **Windows:** Not officially supported (open tracking issue).
- **CUDA:** 12.9 default; CUDA 13 for Blackwell. Minimum compute capability SM75 (Turing+) for the default FlashInfer backend — older GPUs need `--attention-backend triton --sampling-backend pytorch`.
- **Python:** 3.10–3.13.

## 3. Hardware Support

- **NVIDIA CUDA:** GB200, B300, H100, A100, L40S, L4, A10, T4, Jetson. Default FlashInfer kernels; tensor, pipeline, expert, and data parallelism all supported.
- **AMD ROCm:** MI355, MI325, MI300 series. FP8, AWQ, GPTQ, MXFP4, compressed-tensors all work; `awq_marlin` / `gptq_marlin` do not.
- **CPU:** Intel Xeon x86-64 path with dedicated docs (not GPU-accelerated).
- **Other accelerators:** Google TPU (sglang-jax), Ascend NPU (CANN), Intel XPU — each with separate install guides.
- **Multi-GPU / multi-node:** Tensor + pipeline + expert + data parallelism; multi-node via Kubernetes, Docker Compose, or SkyPilot.
- **KV cache:** RadixAttention prefix caching (automatic reuse across requests); paged attention for memory-efficient KV.

## 4. Model Formats

- **safetensors / HuggingFace:** Primary; loaded from Hub or local path.
- **GPTQ:** Offline pre-quantized; NVIDIA, AMD, Ascend.
- **AWQ:** Offline pre-quantized; NVIDIA, AMD, Ascend. Marlin-fused `awq_marlin` is NVIDIA-only.
- **FP8:** Offline and online (`--quantization fp8`); NVIDIA SM80+ and AMD MI300+.
- **GGUF:** NVIDIA and Ascend only; not supported on ROCm.
- **FP4 / MXFP4:** NVIDIA Blackwell (native FP4 recommended; ModelOpt FP4 from SM80+) and AMD MI300+ MXFP4.
- **INT4 / INT8:** Via GPTQ, AWQ, bitsandbytes, torchao (`int4wo-128`, `int8dq`), auto-round (Intel).
- **Other backends:** `compressed-tensors`, `torchao`, `bitsandbytes`, `auto-round`, NVIDIA `ModelOpt` (FP8/FP4), Ascend `ModelSlim`, AMD `quark_int4fp8_moe` / `quark_mxfp4`.
- Quantization can be offline (load pre-quantized) or online (`--quantization <method>`). Offline is recommended for performance.

## 5. API Surface

OpenAI-compatible? Native API? Streaming? Tool calling? Embeddings?

## 6. Performance

Throughput (tok/s), latency, batch support. Cite source or note "not benchmarked".

## 7. Documented Strengths

Documented strengths from maintainer docs, benchmarks, or independent comparisons. Cite source.

## 8. Documented Weaknesses

Documented limitations from issue tracker, docs, or community reports. Cite source.

## 9. Sources

- [sgl-project/sglang](https://github.com/sgl-project/sglang) — observed 2026-06-14
