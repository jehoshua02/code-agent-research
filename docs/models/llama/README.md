# Llama (Meta)

## What It Is

The Llama model family is Meta's open-weight large language model series. Released under Meta's custom Llama Community License Agreement (not OSI-approved open source), the weights are freely downloadable for most commercial use up to 700 million monthly active users. Above that threshold, a separate Meta license is required.

Key generations relevant to coding:

- **Llama 3** — released April 2024. Dense transformer, 8B and 70B sizes.
- **Llama 3.1** — released July 23, 2024. Adds 405B, extends context to 128K, improves tool use.
- **Llama 3.2** — released September 2024. Adds multimodal vision (11B, 90B) and edge models (1B, 3B).
- **Llama 3.3** — released December 2024. 70B only; matches 3.1 405B performance at lower cost.
- **Llama 4** — released April 5, 2025. First MoE architecture in the Llama family. Natively multimodal. Scout and Maverick are open-weight; Behemoth (teacher model) weights are not yet public as of May 2026.

Architecture: all Llama 3.x models use grouped-query attention (GQA) and standard dense transformer design. Llama 4 uses sparse mixture-of-experts (MoE) with early-fusion native multimodality.

License note: Llama 4 multimodal models cannot be deployed by entities domiciled in the EU. Text-only use is not blocked.

## Variants

### Llama 3 (April 2024)

| Model | Params | Context | Notes |
|---|---|---|---|
| Llama 3 8B | 8B | 8K | Edge/local use |
| Llama 3 70B | 70B | 8K | Best open model at launch |

### Llama 3.1 (July 2024)

| Model | Params | Context | Notes |
|---|---|---|---|
| Llama 3.1 8B | 8B | 128K | Multilingual, tool use |
| Llama 3.1 70B | 70B | 128K | Strong coding, tool use |
| Llama 3.1 405B | 405B | 128K | First open model rivaling GPT-4 class |

### Llama 3.2 (September 2024)

| Model | Params | Context | Notes |
|---|---|---|---|
| Llama 3.2 1B | 1B | 128K | Text only, edge/mobile |
| Llama 3.2 3B | 3B | 128K | Text only, edge/mobile |
| Llama 3.2 11B Vision | 11B | 128K | Multimodal (image+text) |
| Llama 3.2 90B Vision | 90B | 128K | Multimodal (image+text) |

### Llama 3.3 (December 2024)

| Model | Params | Context | Notes |
|---|---|---|---|
| Llama 3.3 70B | 70B | 128K | Matches 3.1 405B quality at 70B cost |

### Llama 4 (April 2025) — MoE

| Model | Active Params | Total Params | Experts | Context | Notes |
|---|---|---|---|---|---|
| Llama 4 Scout | 17B | 109B | 16 | 10M tokens | Single H100 deployable |
| Llama 4 Maverick | 17B | 400B | 128 | 1M tokens | Requires multi-GPU |
| Llama 4 Behemoth | 288B active | ~2T total | 16 | 10M tokens | Weights not yet public; teacher model |

Note: Llama 4 context windows were pretrained at 256K; the 1M and 10M figures are from instruct tuning extensions.

## Pricing

Meta does not sell API access directly. Pricing is set by third-party hosting providers.

### Llama 3.1 (representative provider rates)

| Model | Provider | Input ($/1M) | Output ($/1M) |
|---|---|---|---|
| Llama 3.1 8B | Groq | $0.05 | $0.08 |
| Llama 3.1 8B | DeepInfra (FP8) | $0.02 | $0.02 |
| Llama 3.1 70B | Groq | $0.59 | $0.79 |
| Llama 3.1 70B | DeepInfra | $0.23 | $0.40 |
| Llama 3.1 405B | Groq | $3.00 | $3.00 |

### Llama 3.3 70B

| Provider | Input ($/1M) | Output ($/1M) |
|---|---|---|
| DeepInfra | $0.23 | $0.40 |
| Together AI | $0.88 | $0.88 |

### Llama 4

| Model | Blended ($/1M) | Notes |
|---|---|---|
| Llama 4 Scout | ~$0.08 input / $0.30 output | Via providers |
| Llama 4 Maverick | ~$0.17 input / $0.60 output | Distributed inference reference: $0.19 blended (3:1 ratio) |

