---
name: "LlamaIndex Agents"
maker: "LlamaIndex"
license: "MIT"
license_category: "mit"
status: "active"
url: "https://github.com/run-llama/llama_index"
last_verified: "2026-06-14"
language: "Python"
supports_mcp: "adapter"
programming_model: "composable"
best_for: ["research", "data", "automation"]
notes: "MCP via llama-index-tools-mcp; strongest when paired with LlamaIndex's RAG and indexing ecosystem."
---

# LlamaIndex Agents

_Last verified: 2026-06-14_

## 0. TL;DR

LlamaIndex Agents is the agentic layer of LlamaIndex — a Python framework that lets agents query, retrieve, and reason over your data using LlamaIndex's rich indexing and [RAG](../GLOSSARY.md#rag-retrieval-augmented-generation) primitives. Pick it if your agent's primary job is answering questions over documents, databases, or APIs and you're already using or considering LlamaIndex for data ingestion. The main catch is that it's most powerful when combined with LlamaIndex's data ecosystem; using it purely for general agent tasks adds unnecessary complexity.

## 1. What It Is

LlamaIndex Agents is the agent component of LlamaIndex (run-llama/llama_index, MIT, Python). Active. Built around data-aware agents that compose retrieval, tools, and reasoning over LlamaIndex's retrieval and indexing primitives.

## 2. Install

Python 3.10+ required; Linux, macOS, Windows supported. Install core plus integration packages as needed:

```bash
# Starter bundle (core + common integrations including OpenAI)
pip install llama-index

# Lean core + cherry-pick integrations
pip install llama-index-core
pip install llama-index-llms-openai      # OpenAI
pip install llama-index-llms-ollama      # Ollama
pip install llama-index-embeddings-huggingface
```

300+ integration packages are available on [LlamaHub](https://llamahub.ai/).

## 3. Model Compatibility

Broad via a plugin integration system. First-party packages cover: OpenAI, Anthropic, Google Gemini, Mistral, Cohere, AWS Bedrock, Azure OpenAI, Hugging Face (local transformers and Inference API), Ollama, vLLM (OpenAI-compat), Groq, and many others. OpenRouter is reachable via the `llama-index-llms-openai` package pointed at `https://openrouter.ai/api/v1`. Source: [LlamaHub integrations](https://llamahub.ai/).

## 4. Agent Capabilities

Agent component of LlamaIndex, data-aware. Three agent types: `FunctionAgent` (native function-calling), `ReActAgent` (ReAct prompting), `CodeActAgent` (code execution). Tools as `FunctionTool` (Python), `QueryEngineTool` (query engine), Tool Specs (pre-built collections); passed as `tools=[...]`. Planning per-agent-type; multi-step via Workflows (event-driven, `@step` decorator). Memory: `Memory` class (replaces deprecated `ChatMemoryBuffer`) with `token_limit` (30k default) and `chat_history_token_ratio` (0.7); `MemoryBlock` types — `StaticMemoryBlock`, `FactExtractionMemoryBlock`, `VectorMemoryBlock`; persistence via SQLite by default, PostgreSQL supported. Multi-agent via `AgentWorkflow` (with `can_handoff_to`), orchestrator + sub-agents as tools, or custom `Workflow` planner. HITL: `ctx.wait_for_event(HumanResponseEvent, ...)` pauses; resume via `ctx.send_event(HumanResponseEvent(...))`. State via `WorkflowCheckpointer` and DBOS Durable Execution integration. Observability: `set_global_handler("arize_phoenix")` or instrumentation module (v0.10.20+); integrations include MLflow, Langfuse, SigNoz, OpenTelemetry, Weave, etc. Retry: `error_on_no_tool_call=False`, workflow `retry_steps`. Async-first throughout; sync requires `asyncio.run()`. Source: developers.llamaindex.ai.

## 5. MCP Support

Via adapter — `llama-index-tools-mcp` package integrates MCP servers as LlamaIndex tool specs. Source: [PyPI llama-index-tools-mcp](https://pypi.org/project/llama-index-tools-mcp/).

## 6. Programming Model

Imperative / compositional. Agents are built in Python by composing retrieval indices, tool specs, and LLM settings. Two main paradigms: (1) classic `ReActAgent` / `FunctionCallingAgent` that loop over tool calls; (2) newer `Workflows` (event-driven, async state machines using decorators). Logic lives in Python code; there is no separate config layer. Example:

```python
from llama_index.core.agent import ReActAgent
from llama_index.core.tools import FunctionTool
from llama_index.llms.openai import OpenAI

tool = FunctionTool.from_defaults(fn=my_func)
agent = ReActAgent.from_tools([tool], llm=OpenAI(model="gpt-4o"), verbose=True)
agent.chat("What is 2+2?")
```

## 7. Documented Strengths

- **RAG as a first-class agent primitive.** `QueryEngineTool` wraps any index or retrieval pipeline as a tool; agents can cite sources, run semantic search, and chain retrieval steps without external glue. Source: [sider.ai — LlamaIndex Review 2025](https://sider.ai/blog/ai-tools/llamaindex-review-2025-is-it-the-best-rag-framework-for-production-ai).
- **300+ integrations via LlamaHub.** Data loaders, LLM providers, embedding models, and vector stores are available as drop-in packages, making it straightforward to connect any data source to an agent. Source: [LlamaHub](https://llamahub.ai/).
- **Built-in RAG-aware evaluation.** Answer correctness, context faithfulness, hallucination detection, and grounding scores are available out of the box — rare in agent frameworks. Source: [sider.ai — LlamaIndex Review 2025](https://sider.ai/blog/ai-tools/llamaindex-review-2025-is-it-the-best-rag-framework-for-production-ai).
- **Event-driven Workflows for complex orchestration.** `Workflow` with `@step` decorators and `wait_for_event` provides async multi-agent pipelines with human-in-the-loop pause/resume without requiring a graph abstraction library. Source: [LlamaIndex docs — Workflows](https://docs.llamaindex.ai/en/stable/module_guides/workflow/).

## 8. Documented Weaknesses

- **Memory is session-scoped by default.** The `Memory` class holds conversation history only while the agent runs; context is lost on restart, making multi-session continuity a gap for repeat-user applications. Source: [vectorize.io Hindsight — Teaching the Llama to Remember](https://hindsight.vectorize.io/blog/2026/03/30/llamaindex-agent-memory).
- **Fewer pre-built agent tools than LangChain.** LlamaIndex "does not come with as many pre-baked agent personas or chains," requiring developers to construct tool logic from lower-level components. Source: [ZenML — LlamaIndex vs LangChain](https://www.zenml.io/blog/llamaindex-vs-langchain).
- **No first-party evaluation/observability dashboard.** LlamaIndex "doesn't (yet) have a full evaluation suite like LangSmith," requiring integration with third-party tools (Arize Phoenix, Langfuse, MLflow) for production monitoring. Source: [ZenML — LlamaIndex vs LangChain](https://www.zenml.io/blog/llamaindex-vs-langchain).
- **Overkill for non-retrieval agent tasks.** The RAG-centric design adds unnecessary complexity when agents don't need document indexing; reviewers note it is best reserved for "data-aware LLM applications" rather than general orchestration. Source: [ZenML — LlamaIndex vs LangChain](https://www.zenml.io/blog/llamaindex-vs-langchain).

## 9. Sources

- [run-llama/llama_index](https://github.com/run-llama/llama_index) — observed 2026-06-14
