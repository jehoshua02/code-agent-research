---
name: "Command R"
maker: "Cohere"
license: "CC-BY-NC 4.0"
license_category: "source-available"
status: "active"
url: "https://huggingface.co/CohereForAI"
last_verified: "2026-06-14"
variants: ["Command-R-35B", "Command-R-32B", "Command-R+-104B", "Command-R7B-7B", "Command-A-111B"]
params_total: "111B"
has_moe: false
context_window: 262144
modalities: ["text"]
gated: false
released: "2025-03"
hardware_tiers: ["12gb", "16gb", "24gb", "24gb+"]
best_for: ["research", "automation", "data"]
notes: "CC-BY-NC license blocks production use without a separate Cohere commercial agreement"
---

# Command R

_Last verified: 2026-06-14_

## 0. TL;DR

Command R is Cohere's open-weight model family purpose-built for [retrieval-augmented generation](../GLOSSARY.md#rag-retrieval-augmented-generation) — tasks where the model needs to search through documents, cite its sources, and call tools reliably — rather than being a general-purpose chat model. Pick Command R if you're building a document Q&A or enterprise search application and want a model with first-class, structured tool-calling baked in and strong multilingual support across 23 languages. The main catch is the non-commercial CC-BY-NC license: you can experiment freely, but any production use requires a separate Cohere commercial agreement.

## 1. What It Is

Command R / Command R+ / Command A are Cohere's open-weight families. Released under CC-BY-NC 4.0 (non-commercial; commercial use requires a Cohere license). Optimized for retrieval-augmented generation and tool use; multilingual.

## 2. Variants

| Name | Params | Released | Intended Use |
|---|---|---|---|
| Command R v0.1 (`c4ai-command-r-v01`) | 35B | Mar 2024 | RAG, tool use, long-context |
| Command R 08-2024 | 32B | Aug 2024 | Updated RAG, multilingual (23 languages) |
| Command R+ v0.1 | 104B | Mar 2024 | Advanced reasoning, RAG, multi-step tools |
| Command R+ 08-2024 | 104B | Aug 2024 | Updated; grounded generation, citations |
| Command R7B (`c4ai-command-r7b-12-2024`) | 7B | Dec 2024 | Lightweight enterprise; reasoning, RAG, code |
| Command A (`c4ai-command-a-03-2025`) | 111B | Mar 2025 | Agentic tasks; deployable on 2 GPUs |

Note: Command R was 35B in v0.1 but 32B in 08-2024 (Cohere reduced size between releases).

## 3. Context Window

- Command R v0.1 / 08-2024 / R+ / R7B: **128K** tokens.
- Command A: **256K** native; HF default config caps at 128K — manual change required for full 256K.
- Practical caveat: grounded-generation prompts add overhead; effective RAG context often ≤100K in practice.

## 4. Hardware Requirements

| Model | FP16 | Q8 | Q4 | Min viable GPU |
|---|---|---|---|---|
| Command R7B (7B) | ~14 GB | ~7 GB | ~4 GB | RTX 3060 12 GB |
| Command R 08-2024 (32B) | ~64 GB | ~32 GB | ~16 GB | RTX 4090 24 GB (Q4); A100 80 GB (FP16) |
| Command R+ (104B) | ~208 GB | ~104 GB | ~52 GB | 2× RTX 4090 or A100 80 GB (Q4); 3× A100 80 GB (FP16) |
| Command A (111B) | ~222 GB | ~111 GB | ~56 GB | 2× A100 80 GB (per model card); FP16 needs 3+ A100 80 GB |

CPU offload viable via llama.cpp; 64 GB RAM recommended for R+ partial offload.

## 5. Where To Get Weights

- HuggingFace org: https://huggingface.co/CohereForAI
- **Gated:** no HF access gates; publicly downloadable. Use is subject to Cohere Labs' Acceptable Use Policy.
- License: **CC-BY-NC** (Creative Commons Attribution-NonCommercial). Commercial use requires a separate Cohere license agreement.

## 6. Runtime Support

