# GPT Model Family (OpenAI)

## What It Is

OpenAI's GPT (Generative Pre-trained Transformer) family is a series of proprietary, cloud-only large language models. The family spans multiple generations: GPT-4 Turbo (late 2023), GPT-4o (May 2024), GPT-4.1 (April 2025), GPT-5 (August 2025) through GPT-5.5 (April 2026), plus reasoning-specialized o-series models (o1, o3) and Codex-branded agentic coding variants (GPT-5.1-Codex, GPT-5.3-Codex). All are API-only — no weights are released for self-hosting (the separate GPT-OSS line, released 2026 under Apache 2.0, is a distinct product not covered here). The GPT family dominates coding tool integrations across Cursor, GitHub Copilot, Windsurf, and OpenAI's own Codex CLI.

## Variants

### GPT-4 Turbo
- Released: November 2023 (GA April 2024 as `gpt-4-turbo-2024-04-09`)
- 128K context, up to 4K output tokens
- Vision capable; replaced by GPT-4o for most use cases
- Now considered legacy; API still available

### GPT-4o
- Released: May 2024
- Natively multimodal (text, vision, audio)
- 128K context, up to 16K output tokens
- Faster and cheaper than GPT-4 Turbo with comparable English/coding performance
- Retired from ChatGPT February 13, 2026; API endpoint still available

### GPT-4o mini
- Released: July 18, 2024
- 128K context, up to 16K output tokens
- Budget tier; outperforms GPT-3.5 Turbo on academic benchmarks

### GPT-4.1 Family
- Released: April 14, 2025
- Three variants: GPT-4.1, GPT-4.1 mini, GPT-4.1 nano
- 1M token context window across all three variants (8x GPT-4o)
- Strong instruction-following and agentic coding focus
- Retired from ChatGPT February 13, 2026; API still accessible

### GPT-5
- Released: August 7, 2025
- 400K context window
- Thinking mode (chain-of-thought) and Pro variant with extended compute
- Sets state-of-the-art at launch on SWE-bench Verified, AIME 2025, GPQA

### GPT-5.2
- Released: late 2025
- Variants: Instant, Thinking, Pro
- 256K input context window
- Improved agentic reasoning; replaces GPT-4.1 and GPT-4o in ChatGPT default

### GPT-5.3 / GPT-5.4 / GPT-5.5
- GPT-5.4 released March 5, 2026 (Mini and Nano March 17, 2026)
- GPT-5.5 released April 23, 2026
- GPT-5.5: 1M+ context (922K input, 128K output), multimodal (text + images)
- Knowledge cutoff: December 2025 for GPT-5.5
- GPT-5.4 became OpenAI's flagship model replacing o-series reasoning models

### o1
- Released: September 2024 (preview); full release late 2024
- Chain-of-thought reasoning via reinforcement learning ("thinking" before answering)
- Specialized for multi-step logic, math, science, coding
- Variants: o1, o1-mini, o1-pro (extended compute, ChatGPT Pro only)
- 200K context window

### o3
- Released: o3-mini January 31, 2025; o3 and o4-mini April 16, 2025; o3-pro June 10, 2025
- Improved reasoning over o1; supports adjustable reasoning effort (low/medium/high/xhigh)
- 200K context window, up to 100K output tokens
- Variants: o3-mini, o3, o3-pro, o4-mini
- o-series retired from ChatGPT by mid-2026; superseded by GPT-5.4

### GPT-5.1-Codex / GPT-5.1-Codex-Max
- Agentic coding model; first natively trained for multi-context-window operation via compaction
- Enables project-scale refactors, deep debugging, multi-hour agent loops over millions of tokens
- First model trained to operate in Windows environments
- Predecessor to GPT-5.3-Codex

### GPT-5.3-Codex
- Released: February 5–24, 2026
- OpenAI's most capable agentic coding model at release
- 400K context window, up to 128K output tokens
- Supports low/medium/high/xhigh reasoning effort
- ~25% faster than predecessor
- Variants: GPT-5.3-Codex (flagship), GPT-5.3-Codex-Spark (text-only, >1000 tokens/sec, 128K context)
- Succeeded by GPT-5.4 and GPT-5.5 in the Codex CLI

## Pricing

All prices are per 1 million tokens (input / output). All models are cloud API only.

| Model | Input | Output | Notes |
|---|---|---|---|
| GPT-4 Turbo | $10.00 | $30.00 | Legacy |
| GPT-4o | $2.50 | $10.00 | Retired from ChatGPT Feb 2026 |
| GPT-4o mini | $0.15 | $0.60 | |
| GPT-4.1 | $2.00 | $8.00 | 26% cheaper than GPT-4o |
| GPT-4.1 mini | $0.40 | $1.60 | |
| GPT-4.1 nano | $0.10 | $0.40 | |
| GPT-5 | $1.25 | $10.00 | |
| GPT-5.2 | ~$1.75 | ~$14.00 | |
| GPT-5.5 | $5.00 | $30.00 | |
| o1 | $15.00 | $60.00 | Deep reasoning; high cost |
| o3-mini | $1.10 | $4.40 | Post-March 2026 price cut |
| o3 | $2.00 | $8.00 | Post-80% price cut March 2026 |
| o3-pro | $20.00 | $80.00 | |
| GPT-5.3-Codex | $1.75 | $14.00 | Codex CLI; credit-based in Codex |

