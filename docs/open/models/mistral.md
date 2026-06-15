---
name: "Mistral"
maker: "Mistral AI"
license: "Apache-2.0"
license_category: "apache-2.0"
status: "active"
url: "https://huggingface.co/mistralai"
last_verified: "2026-06-14"
variants: ["7B", "Mixtral-8x7B", "Mixtral-8x22B", "NeMo-12B", "Large-2407", "Codestral-22B", "Small-3.1-24B", "Large-3-675B"]
params_total: "675B"
has_moe: true
params_active: "41B"
context_window: 262144
modalities: ["text", "vision"]
gated: false
released: "2025-03"
hardware_tiers: ["8gb", "12gb", "16gb", "24gb", "24gb+"]
best_for: ["coding", "research", "writing", "automation"]
notes: "Codestral v0.1 and Large-2407 are non-commercial; check license per variant"
---

# Mistral

_Last verified: 2026-06-14_

## 0. TL;DR

Mistral is a French AI startup's open-weight model family covering everything from a fast 7B general-purpose model to a 675B frontier reasoning giant, with most models under the permissive Apache 2.0 license. Pick Mistral if you want strong European-language support, reliable function/tool calling, or a capable code-generation model (Codestral); the smaller models are among the best in their size class for efficiency. The catch: the older Mistral Large and Codestral v0.1 carry non-commercial licenses, and the flagship Large 3 [mixture-of-experts](../GLOSSARY.md#moe-mixture-of-experts) model demands a multi-H100 setup.

## 1. What It Is

Mistral is Mistral AI's open-weight family. Smaller models (Mistral 7B, Mixtral 8x7B/8x22B, Mistral Small, Codestral Mamba) under Apache 2.0; flagship Mistral Large under Mistral Research License (non-commercial unless licensed). Dense and MoE architectures.

## 2. Variants

| Name | Total / Active Params | Released | Architecture | License | Intended Use |
|---|---|---|---|---|---|
| Mistral-7B-Instruct v0.3 | 7B | May 2024 | Dense | Apache 2.0 | General chat, function calling |
| Mixtral-8x7B-Instruct | 47B / ~13B | Dec 2023 | MoE | Apache 2.0 | General chat |
| Mixtral-8x22B-Instruct | 141B / 39B | Apr 2024 | MoE | Apache 2.0 | Reasoning, coding, multilingual |
| Mistral-NeMo-Instruct-2407 | 12B | Jul 2024 | Dense (w/ NVIDIA) | Apache 2.0 | Drop-in mid-size, multilingual |
| Mistral-Large-Instruct-2407 | 123B | Jul 2024 | Dense | Mistral Research License (NC) | Complex reasoning |
| Codestral-22B v0.1 | 22B | May 2024 | Dense | MNLP-0.1 (non-prod) | Code, 80+ languages, FIM |
| Mistral-Small-3.1 | 24B | Mar 2025 | Dense multimodal | Apache 2.0 | Multimodal, agentic |
| Mistral-Large-3 | 675B / 41B | Dec 2025 | MoE | Apache 2.0 | Frontier reasoning, agentic, multimodal |

## 3. Context Window

- Mistral-7B v0.3: 32,768.
- Mixtral-8x7B: 32,768.
- Mixtral-8x22B: ~65,536 (64K).
- Mistral NeMo 12B: 128K (trained with FP8 quant awareness).
- Mistral Large 2 (2407): 128K.
- Codestral-22B v0.1: 32K.
- Mistral Small 3.1: 128K.
- Mistral Large 3: 256K.
- Practical caveat: KV-cache VRAM grows fast above 32K; vLLM / `mistral-inference` with paged attention recommended.

## 4. Hardware Requirements

| Model | FP16 | Q8 | Q4 | Min viable GPU |
|---|---|---|---|---|
| Mistral-7B | ~14 GB | ~7.5 GB | ~4 GB | RTX 3060 12 GB (Q4); 3090 (FP16) |
| Mixtral-8x7B | ~94 GB | ~47 GB | ~27 GB | 2× RTX 3090/4090 (Q4); 4× A100 (FP16) |
| Mixtral-8x22B | ~282 GB | ~141 GB | ~70 GB | 3–4× 24 GB (Q4); 8× A100 80 GB (FP16) |
| Mistral NeMo 12B | ~24 GB | ~12 GB | ~6.5 GB | RTX 3060 12 GB (Q4); 3090 (Q8) |
| Mistral Large 2 (123B) | ~246 GB | ~123 GB | ~62 GB | Multi-GPU cluster |
| Codestral-22B | ~44 GB | ~22 GB | ~12 GB | RTX 3090/4090 (Q4/Q8) |
| Mistral Small 3.1 (24B) | ~48 GB | ~24 GB | ~13 GB | RTX 3090/4090 (Q4/Q8) |
| Mistral Large 3 (675B MoE) | ~1350 GB | ~675 GB | ~338 GB | 8–16× H100 80 GB at Q4 |

System RAM for CPU offload: roughly 2× model size at chosen precision.

