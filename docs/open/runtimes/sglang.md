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

Full OpenAI-compatible endpoints: `/v1/chat/completions` (applies chat templates), `/v1/completions` (raw text), `/v1/embeddings`. SSE streaming on both via `stream=True`.

- **Tool / function calling:** OpenAI-compatible on `/v1/chat/completions`. Dedicated native `/parse_function_call`. Supported families: Llama 3.1/3.2/3.3/4, Qwen, DeepSeek-v3, Mistral, GLM. [tool_parser docs](https://docs.sglang.io/docs/advanced_features/tool_parser.md).
- **Vision (multimodal):** OpenAI-compatible vision API (images as `image_url` content). Llama 3.2, LLaVA-OneVision, Qwen2.5-VL, Gemma3, etc. [openai_api_vision](https://docs.sglang.io/docs/basic_usage/openai_api_vision.md).
- **Structured outputs:** JSON schema (`response_format`), regex, EBNF grammar. Backends: XGrammar (default), Outlines, Llguidance. Available via OpenAI API (`response_format`/`extra_body`), native `/generate` (`sampling_params`), and offline engine. "3× faster JSON decoding with compressed finite state machine." [structured_outputs](https://docs.sglang.io/docs/advanced_features/structured_outputs.md).
- **Logprobs:** Native via `/generate` with `return_logprob`, `logprob_start_len`, `top_logprobs_num`, `token_ids_logprob`, `return_text_in_logprobs`.
- **Native non-OpenAI APIs:** `/generate`, `/encode`, `/v1/rerank`, `/v1/score`, `/classify`, `/tokenize`, `/detokenize`, `/flush_cache`, `/update_weights_from_disk`, `/get_model_info`, `/server_info`, `/health`, MoE expert distribution. Ollama-compatible API also documented.

## 6. Performance

Maintainers (LMSYS) publish relative throughput figures in release blogs; no single canonical absolute table.

- **vs vLLM/TRT-LLM ([July 2024 blog](https://lmsys.org/blog/2024-07-25-sglang-llama3/), Llama-8B on 1× A100 bf16):** SGLang and TRT-LLM both reached ~**5,000 tok/s** output; vLLM significantly lower. Llama-70B on 8× A100 bf16: **up to 3.1×** vLLM throughput, competitive with TRT-LLM. Llama-70B on 8× H100 fp8: highest of all systems tested.
- **GB200 NVL72 (v0.4 release notes):** "**3.8× Prefill, 4.8× Decode Throughput**" vs prior baseline on DeepSeek; "**2.7× Higher Decoding Throughput**" in large-scale expert-parallelism. Relative only.
- **RadixAttention:** "Up to 5× faster" vs vLLM/Guidance on prefix-cache-heavy multi-call workloads ([Jan 2024 blog](https://lmsys.org/blog/2024-01-17-sglang/)).
- **JSON decoding:** "3× faster" with compressed FSM.

Prefill and decode reported separately in GB200 figures. TTFT/latency charts shown without numeric prose.

## 7. Documented Strengths

Documented strengths from maintainer docs, benchmarks, or independent comparisons. Cite source.

## 8. Documented Weaknesses

Documented limitations from issue tracker, docs, or community reports. Cite source.

## 9. Sources

- [sgl-project/sglang](https://github.com/sgl-project/sglang) — observed 2026-06-14
