# Nemotron

_Last verified: 2026-06-14_

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

Which runtimes load it (ollama, vllm, llama.cpp, transformers, ...). Quantization formats available (GGUF, AWQ, GPTQ, FP8, ...).

## 7. Capabilities

Tool use, function calling, vision, code, languages, etc. What it's trained for.

## 8. Benchmarks

Public benchmark numbers (MMLU, HumanEval, SWE-bench, GAIA, ...). Cite source.

## 9. Documented Strengths

Documented strengths from benchmarks, model card, or independent testing. Cite source.

## 10. Documented Weaknesses

Documented limitations and failure modes from benchmarks, model card, or community reports. Cite source.

## 11. Sources

- [nvidia on HuggingFace](https://huggingface.co/nvidia) — observed 2026-06-14
