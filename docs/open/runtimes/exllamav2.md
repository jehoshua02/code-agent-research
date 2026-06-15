# ExLlamaV2 / ExLlamaV3

_Last verified: 2026-06-14_

## 0. TL;DR

ExLlamaV2 is a Python library optimized for running [quantized](../GLOSSARY.md#quantization) models (GPTQ and its own EXL2 format) on NVIDIA GPUs with high token throughput and low VRAM usage. Pick it if you're a hobbyist or researcher squeezing the most out of a consumer NVIDIA GPU, or if you use Text Generation WebUI (which uses it under the hood). macOS is not supported, and it requires a CUDA-capable NVIDIA GPU — no AMD or CPU-only path.

## 1. What It Is

ExLlamaV2 / V3 (turboderp/exllamav2) is an MIT-licensed Python/CUDA inference library. Active. Specializes in fast, memory-efficient 4-bit (GPTQ/EXL2) GPU inference; used by Text Generation WebUI and other front-ends.

## 2. Install

- **Linux (primary):** `pip install exllamav2`. The PyPI package ships without a prebuilt CUDA extension; it JIT-compiles on first import using the system CUDA Toolkit. Set `EXLLAMA_NOCOMPILE=1` to skip JIT (falls back to slow pure-Python paths).
- **Prebuilt wheels:** Per-platform / Python / CUDA wheels on GitHub Releases (e.g., `cp310-cu121`); install the exact match with `pip install <wheel>.whl`.
- **From source:** `git clone https://github.com/turboderp-org/exllamav2 && pip install -r requirements.txt && pip install .`. Requires CUDA Toolkit (12.1+ recommended, 12.4+ for ExLlamaV3), matching PyTorch, Python dev headers, gcc on Linux / VS Build Tools on Windows.
- **Windows:** Supported with VS Build Tools; prebuilt wheels available.
- **macOS:** Not supported.
- **FlashAttention (optional):** Requires CUDA 12.1+ and matching PyTorch; needed for paged attention.

## 3. Hardware Support

- **NVIDIA CUDA only.** Minimum compute capability **sm_80 (Ampere)** — Turing (RTX 20-series, GTX 16-series) and older are not supported.
- **Supported architectures:** Ampere (sm80), Ada Lovelace (sm89), Hopper (sm90), Blackwell (sm100, tested on RTX 5090). FlashAttention 2.5.7+ silently disabled on unsupported hardware.
- **ROCm / AMD:** Not supported (listed as future work for ExLlamaV3).
- **Metal / macOS:** Not supported.
- **CPU:** No native CPU inference mode; `EXLLAMA_NOCOMPILE=1` does not enable a CPU fallback.
- **Multi-GPU:** Layer-level pipeline split via `--gpu_split auto` or explicit per-device VRAM (`--gpu_split 16,24`). Pipeline-parallel rather than tensor-parallel.
- **Paged attention:** Via FlashAttention 2.5.7+, page size 256; supports continuous batching and mid-batch sequence add/remove.
- **KV cache:** Q4 and Q8 cache modes; dynamic generator deduplicates pages across shared-prefix sequences. No native CPU-RAM offload (open issue #225).

## 4. Model Formats

- **EXL2 (native):** Mixed-precision GPTQ-style quantization, **2 / 3 / 4 / 5 / 6 / 8 bpw**, bit widths can vary per layer/tensor (e.g., 2.55 bpw Llama 2 70B in 24 GB VRAM). Quantized offline with the included `convert.py` and a calibration dataset.
- **GPTQ:** 4-bit, loaded from safetensors (same compatibility as ExLlamaV1).
- **safetensors:** Container for EXL2 and GPTQ weights; full-precision FP16/BF16 HuggingFace models can be loaded directly for inference or as input to quantization.
- **GGUF:** Not supported by the core engine. Some third-party wrappers ship optional GGUF support (`exllamav2[gguf]` in certain forks), not upstream.

## 5. API Surface

ExLlamaV2 does **not** ship an OpenAI-compatible HTTP server. The README recommends **TabbyAPI** (a separate project) — "a FastAPI-based server that provides an OpenAI-style web API" with embeddings and Jinja2 chat templates. TabbyAPI's endpoint coverage (`/v1/chat/completions`, `/v1/completions`, `/v1/embeddings`, tool calling, logprobs) is documented in TabbyAPI itself.

Natively in ExLlamaV2:

- **WebSocket server** (`ExLlamaV2WebSocketServer`, `examples/ws_server.py`): bespoke JSON-over-WebSocket protocol; not OpenAI-compatible.
- **Streaming:** Token-by-token via `ExLlamaV2StreamingGenerator` and `ExLlamaV2DynamicGenerator.iterate()` (pull-based iteration, prefill/streaming stages distinct). Network streaming through the WebSocket server.
- **Structured outputs:** Integrations with `lm-format-enforcer` (`ExLlamaV2TokenEnforcerFilter`) and `formatron` (`FormatterBuilder`) — both enforce Pydantic/JSON Schema at the token level.
- **Vision / multimodal:** Native via `ExLlamaV2VisionTower` + `ExLlamaV2Embedding`. Tested: Pixtral 12B, Mistral-Small 3.1 24B, Qwen2-VL 7B, Gemma3 27B.
- **Tool calling, logprobs:** Not documented or demonstrated in the core repo.

Sources: [ExLlamaV2 README](https://github.com/turboderp-org/exllamav2), [examples/](https://github.com/turboderp-org/exllamav2/tree/master/examples).

## 6. Performance

Maintainer-published throughput (single RTX 4090, single-sequence decode):

| Model | Format | Decode (tok/s) |
|---|---|---|
| Llama 7B | GPTQ 4-bit, 128 group | ~205 |
| Llama 2 7B | EXL2 3.0 bpw | ~257 |
| Llama 2 70B | EXL2 2.5 bpw | ~38 |
| TinyLlama 1.1B | EXL2 3.0 bpw | ~770 |

Prefill throughput not reported separately. No TTFT, multi-GPU scaling, or batch-size curves in the README. The `doc/dynamic.md` notes batch/continuous-batching benchmarks may be added "in the future." Source: [ExLlamaV2 README](https://github.com/turboderp-org/exllamav2) (Performance section).

## 7. Documented Strengths

Documented strengths from maintainer docs, benchmarks, or independent comparisons. Cite source.

## 8. Documented Weaknesses

Documented limitations from issue tracker, docs, or community reports. Cite source.

## 9. Sources

- [turboderp/exllamav2](https://github.com/turboderp/exllamav2) — observed 2026-06-14