Supported by **Hugging Face Transformers** (primary; Cohere provides model cards with Transformers-first examples), **vLLM** (BF16, AWQ, GPTQ), **llama.cpp** (GGUF for all sizes), and **Ollama** (GGUF). Command A's 256K context at full length requires vLLM or SGLang with chunked prefill. **MLX** supports R7B and Command R (32B) on Apple Silicon. Community GGUF quants (Q2–Q8) available for all sizes; AWQ and GPTQ available from community sources. No FP8 official release.

## 7. Capabilities

Command R / R+ / A are explicitly designed for **retrieval-augmented generation (RAG)** with grounded generation and citation output, **multi-step tool use** (structured tool-call format with parallel and sequential calling), and multilingual tasks (23 languages including EN, FR, DE, ES, IT, PT, JA, KO, ZH, AR). Command A adds **agentic** workflows with stronger multi-hop reasoning. No vision capability. Code generation is supported but not the primary focus. ([Command R model card](https://huggingface.co/CohereForAI/c4ai-command-r-plus-08-2024))

## 8. Benchmarks

Results below are for Command R+ v0.1 (104B) unless noted. Cohere's model card explicitly notes these scores "do not capture RAG, multilingual, or tooling performance." ([HuggingFace model card](https://huggingface.co/CohereLabs/c4ai-command-r-plus))

| Benchmark | Score | Notes |
|---|---|---|
| MMLU | 75.7 | Command R+ v0.1; 5-shot |
| HellaSwag | 88.6 | Command R+ v0.1 |
| ARC-Challenge | 71.0 | Command R+ v0.1 |
| WinoGrande | 85.4 | Command R+ v0.1 |
| GSM8K | 70.7 | Command R+ v0.1 |
| RAG human-preference win rate | 71.8–81.6% vs. GPT-4 Turbo | Command R (35B); internal eval ([Cohere blog](https://langbase.com/models/cohere/command-r/benchmarks)) |
| BFCL / ToolTalk tool-use | Outperforms GPT-4 Turbo (no exact figure published) | Command R+; ([Sebastian Ruder's write-up](https://www.ruder.io/command-r/)) |

HumanEval, MATH, GPQA, IFEval, and SWE-bench scores were not officially published.

## 9. Documented Strengths

- **RAG and grounded generation**: Command R's primary design target; achieves 71.8–81.6% human-preference win rate over GPT-4 Turbo on enterprise RAG tasks, with structured citation output built into the model's prompt format. ([Cohere blog / langbase summary](https://langbase.com/models/cohere/command-r/benchmarks))
- **Multi-step tool use**: Command R+ outperforms GPT-4 Turbo on the Berkeley Function Calling Leaderboard (BFCL) and Microsoft ToolTalk (Hard) benchmarks for zero-shot, parallel, and sequential tool calling. ([Sebastian Ruder](https://www.ruder.io/command-r/))
- **Multilingual coverage**: Natively trained in 23 languages; leads peer models on Japanese, Korean, and Chinese translation tasks (FLORES BLEU L2→EN 35.7%). ([Cohere / langbase](https://langbase.com/models/cohere/command-r/benchmarks))
- **128K–256K context**: Command A extends to 256K tokens with near-perfect Needle-in-a-Haystack recall at all depths, enabling very long document RAG without chunking loss.

## 10. Documented Weaknesses

- **General reasoning trails larger models**: MMLU 75.7 for the 104B R+ is below comparably sized open models like Llama 3 70B (79.5) or Mixtral 8×22B; GSM8K 70.7 lags significantly behind frontier models. ([HuggingFace model card](https://huggingface.co/CohereLabs/c4ai-command-r-plus))
- **Non-commercial license**: CC-BY-NC 4.0 blocks production deployment without a separate Cohere commercial agreement, limiting self-hosted enterprise use. ([Cohere model card / license](https://huggingface.co/CohereLabs/c4ai-command-r-plus))
- **Code generation not a focus**: No HumanEval scores published; model card and documentation consistently de-prioritize coding tasks in favor of RAG and tool use.
- **TruthfulQA only 56.3**: Relatively low factual accuracy on TruthfulQA, suggesting potential for hallucination outside of grounded (cited-source) generation workflows. ([HuggingFace model card](https://huggingface.co/CohereLabs/c4ai-command-r-plus))

## 11. Sources

- [CohereForAI on HuggingFace](https://huggingface.co/CohereForAI) — observed 2026-06-14
