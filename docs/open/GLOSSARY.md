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
Count of learned weights. Reported in billions (B) or trillions (T). More params = larger file and slower inference per token, all else equal. Capability depends on training data, methodology, and alignment as well — not on param count alone. MoE models report both total params (storage) and active params (per-token compute).

### MoE (Mixture of Experts)
Architecture where only a subset of params is used per token. Active params drive compute cost; total params drive storage/VRAM. Example: DeepSeek-V3 is 671B total / 37B active.

### Dense
Architecture where every parameter participates in every token's compute (the default for most models). Contrast with MoE.

### Context window
Maximum number of tokens (prompt + output) the model can attend to in one call. **Native context** = the length the model was trained on. **Extended context** uses position-encoding tricks (YaRN, position interpolation, rope scaling) to operate beyond native. Practical effective context — where retrieval and reasoning quality stay usable — is often less than the advertised maximum; verify per-model.

### Token
The model's atomic input/output unit — usually a sub-word or whole word produced by a tokenizer. English averages roughly 0.75 tokens per word; code varies. Costs, context limits, and throughput are all measured in tokens.

### Embedding
A fixed-length numeric vector representing the meaning of a piece of text. Produced by embedding models (different from generation models). Used for similarity search in RAG, vector databases, and semantic memory.

### Quantization
Lossy compression of weights to fewer bits per parameter, to fit smaller VRAM and improve throughput. The relationship "fewer bits → smaller VRAM + faster, but lower quality" is the rule of thumb; specifics vary by method.

Format vs method:

- **GGUF** — file format used by llama.cpp and downstream runtimes. Can hold weights at any precision (including unquantized). Quantization variants are method codes inside the file: `Q2_K`, `Q4_K_M`, `Q5_K_M`, `Q8_0`, etc. As a rough guide, the leading number is bits per weight; suffixes (`_K`, `_M`, `_0`) encode the scheme. Higher bits = more precision, with method nuances.
- **AWQ, GPTQ** — quantization methods/formats commonly used with GPU runtimes (vLLM, ExLlama, etc.). Most-shipped variants are 4-bit, but the methods support other bit widths.
- **EXL2** — ExLlama format with mixed-bit-rate quantization across layers.
- **FP32 / FP16 / BF16 / FP8** — IEEE-style floating-point precisions. FP32 is full precision, FP16/BF16 are half, FP8 is quarter. Often called "precisions" rather than "quantization," though FP8 sits at the boundary.

### Tool use / function calling
Model emits structured calls to external functions (declared in the prompt or via API). Framework executes the call and feeds the result back into context. "Function calling" is OpenAI's specific term; "tool use" is broader (Anthropic). They are largely interchangeable.

### System prompt
Instructions provided to the model before the conversation begins, defining its role, constraints, or personality. Distinct from user-supplied messages.

### Reasoning model
A model trained to produce explicit step-by-step thinking before its final answer. Examples: OpenAI o-series, DeepSeek-R1. The thinking tokens are often charged or visible separately from the final response.

### Fine-tuning
Adjusting a pre-trained model's weights on a smaller task-specific dataset. Full fine-tuning updates all weights; LoRA (Low-Rank Adaptation) updates a small added adapter and is much cheaper.

## 3. Hardware

### VRAM
GPU memory. The main constraint on what model fits. Quantization, context length, and KV cache all consume VRAM.

### KV cache
Per-token attention state cached during generation. Grows linearly with context length. Often the deciding factor between "fits" and "doesn't" at long contexts.

### PagedAttention
A memory-management technique for KV cache (introduced by vLLM) that stores it in fixed-size blocks like virtual-memory pages. Avoids fragmentation and enables more concurrent requests.

### Offload
Moving some model layers to CPU RAM (or disk) when they don't fit in VRAM. Slower but enables larger models. System RAM bandwidth becomes the bottleneck.

### Tokens per second (tok/s)
Generation throughput. Reported as prefill (input processing) and decode (output) separately.

### Prefill / decode
Two phases of LLM inference. **Prefill** is the initial pass over the input prompt — compute-heavy, parallelizable. **Decode** is producing the output one token at a time — memory-bandwidth-bound, hard to parallelize per-request.

### Batching
Serving multiple requests at once on the same GPU. **Static batching** waits for the slowest. **Continuous batching** (vLLM, SGLang, TGI) starts new requests as old ones finish — dramatically higher throughput at the cost of complexity.