Self-hosting eliminates per-token fees; cost is compute (see Hardware Requirements).

## Context Window

| Generation | Context |
|---|---|
| Llama 3 | 8K |
| Llama 3.1, 3.2, 3.3 | 128K |
| Llama 4 Scout | 10M (instruct); pretrained at 256K |
| Llama 4 Maverick | 1M (instruct); pretrained at 256K |

Practical limit for Llama 3.x at 128K: KV cache memory grows significantly. A 70B model's KV cache goes from ~1.6 GB at 2K context to ~42 GB at 128K. Self-hosters must budget VRAM for both weights and KV cache.

## Benchmarks

### Coding — HumanEval (pass@1, 0-shot)

| Model | HumanEval |
|---|---|
| Llama 3.1 8B | 72.6 |
| Llama 3.1 70B | 80.5 |
| Llama 3.1 405B | 89.0 |
| Llama 3.3 70B | 88.4 |
| Llama 4 Scout | ~86.0 (estimated from search results) |
| Llama 4 Maverick | Not separately reported on HumanEval |

### Coding — MBPP EvalPlus (pass@1, 0-shot)

| Model | MBPP EvalPlus |
|---|---|
| Llama 3.1 8B | 72.8 |
| Llama 3.1 70B | 86.0 |
| Llama 3.3 70B | 87.6 |

### Coding — LiveCodeBench (official Llama 4 data)

| Model | LiveCodeBench |
|---|---|
| Llama 4 Scout | 32.8 |
| Llama 4 Maverick | 43.4 |
| Llama 4 Behemoth | 49.4 (preview, still in training at April 2025) |

### General reasoning

| Model | MMLU Pro |
|---|---|
| Llama 4 Scout | 74.3 |
| Llama 4 Maverick | 80.5 |

### Competitive context

- Llama 3.1 405B at HumanEval 89.0 was competitive with GPT-4o at launch (July 2024). Claude 3.5 Sonnet scored higher.
- Llama 3.3 70B at HumanEval 88.4 effectively matches Llama 3.1 405B quality, with far lower hardware cost.
- Llama 4 Maverick's LiveCodeBench score of 43.4 is competitive with DeepSeek V3 at roughly half the active parameters.
- Llama 4 Scout's 10M context window is the largest of any open-weight model as of May 2026.

## Hardware Requirements

### Llama 3.1 / 3.3

| Model | Quantization | VRAM | Notes |
|---|---|---|---|
| 8B | Q4_K_M | ~5 GB | Runs on RTX 3060 |
| 8B | FP16 | ~16 GB | RTX 4080 or better |
| 70B | Q4_K_M | ~43 GB | Dual RTX 3090 or single A100 80GB |
| 70B | Q8_0 | ~70 GB | Dual A100 40GB |
| 70B | FP16 | ~148 GB | Minimum; ~178 GB with overhead |
| 405B | Q4_K_M | ~230 GB | Multi-GPU required |
| 405B | Q8_0 | ~405 GB | 8× A100 80GB minimum |
| 405B | FP16 | ~810 GB | Multi-node; near 1 TB with KV overhead |

Recommended practical setup for 70B: dual A100 80GB with AWQ 4-bit delivers enterprise-grade throughput at ~35 GB per GPU. For 405B, FP8 quantization on 8× H100 is the practical minimum for single-node deployment.

KV cache at 128K context adds up to ~42 GB for 70B — budget this on top of weight VRAM.

### Llama 4 Scout (109B total, 17B active)

| Quantization | VRAM | Notes |
|---|---|---|
| Q4_K_M | ~10–12 GB | RTX 4060 Ti 16GB |
| Q5_K_M | ~14–16 GB | RTX 5060 Ti 16GB |
| Q8_0 | ~20–24 GB | RTX 3090 / RTX 4090 |
| FP16 | ~55 GB | Mac Studio M4 Max 128GB |

Scout is the first Llama 4 model deployable on a single H100. Memory stores all 109B parameters despite only 17B activating per token.

### Llama 4 Maverick (400B total, 17B active)

