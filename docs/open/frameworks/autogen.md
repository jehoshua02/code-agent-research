---
name: "AutoGen"
maker: "Microsoft"
license: "CC-BY-4.0"
license_category: "custom-permissive"
status: "active"
url: "https://github.com/microsoft/autogen"
last_verified: "2026-06-14"
language: "Python"
supports_mcp: "native"
programming_model: "imperative"
best_for: ["automation", "research"]
notes: "Now in maintenance mode; Microsoft recommends new projects use Microsoft Agent Framework."
---

# AutoGen

_Last verified: 2026-06-14_

## 0. TL;DR

AutoGen is a Microsoft Python framework for building systems where multiple specialized [agents](../GLOSSARY.md#agent) collaborate by exchanging messages, optionally looping in a human. Pick it if you want to split complex tasks across agents with distinct roles and need flexible human-in-the-loop approval. The main catch is that AutoGen is now in maintenance mode — Microsoft recommends new projects use Microsoft Agent Framework instead.

## 1. What It Is

AutoGen is a CC-BY-4.0 Python framework from Microsoft (microsoft/autogen) for building multi-agent conversation systems. Active. Models problems as multiple specialized agents exchanging messages, with optional human-in-the-loop.

## 2. Install

Python 3.10+ required; Linux, macOS, Windows supported.

**Note:** AutoGen is now in maintenance mode. Microsoft recommends new projects use [Microsoft Agent Framework](https://github.com/microsoft/agent-framework). Existing AutoGen users can continue with the packages below.

```bash
# AgentChat + OpenAI extension
pip install -U "autogen-agentchat" "autogen-ext[openai]"

# Optional: no-code GUI
pip install -U autogenstudio
```

Extras: `autogen-ext[azure]`, `autogen-ext[anthropic]`, `autogen-ext[ollama]`, etc.

## 3. Model Compatibility

Supports any OpenAI-compatible endpoint plus provider-specific extensions. First-party extensions in `autogen-ext` cover: OpenAI, Azure OpenAI, Anthropic, Ollama (local), Google Gemini, AWS Bedrock, Mistral, and vLLM (via OpenAI-compat). OpenRouter is reachable via the OpenAI client pointed at `https://openrouter.ai/api/v1`. Source: [AutoGen models docs](https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/tutorial/models.html).

## 4. Agent Capabilities

Conversation-driven multi-agent framework. Tools are plain Python (sync or async) functions on `AssistantAgent`; auto-converted to schemas; v0.4+ executes inline in `run()`. Planning emerges from team architecture: `SelectorGroupChat` uses LLM-driven speaker selection, `MagenticOneGroupChat` has dual-loop Task/Progress Ledger orchestration, `GraphFlow` for directed-graph workflows. Memory via `Memory` protocol: `ListMemory`, `ChromaDBVectorMemory`, `RedisMemory`, `Mem0Memory`; RAG-aware. Multi-agent: `RoundRobinGroupChat`, `SelectorGroupChat`, `MagenticOneGroupChat`, `Swarm` (`HandoffMessage`). HITL via `UserProxyAgent` (blocks team) or between-runs (max_turns=1 pattern). State: `save_state()`/`load_state()` JSON-serializable. Observability via OpenTelemetry (`opentelemetry-instrumentation-openai`). Retry: tool-level error signaling via `is_error`; orchestrator-level recovery in MagenticOne. Both sync (`.run()`) and async streaming (`.run_stream()`). Source: microsoft.github.io/autogen.
## 5. MCP Support

Native — built into `autogen-ext` via `McpWorkbench` and `StdioServerParams`. Connect to any MCP server (stdio or SSE) and expose its tools directly to agents. Multiple MCP servers can be combined in a list. Source: [AutoGen README MCP example](https://github.com/microsoft/autogen#mcp-server).

```python
from autogen_ext.tools.mcp import McpWorkbench, StdioServerParams
async with McpWorkbench(server_params) as mcp:
    agent = AssistantAgent("agent", model_client=client, workbench=mcp)
```

## 6. Programming Model

Imperative / event-driven. Logic lives in Python code using the layered API: Core (message passing, distributed runtime), AgentChat (opinionated high-level agents and teams), Extensions (provider integrations). Agents are defined by subclassing or instantiating `AssistantAgent`, wired into teams (`RoundRobinGroupChat`, `SelectorGroupChat`) or direct handoffs. Control flow is explicit Python; no separate config files required (though AutoGen Studio offers a no-code GUI). Example:

```python
from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient

agent = AssistantAgent("helper", model_client=OpenAIChatCompletionClient(model="gpt-4o"))
result = await agent.run(task="Summarize the news.")
```

## 7. Documented Strengths

- **Flexible multi-agent team topologies.** `RoundRobinGroupChat`, `SelectorGroupChat`, and `MagenticOneGroupChat` provide distinct collaboration patterns out of the box, with `GraphFlow` for directed-graph workflows. Source: [AutoGen AgentChat docs](https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/).
- **MagenticOne competitive on agentic benchmarks.** The Orchestrator + specialist agent system achieves "statistically competitive performance to the state-of-the-art" on GAIA, AssistantBench, and WebArena. Source: [Microsoft Research — Magentic-One paper (arXiv:2411.04468)](https://arxiv.org/abs/2411.04468).
- **Human-in-the-loop as a first-class citizen.** `UserProxyAgent` can block the team for human approval at any turn; `max_turns=1` pattern supports between-run review. Source: [AutoGen AgentChat tutorial](https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/tutorial/).
- **Native MCP support.** `McpWorkbench` in `autogen-ext` connects directly to any stdio or SSE MCP server without third-party adapters. Source: [AutoGen README MCP example](https://github.com/microsoft/autogen#mcp-server).

## 8. Documented Weaknesses

- **Officially in maintenance mode.** Microsoft confirmed AutoGen will receive only bug fixes and security patches; no new features or performance improvements are planned. New projects are directed to Microsoft Agent Framework. Source: [AI DEV DAY — "Is AutoGen Deprecated?"](https://aidevdayindia.org/blogs/ai-agent-framework-decision-matrix/is-autogen-deprecated-maintenance-mode-microsoft.html).
- **Unpredictable loops in production.** The "agents having a conversation" pattern is noted to "work great in demos but create unpredictable, hard-to-debug loops in production." Source: [buildmvpfast.com — LangGraph vs CrewAI vs AutoGen comparison 2026](https://www.buildmvpfast.com/blog/langgraph-vs-crewai-vs-autogen-vs-swarms-agent-framework-2026).
- **No native observability standard.** Observability depends on OpenTelemetry instrumentation rather than a first-party tracing product; the framework will not receive updates to support emerging tool standards. Source: [AI DEV DAY — maintenance mode analysis](https://aidevdayindia.org/blogs/ai-agent-framework-decision-matrix/is-autogen-deprecated-maintenance-mode-microsoft.html).
- **Community fragmentation.** The AG2 community fork was created to continue feature development after Microsoft halted it, meaning the ecosystem is now split between two incompatible paths. Source: [AI DEV DAY — maintenance mode analysis](https://aidevdayindia.org/blogs/ai-agent-framework-decision-matrix/is-autogen-deprecated-maintenance-mode-microsoft.html).

## 9. Sources

- [microsoft/autogen](https://github.com/microsoft/autogen) — observed 2026-06-14
