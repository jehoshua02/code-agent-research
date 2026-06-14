# llama.cpp

_Last verified: 2026-06-14_

## 1. What It Is

llama.cpp (ggml-org/llama.cpp) is an MIT-licensed C/C++ inference framework. Active. Runs LLMs efficiently on CPU and GPU (CUDA, Metal, ROCm, Vulkan) using the GGUF format; the upstream of many derived runtimes (Ollama, KoboldCpp, llamafile).

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

- [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp) — observed 2026-06-14