| Quantization | VRAM | Notes |
|---|---|---|
| Q4_K_M | ~22–28 GB | RTX 4090 (tight) |
| Q5_K_M | ~30–36 GB | RTX 5090 (32GB) |
| Q8_0 | ~55–65 GB | A100 80GB |
| FP16 | ~110–130 GB | Mac Studio M4 Max 128GB (only consumer option) |

Full-quality multi-GPU Maverick: 4× H100 recommended. Consumer Q4 on RTX 4090 is feasible but tight.

Inference runtimes: Ollama, vLLM, and llama.cpp all support Llama 3.x and Llama 4. Ollama is simplest for local use. vLLM is preferred for production multi-GPU high-throughput serving.

## Supported Tools

### Platforms using Llama directly

- **Cursor** — fine-tuned Llama 3 70B for "fast apply" (full-file code edits). Using speculative decoding adapted for code editing ("speculative edits"), Cursor reported achieving >1000 tokens/second on their fine-tuned 70B model in May 2024, surpassing GPT-4o on their task. Note: Cursor's Tab completion (Fusion model) is a separate proprietary model; base model not publicly confirmed.
- **Meta AI** — Llama 4 powers meta.ai assistant.
- **GitHub Copilot** — has offered Llama 3.1 405B as a selectable model.
- **Amazon Bedrock** — hosts Llama 3.1, 3.2, 3.3.
- **Google Vertex AI** — hosts Llama 3.x variants.
- **Groq** — fast inference for Llama 3.1 and 3.3 (LPU hardware).

### Self-hosting / local tools

- **Ollama** — native support for all Llama 3.x and Llama 4 variants. Simplest local setup.
- **vLLM** — full tool calling support for Llama 3.1, 3.2, 3.4; parallel tool calls supported in Llama 4 (not in 3.x).
- **llama.cpp** — GGUF format, runs all sizes with quantization.
- **Continue.dev** — open-source VS Code/JetBrains coding assistant; supports Ollama and vLLM backends with Llama models.
- **Tabby** — self-hosted code completion server with Llama 3 support.
- **LM Studio** — GUI for local Llama inference.

### Fine-tuning ecosystem

- **Unsloth** — efficient LoRA/QLoRA fine-tuning for all Llama generations, including Llama 4.
- **LlamaFactory** — unified fine-tuning for 100+ LLMs including full Llama family.
- **Amazon SageMaker JumpStart** — managed fine-tuning for Llama 3.1 8B and 70B.

## Strengths

- **Open weights** — full model weights available for download, self-hosting, and fine-tuning. No API dependency.
- **Best-in-class open-weight coding (Llama 3.x)** — Llama 3.1 405B and Llama 3.3 70B are among the strongest open models for code generation.
- **Proven as fine-tuning base** — Cursor's >1000 tok/s code-edit model shows Llama 3 70B can be specialized aggressively. Wide ecosystem of fine-tuned variants.
- **Llama 4 Scout: extreme context** — 10M token context window, deployable on a single H100 at full precision or on consumer GPU at Q4. No open-weight competitor matches this context length.
- **Llama 4 efficiency** — MoE design activates only 17B parameters per token despite 109B–400B total params, enabling high throughput per compute unit.
- **Tool use** — Llama 3.1+ has native function calling. Llama 4 adds parallel tool calls. Supported natively in vLLM and Ollama.
- **Cost** — third-party API providers offer Llama 3.1 8B from $0.02/1M tokens. Self-hosting reduces cost to near zero at scale.
- **Broad inference stack support** — Ollama, vLLM, llama.cpp, TGI, SGLang all support the full family.

## Weaknesses

- **Not OSI open source** — the Llama Community License imposes the 700M MAU commercial cap, "Built with Llama" attribution requirements, and EU restrictions on Llama 4 multimodal models.
- **Llama 4 coding benchmarks are modest** — LiveCodeBench 32.8 (Scout) and 43.4 (Maverick) trail frontier closed models. Llama 4 is strongest on vision and long-context tasks, not coding specifically.
- **Llama 4 Behemoth not yet public** — the 2T-parameter teacher model that trained Scout and Maverick has no public weights as of May 2026.
- **405B is expensive to self-host** — requires 8× H100 or equivalent for production use. Not practical for small teams without cloud budget.
- **Llama 4 context window caveat** — Scout's 10M and Maverick's 1M context were achieved via instruct-tuning; base pretraining was at 256K. Real-world quality at extreme lengths may degrade.
- **Parallel tool calls missing in Llama 3.x** — vLLM explicitly does not support parallel tool calls for Llama 3 models; this is fixed in Llama 4.
- **No code-specific variant** — unlike DeepSeek (Coder), Qwen (Coder), or StarCoder, Meta has not released a dedicated code model. General-purpose Llama is competitive but not purpose-built for code.
- **Context window vs. VRAM tradeoff** — 128K context on 70B requires ~42 GB KV cache on top of ~43 GB model weights at Q4. Full context at full quality on a single consumer GPU is not feasible.