GPT-5.3-Codex is also available in the Codex platform via a credit system (43.75 credits/1M input, 350 credits/1M output). GPT-5.5 in Codex: 125/750 credits per 1M input/output.

## Context Window

| Model | Context Window | Max Output |
|---|---|---|
| GPT-4 Turbo | 128K | 4K |
| GPT-4o | 128K | 16K |
| GPT-4o mini | 128K | 16K |
| GPT-4.1, mini, nano | 1M | — |
| GPT-5 | 400K | — |
| GPT-5.2 | 256K | — |
| GPT-5.5 | 922K input | 128K |
| o1 | 200K | 100K |
| o3, o3-mini | 200K | 100K |
| GPT-5.3-Codex | 400K | 128K |
| GPT-5.3-Codex-Spark | 128K | — |

GPT-4.1 achieves 100% accuracy on needle-in-haystack retrieval tests across all positions at the full 1M token limit. GPT-5.1-Codex-Max extends effective context further via native compaction across multiple context windows.

## Benchmarks

### SWE-bench Verified (real-world GitHub issue resolution)

| Model | Score |
|---|---|
| GPT-4o | 33.2% |
| GPT-4.1 | 54.6% |
| o1 | 48.9% |
| o3 | 71.7% |
| GPT-5 (with thinking) | 74.9% |
| GPT-5.2 Thinking | 80.0% |
| GPT-5.5 | 88.7% |

### SWE-bench Pro (harder multi-file problems)

| Model | Score |
|---|---|
| GPT-5.2 | 55.6% |
| GPT-5.5 | 58.6% |
| GPT-5.3-Codex | State-of-the-art at release (exact % unreported) |

### Terminal-Bench 2.0

| Model | Score |
|---|---|
| GPT-5.3-Codex | 77.3% (state-of-the-art at release) |

### HumanEval

| Model | Score |
|---|---|
| GPT-4o | 90.2% |

### AIME 2025 (math reasoning)

| Model | Score |
|---|---|
| o3-mini-high | 96.7% |
| GPT-5 with thinking | 99.6% |
| GPT-5 Pro with Python tools | 100% |

### GPQA Diamond (graduate-level science)

| Model | Score |
|---|---|
| o3 | 87.7% |
| GPT-5 with thinking | 85.7% |
| GPT-5 Pro with tools | 89.4% |

### Code Diff Accuracy (targeted code edits)

| Model | Score |
|---|---|
| GPT-4o | 18.3% |
| GPT-4.1 | 52.9% |

GPT-4.1 also reduced extraneous edits (unnecessary code changes) from 9% (GPT-4o) to 2% — a key practical improvement for coding tools. Windsurf reported 60% higher performance scores with GPT-4.1 vs GPT-4o.

## Hardware Requirements

All models in this family are **proprietary cloud-only APIs**. There are no public weights and no self-hosting option. Hardware requirements are irrelevant for end users — OpenAI runs all inference on their own infrastructure.

The separate **GPT-OSS** models (20B and 120B, Apache 2.0, released 2026) are self-hostable but are a distinct product family not covered here. For reference: GPT-OSS-20B requires ~16 GB VRAM; GPT-OSS-120B fits on a single 80 GB H100/A100 in MXFP4.

## Supported Tools

### Direct API / SDK
- OpenAI Python and Node.js SDKs (Chat Completions, Responses API)
- Responses API supports built-in tools: web search, code interpreter, remote MCP servers, file search, computer use
- Function calling and structured outputs across GPT-4o, GPT-4.1, GPT-5.x, and o-series

### Coding Tools and IDEs
- **GitHub Copilot**: GPT-4o, GPT-4.1, and GPT-5 series available as selectable models; GPT-5 launched across Microsoft/GitHub platforms
- **Cursor**: GPT-4o, GPT-4.1, GPT-5 series supported
- **Windsurf**: GPT-4.1 (60% performance improvement reported vs GPT-4o)
- **OpenAI Codex CLI**: GPT-5 is default; GPT-5.3-Codex and GPT-5.5 available; GPT-5.4 is the current flagship
- **ChatGPT (web/app)**: GPT-5.3 Instant and GPT-5.4 Thinking/Pro as defaults (as of early 2026)

### o-series in Tools
- o1 and o3 available in GitHub Copilot for complex reasoning tasks
- o3 and o4-mini support tool calls and function calling within chain-of-thought via Responses API

## Strengths

