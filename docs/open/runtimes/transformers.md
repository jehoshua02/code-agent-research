---
name: "transformers"
maker: "HuggingFace"
license: "Apache-2.0"
license_category: "apache-2.0"
status: "active"
url: "https://github.com/huggingface/transformers"
last_verified: "2026-06-14"
language: "Python"
platforms: ["linux", "macos", "windows"]
gpu_backends: ["cuda", "rocm", "metal", "cpu"]
api_openai_compat: false
supports_mcp: "none"
formats: ["safetensors", "gguf", "gptq", "awq"]
notes: "Library, not a server; GGUF loads as dequantized FP32 — for inference use llama.cpp or vLLM."
---

# transformers (HF baseline)

_Last verified: 2026-06-14_

## 0. TL;DR

HuggingFace Transformers is the Python library for loading and running open-weight models — it's the reference implementation most other tools are built on top of. Pick it when you need programmatic access to model internals (fine-tuning, embeddings, custom pipelines) rather than a ready-made API server. The catch is that it's a library, not a server: raw throughput is lower than purpose-built serving engines, and you have to wire up your own HTTP layer if you need an API endpoint.

## 1. What It Is

transformers (huggingface/transformers) is HuggingFace's Apache 2.0 Python library for loading and running model architectures. Active. More a library than a runtime — typically used directly by developers or wrapped by serving stacks; the canonical reference implementation for most open-weight architectures.

## 2. Install

Python 3.10+ and PyTorch 2.4+. Linux, macOS, and Windows are all supported; GPU support comes from the underlying framework (PyTorch / TensorFlow) and is installed separately.

```bash
pip install transformers                          # base
pip install "transformers[torch]"                 # bundle PyTorch
pip install torch --index-url https://download.pytorch.org/whl/cpu  # CPU-only torch
pip install git+https://github.com/huggingface/transformers          # dev/main
conda install conda-forge::transformers
```

