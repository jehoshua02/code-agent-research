# BeeAI

_Last verified: 2026-06-14_

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

Tool use, planning, memory, multi-agent, human-in-the-loop, state persistence.

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

Documented strengths from maintainer docs, benchmarks, or independent reviews. Cite source.

## 8. Documented Weaknesses

Documented limitations from issue tracker, docs, or community reports. Cite source.

## 9. Sources

- [i-am-bee/beeai-framework](https://github.com/i-am-bee/beeai-framework) — observed 2026-06-14
