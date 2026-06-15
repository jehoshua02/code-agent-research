---
name: "Nemotron"
maker: "NVIDIA"
license: "NVIDIA Open Model License"
license_category: "custom-permissive"
status: "active"
url: "https://huggingface.co/nvidia"
last_verified: "2026-06-14"
variants: ["Nemotron-Mini-4B-Instruct", "Nemotron-3-Nano-4B", "Llama-3.1-Nemotron-70B-Instruct", "Llama-3.1-Nemotron-70B-Reward", "Nemotron-4-340B-Base", "Nemotron-4-340B-Instruct", "Nemotron-4-340B-Reward"]
params_total: "340B"
has_moe: false
context_window: 131072
modalities: ["text"]
gated: false
released: "2024-10"
hardware_tiers: ["8gb", "12gb", "16gb", "24gb", "24gb+"]
best_for: ["research", "automation"]
notes: "Nemotron-4-340B has only 4K context; Llama-3.1-Nemotron-70B inherits 128K from Llama 3.1"
---

# Nemotron

_Last verified: 2026-06-14_

## 0. TL;DR

Nemotron is NVIDIA's open-weight model family, optimized specifically for NVIDIA hardware — models come with dedicated support in NVIDIA's own serving tools (TensorRT-LLM, NIM) and a wide array of pre-built [quantizations](../GLOSSARY.md#quantization). Pick Nemotron if you're already running on NVIDIA infrastructure and want a commercially-licensed model that's tuned for high-throughput serving with minimal setup friction, or if you need a reward model for building your own AI training pipeline. The main catch is that the 340B flagship needs an entire multi-GPU server to run, the license requires attribution, and the older Nemotron-4 models top out at a very short 4K context window.

## 1. What It Is

Nemotron is NVIDIA's open-weight family. Released under the NVIDIA Open Model License — permits commercial use with attribution requirements. Includes models derived from Llama and fully NVIDIA-trained variants, often co-developed for NVIDIA hardware.

## 2. Variants

**Nemotron-4 (NVIDIA-native, 2024):**

| Name | Params | Released | Intended Use |
|---|---|---|---|
| Nemotron-4-340B-Base | 340B | Jun 2024 | Pre-trained base; synthetic data |
| Nemotron-4-340B-Instruct | 340B | Jun 2024 | English chat; synthetic data pipeline |
| Nemotron-4-340B-Reward | 340B | Jun 2024 | Reward modeling for RLHF |

**Llama-Nemotron (Llama 3.1 fine-tunes, 2024):**

| Name | Params | Released | Intended Use |
|---|---|---|---|
| Llama-3.1-Nemotron-70B-Instruct-HF | 70B | Oct 2024 | General helpfulness, RLHF-tuned |
| Llama-3.1-Nemotron-70B-Reward | 70B | Oct 2024 | Reward model for alignment |

Note: Nemotron 3 (Nano / Super / Ultra hybrid-MoE) was announced late 2025/early 2026; not covered by the model cards above.

## 3. Context Window

- **Nemotron-4-340B:** **4,096** tokens — no extended-context variant.
- **Llama-3.1-Nemotron-70B:** **128K** input (inherits Llama 3.1); max output 4,096 per generation. Practical limit often 32K–64K due to KV cache size.

## 4. Hardware Requirements

**Nemotron-4-340B** (per model card): BF16 needs 8× H200 (1 node), 16× H100 80 GB (2 nodes), or 16× A100 80 GB (2 nodes). ~680 GB at BF16; Q4 ~170 GB.

**Llama-3.1-Nemotron-70B** (per model card): minimum 2× A100 80 GB; requires NVIDIA Ampere or newer.

| Variant | Q4 | Q8 | FP16 |
|---|---|---|---|
| Nemotron-70B | ~40 GB | ~75 GB | ~140 GB |
| Nemotron-4-340B | ~170 GB | ~340 GB | ~680 GB |

NVIDIA also provides 45+ quantized variants of the 70B (FP8, INT8, etc.) via NGC.

## 5. Where To Get Weights

- HuggingFace org: https://huggingface.co/nvidia
- **Gated:** no HF gating mentioned on the listed cards.
- License: **NVIDIA Open Model License** (commercial use permitted; derivatives allowed; generated outputs owned by the developer). Llama-3.1-Nemotron-70B additionally inherits the **Llama 3.1 Community License**.

## 6. Runtime Support

NVIDIA's preferred runtime is **TensorRT-LLM** (their optimized inference engine for NVIDIA GPUs) and **NVIDIA NIM** (containerized serving). Both Nemotron-4-340B and Llama-3.1-Nemotron-70B are also supported by **vLLM** (BF16, FP8, INT8 via NGC) and **Hugging Face Transformers**. The Nemotron-70B (Llama 3.1 base) loads on **llama.cpp** (GGUF) and **Ollama** like any Llama 3.1 model. NVIDIA ships 45+ quantized variants of the 70B via NGC including **FP8, INT8, and AWQ**. Nemotron-4-340B community GGUF quants exist but are not officially published.

## 7. Capabilities

Llama-3.1-Nemotron-70B-Instruct is RLHF-tuned for **general helpfulness** and ranked highly on Arena Hard and MT-Bench. It supports **tool/function calling** (inherited from Llama 3.1's format). Nemotron-4-340B is English-focused, trained for general chat and as a **synthetic data generator** for AI alignment pipelines. No vision in either family (Nemotron 3 Nano/Super/Ultra added vision, per late-2025 announcements). No multilingual design goal for Nemotron-4; Llama-3.1-Nemotron-70B inherits Llama's 8-language multilingual training. ([Llama-3.1-Nemotron-70B model card](https://huggingface.co/nvidia/Llama-3.1-Nemotron-70B-Instruct-HF))

## 8. Benchmarks

Sources: Nemotron-4-340B Technical Report ([arXiv 2406.11704](https://arxiv.org/abs/2406.11704)) and Llama-3.1-Nemotron-70B model card ([HuggingFace](https://huggingface.co/nvidia/Llama-3.1-Nemotron-70B-Instruct-HF)).

**Nemotron-4-340B-Base:**

| Benchmark | Score | vs. Llama-3-70B |
|---|---|---|
| MMLU (5-shot) | 81.1 | 79.5 |
| HumanEval (0-shot) | 57.3 | 48.2 |
| BBH (3-shot) | 85.4 | 81.3 |
| ARC-Challenge | 94.3 | 93.0 |

**Nemotron-4-340B-Instruct:**

| Benchmark | Score |
|---|---|
| MT-Bench | 8.22 |
| MMLU (0-shot) | 78.7 |
| GSM8K (0-shot) | 92.3 |
| IFEval (Prompt-Strict) | 79.9 |
| Arena Hard | 54.2 |

**Llama-3.1-Nemotron-70B-Instruct (RLHF fine-tune of Llama 3.1-70B):**

| Benchmark | Score |
|---|---|
| Arena Hard | 85.0 (#1 open-source at Oct 2024) |
| AlpacaEval 2 LC | 57.6 (tied GPT-4o) |
| MT-Bench | 8.98 |
| MMLU-Pro | 62.8 |

**Nemotron-4-340B-Reward:** RewardBench Overall 92.0 (ranked #1 at publication time). GPQA, MATH, and SWE-bench not reported.

## 9. Documented Strengths

- **Top-ranked open-source helpfulness (Nemotron-70B)**: Llama-3.1-Nemotron-70B-Instruct ranked #1 on Arena Hard (85.0) as of October 2024, outperforming GPT-4o (79.3) and Claude 3.5 Sonnet (79.2) on that benchmark at the time. ([HuggingFace model card](https://huggingface.co/nvidia/Llama-3.1-Nemotron-70B-Instruct-HF))
- **Leading reward model**: Nemotron-4-340B-Reward achieved RewardBench Overall 92.0, ranking #1 among reward models at publication, making it valuable as a quality signal in synthetic data pipelines and RLHF. ([Nemotron-4 tech report](https://arxiv.org/abs/2406.11704))
- **Optimized for NVIDIA hardware**: TensorRT-LLM and NVIDIA NIM support with 45+ pre-built quantized variants (FP8, INT8, AWQ) means near-zero deployment friction on NVIDIA infrastructure. ([NVIDIA NGC / model card](https://huggingface.co/nvidia/Llama-3.1-Nemotron-70B-Instruct-HF))
- **Synthetic data generation pipeline**: Nemotron-4-340B was used to generate the entire training dataset for its own Instruct variant via RLHF; the pipeline is documented and reproducible as a template for others. ([Nemotron-4 tech report](https://arxiv.org/abs/2406.11704))

## 10. Documented Weaknesses

- **Nemotron-4-340B requires massive hardware**: BF16 inference needs 8× H200 or 16× A100 80 GB GPUs; this puts the 340B out of reach for anyone without a full multi-node NVIDIA server cluster. ([Nemotron-4 tech report](https://arxiv.org/abs/2406.11704))
- **4K context window on Nemotron-4**: The 340B series has only a 4,096-token context — effectively unusable for long-document or multi-turn agentic tasks without chunking. ([Nemotron-4 tech report](https://arxiv.org/abs/2406.11704))
- **HumanEval regression in Nemotron-4 Instruct**: The Instruct 340B scores 73.2 on HumanEval versus 81.7 for Llama-3-70B-Instruct — instruction tuning degraded code performance relative to a much smaller model. ([Nemotron-4 tech report](https://arxiv.org/abs/2406.11704))
- **NVIDIA Open Model License, not Apache 2.0**: While permissive for commercial use, the NVIDIA license requires attribution and restricts uses that compete with NVIDIA products; it is not as unrestricted as Apache 2.0.

## 11. Sources

- [nvidia on HuggingFace](https://huggingface.co/nvidia) — observed 2026-06-14
