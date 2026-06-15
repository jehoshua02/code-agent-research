# View — By Task

Stack combinations suited to each task. Each section lists relevant models, runtimes, frameworks, MCP servers, techniques, and applications as links to entity files. Authoritative content lives in those entity files.

## 1. Coding

- **Models:** [Qwen](../models/qwen.md) (Qwen2.5-Coder / Qwen3 — strong on HumanEval/LiveCodeBench), [DeepSeek](../models/deepseek.md) (R1 SWE-Verified 49.2%), [Granite](../models/granite.md) (Granite-3.3-8B HumanEval 89.7), [Phi](../models/phi.md) (Phi-4 HumanEval 82.6, fits 16 GB), [Llama](../models/llama.md) (405B HumanEval 89.0)
- **Runtimes:** [Ollama](../runtimes/ollama.md), [llama.cpp](../runtimes/llama-cpp.md), [vLLM](../runtimes/vllm.md)
- **Frameworks:** [LangGraph](../frameworks/langgraph.md), [Smolagents](../frameworks/smolagents.md) (CodeAgent emits Python), [Pydantic AI](../frameworks/pydantic-ai.md)
- **MCP servers:** [Filesystem](../mcp-servers/filesystem.md), [Shell](../mcp-servers/shell.md), [Git / GitHub](../mcp-servers/git-github.md), [Code Execution](../mcp-servers/code-execution.md)
- **Applications:** [OpenCode](../applications/opencode.md), [Aider](../applications/aider.md), [OpenHands](../applications/openhands.md), [Continue](../applications/continue.md), [SWE-agent](../applications/swe-agent.md)
- **Techniques:** [ReAct](../techniques/react.md), [Plan-and-execute](../techniques/plan-and-execute.md), [Tool use](../techniques/tool-use.md), [Reflection](../techniques/reflection.md)

## 2. Research / Web Browsing

- **Models:** [Llama](../models/llama.md) (Scout 10M context), [Command R](../models/command-r.md) (grounded generation, citation output, 256K context), [Falcon](../models/falcon.md) (H1 256K native context), [Qwen](../models/qwen.md) (128K context, tool calling), [Mistral](../models/mistral.md) (NeMo 12B 128K; strong multilingual)
- **Runtimes:** [vLLM](../runtimes/vllm.md) (long-context chunked prefill), [SGLang](../runtimes/sglang.md), [Ollama](../runtimes/ollama.md)
- **Frameworks:** [LlamaIndex Agents](../frameworks/llamaindex-agents.md) (data connectors + RAG), [LangGraph](../frameworks/langgraph.md), [Haystack Agents](../frameworks/haystack-agents.md)
- **MCP servers:** [Web Fetch](../mcp-servers/web-fetch.md), [Web Search](../mcp-servers/web-search.md), [Browser Control](../mcp-servers/browser-control.md), [Memory](../mcp-servers/memory.md)
- **Applications:** [OpenHands](../applications/openhands.md), [OpenClaw](../applications/openclaw.md), [Goose](../applications/goose.md)
- **Techniques:** [RAG](../techniques/rag.md), [ReAct](../techniques/react.md), [KV cache reuse](../techniques/kv-cache-reuse.md), [Few-shot](../techniques/few-shot.md)

## 3. Writing / Content

- **Models:** [Llama](../models/llama.md) (strong IFEval instruction following), [Gemma](../models/gemma.md) (IFEval ~90 for 4B and 27B, 140+ languages), [Mistral](../models/mistral.md) (multilingual European; efficient throughput), [Qwen](../models/qwen.md) (hybrid thinking mode for long-form), [Hermes](../models/hermes.md) (scratchpad / internal-monologue pattern)
- **Runtimes:** [Ollama](../runtimes/ollama.md), [llama.cpp](../runtimes/llama-cpp.md), [transformers](../runtimes/transformers.md)
- **Frameworks:** [LangGraph](../frameworks/langgraph.md), [CrewAI](../frameworks/crewai.md), [DSPy](../frameworks/dspy.md) (optimizes prompts for quality)
- **MCP servers:** [Filesystem](../mcp-servers/filesystem.md), [Productivity](../mcp-servers/productivity.md) (Notion, Google Docs)
- **Applications:** [OpenClaw](../applications/openclaw.md), [Open Interpreter](../applications/open-interpreter.md)
- **Techniques:** [Chain-of-thought](../techniques/chain-of-thought.md), [Reflection](../techniques/reflection.md), [Few-shot](../techniques/few-shot.md), [Self-consistency](../techniques/self-consistency.md)

## 4. Personal Automation

- **Models:** [Qwen](../models/qwen.md) (tool calling, 100+ languages), [Phi](../models/phi.md) (MIT, runs on consumer hardware), [Granite](../models/granite.md) (enterprise tool calling, 128K context), [SmolLM](../models/smollm.md) (on-device, zero cloud dependency), [Gemma](../models/gemma.md) (Gemma 4 multimodal, Apache 2.0)
- **Runtimes:** [Ollama](../runtimes/ollama.md), [llama.cpp](../runtimes/llama-cpp.md), [MLX](../runtimes/mlx.md) (Apple Silicon on-device)
- **Frameworks:** [agno](../frameworks/agno.md) (50+ provider modules, production runtime), [mcp-agent](../frameworks/mcp-agent.md) (MCP-first design), [Pydantic AI](../frameworks/pydantic-ai.md)
- **MCP servers:** [Filesystem](../mcp-servers/filesystem.md), [Shell](../mcp-servers/shell.md), [Productivity](../mcp-servers/productivity.md) (calendar, email, tasks), [Memory](../mcp-servers/memory.md)
- **Applications:** [Goose](../applications/goose.md), [OpenClaw](../applications/openclaw.md), [Open Interpreter](../applications/open-interpreter.md), [AutoGPT](../applications/autogpt.md)
- **Techniques:** [ReAct](../techniques/react.md), [Tool use](../techniques/tool-use.md), [Plan-and-execute](../techniques/plan-and-execute.md), [Prompt caching](../techniques/prompt-caching.md)

## 5. Data Analysis

- **Models:** [DeepSeek](../models/deepseek.md) (R1 strong on math + code; distill variants for consumer GPU), [Qwen](../models/qwen.md) (Qwen2.5-Coder + math variants), [Phi](../models/phi.md) (MATH 80.4 at 14B), [Granite](../models/granite.md) (MATH-500 69.0; documented data provenance), [Llama](../models/llama.md) (tool calling format)
- **Runtimes:** [vLLM](../runtimes/vllm.md), [SGLang](../runtimes/sglang.md) (structured output), [transformers](../runtimes/transformers.md)
- **Frameworks:** [LlamaIndex Agents](../frameworks/llamaindex-agents.md), [Haystack Agents](../frameworks/haystack-agents.md), [DSPy](../frameworks/dspy.md)
- **MCP servers:** [Database](../mcp-servers/database.md) (SQL / SQLite / Postgres), [Code Execution](../mcp-servers/code-execution.md), [Filesystem](../mcp-servers/filesystem.md)
- **Applications:** [Open Interpreter](../applications/open-interpreter.md), [OpenHands](../applications/openhands.md)
- **Techniques:** [Tool use](../techniques/tool-use.md), [Chain-of-thought](../techniques/chain-of-thought.md), [Constrained decoding](../techniques/constrained-decoding.md), [RAG](../techniques/rag.md)
