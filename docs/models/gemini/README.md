# Gemini

## What It Is

Gemini is Google DeepMind's flagship model family. All variants are proprietary, closed-weight, API-only (no self-hosting). The family spans four generations: 1.5 (now fully shutdown), 2.0 (deprecated, shutdown June 1, 2026), 2.5 (current stable), and 3.x (latest, partially in preview). The series uses Mixture-of-Experts (MoE) transformer architecture. All models are natively multimodal (text, image, audio, video). The primary developer interface is Google AI Studio and the Gemini API; enterprise access is through Vertex AI.

Key notes on scope of this document:
- Gemini 1.5 Pro and Flash are fully shutdown (404 errors as of April 2026).
- Gemini 2.0 Flash shuts down June 1, 2026.
- Gemini 2.5 Pro and Flash shut down June 17, 2026 (earliest possible date).
- Gemini 3 Flash (released December 17, 2025) and Gemini 3.1 Pro (released February 19, 2026) are the current frontier models.

## Variants

### Gemini 1.5 Pro (SHUTDOWN)
- Released: February 15, 2024 (limited preview); generally available mid-2024
- Architecture: MoE transformer
- Status: Fully shutdown; all requests return 404
- Originally featured: 1M token context window (later expanded to 2M for some tiers), natively multimodal
- Replacement: Gemini 2.5 Pro (now also deprecated) → Gemini 3.1 Pro

### Gemini 1.5 Flash (SHUTDOWN)
- Released: May 2024 alongside 1.5 Pro GA
- Status: Fully shutdown; all requests return 404
- Positioned as: Faster, cheaper variant of 1.5 Pro; 1M token context
- Replacement: Gemini 2.5 Flash → Gemini 3 Flash

### Gemini 2.0 Flash (DEPRECATED — shutdown June 1, 2026)
- Released: February 5, 2025 (GA); experimental December 2024
- Context window: 1,048,576 tokens; max output: 8,192 tokens
- Native tool use, multimodal input (text, image, audio, video)
- 2x faster than Gemini 1.5 Pro on generation speed
- Successor: Gemini 2.5 Flash

### Gemini 2.5 Flash (DEPRECATED — shutdown June 17, 2026)
- Released: Spring 2025
- Context window: 1,048,576 tokens; max output: 65,535 tokens
- Supports optional "thinking" mode (extended reasoning)
- Positioned as: Best price-performance for high-volume low-latency tasks
- SWE-bench Verified: 60.4% (non-thinking)
- Successor: Gemini 3 Flash

### Gemini 2.5 Flash-Lite (DEPRECATED — shutdown July 22, 2026)
- Budget-optimized variant; fastest in the 2.5 series
- SWE-bench Verified: 41.3% (non-thinking), 44.9% (thinking, multi-attempt)
- LiveCodeBench v5: 58.4% (thinking), 52.1% (non-thinking)

### Gemini 2.5 Pro (DEPRECATED — shutdown June 17, 2026)
- Released: March 2025
- Context window: 1,048,576 tokens; max output: 65,535 tokens
- Knowledge cutoff: January 2025
- Architecture: MoE, native thinking/reasoning mode
- Flagship of the 2.5 generation; deep reasoning, long context
- SWE-bench Verified: 63.8% (at launch); ~73–78% with updated agent scaffolding
- AIME 2025: 86.7%; GPQA Diamond: 84.0%; MMMU: 81.7%; LiveCodeBench v5: 70.4%; Aider Polyglot: 74.0%
- Successor: Gemini 3.1 Pro

### Gemini 3 Flash (CURRENT)
- Released: December 17, 2025
- Context window: 1,048,576 tokens; max output: 65,536 tokens
- Knowledge cutoff: January 2025
- Supports thinking/reasoning mode
- Generation speed: ~183 tokens/second (Artificial Analysis)
- Uses ~30% fewer tokens than 2.5 Pro on typical tasks
- SWE-bench Verified: 78%; GPQA Diamond: 90.4%; Humanity's Last Exam: 33.7%; MMMU Pro: 81.2%
- Outperforms Gemini 3 Pro and 2.5 Pro on SWE-bench
- Positioned as: Frontier-class reasoning with Flash-level latency

