# transformers (HF baseline)

_Last verified: 2026-06-14_

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

OpenAI-compatible? Native API? Streaming? Tool calling? Embeddings?

## 6. Performance

Throughput (tok/s), latency, batch support. Cite source or note "not benchmarked".

## 7. Documented Strengths

Documented strengths from maintainer docs, benchmarks, or independent comparisons. Cite source.

## 8. Documented Weaknesses

Documented limitations from issue tracker, docs, or community reports. Cite source.

## 9. Sources

- [huggingface/transformers](https://github.com/huggingface/transformers) — observed 2026-06-14
