# MLX / mlx-lm

_Last verified: 2026-06-14_

## 0. TL;DR

MLX / mlx-lm is Apple's own framework for running LLMs on Apple Silicon Macs, exploiting the unified CPU+GPU memory to run larger models than discrete-GPU machines can. Pick it if you're on an M-series Mac and want maximum local performance without touching llama.cpp or CUDA. The hard constraint: Apple Silicon and macOS only — nothing else is supported.

## 1. What It Is

MLX (ml-explore/mlx) and mlx-lm (ml-explore/mlx-lm) are MIT-licensed Apple frameworks. Active. Apple-Silicon-native array library and LLM tooling using the Metal GPU; macOS-only, designed to exploit unified memory on M-series chips.

## 2. Install

Apple Silicon Mac (M1 or later), macOS ≥ 14.0 (15.0+ recommended for memory-wiring optimizations on large models), Python ≥ 3.10.

```bash
pip install mlx-lm
# or
conda install -c conda-forge mlx-lm
```

The `mlx` core array framework is installed automatically as a dependency. No Linux or Windows support for the Apple Silicon backend; no CUDA or ROCm path. (Linux-only `mlx[cuda]`/`mlx[cpu]` variants of the core framework exist but are outside the mlx-lm workflow.)

## 3. Hardware Support

- **Metal / Apple Silicon only:** M1, M2, M3, M4 (base/Pro/Max/Ultra). Metal backend; no extra drivers.
- **No CUDA, no ROCm, no Intel/AMD GPU.**
- **Unified memory:** CPU and GPU share the same physical RAM pool — no separate VRAM budget; all system RAM is addressable by the GPU.
- **CPU fallback:** Available within the same unified memory space; significantly slower than Metal.
- **Multi-GPU:** Not applicable (Apple Silicon is single-chip; M-Ultra variants present as a single device).

## 4. Model Formats

- **Native MLX format:** Directory of `.safetensors` shards with `config.json` and tokenizer files; auto-sharded when > 5 GB. Thousands of pre-converted models on the `mlx-community` Hugging Face org.
- **Convert from HuggingFace safetensors:** `mlx_lm.convert --hf-path <repo> --mlx-path ./mlx_model`.
- **Quantization:** `-q` flag defaults to 4-bit affine, group size 64. Options: `--q-bits` (2/3/4/6/8), `--q-group-size`, `--q-mode` (`affine` default, `mxfp4`, `nvfp4`, `mxfp8`), `--quant-predicate` for mixed recipes (`mixed_2_6`, `mixed_3_4`, `mixed_3_6`, `mixed_4_6`).
- **GGUF:** No native loading. `mlx_lm.fuse --export-gguf` can export (Llama/Mistral/Mixtral only, fp16). Importing GGUF requires a third-party tool (e.g., `gguf2mlx`).

## 5. API Surface

`mlx_lm` is primarily a **Python library** (`mlx_lm.generate`, `mlx_lm.stream_generate`), not an OpenAI-compatible server. A lightweight HTTP server is included via `mlx_lm.server` (documented in `SERVER.md`) but carries the warning "not recommended for production as it only implements basic security checks."

- **Endpoints:** `POST /v1/chat/completions` (chat-style generation), `GET /v1/models`. No `/v1/completions` or `/v1/embeddings`.
- **Streaming:** SSE via `"stream": true` on `/v1/chat/completions`; Python-side via `stream_generate()`.
- **Logprobs:** `logprobs` parameter (1–10); response includes `token_logprobs` and `top_logprobs`.
- **Tool / function calling:** Not supported in the built-in server or library.
- **Vision (multimodal):** Not part of `mlx_lm`; handled by the separate `mlx_vlm` package (`pip install mlx-vlm`).
- **Structured outputs:** Not documented.
- **Embeddings:** No `/v1/embeddings` endpoint; embedding extraction requires custom Python code.

Sources: [mlx-lm SERVER.md](https://github.com/ml-explore/mlx-lm/blob/main/mlx_lm/SERVER.md), [README](https://github.com/ml-explore/mlx-lm/blob/main/README.md).

## 6. Performance

Not officially benchmarked by maintainers. No canonical tok/s, TTFT, or batch-size figures are published in the mlx-lm README, SERVER.md, or official docs. The Ollama team published a relative claim of "up to 20% faster" output speed vs prior Ollama builds when switching to the MLX engine on Apple Silicon ([Ollama MLX post](https://ollama.com/blog/mlx-performance)), but no absolute numbers. Community benchmarks vary widely by model size and chip (M3 Max, M4 Ultra, etc.) and are not maintainer-sourced.

## 7. Documented Strengths

- **Best Apple Silicon throughput for small models**: Community benchmarks (June 2026) show Gemma 4 E2B at ~158 tok/s and Phi-4 Mini at ~135 tok/s on M5 Max via MLX — figures not reachable by llama.cpp or GGUF paths on the same hardware. ([llmcheck.net benchmarks](https://llmcheck.net/benchmarks))
- **Runs 70B models at practical speeds on a laptop**: Llama 3.1 70B Q4_K_M achieves ~20 tok/s on M4 Max — a 40 GB model running at usable speed on consumer hardware due to unified memory. ([seankim blog, M4 Max benchmarks](https://blog.imseankim.com/apple-m4-max-macbook-pro-ai-inference-benchmarks/))
- **Memory-efficient native format**: MLX safetensors format is consistently 7–13% smaller than equivalent GGUF (e.g., Qwen3-235B-A22B: 124 GB MLX vs 133 GB GGUF), enabling larger models in unified RAM. ([yage.ai MLX vs llama.cpp](https://yage.ai/share/mlx-apple-silicon-en-20260331.html))
- **Zero-copy unified memory**: Tensor operations share the same physical pool across CPU and GPU with no data movement overhead — the fundamental architectural advantage Apple Silicon provides and MLX exploits. ([arxiv 2601.19139](https://arxiv.org/html/2601.19139))

## 8. Documented Weaknesses

- **Apple Silicon + macOS only**: No CUDA, ROCm, or Linux path for mlx-lm; the project itself warns the server is "not recommended for production." ([mlx-lm SERVER.md](https://github.com/ml-explore/mlx-lm/blob/main/mlx_lm/SERVER.md))
- **No tool calling or embeddings endpoint**: The built-in server exposes only `/v1/chat/completions` and `/v1/models`; tool use and `/v1/embeddings` are absent. ([mlx-lm README](https://github.com/ml-explore/mlx-lm/blob/main/README.md))
- **Prefill lags llama.cpp for short contexts**: Independent comparisons find MLX prefill throughput below llama.cpp on short prompts; advantage is mainly in decode speed on large models. ([medium: On-Device LLM Runtime decision framework](https://medium.com/@michael.hannecke/choosing-an-on-device-llm-runtime-on-apple-silicon-a-decision-framework-beyond-benchmarks-2449067b8b67))
- **Rapidly changing API**: Framework API is still evolving quickly, making production pinning difficult; Metal 4 compatibility issues reported on newest Apple hardware. ([yage.ai](https://yage.ai/share/mlx-apple-silicon-en-20260331.html))

## 9. Sources

- [ml-explore/mlx-lm](https://github.com/ml-explore/mlx-lm) — observed 2026-06-14
