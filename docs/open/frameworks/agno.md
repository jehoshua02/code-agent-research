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

Tool use, planning, memory, multi-agent, human-in-the-loop, state persistence.

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
