# TGI (text-generation-inference)

_Last verified: 2026-06-14_

## 1. What It Is

Text Generation Inference (huggingface/text-generation-inference) is HuggingFace's production inference server. Apache 2.0 (re-licensed after a brief HFOIL period). Active. Rust+Python, OpenAI-compatible, supports many model architectures with tensor parallelism.

## 2. Install

Supported platforms (Linux / macOS / Windows / specific distros). Concrete install steps for each. Note any per-runtime quirks (driver versions, kernel modules, etc.). See [../README.md](../README.md#4-deployment-notes) for general reader-facing deployment context.

## 3. Hardware Support

CUDA / ROCm / Metal / CPU. Multi-GPU. Memory mapping. Offloading.

## 4. Model Formats

GGUF, AWQ, GPTQ, FP8, safetensors, etc. Quantization options.

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
