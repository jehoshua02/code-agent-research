# Considered

Entities researched and decided **not** to add as full entries, with the [inclusion criterion](README.md#22-inclusion-criteria) they failed (or the reason they fall outside scope). Keeping the record means readers know the analysis happened — they don't have to wonder whether we forgot.

When new readers (or future versions of ourselves) ask "what about X?", check here first. If X is listed, the decision is recorded. If X isn't listed, it's genuinely unexamined and worth evaluating.

## 1. Excluded

| Name | Decision | Reason |
|---|---|---|
| ClaudeBot | Excluded | Long-tail. Multiple small Claude wrappers exist (Telegram bot, IRC bot, etc.); highest ★159 (2026-06-14). None meet the adoption signal or distinct-contribution criteria; redundant with already-included agentic-coding applications. |

## 2. Model-specific ecosystem sweeps

Model-specific runtimes and applications are first-class entries (see [README §2.1](README.md#21-categories)). Tracking which model ecosystems have been swept here so we don't miss notable model-specific tooling.

| Model family | Swept | Notable additions | Notes |
|---|---|---|---|
| Gemma | Yes (2026-06-14) | [gemma.cpp](runtimes/gemma-cpp.md), [Gemma Chat](applications/gemma-chat.md), [Gemma Gem](applications/gemma-gem.md) | Considered but not added: gemma_pytorch and google-deepmind/gemma — reference / library implementations, cross-referenced from [gemma.md](models/gemma.md) §6 Runtime Support instead. gemma-tuner-multimodal (fine-tuning), gemma-2B-10M (research) — out of scope for now (no fine-tuning or research-experiment categories in survey yet). |
| Llama | Not yet | | Llama-specific runtimes, fine-tunes, and chat apps exist; pending sweep. |
| Qwen | Not yet | | |
| Mistral | Not yet | | |
| DeepSeek | Not yet | | |
| Other | Not yet | | Phi, Yi, Falcon, Command R, StarCoder2, OLMo, Granite, Nemotron, DBRX, SmolLM, Hermes, Hunyuan |

## 3. Out of scope (not self-hostable)

These are real, notable projects — but they're hosted SaaS, so they fall outside this survey's "self-hostable" boundary. Listed here so readers know we evaluated them and how to relate them to the survey.

| Name | Relationship to survey |
|---|---|
| OpenRouter | Hosted API aggregator providing one OpenAI-compatible endpoint over 300+ models from many providers. Many in-scope frameworks and applications can target it as a backend; that should be noted in their `Model Compatibility` sections (Pass C). It is not itself a survey entity. |

## 4. Borderline (currently included with notes)

These passed inclusion as borderline cases. They appear as full entries in their layer with a borderline note in §1 and INDEX. Listed here so the borderline calls are transparent and trackable.

| Name | Layer | Borderline reason | Revisit when |
|---|---|---|---|
| [GSD-PI](applications/gsd-pi.md) | Applications | ★626 (under ★1,000 adoption threshold) but ~1 month old; candidate for distinct-contribution criterion | 3 months after first observation (so ~2026-09) |
| [Gemma Gem](applications/gemma-gem.md) | Applications | ★930 (under ★1,000) but distinct contribution: Gemma 4 on-device via WebGPU | 3 months after first observation (so ~2026-09) |
