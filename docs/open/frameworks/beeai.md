---
name: "BeeAI"
maker: "IBM Research"
license: "Apache-2.0"
license_category: "apache-2.0"
status: "active"
url: "https://github.com/i-am-bee/beeai-framework"
last_verified: "2026-06-14"
language: "Python"
supports_mcp: "native"
programming_model: "imperative"
best_for: ["automation", "research", "coding"]
notes: "Dual Python+TypeScript SDKs; constraint-based RequirementAgent; Linux Foundation governance."
---

# BeeAI

_Last verified: 2026-06-14_

## 0. TL;DR

BeeAI is an IBM Research-originated Python and TypeScript framework for production-ready agents, with a unified `ChatModel` abstraction that works across Ollama, OpenAI, Anthropic, watsonx, and more. Pick it if you need both Python and TypeScript SDKs from a single framework or want production-oriented defaults (structured outputs, error handling, observability) out of the box. The main catch is that it's less widely adopted than LangGraph or CrewAI, so community resources and third-party tutorials are thinner.

## 1. What It Is

BeeAI is an Apache-2.0 Python and TypeScript framework (i-am-bee/beeai-framework), originally from IBM Research. Active. Provides production-oriented agent components with both Python and TypeScript SDKs.

## 2. Install

**Python** (requires Python >=3.11, <3.14):

```bash
pip install beeai-framework
```

**TypeScript/Node.js**:

```bash
npm install beeai-framework
```

Linux, macOS, Windows supported. Starter templates available: [beeai-framework-py-starter](https://github.com/i-am-bee/beeai-framework-py-starter) and [beeai-framework-ts-starter](https://github.com/i-am-bee/beeai-framework-ts-starter).

## 3. Model Compatibility

Model-agnostic via a unified `ChatModel` backend abstraction (`ChatModel.from_name("provider:model")`). Supported backends include Ollama, IBM watsonx, OpenAI, Anthropic, Google Gemini, AWS Bedrock, Azure, Groq, and any OpenAI-compatible endpoint. The README example uses `ollama:granite3.3:8b` directly. Source: [BeeAI framework README](https://github.com/i-am-bee/beeai-framework) and [backend docs](https://framework.beeai.dev/modules/backend#supported-providers).

## 4. Agent Capabilities

IBM-backed agent framework (Python + TypeScript). Tools via `@tool` decorator or class extending `Tool` with `input_schema` (Pydantic) and async `_run`; outputs `StringToolOutput`/`JSONToolOutput`; built-in includes DuckDuckGo, Wikipedia, Grep, OpenMeteo, Python/Shell exec, file ops, OpenAPI, MCP adapter. Planning: `RequirementAgent` is recommended — constraint-based via `ConditionalRequirement` (`force_at_step`, `min/max_invocations`, `consecutive_allowed`, `priority`, `custom_checks`); legacy `ReActAgent` does Thought/Action/Observation; `LiteAgent` minimal; `ToolCallChecker` breaks infinite loops. Memory implementations: `UnconstrainedMemory`, `SlidingMemory`, `TokenMemory`, `SummarizeMemory`; snapshots via `create_snapshot`/`load_snapshot`. Multi-agent via `HandoffTool` (transfer execution) and `AgentWorkflow` (sequential/parallel pipelines); workflow steps return `NEXT`/`SELF`/`END`; A2A and ACP integrations. HITL: `AskPermissionRequirement` gates tools (`include`/`exclude`/`remember_choices`/`hide_disallowed`/custom handler). State: `Serializable` protocol with `createSnapshot`/`loadSnapshot`; serializes memory, agents, tools, custom classes. Observability via OpenTelemetry (`openinference-instrumentation-beeai`) → Phoenix/Langfuse/Langsmith; `GlobalTrajectoryMiddleware` captures all events; `Emitter` for event-driven hooks. Retry: agent options `max_iterations`, `total_max_retries`, `max_retries_per_step`; recoverable tool error hints; `FrameworkError` hierarchy. Async-first throughout; tools, requirements, agents all async; no documented sync wrappers. Source: framework.beeai.dev.

## 5. MCP Support

Native — as of May 2025, BeeAI added native MCP integration. Agents can expose themselves as MCP servers and consume MCP tools. Also supports A2A protocol. Source: [BeeAI README changelog, 2025-05-15](https://github.com/i-am-bee/beeai-framework); [MCP integration docs](https://framework.beeai.dev/integrations/mcp).

## 6. Programming Model

Imperative / component-based. Logic lives in Python (or TypeScript) code. Agents are instantiated with an LLM backend, tools, memory, and optional middleware. The `RequirementAgent` pattern lets developers set behavioral rules (e.g. "always use ThinkTool first"). Multi-agent handoffs are done via `HandoffTool`. No separate config files; all wiring is in Python. Example:

```python
from beeai_framework.agents.requirement import RequirementAgent
from beeai_framework.backend import ChatModel
from beeai_framework.tools.search.wikipedia import WikipediaTool

agent = RequirementAgent(
    llm=ChatModel.from_name("ollama:granite3.3:8b"),
    tools=[WikipediaTool()],
    role="Researcher",
    instructions="Answer general questions.",
)
response = await agent.run("Who built the Eiffel Tower?")
```

## 7. Documented Strengths

- **Dual-SDK (Python + TypeScript) from one framework**: Both SDKs share the same abstractions and `ChatModel.from_name()` pattern, cutting dual-stack maintenance burden. Docs: [framework.beeai.dev](https://framework.beeai.dev/).
- **OpenInference/OTel observability built in**: `openinference-instrumentation-beeai` emits traces to Phoenix, Langfuse, or Langsmith; `GlobalTrajectoryMiddleware` captures every agent event. Docs: [framework.beeai.dev/observability](https://framework.beeai.dev/); [IBM think](https://www.ibm.com/think/topics/beeai).
- **Linux Foundation open governance**: Transferred from IBM Research to the Linux Foundation; enterprise-grade stability guarantees and community governance model. Source: [ibm.com/think/news/beeai-open-source-multiagent](https://www.ibm.com/think/news/beeai-open-source-multiagent).
- **Four built-in memory strategies**: `UnconstrainedMemory`, `SlidingMemory`, `TokenMemory`, and `SummarizeMemory` cover common production trade-offs without custom code. Docs: [framework.beeai.dev](https://framework.beeai.dev/).

## 8. Documented Weaknesses

- **Thin community and ecosystem**: Fewer third-party tutorials, integrations, and Stack Overflow answers than LangGraph or CrewAI; noted in comparative overviews. Source: [ibm.com/think/topics/beeai](https://www.ibm.com/think/topics/beeai).
- **Open CVEs in dependency tree**: Multiple unresolved CVEs (including PyTorch RCE CVE-2025-32434) and outdated LangChain dependencies flagged in open issue tracker. [github.com/i-am-bee/beeai-framework/issues](https://github.com/i-am-bee/beeai-framework/issues).
- **Async-only Python API**: No documented sync wrappers; forces async-all-the-way for callers that don't already use asyncio. Docs: [framework.beeai.dev](https://framework.beeai.dev/).
- **Multimodal tool outputs not yet supported**: Image/file output from tools is an open feature request, limiting vision-heavy workflows. [github.com/i-am-bee/beeai-framework/issues](https://github.com/i-am-bee/beeai-framework/issues).

## 9. Sources

- [i-am-bee/beeai-framework](https://github.com/i-am-bee/beeai-framework) — observed 2026-06-14
