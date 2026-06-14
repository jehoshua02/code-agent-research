# Qwen

_Last verified: 2026-06-14_

## 1. What It Is

Qwen is Alibaba's open-weight model family. Qwen2.5 and Qwen3 lines released under Apache 2.0 (most checkpoints). General-purpose models with strong multilingual support, math/coding-specific variants (Qwen-Coder, Qwen-Math), and dense + MoE architectures.

## 2. Variants

**Qwen3 family** (April 2025):

| Name | Total / Active Params | Architecture | Native Context | Intended Use |
|---|---|---|---|---|
| Qwen3-0.6B / 1.7B / 4B | 0.6B / 1.7B / 4B | Dense | 32K | Edge / on-device |
| Qwen3-8B / 14B / 32B | 8B / 14B / 32B | Dense | 128K | General chat, coding, reasoning |
| Qwen3-30B-A3B | 30B / 3B | MoE (128 experts, 8 active) | 32K (128K w/ YaRN) | Efficient reasoning, agentic |
| Qwen3-235B-A22B | 235B / 22B | MoE | 32K (128K w/ YaRN) | Frontier-scale reasoning |

All Qwen3 models support a hybrid thinking mode (toggle between extended CoT and direct response) and 100+ languages.

**Earlier families:** Qwen2.5 (0.5B–72B dense, 128K context, Sep 2024); Qwen2.5-Coder / Qwen2.5-Math (specialist variants); QwQ-32B (reasoning, ~Mar 2025); Qwen-VL / Qwen2-VL (multimodal).

## 3. Context Window

- Qwen3 0.6B–4B: 32K native.
- Qwen3 8B–32B dense: **128K** native.
- Qwen3 MoE (30B-A3B, 235B-A22B): 32K native, extendable to 131,072 (128K) via YaRN — quality at the far end of YaRN-extended contexts is not fully validated.
- Qwen2.5-72B: 131,072 native.
- Recommended runtimes for long context: SGLang and vLLM.

## 4. Hardware Requirements

No official VRAM table; estimates derived from parameter count × bytes-per-param. MoE models require **total** params in VRAM, not just active.

| Variant | FP16 | Q8 | Q4 | Min viable GPU |
|---|---|---|---|---|
| Qwen3-0.6B | ~1.2 GB | ~0.6 GB | ~0.4 GB | Any modern GPU/CPU |
| Qwen3-4B | ~8 GB | ~4 GB | ~2.5 GB | RTX 3050 (Q4); RTX 3060 12 GB (FP16) |
| Qwen3-8B | ~16 GB | ~8 GB | ~5 GB | RTX 3080 (Q4); RTX 3090/4090 (FP16) |
| Qwen3-32B | ~64 GB | ~32 GB | ~18 GB | 2× RTX 4090 (Q4/Q8); A100 80 GB (FP16) |
| Qwen2.5-72B | ~144 GB | ~72 GB | ~40 GB | 1× A100 80 GB (Q4); 2× A100 80 GB (FP16) |
| Qwen3-30B-A3B | ~60 GB | ~30 GB | ~17 GB | 2× RTX 4090 (Q4); A100 80 GB (Q8) |
| Qwen3-235B-A22B | ~470 GB | ~235 GB | ~120 GB | 4–8× A100 80 GB |

CPU offload viable for ≤32B with ≥64 GB system RAM (reduced throughput).

## 5. Where To Get Weights

- HuggingFace org: https://huggingface.co/Qwen
- **Gated:** no for Qwen3 (download directly, no form). Qwen2.5 uses Alibaba's proprietary Qwen license (commercial OK, more restrictive than Apache).
- License: **Apache 2.0** for all Qwen3 sizes — unusually permissive for a frontier family.
- Also distributed via ModelScope (Alibaba) and Kaggle.

## 6. Runtime Support

Supported by **vLLM** (BF16, FP8, AWQ, GPTQ), **SGLang** (BF16/FP8), **Hugging Face Transformers**, **llama.cpp** (GGUF), **Ollama** (GGUF), and **MLX** (MLX-LM for Apple Silicon). Qwen3 MoE models require vLLM ≥0.8 or SGLang for efficient expert routing. Common quant formats: GGUF (Q2–Q8), AWQ (INT4), GPTQ (INT4/INT8), FP8 (for server-grade GPUs). Qwen2.5-VL requires runtime image-preprocessing support (transformers or vLLM with vision extras).

## 7. Capabilities

Qwen3 models are trained for multilingual chat (100+ languages), **tool/function calling** (built-in tool-call format), coding (Qwen2.5-Coder / Qwen3 competitive on HumanEval/LiveCodeBench), and math reasoning. All Qwen3 models support a hybrid "thinking" mode — toggling between extended chain-of-thought and direct response at inference time. Qwen2-VL and Qwen2.5-VL variants add **vision** (image + video understanding). ([Qwen3 blog](https://qwenlm.github.io/blog/qwen3/))

## 8. Benchmarks

Public benchmark numbers (MMLU, HumanEval, SWE-bench, GAIA, ...). Cite source.

## 9. Documented Strengths

Documented strengths from benchmarks, model card, or independent testing. Cite source.

## 10. Documented Weaknesses

Documented limitations and failure modes from benchmarks, model card, or community reports. Cite source.

## 11. Sources

- [Qwen on HuggingFace](https://huggingface.co/Qwen) — observed 2026-06-14
