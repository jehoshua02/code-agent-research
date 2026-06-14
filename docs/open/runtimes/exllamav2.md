# ExLlamaV2 / ExLlamaV3

_Last verified: 2026-06-14_

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

OpenAI-compatible? Native API? Streaming? Tool calling? Embeddings?

## 6. Performance

Throughput (tok/s), latency, batch support. Cite source or note "not benchmarked".

## 7. Documented Strengths

Documented strengths from maintainer docs, benchmarks, or independent comparisons. Cite source.

## 8. Documented Weaknesses

Documented limitations from issue tracker, docs, or community reports. Cite source.

## 9. Sources

- [turboderp/exllamav2](https://github.com/turboderp/exllamav2) — observed 2026-06-14
