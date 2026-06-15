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

- **Fine-grained control flow.** Explicit `StateGraph` nodes and conditional edges let developers encode pause, branch, retry, and hand-off logic that pure chain-of-prompts frameworks cannot express. Source: [LangGraph overview — "low-level orchestration framework"](https://docs.langchain.com/oss/python/langgraph/overview).
- **Built-in persistence and time-travel.** Checkpointers (`SqliteSaver`, `PostgresSaver`) persist state across failures; forking and time-travel replay let developers inspect or rerun any past state snapshot. Source: [LangGraph overview — "persist through failures"](https://docs.langchain.com/oss/python/langgraph/overview).
- **Human-in-the-loop as a first-class primitive.** `interrupt(value)` and compile-time breakpoints allow inspecting and modifying agent state mid-run without external tooling. Source: [LangGraph overview — "inspect and modify agent state at any point"](https://docs.langchain.com/oss/python/langgraph/overview).
- **Deep observability via LangSmith.** Three env vars enable automatic tracing of execution paths, state transitions, and runtime metrics across all nodes. Source: [LangSmith observability — "deep visibility into complex agent behavior"](https://www.langchain.com/langsmith/observability).

## 8. Documented Weaknesses

- **Steep learning curve for newcomers.** The official docs explicitly recommend LangChain's higher-level prebuilt agents for users "just getting started," framing the `StateGraph` API as inherently complex. Source: [LangGraph overview — "just getting started with agents"](https://docs.langchain.com/oss/python/langgraph/overview).
- **Boilerplate-heavy for simple cases.** The LangGraph team's own v1 roadmap issue asks users to identify what "feels unnecessarily complex or boilerplate-heavy" around `StateGraph`, acknowledging the verbosity problem. Source: [GitHub issue #4973 — LangGraph v1 roadmap feedback](https://github.com/langchain-ai/langgraph/issues/4973).
- **Breaking changes in prebuilt layer.** `langgraph-prebuilt==1.0.2` introduced a breaking change without proper version constraints, allowing incompatible versions to install silently. Source: [GitHub issue #6363](https://github.com/langchain-ai/langgraph/issues/6363).
- **Observability requires a separate paid service.** Full tracing depends on LangSmith, which is a hosted product; there is no equivalent built-in open-source observability option for teams that cannot use external SaaS. Source: [LangSmith pricing — langchain.com](https://www.langchain.com/langsmith).

## 9. Sources

- [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) — observed 2026-06-14
