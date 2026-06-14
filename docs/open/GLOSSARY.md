# Glossary

Terms used throughout this survey. Alphabetical within each section. Keep entries short — one or two sentences plus an example.

## 1. Layers

### Model
Trained weights. A function from prompt tokens to predicted next-token probabilities. Examples: Llama 3.3 70B, Qwen2.5-Coder-32B, DeepSeek-V3.

### Runtime
Inference engine. Loads model weights and executes generation. No agent loop or tool-call logic of its own (though it may expose tool-calling APIs). Examples: vLLM, llama.cpp, Ollama, LM Studio, MLX, TGI, SGLang.

### Framework
Agent harness. Sits on top of a runtime (via its API). Handles the loop: plan → call tools → observe → continue. Manages memory, state, multi-step reasoning, MCP integration. Doesn't run inference itself. Examples: LangGraph, AutoGen, CrewAI, Letta, Smolagents.

### MCP server
Process that exposes tools/resources/prompts to an agent over the Model Context Protocol. The framework discovers and calls them. Examples: filesystem, shell, web fetch, browser control.

### Technique
A pattern applied at any layer. Examples: RAG (retrieval-augmented generation), ReAct (reason + act), tool use, prompt caching.

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
A loop that uses a model to plan and act over multiple steps, calling tools and consuming their results. Built with a framework, runs against a runtime.

### Self-hostable
You can run it yourself on hardware you control. Excludes API-only services. Includes everything in this survey.
