# TGI (text-generation-inference)

_Last verified: 2026-06-14_

## 0. TL;DR

TGI (Text Generation Inference) is HuggingFace's production-grade inference server — a Docker image you point at a HuggingFace model ID to get an OpenAI-compatible API endpoint with [continuous batching](../GLOSSARY.md#batching) and tensor parallelism. Pick it if you're already in the HuggingFace ecosystem and want a supported, production-ready server without much custom config. The main friction is it's Docker-first with Linux+NVIDIA as the assumed environment; macOS and Windows are not first-class.

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

TGI exposes two parallel surfaces.

**Native TGI API** (since v1.0): `POST /generate`, `POST /generate_stream`, `POST /tokenize`, `POST /embed`, `GET /info`, `GET /health`, `GET /metrics` (Prometheus).

**OpenAI-compatible Messages API** (since v1.4.0): `POST /v1/chat/completions` is fully compatible with OpenAI Chat Completion (point `base_url` at TGI with no other client changes). `/v1/completions` and `/v1/embeddings` are **not** explicitly documented as supported.

- **Tool / function calling:** Supported on `/v1/chat/completions` via OpenAI `tools` / `tool_choice` schema (since v1.4.3; `auto`, `none`, `required`, or named function). Implemented as grammar-constrained generation via [outlines](https://github.com/outlines-dev/outlines).
- **Vision (multimodal):** Idefics 1/2/3, LLaVA-Next 1.6, PaliGemma, Mllama (Llama 3.2 Vision), Qwen2-VL, Qwen2.5-VL, Gemma3, Llama4.
- **Streaming:** SSE on both `/generate_stream` and `/v1/chat/completions` (`stream: true`).
- **Structured outputs:** Grammar-constrained generation via outlines — JSON schema (incl. Pydantic) and regex on `/generate`. Disable with `--disable-grammar-support`.
- **Logprobs:** Supported. Prefill logprobs off by default (VRAM); enable with `--enable-prefill-logprobs`. `top_n_tokens` (up to `--max-top-n-tokens`, default 5) returns top-N per step.

Sources: [api_reference](https://huggingface.co/docs/text-generation-inference/en/reference/api_reference), [using_guidance](https://huggingface.co/docs/text-generation-inference/en/basic_tutorials/using_guidance), [streaming](https://huggingface.co/docs/text-generation-inference/en/conceptual/streaming).

## 6. Performance

Not benchmarked by maintainer. The docs describe enabling features — continuous batching, Flash/Paged Attention, tensor parallelism, speculative decoding (n-gram or Medusa via `--speculate`), CUDA graph capture for fixed batch sizes (1, 2, 4, 8, 16, 32), quantization (AWQ/GPTQ/FP8/bitsandbytes) — but publish no specific tokens/sec, TTFT, or inter-token latency numbers. The launcher distinguishes prefill from decode conceptually (`--max-batch-prefill-tokens`, `--max-batch-total-tokens`, `--waiting-served-ratio`, `--max-waiting-tokens`) without numerical results. The README notes TGI is in maintenance mode, pointing users toward vLLM and SGLang. Sources: [index](https://huggingface.co/docs/text-generation-inference/en/index), [launcher](https://huggingface.co/docs/text-generation-inference/en/reference/launcher).

## 7. Documented Strengths

Documented strengths from maintainer docs, benchmarks, or independent comparisons. Cite source.

## 8. Documented Weaknesses

Documented limitations from issue tracker, docs, or community reports. Cite source.

## 9. Sources

- [huggingface/text-generation-inference](https://github.com/huggingface/text-generation-inference) — observed 2026-06-14
