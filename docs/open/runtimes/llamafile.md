# llamafile

_Last verified: 2026-06-14_

## 0. TL;DR

llamafile bundles a [GGUF](../GLOSSARY.md#quantization) model and the llama.cpp runtime into a single executable file that runs on macOS, Linux, Windows, and BSDs with no install whatsoever — download, chmod +x, run. Pick it for the ultimate zero-friction demo or air-gapped deployment where you can't install software. The constraint is file size: Windows caps executables at 4 GB, so models larger than that need a separate GGUF file alongside the binary, and it's not suited for multi-user throughput.

## 1. What It Is

llamafile (Mozilla-Ocho/llamafile) is an Apache 2.0 project that combines llama.cpp with Cosmopolitan Libc to ship LLMs as single-file portable executables that run on macOS, Linux, Windows, FreeBSD, OpenBSD, and NetBSD without install.

## 2. Install

No install: download a `.llamafile`, mark it executable, run it. The APE (Actually Portable Executable) format (via Cosmopolitan Libc) produces a single file that runs on all six supported OSes.

- **Supported OSes:** macOS, Linux, Windows, FreeBSD, OpenBSD, NetBSD.
- **macOS / Linux / BSD:** `chmod +x model.llamafile && ./model.llamafile`.
- **Windows:** Rename to `model.llamafile.exe`, then run. Windows enforces a **4 GB max executable size** — for larger models, use a standalone `llamafile` binary with an external GGUF (`./llamafile -m model.gguf`).
- **Headless:** pass `--nobrowser` (e.g., `./model.llamafile --server --nobrowser --host 0.0.0.0`).
- **GPU drivers:** Standard NVIDIA or AMD GPU driver is sufficient. No CUDA Toolkit or ROCm SDK install required by end users — llamafile JIT-compiles GPU kernels at runtime via `nvcc`/`hipcc` if present, falling back to CPU otherwise.

## 3. Hardware Support

- **CUDA (NVIDIA, Linux):** JIT via `nvcc` (`$PATH` or `/usr/local/cuda/bin/nvcc`). Targets Pascal through Hopper; Blackwell (sm_120/121) with CUDA 13.x. CUDA on Windows pending as of v0.10.0.
- **ROCm/HIP (AMD, Linux):** JIT via `hipcc` at `/opt/rocm/bin/hipcc` or `$ROCM_PATH`. Targets Vega 20 (gfx906), RDNA2 (gfx1030), RDNA3 (gfx1100), and other GFX architectures.
- **Metal (Apple Silicon):** macOS ARM64; small Metal module compiled at runtime via system `cc` / Xcode Command Line Tools.
- **Vulkan / OpenCL:** Not currently supported.
- **CPU:** Hand-tuned llama.cpp kernels with runtime dispatch — AVX, AVX2, AVX-512 (added v0.7; up to 10× faster prompt eval on Zen 4); ARM64 NEON.
- **Multi-GPU:** No multi-GPU orchestration. On mixed-vendor systems, backend priority is Metal → AMD → NVIDIA, one backend at a time.
- **No GPU toolkit install required** for end users — JIT activates when drivers and compilers are present.

## 4. Model Formats

- **GGUF only.** Inherits full llama.cpp GGUF support.
- **Two usage modes:**
  - **Embedded:** GGUF zipped (PKZIP) inside the `.llamafile` for a self-contained binary.
  - **External:** standalone `llamafile` binary loads any `.gguf` (`./llamafile -m model.gguf`) — required for >4 GB models on Windows.
- **Quantization:** all llama.cpp types — F32, F16, BF16, Q8_0, Q4_0, K-quants (Q4_K, Q4_K_M, Q5_K, Q5_K_M, Q6_K, Q6_K_M), etc. v0.7 added native BF16 (CPU) and AVX-512 paths for F16/BF16/Q8_0/Q4_0/F32.
- Any GGUF from Hugging Face loads directly — no conversion step needed.

## 5. API Surface

llamafile embeds llama.cpp's server, exposing the same endpoint surface as `llama-server`:

- **OpenAI-compatible:** `POST /v1/chat/completions`, `POST /v1/completions`, `POST /v1/embeddings`.
- **Native llama.cpp endpoints:** `POST /completion`, `POST /embedding`, `POST /infill` (code fill-in-the-middle), `GET /slots`, `GET /metrics` (Prometheus), `GET /health`.
- **Tool / function calling:** Supported via `--jinja` flag, using chat-template-based tool parsing.
- **Vision (multimodal):** Experimental — `image_url` and `input_audio` content parts on `/v1/chat/completions`; requires a vision model with `--mmproj`.
- **Streaming:** SSE via `"stream": true`.
- **Structured outputs:** GBNF grammar (`grammar` parameter) and JSON Schema (`json_schema` parameter).
- **Logprobs:** Via `n_probs` on native `/completion` endpoint (top-N token probabilities).
- **Built-in web UI:** Opens automatically in-browser on launch (suppress with `--nobrowser`); separate from the API.

Third-party reference confirms: completion ✅, streaming ✅, embeddings ✅, list models ✅; vision ❌ (not surfaced through documented official paths). Source: [Mozilla-Ocho/llamafile README](https://github.com/Mozilla-Ocho/llamafile), [docs.mozilla.ai/llamafile](https://docs.mozilla.ai/llamafile/).

## 6. Performance

Not officially benchmarked by maintainers. The README includes AVX-512 optimization notes (v0.7: "up to 10× faster prompt eval on Zen 4 vs prior llamafile" for AVX-512 CPUs) but provides no absolute tok/s figures. No canonical throughput, TTFT, or batch-size numbers are published. GPU performance inherits llama.cpp JIT-compiled CUDA/ROCm/Metal kernels but no benchmarks are cited for these paths. Source: [Mozilla-Ocho/llamafile README](https://github.com/Mozilla-Ocho/llamafile).

## 7. Documented Strengths

- **True zero-install portability:** A single `.llamafile` file runs on macOS, Linux, Windows, FreeBSD, OpenBSD, and NetBSD with no SDK, no package manager, and no dependencies — via Cosmopolitan Libc's APE format. Source: [README](https://github.com/Mozilla-Ocho/llamafile).
- **No GPU toolkit required:** GPU acceleration (CUDA/ROCm/Metal) activates via JIT compilation at runtime if compilers are present; end users need only the standard driver, not CUDA Toolkit or ROCm SDK. Source: [README](https://github.com/Mozilla-Ocho/llamafile).
- **Significant CPU prompt-eval improvement (v0.7):** AVX-512 hand-tuned kernels deliver "up to 10× faster prompt eval on Zen 4" CPUs compared to prior llamafile versions. Source: [README](https://github.com/Mozilla-Ocho/llamafile).
- **Ideal for air-gapped or constrained deployments:** No network access needed after download; embeds model + runtime in one file for fully offline use. Source: [README](https://github.com/Mozilla-Ocho/llamafile).

## 8. Documented Weaknesses

- **Windows 4 GB executable limit:** Windows enforces a 4 GB cap on executable size; models larger than that cannot be embedded and must run as a separate GGUF file alongside the binary. Source: [README](https://github.com/Mozilla-Ocho/llamafile).
- **No CUDA acceleration on Windows (as of v0.10.0):** CUDA JIT is Linux-only; Windows users fall back to CPU on NVIDIA hardware. Source: [README](https://github.com/Mozilla-Ocho/llamafile).
- **No multi-GPU support:** Backend priority is Metal → AMD → NVIDIA; only one GPU backend activates at a time; no tensor-parallel or layer-split across devices. Source: [README](https://github.com/Mozilla-Ocho/llamafile).
- **Not designed for concurrent multi-user serving:** Inherited from llama.cpp's slot-based KV cache — once concurrent requests exceed configured slots, VRAM and latency degrade rapidly; no continuous batching scheduler. Source: [community analysis](https://markaicode.com/alternatives/llamacpp-alternatives/).

## 9. Sources

- [Mozilla-Ocho/llamafile](https://github.com/Mozilla-Ocho/llamafile) — observed 2026-06-14
