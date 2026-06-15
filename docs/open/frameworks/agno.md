# agno

_Last verified: 2026-06-14_

## 1. What It Is

Agno is an Apache-2.0 Python framework (agno-agi/agno). Active. Model-agnostic, multi-modal agent framework with built-in support for tools, structured outputs, and memory across many providers.

## 2. Install

Python >=3.7 required (3.10+ for most provider integrations); Linux, macOS, Windows supported.

```bash
pip install agno
```

Provider-specific dependencies are installed as needed per model class (e.g. `pip install anthropic` for Claude, `pip install google-genai` for Gemini). See [docs.agno.com](https://docs.agno.com) for per-provider setup.

## 3. Model Compatibility

Extremely broad — Agno has first-class provider modules (`agno.models.<provider>`) for: OpenAI, Anthropic, AWS Bedrock, Azure OpenAI, Azure AI Foundry, Cerebras, Cloudflare, Cohere, DeepInfra, DeepSeek, Fireworks, Google Gemini, Groq, HuggingFace, IBM, LiteLLM, LlamaCpp (local), LM Studio (local), Meta, Mistral, Moonshot, NVIDIA, Ollama (local), **OpenRouter**, Perplexity, SambaNova, Together AI, Vertex AI, vLLM, xAI, and more. Source: [docs.agno.com llms-full.txt provider modules](https://docs.agno.com/llms-full.txt).

## 4. Agent Capabilities

Model-agnostic, multi-modal agent framework with the broadest provider coverage. Tools are plain Python functions auto-converted to JSON Schema (docstring + `Args:` required); 120+ built-in Toolkits; per-run `RunContext` injectable; `function_calling_llm` allows a separate model. Concurrent tool exec under `arun`. Planning framed as "reasoning": Reasoning Models (e.g. extended-thinking), Reasoning Tools (scratchpad), Reasoning Agents (`reasoning=True`, ReAct loop with self-correction). Memory has two concepts — Session History (`add_history_to_context`) and User Memory (persistent facts: `update_memory_on_run=True` for auto, `enable_agentic_memory=True` for agent-driven); backends include PostgreSQL, SQLite, MongoDB. Multi-agent via `Teams` with three `TeamMode` — Route, Coordinate (default), Broadcast; nesting supported. HITL: "team runs can pause for human-in-the-loop and continue after approval"; agent-level supported. State persistence via 13+ storage backends (SQLite/PostgreSQL recommended; async variants); resumed by `session_id`. Observability: OpenTelemetry → Arize Phoenix, Langfuse, Langsmith, Logfire, Maxim, MLflow, OpenLIT, Weave, etc.; auto-instruments runs/tools/perf/errors/tokens. Retry/error handling: no dedicated retry mechanism documented; self-correction via reasoning loop. Sync (`Agent.run()`) and async (`Agent.arun()`); both with streaming via `stream=True` / `stream_events=True`. Source: docs.agno.com.

## 5. MCP Support

Native — bidirectional. Agents can consume MCP tools via `MCPTools` class; AgentOS (the runtime layer) can also expose itself as an MCP server via `enable_mcp_server=True`. MCP server lifecycle is automatically managed within AgentOS. Source: [docs.agno.com/agent-os/mcp](https://docs.agno.com/agent-os/mcp/mcp) and [docs.agno.com/tools/mcp/overview](https://docs.agno.com/tools/mcp/overview).

## 6. Programming Model

Imperative / platform-oriented. Core agent logic is written in Python using `Agent` objects instantiated with model, tools, memory, and instructions. The higher-level `AgentOS` runtime layer wraps agents/teams/workflows and exposes them as a production REST API (50+ endpoints) with SSE, scheduling, RBAC, and observability baked in. No graph DSL is required; multi-agent teams use a `Team` class with member agents. Example:

```python
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    tools=[DuckDuckGoTools()],
    instructions="Search the web to answer questions.",
)
agent.print_response("What happened in AI this week?")
```

## 7. Documented Strengths

Documented strengths from maintainer docs, benchmarks, or independent reviews. Cite source.

## 8. Documented Weaknesses

Documented limitations from issue tracker, docs, or community reports. Cite source.

## 9. Sources

- [agno-agi/agno](https://github.com/agno-agi/agno) — observed 2026-06-14