## 5. Where To Get Weights

- HuggingFace org: https://huggingface.co/mistralai
- **Gated:** no for Apache 2.0 models (Mistral 7B, Mixtral, NeMo, Small 3.1, Large 3). Yes for Codestral-22B v0.1 (MNLP-0.1, non-commercial) and Mistral-Large-Instruct-2407 (Mistral Research License, non-commercial) — must accept on HF.
- Codestral 2 (Apr 2026) was relicensed to Apache 2.0.
- Also on Mistral's La Plateforme, AWS, Azure, GCP.

## 6. Runtime Support

Supported by **vLLM** (BF16, FP8, AWQ, GPTQ), **SGLang**, **Hugging Face Transformers**, **llama.cpp** (GGUF), and **Ollama** (GGUF). Mistral also ships `mistral-inference`, their own lightweight reference server. MoE models (Mixtral, Mistral Large 3) need vLLM ≥0.5 or SGLang for expert routing. **MLX** supports smaller sizes (7B, 12B, 24B) on Apple Silicon. Common quant formats: GGUF (Q2–Q8), AWQ (INT4), GPTQ (INT4/INT8), FP8 (NeMo 12B and Large 3).

## 7. Capabilities

Mistral Instruct models are trained for general instruction following and **function/tool calling** via a structured `[TOOL_CALLS]` format (introduced in Mistral-7B v0.3 and Mixtral). Codestral specializes in code generation with fill-in-the-middle (FIM) across 80+ programming languages. Mistral Small 3.1 and Large 3 add **vision** (image understanding) and stronger agentic behavior. Strong multilingual support across European languages (EN, FR, DE, ES, IT, PT, RU); Mixtral-8x22B and NeMo 12B especially strong on multilingual tasks. ([Mistral function calling docs](https://docs.mistral.ai/capabilities/function_calling/))

## 8. Benchmarks

Numbers from official Mistral announcements. Mixtral 8x22B numbers from the [Mistral announcement (Apr 2024)](https://mistral.ai/news/mixtral-8x22b/); Mistral Small 3/3.1 numbers from the [Mistral Small 3 announcement (Jan 2025)](https://mistral.ai/news/mistral-small-3/) and llm-stats.com aggregating official card data.

| Benchmark | Mixtral 8x22B Instruct | Mistral Small 3.1 24B Instruct |
|---|---|---|
| MMLU | ~80% (visual chart) | 80.6 |
| MMLU-Pro | — | 56.0 |
| HumanEval | — | 88.4 |
| MATH | — | 69.3 |
| GSM8K (maj@8) | 90.8 | — |
| GPQA | — | 37.5 |

Mistral Small 3 (predecessor) scored IFEval 82.9. ([Mistral Small 3 announcement, Jan 2025](https://mistral.ai/news/mistral-small-3/))

## 9. Documented Strengths

- **Efficiency at size**: Mistral Small 3.1 (24B) is claimed to run >3× faster than Llama 3.3 70B on identical hardware at 150 tokens/s, while scoring comparably on MMLU (80.6 vs ~86). ([Mistral Small 3 announcement, Jan 2025](https://mistral.ai/news/mistral-small-3/))
- **Multilingual European coverage**: Mixtral 8x22B is natively fluent in English, French, German, Italian, and Spanish — broader European-language quality than most open models. ([Mixtral 8x22B announcement, Apr 2024](https://mistral.ai/news/mixtral-8x22b/))
- **Mature function-calling format**: Mistral introduced a structured `[TOOL_CALLS]` format across its family early; the format is well-supported in tooling ecosystems. ([Mistral function calling docs](https://docs.mistral.ai/capabilities/function_calling/))
- **Apache 2.0 for most models**: 7B, Mixtral 8x7B/8x22B, NeMo, Small 3.1, and Large 3 all under Apache 2.0 — commercially deployable without restriction.

## 10. Documented Weaknesses

- **No RL/reasoning optimization in Small line**: Mistral Small 3 is "neither trained with RL nor synthetic data," explicitly lacking the reasoning-chain capabilities of models like DeepSeek-R1 or QwQ. ([Mistral Small 3 announcement, Jan 2025](https://mistral.ai/news/mistral-small-3/))
- **GPQA score is modest**: Mistral Small 3.1 scores 37.5 on GPQA, well below DeepSeek-R1 (71.5) and even mid-range reasoning models. ([llm-stats.com, citing official card](https://llm-stats.com/models/compare/mistral-small-3.1-24b-base-2503-vs-mistral-small-3.1-24b-instruct-2503))
- **Codestral and Large 2 licensing**: Codestral-22B v0.1 (MNLP-0.1) and Mistral-Large-2407 (Mistral Research License) are non-commercial — a footgun for teams who pick those variants without checking licenses.
- **Mistral Large 3 hardware demands**: 675B MoE requires 8–16× H100 80 GB at Q4 precision; not accessible for self-hosted deployments outside hyperscalers.

## 11. Sources

- [mistralai on HuggingFace](https://huggingface.co/mistralai) — observed 2026-06-14