### CUDA / ROCm / Metal
GPU compute platforms. **CUDA** = NVIDIA. **ROCm** = AMD. **Metal** = Apple Silicon. Runtimes target one or more; CUDA has the broadest support, ROCm is catching up, Metal is Apple-only.

## 4. Tasks and protocols

### MCP (Model Context Protocol)
Anthropic-originated open protocol for connecting agents to tools. Transports: stdio, SSE, streamable HTTP.

### MCP transports
**stdio** = the agent launches the MCP server as a subprocess and talks via stdin/stdout. **SSE** (Server-Sent Events) = HTTP streaming, one-direction server→client (older MCP variant). **Streamable HTTP** = newer MCP transport that supports bidirectional streaming over HTTP.

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

### BYOK (Bring Your Own Key)
The application doesn't host a model itself — you supply API keys for your preferred provider(s) and pay them directly. Common with agentic coding tools.

### Headless
A program that runs without a graphical interface — driven by API, CLI flags, or scripts. Important for automation: a headless agent can be driven by another agent.

## 5. Agent patterns (named techniques)

### ReAct (Reason + Act)
The model writes a Thought → executes an Action (tool call) → reads the Observation → repeats. Most agent frameworks default to this loop. Source: Yao et al. 2022.

### Chain-of-thought (CoT)
Prompting the model to write its reasoning before its final answer. Improves multi-step problems. Source: Wei et al. 2022.

### Tree-of-thought (ToT)
Maintains a search tree of partial reasoning paths and backtracks when needed. More expensive than CoT but handles tasks where early steps may be wrong. Source: Yao et al. 2023.

### Plan-and-execute
A planner LLM call decomposes the task; an executor carries out each sub-task. Trades a planning roundtrip for staying on track over long horizons. Source: Wang et al. 2023.

### Reflexion / reflection
The agent evaluates its own output, writes a self-critique, and tries again using that critique. Source: Shinn et al. 2023.

### Self-consistency
Sample multiple chain-of-thought paths at non-zero temperature, then majority-vote the answer. Trades cost for accuracy. Source: Wang et al. 2022.

### Handoff / agent handoff
One agent transfers control to another by emitting a "handoff" tool call or message. Popularized by OpenAI Swarm; appears in AutoGen, BeeAI, and others.

### Supervisor-worker / orchestrator-worker
A "supervisor" agent decides what sub-tasks to delegate; "worker" agents do the actual work. Used in CrewAI hierarchical mode, mcp-agent's Orchestrator, AutoGen MagenticOne.

### Multi-agent
Any system where multiple specialized agents collaborate. May use handoffs, supervisor-worker, group chat, or a graph topology.

### Subgraph / nested agent
An agent (or graph of nodes) used as a step inside a larger agent. Enables hierarchical composition.

### Human-in-the-loop (HITL)
The agent pauses for human approval, input, or correction at predefined points or on certain tool calls. Mechanism varies: interrupts, deferred tools, approval-required tools.

### RAG (Retrieval-Augmented Generation)
Before answering, the agent retrieves relevant documents from a store (usually a vector database) and includes them in context. Reduces hallucination and lets the model answer about information not in its training data. Source: Lewis et al. 2020.

### Vector database (vector DB)
A database optimized for storing and searching by similarity over embeddings. Used as the retrieval layer in RAG. Examples: Qdrant, Weaviate, Chroma, Milvus, pgvector.

## 6. Runtime & API surface

### OpenAI-compatible API
A runtime exposes endpoints that mimic OpenAI's REST API (`/v1/chat/completions`, `/v1/embeddings`, etc.) so existing OpenAI-API client code can talk to it unchanged. Most modern open-source runtimes offer this.

### SSE (Server-Sent Events)
HTTP streaming standard the LLM world uses for streaming chat completions. The server pushes events to the client over a long-lived HTTP connection.

### Streaming
Sending partial output as it's generated rather than waiting for the full response. Implemented via SSE in OpenAI-compatible APIs. Critical UX for chat and agent visibility.

### Structured outputs
The runtime forces the model's output to match a schema (JSON Schema, regex, context-free grammar) by masking token logits at decode time. Guarantees parseable output. Often called "JSON mode" when restricted to JSON.

### Logprobs
The log-probabilities the model assigned to each output token. Useful for confidence estimation, classification, and debugging.

### Tool parser / tool calling
The runtime parses model output for tool-call syntax (which varies by model — Llama, Hermes, Mistral all use different formats) and returns structured tool-call objects to the client. Without a parser, you'd have to regex it yourself.

