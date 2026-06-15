# Frameworks — Index

| Framework | License | Language | MCP | Programming Model | Notes |
|---|---|---|---|---|---|
| [agno](agno.md) | Apache-2.0 | Python | native | imperative | Broadest provider coverage (30+); bidirectional MCP; AgentOS runtime exposes REST API with RBAC. |
| [Atomic Agents](atomic-agents.md) | MIT | Python | none | composable | Single-responsibility AtomicAgent components chained via Pydantic schema matching; built on Instructor. |
| [AutoGen](autogen.md) | CC-BY-4.0 | Python | native | imperative | Now in maintenance mode; Microsoft recommends new projects use Microsoft Agent Framework. |
| [BeeAI](beeai.md) | Apache-2.0 | Python | native | imperative | Dual Python+TypeScript SDKs; constraint-based RequirementAgent; Linux Foundation governance. |
| [CrewAI](crewai.md) | MIT | Python | native | role-based | YAML/Python hybrid config; LLM routing via LiteLLM (100+ providers). |
| [DSPy](dspy.md) | MIT | Python | none | declarative | Prompt-as-program paradigm; optimizer (MIPROv2, SIMBA) compiles typed Signatures into tuned prompts. |
| [Haystack Agents](haystack-agents.md) | Apache-2.0 | Python | adapter | declarative | Agents are Components in a Haystack Pipeline graph; MCP via Hayhooks companion tool. |
| [LangGraph](langgraph.md) | MIT | Python | adapter | graph | MCP via langchain-mcp-adapters; also available as a JS/TS npm package. |
| [Letta](letta.md) | Apache-2.0 | Python | none | imperative | Formerly MemGPT; requires a Letta Cloud or self-hosted server — no simple library mode. |
| [LlamaIndex Agents](llamaindex-agents.md) | MIT | Python | adapter | composable | MCP via llama-index-tools-mcp; strongest when paired with LlamaIndex's RAG and indexing ecosystem. |
| [mcp-agent](mcp-agent.md) | Apache-2.0 | Python | native | imperative | Low activity since early 2026; last commit January 25, 2026 — long-term maintenance uncertain. |
| [OpenAI Swarm](openai-swarm.md) | MIT | Python | none | imperative | Superseded by the OpenAI Agents SDK; retained as an educational reference for the handoff pattern. |
| [Pydantic AI](pydantic-ai.md) | MIT | Python | native | imperative | Type-safe agent generics with FastAPI-style decorators; deep Logfire/OTel observability built in. |
| [Smolagents](smolagents.md) | Apache-2.0 | Python | native | code-emitting | CodeAgent emits Python as tool calls; sandbox (e2b/Docker) required in production. |
