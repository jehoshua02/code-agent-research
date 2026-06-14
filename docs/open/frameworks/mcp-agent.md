# mcp-agent

_Last verified: 2026-06-14_

## 1. What It Is

mcp-agent is an Apache-2.0 Python framework from LastMile AI (lastmile-ai/mcp-agent). Low activity since early 2026. Minimal framework specifically for building MCP-native agents with patterns like augmented LLMs and orchestrator-workers.

## 2. Install

Python 3.10+ required; Linux, macOS, Windows supported. Recommended via [uv](https://docs.astral.sh/uv/):

```bash
uv add "mcp-agent"
# Or: pip install mcp-agent
```

Provider-specific extras:

```bash
pip install "mcp-agent[openai]"     # OpenAI
pip install "mcp-agent[anthropic]"  # Anthropic
```

Scaffold a project with the CLI:

```bash
uvx mcp-agent init
```

## 3. Model Compatibility

Supports multiple LLM providers via purpose-built `AugmentedLLM` wrappers: `OpenAIAugmentedLLM`, `AnthropicAugmentedLLM`, and others in `mcp_agent.workflows.llm`. Any OpenAI-compatible endpoint (including OpenRouter, Ollama, vLLM) can be used via the OpenAI wrapper with a custom `base_url`. Source: [mcp-agent README](https://github.com/lastmile-ai/mcp-agent).

## 4. Agent Capabilities

Tool use, planning, memory, multi-agent, human-in-the-loop, state persistence.

## 5. MCP Support

Native — MCP is the core design premise. mcp-agent fully implements MCP (tools, resources, prompts, notifications, OAuth, sampling, elicitation, roots). Handles MCP server lifecycle management automatically. Agents can also be exposed as MCP servers. Source: [mcp-agent README](https://github.com/lastmile-ai/mcp-agent#full-mcp-support).

## 6. Programming Model

Imperative / pattern-based. Logic lives in Python code. The framework implements each of Anthropic's "Building Effective Agents" patterns (augmented LLM, orchestrator-workers, evaluator-optimizer, router, map-reduce) as composable building blocks. An `MCPApp` context manages server connections; agents are wired with `Agent(server_names=[...])` then attached to an LLM. Optional Temporal backend for durable execution with no API changes. Example:

```python
from mcp_agent.app import MCPApp
from mcp_agent.agents.agent import Agent
from mcp_agent.workflows.llm.augmented_llm_openai import OpenAIAugmentedLLM

app = MCPApp(name="demo")
async with app.run():
    agent = Agent(name="finder", instruction="Use tools to answer.", server_names=["filesystem"])
    async with agent:
        llm = await agent.attach_llm(OpenAIAugmentedLLM)
        result = await llm.generate_str("Summarize README.md in two sentences.")
```

## 7. Documented Strengths

Documented strengths from maintainer docs, benchmarks, or independent reviews. Cite source.

## 8. Documented Weaknesses

Documented limitations from issue tracker, docs, or community reports. Cite source.

## 9. Sources

- [lastmile-ai/mcp-agent](https://github.com/lastmile-ai/mcp-agent) — observed 2026-06-14
