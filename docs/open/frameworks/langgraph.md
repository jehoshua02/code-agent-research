# LangGraph

_Last verified: 2026-06-14_

## 0. TL;DR

LangGraph is a Python library for building agents as graphs of nodes and edges, where each node is a step in the [workflow](../GLOSSARY.md#workflow) and edges encode control flow. Pick it if you want fine-grained control over the agent loop — pause, branch, retry, or hand off between agents — plus built-in observability through LangSmith. The main catch is a steeper learning curve: you think in graph state machines, not in straightforward imperative scripts.

## 1. What It Is

LangGraph is an MIT-licensed Python framework from LangChain (langchain-ai/langgraph) for building stateful agent workflows as graphs of nodes and edges. Active development. Takes a graph-state-machine approach distinct from chain-of-prompts or imperative loops.

## 2. Install

Python 3.10+ required; Linux, macOS, Windows all supported. Also available as a JavaScript/TypeScript library (`langgraph` on npm).

```bash
pip install -U langgraph
```

For JS/TS:

```bash
npm install @langchain/langgraph
```

No mandatory extras for core use; LLM provider packages (e.g. `langchain-openai`, `langchain-anthropic`) are installed separately as needed.

## 3. Model Compatibility

LangGraph is model-agnostic and delegates inference to LangChain integration packages. Any provider with a LangChain integration works: OpenAI, Anthropic, Google Gemini, Mistral, Cohere, AWS Bedrock, Azure OpenAI, Ollama (local), Hugging Face Inference, vLLM (via OpenAI-compat endpoint), and OpenRouter (via `langchain-openai` pointed at `https://openrouter.ai/api/v1`). Source: [LangChain integrations hub](https://python.langchain.com/docs/integrations/llms/).

## 4. Agent Capabilities

Graph-based agent execution. Tools are `@tool`-decorated Python callables; `ToolNode` executes them within graph nodes; `ToolRuntime` injects state/context/store/stream-writer/retry-info. Planning is the graph itself (nodes + edges); the Deep Agents harness adds a `write_todos` tool. Memory: short-term via checkpointers scoped to `thread_id`; long-term via `BaseStore` with semantic/episodic/procedural types. Multi-agent via subgraphs and Deep Agents' `task` tool (sync + async subagents). Human-in-the-loop via `interrupt(value)` and compile-time/runtime breakpoints; resume with `Command(resume=value)`. State persistence: checkpointers — `InMemorySaver`, `SqliteSaver`, `PostgresSaver`, `CosmosDBSaver`; time-travel and forking supported. Observability: automatic LangSmith tracing via three env vars (`LANGSMITH_TRACING`, `LANGSMITH_API_KEY`, `LANGSMITH_PROJECT`). Retry: `ModelRetryMiddleware`, `ToolRetryMiddleware`, `@wrap_tool_call`. Both sync (`.invoke`/`.stream`) and async (`.ainvoke`/`.astream`/`.abatch`) throughout. Source: docs.langchain.com/oss/python/langgraph/overview.
## 5. MCP Support

Via adapter — the `langchain-mcp-adapters` package (v0.3.0+) wraps MCP servers and exposes their tools as LangChain tools usable in LangGraph agents. Install:

```bash
pip install langchain-mcp-adapters
```

Source: [langchain-ai/langchain-mcp-adapters README](https://github.com/langchain-ai/langchain-mcp-adapters).

## 6. Programming Model

Graph-based. Developers define a `StateGraph` in Python code: nodes are Python functions or runnables, edges are conditional or unconditional transitions, and a shared typed `State` object flows between them. Logic lives entirely in code; there is no separate config layer. Compile the graph with `.compile()` then invoke it. Example sketch:

```python
from langgraph.graph import StateGraph, END
from typing import TypedDict

class State(TypedDict):
    messages: list

graph = StateGraph(State)
graph.add_node("agent", call_model)
graph.add_node("tools", call_tools)
graph.add_edge("agent", "tools")
graph.add_edge("tools", END)
app = graph.compile()
```

## 7. Documented Strengths

Documented strengths from maintainer docs, benchmarks, or independent reviews. Cite source.

## 8. Documented Weaknesses

Documented limitations from issue tracker, docs, or community reports. Cite source.

## 9. Sources

- [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) — observed 2026-06-14