### Gemini 3 Pro (CURRENT)
- Preceded 3.1 Pro; intermediate generation
- Context window: 1,048,576 tokens
- Outperformed by both Gemini 3 Flash (on coding) and Gemini 3.1 Pro (on reasoning)

### Gemini 3.1 Pro (CURRENT — Preview)
- Released: February 19, 2026 (preview)
- Context window: 1,048,576 tokens; max output: 64,000 tokens
- Multimodal input: text, images, audio, video, code repositories
- Architecture: Google's most capable model for complex tasks
- SWE-bench Verified: 80.6%; ARC-AGI-2: 77.1%; GPQA Diamond: 94.3%; LiveCodeBench Pro: 2887 Elo; MRCR v2 Long Context (128k): 84.9%
- Described as optimized for "agentic performance, advanced coding, long context, and multimodal understanding"
- Artificial Analysis Intelligence Index: 57 (well above median of 35)

### Gemini 3.1 Flash-Lite (CURRENT — Preview)
- Released: March 2026 (preview)
- Budget-optimized successor to 2.5 Flash-Lite
- 45% faster answer generation; 2.5x lower time-to-first-token vs predecessor

### Specialized Models (not covered in depth)
- Gemini 2.5 Flash Live / 3.1 Flash Live: Real-time voice/dialogue
- Gemini 2.5 Flash TTS / 3.1 Flash TTS: Text-to-speech
- Gemini Embedding 2: Multimodal embeddings for RAG/search
- Gemini Robotics-ER 1.6: Embodied reasoning for robotics
- Computer Use: Browser/UI automation

## Pricing

All prices are per 1 million tokens via the Gemini API (Google AI Studio). Vertex AI pricing may differ. Free tier available with rate limits; no credit card required for free tier access.

### Current Models

| Model | Input (≤200k ctx) | Input (>200k ctx) | Output (≤200k ctx) | Output (>200k ctx) |
|---|---|---|---|---|
| Gemini 3.1 Pro (preview) | $2.00 | $4.00 | $12.00 | $18.00 |
| Gemini 3 Flash | $0.50 | — | $3.00 | — |
| Gemini 3.1 Flash-Lite (preview) | $0.25 | — | $1.50 | — |
| Gemini 2.5 Pro | $1.25 | $2.50 | $10.00 | $15.00 |
| Gemini 2.5 Flash | $0.30 | — | $2.50 | — |

### Deprecated / Legacy Models (for reference)

| Model | Input | Output | Status |
|---|---|---|---|
| Gemini 2.0 Flash | $0.10 | $0.40 | Shutdown June 1, 2026 |
| Gemini 1.5 Pro | ~$3.50 (was reduced 64%) | ~$10.50 | Shutdown |
| Gemini 1.5 Flash | ~$0.075 | ~$0.30 | Shutdown |

### Batch Pricing
Batch mode (async) offers ~50% reduction on standard rates for all models.

### Caching
Context caching is available on 2.5 and 3.x series. Storage billed separately ($1.00–$8.10 per 1M tokens per hour depending on model). Cache hit discount up to 90% on input tokens (Gemini 2.5 Flash: cached input $0.03/1M vs $0.30/1M standard).

### Google Search Grounding
Free up to 5,000 prompts/month (Gemini 3 series); $14/1,000 queries thereafter.

### Free Tier (rate-limited, no credit card)
Models available for free: Gemini 3.1 Flash-Lite, Gemini 2.5 Flash, Gemini 2.5 Flash-Lite, Gemini 2.0 Flash, Gemini Embedding models.
- Pro models: 25 requests/minute
- Flash models: 500 requests/minute