## Sources

- [Meta Llama 4 announcement blog](https://ai.meta.com/blog/llama-4-multimodal-intelligence/)
- [Introducing Llama 3.1 — Meta AI blog](https://ai.meta.com/blog/meta-llama-3-1/)
- [Llama 3.2 — Meta AI blog](https://ai.meta.com/blog/llama-3-2-connect-2024-vision-edge-mobile-devices/)
- [Llama 4 model page — llama.com](https://www.llama.com/models/llama-4/)
- [Llama 4 Community License Agreement](https://www.llama.com/llama4/license/)
- [Llama 4 Scout vs Maverick comparison — llm-stats.com](https://llm-stats.com/models/compare/llama-4-maverick-vs-llama-4-scout)
- [Llama 4 Scout specs — llm-stats.com](https://llm-stats.com/models/llama-4-scout)
- [Llama 4 Scout vs Maverick — artificialanalysis.ai](https://artificialanalysis.ai/models/comparisons/llama-4-scout-vs-llama-4-maverick)
- [Llama 4 Scout vs Maverick pricing — tokencost.app](https://tokencost.app/blog/llama-4-scout-vs-maverick-api-pricing)
- [Llama 4 Hardware Guide — compute-market.com](https://www.compute-market.com/blog/llama-4-local-hardware-guide-2026)
- [Llama 4 GPU requirements — apxml.com](https://apxml.com/posts/llama-4-system-requirements)
- [Llama 3.1 HumanEval / benchmark comparison — myscale.com](https://www.myscale.com/blog/llama-3-1-405b-70b-8b-quick-comparison/)
- [Llama 3.3 70B coding benchmarks — novita.ai](https://blogs.novita.ai/llama-3-3-70b-for-code/)
- [Llama 3.3 70B vs 3.1 70B comparison — novita.ai](https://blogs.novita.ai/llama-3-1-70b-vs-llama-3-3-70b-better-performance-higher-price/)
- [Llama 3.1 8B eval details — HuggingFace](https://huggingface.co/meta-llama/Llama-3.1-8B)
- [Self-hosting Llama 3.1 70B — HuggingFace blog](https://huggingface.co/blog/abhinand/self-hosting-llama3-1-70b-affordably)
- [VRAM requirements guide — insiderllm.com](https://insiderllm.com/guides/vram-requirements-local-llms/)
- [Llama 3.1 hardware guide — vrlatech.com](https://vrlatech.com/how-to-run-llama-3-locally-hardware-requirements-in-2026/)
- [Cursor + Llama 3 70B fast apply — AI News (Buttondown)](https://buttondown.com/ainews/archive/ainews-to-be-named-9199/)
- [Cursor Llama inference blog post](https://cursor.com/blog/llama-inference)
- [What Cursor's fine-tuned model means — Dan Cleary](https://danjcleary.substack.com/p/what-cursors-fine-tuned-model-means)
- [vLLM tool calling documentation](https://docs.vllm.ai/en/latest/features/tool_calling/)
- [Ollama tool calling documentation](https://docs.ollama.com/capabilities/tool-calling)
- [Groq pricing — groq.com](https://groq.com/pricing)
- [Llama API pricing comparison — aipricing.guru](https://www.aipricing.guru/meta-pricing/)
- [Llama 4 Behemoth specs — apxml.com](https://apxml.com/models/llama-4-behemoth)
- [Llama 4 Wikipedia](https://en.wikipedia.org/wiki/Llama_(language_model))
- [Llama 3.2 on HuggingFace blog](https://huggingface.co/blog/llama32)
