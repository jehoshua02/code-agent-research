# Glossary

Terms used throughout this survey. Alphabetical within each section. Keep entries short — one or two sentences plus an example.

## 0. Conventions

This glossary tries to use definitions as they are commonly used across the industry, not to redefine terms. Where multiple valid usages exist:

- The entry names the variations and cites at least one widely-used source.
- The entry then states which sense this survey uses, and why.
- Phrases like "as used in this survey" or "this survey's sense" mark a deliberate convention choice, not a redefinition.

Where a term is purely the survey's own labeling (e.g., a category we group entries under), the entry says so explicitly.

If you find an entry that conflicts with established industry usage, file an issue — the goal is fidelity to existing terminology, with explicit, sourced choices where the field is genuinely split.

## 1. Layers

### Model
Trained weights. A function from prompt tokens to predicted next-token probabilities. Examples: Llama 3.3 70B, Qwen2.5-Coder-32B, DeepSeek-V3.

### Runtime
Survey's umbrella term for what the industry variously calls **inference engine** (vLLM, SGLang), **inference server** (TGI), or **inference framework** (llama.cpp). The component that loads model weights and executes generation. No agent loop or tool-call logic of its own (though it may expose tool-calling APIs). The survey uses "runtime" for compactness; entity files preserve each project's self-description.

### Framework (agent framework)
Library for building agentic systems. Sits on top of a runtime via its API. Handles the loop: plan → call tools → observe → continue. Manages memory, state, multi-step reasoning, MCP integration. Doesn't run inference itself. Examples: LangGraph, AutoGen, CrewAI, Letta, Smolagents.

### MCP server
Process that exposes tools/resources/prompts to a client over the Model Context Protocol. Per [Anthropic's MCP spec](https://modelcontextprotocol.io). Examples: filesystem, shell, web fetch, browser control.

### Technique
**Survey-specific grouping** for patterns and approaches that are not models, runtimes, frameworks, MCP servers, or applications — typically named methods from papers or community practice. Examples: RAG (retrieval-augmented generation), ReAct (reason + act), prompt caching, speculative decoding. Industry does not use "technique" as a category label; this is the survey's umbrella.

### Layer stack example
Qwen2.5-Coder-32B (model) loaded by vLLM (runtime), driven by LangGraph (framework), calling a filesystem MCP server (tool), using ReAct (technique).

## 2. Model concepts

### Open-weight
Model whose trained weights are publicly downloadable. Does not necessarily mean training data, code, or full license freedom are open. Verify per-model license.

### Parameters (params)
Count of learned weights. Reported in billions (B) or trillions (T). More params = larger, slower, usually more capable. MoE models report both total params (storage) and active params (per-token compute).

### MoE (Mixture of Experts)
Architecture where only a subset of params is used per token. Active params drive compute cost; total params drive storage/VRAM. Example: DeepSeek-V3 is 671B total / 37B active.

### Context window
Maximum number of tokens (prompt + output) the model can attend to in one call. Native context = trained. Extended context (YaRN, position interpolation) trades fidelity for length.

### Quantization
Lossy compression of weights to fewer bits per parameter, to fit smaller VRAM. Common formats:
- **GGUF** (llama.cpp) — Q2_K, Q4_K_M, Q5_K_M, Q8_0, etc. Higher number = more precision.
- **AWQ, GPTQ** — 4-bit quantization for GPU runtimes
- **FP8, FP16, BF16** — full or half precision

### Tool use / function calling
Model emits structured calls to external functions (declared in the prompt or via API). Framework executes the call and feeds the result back into context.

## 3. Hardware

### VRAM
GPU memory. The main constraint on what model fits. Quantization, context length, and KV cache all consume VRAM.

### KV cache
Per-token attention state cached during generation. Grows linearly with context length. Often the deciding factor between "fits" and "doesn't" at long contexts.

### Offload
Moving some model layers to CPU RAM (or disk) when they don't fit in VRAM. Slower but enables larger models. System RAM bandwidth becomes the bottleneck.

### Tokens per second (tok/s)
Generation throughput. Reported as prefill (input processing) and decode (output) separately.

## 4. Tasks and protocols

### MCP (Model Context Protocol)
Anthropic-originated open protocol for connecting agents to tools. Transports: stdio, SSE, streamable HTTP.

### Agent
Overloaded term. This survey uses these specific senses:

- **Agentic system** (per [Anthropic, *Building Effective Agents*](https://www.anthropic.com/research/building-effective-agents)) — an LLM dynamically directs its own process and tool usage; the LLM picks the next step based on intermediate results. Contrasted with a **workflow**.
- **Loose industry sense** — sometimes refers to any LLM-with-tools, even simple single-step function calling. LangChain and HuggingFace docs use this looser sense. Be careful when reading external sources.

Examples: a coding session where the LLM reads files, edits them, runs tests, and decides next steps is agentic. A pipeline that always calls `summarize → classify → store` is a workflow even if each step is an LLM call.

### Workflow
Ambiguous word; depends on the source.

- **In the agent vs workflow distinction** ([Anthropic](https://www.anthropic.com/research/building-effective-agents)) — a predefined sequence of LLM calls and tool invocations where each step's logic is fixed in code. The foil to an agentic system. This is the sense the survey uses by default.
- **In framework jargon** (LangGraph, n8n, etc.) — sometimes also refers to a graph of nodes the framework executes, including ones with agentic branching. Read the source's own definition before transferring claims.

### Application (as used in this survey)
A finished, installable AI product that composes the stack (models + runtimes + framework patterns + MCP). Example: OpenCode is an agentic coding application; Open WebUI is a chat-UI application. Distinct from a **framework** (a library you build applications with) and from a **runtime** (which executes the model).

### Framework vs application
A framework is a library — you write code on top of it to make something. An application is a finished product — you install and run it. LangGraph is a framework; OpenCode is an application. Some projects blur the line (Continue is both an extension product and an extensibility surface).

### Self-hostable
You can run it yourself on hardware you control. Excludes API-only services. Includes everything in this survey.