### Hardware Requirements (Self-Hosted)

Not applicable. All Gemini models (1.5 through 3.1) are closed-weight, proprietary models available only through Google's API. No model weights are released for self-hosting.

For self-hosted Google models, see the **Gemma** family (Gemma 4 is the current open-weight offering from Google DeepMind, available via Ollama/vLLM).

## Context Window

All current Gemini models share a 1,048,576-token (1M) context window for input.

| Model | Input Context | Max Output |
|---|---|---|
| Gemini 3.1 Pro | 1,048,576 | 64,000 |
| Gemini 3 Flash | 1,048,576 | 65,536 |
| Gemini 3.1 Flash-Lite | 1,048,576 | ~65,536 |
| Gemini 2.5 Pro | 1,048,576 | 65,535 |
| Gemini 2.5 Flash | 1,048,576 | 65,535 |
| Gemini 2.0 Flash | 1,048,576 | 8,192 |
| Gemini 1.5 Pro (shutdown) | 2,097,152 (peak) | — |

**Pricing tiers:** For 2.5 Pro and 3.1 Pro, prompts exceeding 200k tokens are billed at a higher rate (see Pricing section). Other models use flat per-token pricing regardless of context length.

**Practical limits:** The 1M context window is the largest offered by any API-accessible model as of May 2026. Google has tested 10M tokens in research settings. Long-context retrieval (Needle in Haystack at 1M tokens) accuracy was 99% for Gemini 1.5 Pro; MRCR v2 at 128k scores 84.9% for Gemini 3.1 Pro.

## Benchmarks

### Coding Benchmarks

| Model | SWE-bench Verified | LiveCodeBench v5 | Aider Polyglot |
|---|---|---|---|
| Gemini 3.1 Pro | 80.6% | 2887 Elo (Pro) | — |
| Gemini 3 Flash | 78.0% | — | — |
| Gemini 2.5 Pro | 63.8% (launch) / ~73–78% (updated scaffolding) | 70.4% | 74.0% |
| Gemini 2.5 Flash | 60.4% | — | — |
| Gemini 2.5 Flash-Lite | 41.3% (non-thinking) / 44.9% (thinking) | 52.1–58.4% | 26.7–27.1% |

Note: SWE-bench scores are sensitive to scaffolding and agent setup. Gemini 2.5 Pro's 63.8% was with a specific custom agent; broader evaluations in 2026 put it at 73–78% with updated frameworks.

### General Intelligence Benchmarks

| Model | GPQA Diamond | MMMU / MMMU Pro | Humanity's Last Exam | ARC-AGI-2 | AA Intelligence Index |
|---|---|---|---|---|---|
| Gemini 3.1 Pro | 94.3% | — | — | 77.1% | 57 |
| Gemini 3 Flash | 90.4% | 81.2% | 33.7% | — | 46 |
| Gemini 2.5 Pro | 84.0% | 81.7% | 18.8% | — | — |
| Gemini 2.5 Flash | — | — | 11.0% | — | 21 |
| Gemini 2.0 Flash | — | — | — | — | 19 |

### Math Benchmarks

| Model | AIME 2025 | AIME 2024 |
|---|---|---|
| Gemini 2.5 Pro | 86.7% | 92.0% |

### Competitive Context (May 2026)

On SWE-bench Verified, as of early 2026:
- Claude 4: ~77.2%
- GPT-5: ~74.9%
- Gemini 3.1 Pro: 80.6%
- Gemini 3 Flash: 78.0%
- Gemini 2.5 Pro: 63.8–78% (scaffolding-dependent)

Gemini 3.1 Pro and 3 Flash are competitive with or ahead of frontier peers on coding benchmarks. Gemini 3 Flash notably outperforms Gemini 3 Pro on SWE-bench, making it the preferred model for agentic coding tasks within the 3.x series.

