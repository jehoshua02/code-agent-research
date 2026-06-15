# View — By Layer

Opinionated top picks at each stack layer, with one-line characterization. For the full list, see each layer's `INDEX.md`. Applications are not a layer (they consume the stack) — see [../applications/INDEX.md](../applications/INDEX.md).

## 1. Models

- [Llama](../models/llama.md) — broadest ecosystem support; more community quants, tutorials, and runtime integrations than any other family.
- [Qwen](../models/qwen.md) — Apache 2.0, no gating, strong coding and math; one of the few frontier-quality families with zero commercial restrictions.
- [DeepSeek](../models/deepseek.md) — R1 distill variants bring frontier-level reasoning (AIME 79.8) to consumer hardware at 7B–32B.
- [Mistral](../models/mistral.md) — efficient at size (Small 3.1 24B beats Llama 70B throughput); mature tool-calling format; Apache 2.0 for most variants.
- [Phi](../models/phi.md) — MIT license, no gating; Phi-4 14B beats GPT-4o on MATH and GPQA, fits on a single 16 GB GPU at Q4.

_See [../models/INDEX.md](../models/INDEX.md) for the full list._

## 2. Runtimes

- [Ollama](../runtimes/ollama.md) — easiest local setup; one command to pull and run any GGUF model; OpenAI-compatible API out of the box.
- [llama.cpp](../runtimes/llama-cpp.md) — broadest hardware support (CUDA, Metal, ROCm, Vulkan, CPU); upstream of Ollama, KoboldCpp, and llamafile.
- [vLLM](../runtimes/vllm.md) — highest throughput for GPU serving; PagedAttention; de facto production choice for multi-user or batch workloads.
- [SGLang](../runtimes/sglang.md) — vLLM-class throughput with built-in constrained/structured output generation; recommended by DeepSeek and Qwen model cards.
- [transformers](../runtimes/transformers.md) — canonical reference library; broadest model architecture support; needed for fine-tuning and custom pipelines.

_See [../runtimes/INDEX.md](../runtimes/INDEX.md) for the full list._

## 3. Frameworks

- [LangGraph](../frameworks/langgraph.md) — graph-based state machines; most adopted for production agentic workflows with complex branching and human-in-the-loop.
- [CrewAI](../frameworks/crewai.md) — declarative multi-agent teams in YAML; low boilerplate for role-based collaborative agents; native MCP support.
- [Pydantic AI](../frameworks/pydantic-ai.md) — type-safe FastAPI-style agent design; built-in MCP; best fit for Python developers who want validated structured outputs.
- [Smolagents](../frameworks/smolagents.md) — HuggingFace's minimalist code-first agent; `CodeAgent` emits Python as the action language; native MCP.
- [LlamaIndex Agents](../frameworks/llamaindex-agents.md) — strong RAG + agent integration; `ReActAgent` or event-driven `Workflows`; large ecosystem of data connectors.

_See [../frameworks/INDEX.md](../frameworks/INDEX.md) for the full list._

## 4. MCP Servers

- [Filesystem](../mcp-servers/filesystem.md) — read/write/search files; the most commonly needed server for any local agent task.
- [Shell](../mcp-servers/shell.md) — run arbitrary shell commands; unlocks code execution, build tools, and system automation.
- [Git / GitHub](../mcp-servers/git-github.md) — git operations and GitHub API; essential for agentic coding and PR workflows.
- [Web Fetch](../mcp-servers/web-fetch.md) — fetch URLs and convert to markdown; Anthropic reference implementation; key for research tasks.
- [Web Search](../mcp-servers/web-search.md) — search engine API access (Brave, Exa, Tavily); pairs with Web Fetch for iterative web research.

_See [../mcp-servers/INDEX.md](../mcp-servers/INDEX.md) for the full list._

## 5. Techniques

- [ReAct](../techniques/react.md) — interleave reasoning and tool calls in a loop; the dominant pattern for multi-step agentic tasks.
- [RAG](../techniques/rag.md) — retrieval-augmented generation; essential for grounding models in private or current knowledge.
- [Tool use / function calling](../techniques/tool-use.md) — structured schema for model-to-tool invocation; required for any agent that takes real actions.
- [Chain-of-thought](../techniques/chain-of-thought.md) — prompt models to show intermediate steps; large accuracy gains on math, code, and logic.
- [Reflection](../techniques/reflection.md) — agent critiques and revises its own output; most effective for code generation with a verifiable test signal.

_See [../techniques/INDEX.md](../techniques/INDEX.md) for the full list._
