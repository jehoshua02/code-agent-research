# TGI (text-generation-inference)

_Last verified: 2026-06-14_

## 1. What It Is

Text Generation Inference (huggingface/text-generation-inference) is HuggingFace's production inference server. Apache 2.0 (re-licensed after a brief HFOIL period). Active. Rust+Python, OpenAI-compatible, supports many model architectures with tensor parallelism.

## 2. Install

Primary distribution is Docker: `ghcr.io/huggingface/text-generation-inference` (NVIDIA image; `-rocm` tag for AMD). Requires CUDA 12.2+ and the NVIDIA Container Toolkit for GPU passthrough (`--gpus all`).

- **Linux (Docker):** `docker run --gpus all --shm-size 64g -p 8080:80 -v $PWD/data:/data ghcr.io/huggingface/text-generation-inference --model-id <model>`
- **Linux (native, from source):** Rust toolchain via `rustup`, Python 3.9+, `protoc`, then `BUILD_EXTENSIONS=True make install`. Launch via `text-generation-launcher --model-id <model>`.
- **macOS:** No native GPU support (no Metal backend). Docker is the only practical path.
- **Windows:** No native build. Docker only.
- **AMD/ROCm Docker:** `ghcr.io/huggingface/text-generation-inference:<tag>-rocm`, run with `--device=/dev/kfd --device=/dev/dri --group-add video`.

## 3. Hardware Support

- **CUDA / NVIDIA:** Fully optimized on H100, A100, A10G, T4 (CUDA 12.2+). On other NVIDIA GPUs continuous batching still works but Flash Attention and Paged Attention are unavailable.
- **ROCm / AMD:** Tested on Instinct MI210, MI250, MI300. Two Flash Attention implementations (Composable Kernel default; Triton variant). Custom Paged Attention kernel default. AWQ and Mistral sliding-window attention are not supported on ROCm.
- **Metal / Apple Silicon:** Not supported.
- **CPU:** Available but explicitly not an intended platform.
- **Other accelerators:** AWS Inferentia, Intel GPU, Intel Gaudi, Google TPU.
- **Multi-GPU:** Tensor parallelism via `--sharded true --num-shard <N>`.

## 4. Model Formats

- **safetensors:** Primary weight format.
- **GPTQ:** Pre-quantized weights (`--quantize gptq`); compatible with AutoGPTQ/Optimum outputs.
- **AWQ:** Pre-quantized weights (`--quantize awq`); NVIDIA only.
- **FP8:** On-the-fly (`--quantize fp8`).
- **bitsandbytes:** On-the-fly 8-bit or 4-bit (`bitsandbytes`, `bitsandbytes-nf4`, `bitsandbytes-fp4`).
- **EETQ:** On-the-fly 8-bit (`--quantize eetq`).
- **Marlin:** Pre-quantized weights.
- **EXL2:** Pre-quantized weights.
- **GGUF:** Not a supported format.

## 5. API Surface

OpenAI-compatible? Native API? Streaming? Tool calling? Embeddings?

## 6. Performance

Throughput (tok/s), latency, batch support. Cite source or note "not benchmarked".

## 7. Documented Strengths

Documented strengths from maintainer docs, benchmarks, or independent comparisons. Cite source.

## 8. Documented Weaknesses

Documented limitations from issue tracker, docs, or community reports. Cite source.

## 9. Sources

- [huggingface/text-generation-inference](https://github.com/huggingface/text-generation-inference) — observed 2026-06-14