On ARC-AGI-2 (abstract reasoning), Gemini 3.1 Pro's 77.1% score is "more than double the reasoning performance of 3 Pro," representing a step-change in abstract reasoning capability.

Speed: Gemini 3 Flash generates ~183 tokens/second; Gemini 2.5 Flash reaches ~232 tokens/second (one of the fastest in its tier at Artificial Analysis). Median comparable model speed is 69–97 tokens/second.

## Hardware Requirements

Not applicable. All Gemini models are proprietary and closed-weight; they run on Google's infrastructure only. There is no path to self-hosting any Gemini model.

For local/self-hosted inference of Google-origin models, use **Gemma 4** (open-weight, available via Ollama and vLLM).

## Supported Tools

### Google-Native Tools
- **Gemini CLI**: Open-source CLI tool; Gemini 3 Flash is the default model; 3.1 Pro available; supports MCP (Model Context Protocol) for connecting local/remote MCP servers. Most generous free tier of any major coding CLI.
- **Gemini Code Assist**: VS Code and IntelliJ plugin; supports Gemini 3 Flash and 3.1 Pro for agent mode, chat, and code generation. Strong Google Cloud / Firebase / BigQuery integration.
- **Google Antigravity**: Google's agent-first IDE (launched November 2025); supports Gemini 3 Pro, 3.1 Pro, Claude Sonnet, and GPT-OSS; multi-agent orchestration via Mission Control; built-in browser.
- **Android Studio**: Gemini 3 Flash integrated for AI coding assistance in Android development.
- **NotebookLM**: Consumer-facing research tool; uses Gemini models.
- **Google AI Studio**: Primary developer playground and API management interface.
- **Vertex AI**: Enterprise API and fine-tuning platform.

### Third-Party Tools
- **GitHub Copilot** (Pro and above): Supports Gemini models as selectable backends alongside Claude and OpenAI models.
- **Cursor**: Gemini models available via API key integration.
- **Windsurf**: Gemini models available via API key integration.
- **OpenRouter**: Gemini 2.5 Flash, 2.5 Pro, 3 Flash available as routed models.
- **LiteLLM / LangChain / LlamaIndex**: Full API support via google-generativeai SDK.

### API Access
Primary SDK: `google-generativeai` (Python), `@google/genai` (JavaScript/TypeScript). Also accessible via OpenAI-compatible endpoint format on some platforms.

## Strengths

**Coding (current models):**
- Gemini 3.1 Pro achieves 80.6% SWE-bench Verified — among the highest of any frontier model as of May 2026.
- Gemini 3 Flash achieves 78% SWE-bench Verified while being 3x faster and significantly cheaper than Gemini 3.1 Pro. This makes it exceptional for agentic coding loops where cost and latency matter.
- Both 3.x models natively support agentic workflows, multi-turn chat, and tool use.

**Context window:**
- 1M token context is the largest of any major API provider. Practical for large codebase ingestion, long audit trails, and multi-file analysis in a single prompt.

**Multimodal:**
- All current models natively handle text, image, audio, and video in a single prompt without adapter layers.

**Speed and cost efficiency:**
- Gemini 3 Flash delivers near-Pro reasoning at ~$0.50/$3.00 per 1M tokens. At 183 tokens/second it is one of the fastest frontier-class reasoning models.
- Gemini 2.5 Flash reaches 232 tokens/second — among the fastest available.

**Free tier:**
- Gemini CLI and API free tier are the most generous in the industry; free access to 2.5 Flash and 3.1 Flash-Lite with high rate limits.

**Thinking/reasoning mode:**
- 2.5 Pro, 2.5 Flash, 3 Flash, and 3.1 Pro all support extended thinking, allowing the model to reason before producing output. Useful for complex coding problems, algorithm design, and debugging.

**Google ecosystem integration:**
- Native integration with Firebase, Cloud Run, BigQuery, Cloud Workstations via Gemini Code Assist and Vertex AI.

## Weaknesses

