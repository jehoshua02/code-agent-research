# Frameworks — Index

| Framework | License | Language | MCP | Programming Model | Notes |
|---|---|---|---|---|---|
| [LangGraph](langgraph.md) | MIT | Python | Via adapter (`langchain-mcp-adapters`) | Graph-based; typed `StateGraph` in Python code | JS/TS library also available |
| [AutoGen](autogen.md) | CC-BY-4.0 | Python | Native (`McpWorkbench` in `autogen-ext`) | Imperative / event-driven; layered Core / AgentChat API | In maintenance mode; successor is MS Agent Framework |
| [CrewAI](crewai.md) | MIT | Python | Native (`MCPServerTool` in `crewai-tools`) | Declarative-hybrid; agents/tasks in YAML, orchestration in Python | |
| [Letta](letta.md) | Apache-2.0 | Python | Not documented (as of Jun 2026) | Imperative / API-driven; message-passing via HTTP or SDK | Python + TypeScript SDKs; also CLI (Node.js) |
| [Smolagents](smolagents.md) | Apache-2.0 | Python | Native (`ToolCollection.from_mcp()`) | Imperative / code-first; `CodeAgent` emits Python as action language | |
| [OpenAI Swarm](openai-swarm.md) | MIT | Python | Not supported | Imperative / minimalist; `Agent` + handoff functions only | Experimental/educational; superseded by OpenAI Agents SDK |
| [LlamaIndex Agents](llamaindex-agents.md) | MIT | Python | Via adapter (`llama-index-tools-mcp`) | Imperative / compositional; `ReActAgent` or event-driven `Workflows` | |
| [Pydantic AI](pydantic-ai.md) | MIT | Python | Native (built-in `MCPServerStdio`/`MCPServerHTTP`) | Imperative / type-safe; FastAPI-style decorator pattern | |
| [Haystack Agents](haystack-agents.md) | Apache-2.0 | Python | Via companion (`Hayhooks` exposes pipelines as MCP servers) | Declarative pipeline / component graph; YAML-serializable | |
| [DSPy](dspy.md) | MIT | Python | Not supported | Declarative / program-based; `Signature` + `Module` compiled by optimizer | Unique: optimizes prompts/weights, not just executes them |
| [BeeAI](beeai.md) | Apache-2.0 | Python+TypeScript | Native (added May 2025) | Imperative / component-based; `RequirementAgent` + handoff tools | Part of Linux Foundation AI & Data |
| [Atomic Agents](atomic-agents.md) | MIT | Python | Not supported | Imperative / composable-component; typed `AtomicAgent[Input, Output]` via Instructor | Requires Python 3.12+ |
| [mcp-agent](mcp-agent.md) | Apache-2.0 | Python | Native (core design; full MCP spec) | Imperative / pattern-based; implements Anthropic's effective-agent patterns | Low activity since early 2026 |
| [agno](agno.md) | Apache-2.0 | Python | Native (bidirectional: `MCPTools` + `AgentOS` as MCP server) | Imperative / platform-oriented; `Agent` objects + `AgentOS` production runtime | 50+ provider modules; broadest model coverage listed |