For GPU, install the matching PyTorch build from [pytorch.org](https://pytorch.org/get-started/locally/) (CUDA, ROCm, or MPS).

## 3. Hardware Support

- **CUDA / NVIDIA:** Via PyTorch; any CUDA-capable GPU.
- **ROCm / AMD:** PyTorch ROCm build; Instinct (MI210/MI250/MI300, FlashAttention2), Radeon Pro, Radeon.
- **Metal / Apple Silicon:** PyTorch MPS backend (`device="mps"`); some quant backends (bitsandbytes, autoawq) only partially supported on MPS.
- **CPU:** Fully supported via CPU-only PyTorch.
- **Multi-GPU:** `device_map="auto"` powered by `accelerate` distributes layers; `max_memory={0: "16GB", 1: "16GB"}` controls per-GPU allocation.
- **Memory offload:** `device_map="auto"` can offload layers to CPU RAM or disk for models larger than VRAM.

## 4. Model Formats

- **safetensors (preferred):** Faster and safer than `.bin`.
- **PyTorch `.bin` / `.pt`:** Legacy, fully supported.
- **GGUF:** Loadable via `gguf_file=` in `from_pretrained()`; weights are dequantized to fp32 (not native quantized inference). Useful to bring llama.cpp models into Transformers for fine-tuning. Requires `pip install gguf`. Supported families include Llama, Mistral, Qwen2, Phi3, Falcon, Bloom, GPT2, Starcoder2.

Quantization backends (via `quantization_config` in `from_pretrained()`):

| Method | Bits | Hardware | Notes |
|---|---|---|---|
| bitsandbytes | 4 / 8 | CUDA (CPU/MPS partial) | On-the-fly NF4 (`load_in_4bit`) or 8-bit (`load_in_8bit`); PEFT compatible. |
| GPTQ (GPTQModel) | 2 / 3 / 4 / 8 | CUDA, ROCm, CPU, Metal | Post-training; AutoGPTQ deprecated — use `gptq-model`. |
| AWQ | 4 | CUDA, ROCm, CPU | Via `autoawq` or `llm-awq`; PEFT compatible. |
| AQLM | 1 / 2 | CUDA, CPU | Extreme compression. |
| compressed-tensors | 1–8 | CUDA, ROCm, CPU | Neural Magic; flexible sparse/dense. |
| torchao | 4 / 8 | CUDA, CPU, MPS (partial) | PyTorch-native (`pytorch/ao`). |
| FBGEMM_FP8 / FineGrained FP8 | 8 (FP8) | CUDA | FP8 precision. |
| HQQ | 1–8 | CUDA, CPU | On-the-fly, no calibration. |
| optimum-quanto | 2 / 4 / 8 | CUDA, CPU, Metal | Via `optimum-quanto`. |
| EETQ | 8 | CUDA | On-the-fly, 8-bit. |

Install backends as needed: `pip install bitsandbytes accelerate`, `auto-gptq`, `autoawq`, `aqlm`, `compressed-tensors`, `torchao`, `gguf`.

## 5. API Surface

`transformers` is a **Python library**, not a server — no built-in HTTP API or OpenAI-compatible endpoint (serving is left to TGI, vLLM, etc.).

Primary APIs:

- `pipeline()` — high-level factory for text-generation, image-to-text, ASR, classification, and dozens of other tasks; handles model loading, tokenization, batching.
- `AutoModelForCausalLM.generate()` (via `GenerationMixin`) — lower-level entry for fine control (quantization, custom logits processors, streaming, scores).

- **Streaming:** `streamer=` argument on `generate()` accepts `TextStreamer` or `TextIteratorStreamer`.
- **Tool / function calling:** Not a built-in library feature; tool-use models handle it via chat templates and prompt formatting.
- **Vision / multimodal:** `pipeline()` supports `image-text-to-text`, `image-classification`, `object-detection`, `depth-estimation`, `video-classification`, etc.; multimodal models use a `processor`. `generate()` accepts `pixel_values`.
- **Structured outputs / constrained decoding:** Partial — `prefix_allowed_tokens_fn` and `logits_processor` (`LogitsProcessorList`) can implement grammar/schema constraints (e.g., integrating Outlines). No out-of-the-box JSON-schema mode.
- **Logprobs:** Pass `return_dict_in_generate=True, output_scores=True`; returned `scores` tuple holds per-token logits. `compute_transition_scores()` converts to per-token logprobs.

Docs: [pipelines](https://huggingface.co/docs/transformers/en/main_classes/pipelines), [text_generation](https://huggingface.co/docs/transformers/en/main_classes/text_generation).

## 6. Performance

Not benchmarked by maintainer (in quantitative terms). The [GPU inference guide](https://huggingface.co/docs/transformers/main/en/perf_infer_gpu_one) covers bitsandbytes 4/8-bit quantization, SDPA/FlashAttention-2, ONNX Runtime via Optimum, and continuous batching, but publishes no canonical tokens/sec or latency figures. The FlashAttention-2 section includes qualitative speedup graphs (Llama-7b, Falcon-7b at seq 4096 across batch sizes) as images with no numbers in text. No prefill-vs-decode breakdown.

## 7. Documented Strengths

- **Widest architecture coverage of any single library:** Supports thousands of model families (LLaMA, Mistral, Falcon, Gemma, Phi, Qwen, CLIP, Whisper, T5, …) with a unified `from_pretrained()` API. Source: [huggingface/transformers README](https://github.com/huggingface/transformers).
- **Broadest quantization backend selection:** bitsandbytes NF4/INT8, GPTQ, AWQ, AQLM, HQQ, compressed-tensors, torchao, FBGEMM FP8, EETQ — all via `quantization_config`; no other single library offers this range. Source: [quantization docs](https://huggingface.co/docs/transformers/quantization).
- **Full training-to-inference workflow:** The only runtime in this list that supports fine-tuning, gradient checkpointing, PEFT/LoRA adapter training, and dataset pipelines alongside inference — making it the standard research tool. Source: [huggingface/transformers README](https://github.com/huggingface/transformers).
- **Direct model internals access:** Logits, hidden states, attention weights, custom logits processors, and generation hooks are all first-class Python objects — essential for research, evaluation, and custom pipelines. Source: [text_generation docs](https://huggingface.co/docs/transformers/en/main_classes/text_generation).

## 8. Documented Weaknesses

- **Significantly lower serving throughput than dedicated engines:** Independent benchmark on Llama-3.2-3B-Instruct (NVIDIA L4): HF pipelines took 12.9 s at batch 32 vs. vLLM's 3.38 s — roughly 4× slower; gap widens at larger batches. Source: [vLLM vs HuggingFace benchmark, Medium 2024](https://medium.com/@alishafique3/vllm-vs-hugging-face-for-high-performance-offline-llm-inference-2d953b4fb3b4).
- **No built-in HTTP server or OpenAI-compatible API:** `transformers` is a library; serving requires wrapping with FastAPI, TGI, vLLM, or another layer. Source: [README](https://github.com/huggingface/transformers).
- **GGUF loads as dequantized FP32 (no native quantized inference):** When loaded via `gguf_file=`, weights are converted to FP32 at load time — the purpose is fine-tuning portability, not quantized inference speed. Source: [GGUF docs](https://huggingface.co/docs/transformers/gguf).
- **MPS (Apple Silicon) is partially supported for quantization backends:** bitsandbytes and autoawq have only partial MPS support; some quant configurations silently fall back to CPU. Source: [perf_infer_gpu docs](https://huggingface.co/docs/transformers/perf_infer_gpu_one).

## 9. Sources

- [huggingface/transformers](https://github.com/huggingface/transformers) — observed 2026-06-14