**Closed weights:**
- No self-hosting option. All inference goes through Google's API. Vendor lock-in and data privacy considerations apply.

**Verbosity:**
- Gemini 2.5 Flash generates ~72M tokens on benchmark tasks vs. a median of 36M for comparable models. Verbose output increases cost and latency in agentic loops.

**Rapid deprecation cycle:**
- The 1.5 and 2.0 generations were fully deprecated within roughly one year of release. The 2.5 series is already deprecated as of late 2026 targets. Codebases relying on specific model versions require frequent migration.

**Thinking mode cost:**
- Extended thinking mode increases token output significantly (reasoning tokens are billed). For Gemini 2.5 Flash-Lite, thinking mode can reduce performance on some benchmarks (SWE-bench non-thinking 41.3% vs. thinking 38.9% in single-attempt mode) while substantially increasing cost.

**Output token limits:**
- Max output of 64,000–65,536 tokens constrains very large single-output tasks (e.g., generating entire large files). Gemini 2.0 Flash had a particularly low 8,192 max output.

**Preview status of frontier models:**
- Gemini 3.1 Pro launched in preview in February 2026 and may not have SLAs or production guarantees available immediately.

**SWE-bench score sensitivity:**
- Gemini 2.5 Pro's reported SWE-bench scores ranged from 63.8% (Google's own launch evaluation) to ~78% (third-party 2026 evaluations), indicating high sensitivity to scaffolding. Benchmark claims should be evaluated carefully.

**No open-weight option in this family:**
- For open-weight models, Google's separate Gemma family must be used.

## Sources

- [Google DeepMind — Introducing Gemini 1.5](https://blog.google/innovation-and-ai/products/google-gemini-next-generation-model-february-2024/)
- [Google Developers Blog — Gemini 2.0 Family Expands](https://developers.googleblog.com/en/gemini-2-family-expands/)
- [Google DeepMind — Gemini 2.5 Flash](https://deepmind.google/technologies/gemini/flash/)
- [Helicone — Gemini 2.5 Pro Benchmarks & Integration Guide](https://www.helicone.ai/blog/gemini-2.5-full-developer-guide)
- [Google Blog — Introducing Gemini 3 Flash](https://blog.google/products-and-platforms/products/gemini/gemini-3-flash/)
- [Google Blog — Gemini 3.1 Pro](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-1-pro/)
- [Google DeepMind — Gemini 3.1 Pro Model Card](https://deepmind.google/models/model-cards/gemini-3-1-pro/)
- [Google AI for Developers — Models](https://ai.google.dev/gemini-api/docs/models)
- [Google AI for Developers — Pricing](https://ai.google.dev/gemini-api/docs/pricing)
- [Google AI for Developers — Deprecations](https://ai.google.dev/gemini-api/docs/deprecations)
- [Artificial Analysis — Gemini 2.5 Flash](https://artificialanalysis.ai/models/gemini-2-5-flash)
- [Artificial Analysis — Gemini 3 Flash](https://artificialanalysis.ai/models/gemini-3-flash-reasoning)
- [Artificial Analysis — Gemini 3.1 Pro Preview](https://artificialanalysis.ai/models/gemini-3-1-pro-preview)
- [Google Developers — Gemini 3 in Gemini Code Assist](https://developers.google.com/gemini-code-assist/docs/gemini-3)
- [Google Developers Blog — Gemini 3 Flash in Gemini CLI](https://developers.googleblog.com/gemini-3-flash-is-now-available-in-gemini-cli/)
- [DevTk.AI — Gemini API Pricing Guide 2026](https://devtk.ai/en/blog/gemini-api-pricing-guide-2026/)
- [OpenRouter — Gemini 2.5 Flash](https://openrouter.ai/google/gemini-2.5-flash)
- [Vertex AI — Gemini 2.5 Flash Docs](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/gemini/2-5-flash)
- [Gemini 2.5 Technical Report (arXiv)](https://arxiv.org/html/2507.06261)