### Multimodal / vision
The model accepts images (and sometimes audio or video) in addition to text. Runtimes expose this via the `image_url` content field on chat completions.

## 7. Memory & state

### Short-term memory
The current conversation history — usually just the messages list in the model's context window. Lasts for the session.

### Long-term memory
Persistent state across sessions. Implementations include vector stores (semantic recall), key-value stores (facts/preferences), or knowledge graphs.

### Semantic / episodic / procedural memory (LangGraph)
A taxonomy borrowed from cognitive psychology. **Semantic**: facts the agent knows (profiles, collections). **Episodic**: prior experiences (often implemented as few-shot examples). **Procedural**: rules and how-to (often updated via reflection).

### Checkpointing
Saving agent state at execution points so a run can be resumed after a crash, restart, or user pause. LangGraph uses thread-id-scoped checkpointers; mcp-agent uses Temporal.

### Snapshot
A serialized capture of execution state, usually at a specific component or step. Haystack pipeline snapshots are JSON files; BeeAI snapshots use a `Serializable` protocol.

### State machine
A program modeled as a finite set of states with explicit transitions between them. LangGraph and pydantic-graph both use this model for agent execution; benefits include resumability and easier reasoning about behavior.

### Durable execution
A pattern where the orchestration framework persists every non-deterministic action so the workflow can be resumed exactly where it left off after any failure. Backends: Temporal, DBOS, Prefect, Restate. mcp-agent and Pydantic AI integrate these.

## 8. Observability & operations

### OpenTelemetry (OTel)
Vendor-neutral standard for telemetry data (traces, metrics, logs). Most modern agent frameworks emit OpenTelemetry traces; you configure an exporter to send them to Phoenix, Langfuse, Jaeger, Datadog, etc.

### Tracing
Recording the execution path of a request as a hierarchical tree of spans. For agents: model calls, tool calls, framework operations all appear as spans you can inspect.

### Span
A single operation in a trace, with a start time, end time, and metadata. Trace = tree of spans.

### Observability backend
Where traces are stored and visualized. Common ones: Arize Phoenix, Langfuse, LangSmith, MLflow, Weights & Biases Weave, Datadog, Jaeger.

### Sandbox
An isolated execution environment that limits what code can do. Used by code-execution MCP servers and some agent frameworks. Implementations range from process isolation (Python subprocess) to Linux containers (Docker, gVisor) to remote serverless (E2B, Modal).

## 9. Security & access

### OAuth / OAuth scope
A standard for delegated authorization. **Scopes** limit what an OAuth-authenticated token can do (e.g., "read calendar" vs "manage calendar"). MCP servers that talk to user-owned services typically use OAuth.

### API key
A static credential the application sends to a provider to authenticate. Simpler than OAuth but less granular — usually only revocable by regenerating.

### Allowlist
A list of permitted operations or destinations. The default-deny twin of a blocklist. Shell MCP servers typically need an allowlist to be safe.

### Prompt injection
An attack where malicious content in input data manipulates the model into ignoring its instructions or leaking information. Hard to defeat in general; the practical defense is to limit what the agent can do with attacker-controlled data.

### SSRF (Server-Side Request Forgery)
An attack where a server is tricked into making HTTP requests to internal addresses (e.g., cloud metadata endpoints) that the attacker shouldn't reach directly. Risk for web-fetch MCP servers.

### Sandbox escape
When code running inside a sandbox finds a way to break out and execute on the host. The reason production code-execution MCP servers use strong isolation (Docker, gVisor) rather than just `subprocess`.

## 10. Inference & decoding

### Prompt caching
The provider (or runtime) caches the server-side key-value state for a static prompt prefix and reuses it across requests. Reduces cost and latency for repeated long prefixes. Available in Anthropic, OpenAI, and some self-hosted runtimes.

### Speculative decoding
A small "draft" model proposes multiple tokens; the large target model verifies them in one parallel pass, accepting matches and resampling the first mismatch. Speeds up generation without changing the output distribution. Source: Leviathan et al. 2022.

### KV cache reuse
Reusing the cached key-value attention state for a shared prefix instead of recomputing it. Cross-request prefix sharing was formalized by PagedAttention (Kwon et al. 2023).

### Few-shot / in-context learning
Providing example input-output pairs in the prompt to teach the model the task format without any weight updates. Documented at scale by Brown et al. GPT-3 2020.