- **Coding performance**: GPT-4.1 onward dramatically outperforms predecessors on real-world code tasks (54.6% → 88.7% on SWE-bench Verified across generations). GPT-5.3-Codex holds state-of-the-art on Terminal-Bench 2.0.
- **Instruction following**: GPT-4.1 achieves 87.4% on IFEval vs 81.0% for GPT-4o; critical for agentic coding workflows where models must follow precise diff/patch formats.
- **Large context**: GPT-4.1's 1M token context and GPT-5.3-Codex's compaction-based multi-context operation enable whole-codebase understanding at scale.
- **Agentic coding**: Codex variants (GPT-5.1-Codex-Max, GPT-5.3-Codex) are explicitly trained on PR creation, code review, frontend coding, Q&A, and long-horizon tasks.
- **Tool integration breadth**: Available in every major coding IDE and platform; function calling, MCP, code interpreter, and computer use all natively supported.
- **Cost-performance trajectory**: Dramatic price reductions across generations (o3 dropped 80% in March 2026; GPT-4.1 is 26% cheaper than GPT-4o with far better coding scores).
- **Multimodal input**: GPT-4o onward supports images; useful for UI screenshot → code workflows.
- **o-series reasoning**: o1/o3 excel at complex algorithmic problems, debugging with multi-step logic, and math-heavy engineering tasks where extra deliberation time pays off.

## Weaknesses

- **No self-hosting**: All flagship GPT models require API access; cannot run locally or on-premises. This is a hard blocker for air-gapped or privacy-sensitive deployments.
- **Output token limits**: GPT-4 Turbo's 4K output cap is a practical constraint for large code generation tasks; later models improved this but GPT-5.3-Codex's 128K output is needed for whole-file rewrites.
- **o-series latency and cost**: o1 at $15/$60 per million tokens and high latency due to chain-of-thought makes it impractical for interactive autocomplete; suited only for batch/complex tasks.
- **Context window inconsistency across versions**: GPT-4o (128K) → GPT-4.1 (1M) → GPT-5 (400K) → GPT-5.2 (256K) — context window size has not monotonically increased across all generations; developers must check per-model specs.
- **Rapid deprecation cycle**: GPT-4o, GPT-4.1, o4-mini all retired from ChatGPT within ~18 months of release; API endpoints lag but tooling integrations must be updated frequently.
- **Pricing opacity for Codex platform**: Codex uses a credit system rather than direct token pricing, making cost estimation harder for agentic workflows.
- **SWE-bench Pro ceiling**: At 58.6%, GPT-5.5 trails Claude Opus 4.7 (64.3%) on harder multi-file real-world problems as of April 2026.
- **Knowledge cutoff**: GPT-5.5 cuts off at December 2025; older models have earlier cutoffs. No built-in retrieval without explicit tool use.

## Sources

- [Introducing GPT-4.1 in the API — OpenAI](https://openai.com/index/gpt-4-1/)
- [GPT-4.1 Full Developer Guide — Helicone](https://www.helicone.ai/blog/gpt-4.1-full-developer-guide)
- [Introducing GPT-5 — OpenAI](https://openai.com/index/introducing-gpt-5/)
- [Introducing GPT-5.2 — OpenAI](https://openai.com/index/introducing-gpt-5-2/)
- [GPT-5.2 Benchmarks — Vellum](https://www.vellum.ai/blog/gpt-5-2-benchmarks)
- [GPT-5 Benchmarks — Vellum](https://www.vellum.ai/blog/gpt-5-benchmarks)
- [Introducing GPT-5.5 — OpenAI](https://openai.com/index/introducing-gpt-5-5/)
- [Introducing o3 and o4-mini — OpenAI](https://openai.com/index/introducing-o3-and-o4-mini/)
- [OpenAI o3 Released: Benchmarks and Comparison to o1 — Helicone](https://www.helicone.ai/blog/openai-o3)
- [OpenAI o3 — Wikipedia](https://en.wikipedia.org/wiki/OpenAI_o3)
- [Introducing GPT-5.3-Codex — OpenAI](https://openai.com/index/introducing-gpt-5-3-codex/)
- [Building more with GPT-5.1-Codex-Max — OpenAI](https://openai.com/index/gpt-5-1-codex-max/)
- [Introducing GPT-5.3-Codex-Spark — OpenAI](https://openai.com/index/introducing-gpt-5-3-codex-spark/)
- [GPT-5.3-Codex — OpenRouter](https://openrouter.ai/openai/gpt-5.3-codex)
- [Codex Models — OpenAI Developers](https://developers.openai.com/codex/models)
- [Codex Pricing — OpenAI Developers](https://developers.openai.com/codex/pricing)
- [Retiring GPT-4o, GPT-4.1, and older models — OpenAI](https://openai.com/index/retiring-gpt-4o-and-older-models/)
- [GPT-4o mini — OpenAI](https://openai.com/index/gpt-4o-mini-advancing-cost-efficient-intelligence/)
- [GPT-4 Turbo Model — OpenAI API Docs](https://platform.openai.com/docs/models/gpt-4-turbo)
- [OpenAI API Pricing — OpenAI](https://openai.com/api/pricing/)
- [Supported AI Models in GitHub Copilot — GitHub Docs](https://docs.github.com/en/copilot/reference/ai-models/supported-models)
- [AI Coding Agents 2026 Comparison — Lushbinary](https://lushbinary.com/blog/ai-coding-agents-comparison-cursor-windsurf-claude-copilot-kiro-2026/)
- [GPT-OSS Self-Hosting Guide — Semaphore](https://semaphore.io/blog/gpt-oss)
