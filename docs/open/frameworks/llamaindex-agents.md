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

Documented strengths from maintainer docs, benchmarks, or independent reviews. Cite source.

## 8. Documented Weaknesses

Documented limitations from issue tracker, docs, or community reports. Cite source.

## 9. Sources

- [run-llama/llama_index](https://github.com/run-llama/llama_index) — observed 2026-06-14
