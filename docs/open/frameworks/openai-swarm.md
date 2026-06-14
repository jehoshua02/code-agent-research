# OpenAI Swarm

_Last verified: 2026-06-14_

## 1. What It Is

OpenAI Swarm is an MIT-licensed Python framework (openai/swarm) for lightweight multi-agent handoffs. Marked experimental/educational by OpenAI; the patterns have been superseded by the OpenAI Agents SDK. Still cited as a reference for the agent-handoff pattern.

## 2. Install

Python 3.10+ required; Linux, macOS, Windows supported. Not published to PyPI — install directly from GitHub:

```bash
pip install git+https://github.com/openai/swarm.git
```

**Note:** Swarm is marked experimental/educational and has been superseded by the [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) for production use.

## 3. Model Compatibility

Hardcoded to the OpenAI Chat Completions API. Any model accessible via the OpenAI Python client works (GPT-4o, GPT-4o-mini, etc.). By extension, any OpenAI-compatible endpoint (Azure OpenAI, OpenRouter via `base_url`, local vLLM/Ollama in OpenAI-compat mode) can be used by overriding the `OpenAI` client. No built-in support for non-OpenAI SDKs.

## 4. Agent Capabilities

Tool use, planning, memory, multi-agent, human-in-the-loop, state persistence.

## 5. MCP Support

Not supported. Swarm has no MCP integration. Source: [openai/swarm README](https://github.com/openai/swarm) — no MCP references found.

## 6. Programming Model

Imperative / minimalist. Logic lives entirely in Python. The two primitives are `Agent` (instructions + list of Python functions as tools) and handoffs (an agent function that returns another `Agent`). Orchestration is a stateless loop: `client.run()` cycles through completions, tool calls, and agent switches until no new tool calls remain. No graph, no config files, no decorators — just functions and `Agent` objects:

```python
from swarm import Swarm, Agent

client = Swarm()
agent_a = Agent(name="A", instructions="You help.", functions=[transfer_to_b])
agent_b = Agent(name="B", instructions="Only speak in haiku.")
response = client.run(agent=agent_a, messages=[{"role": "user", "content": "Hi"}])
```

## 7. Documented Strengths

Documented strengths from maintainer docs, benchmarks, or independent reviews. Cite source.

## 8. Documented Weaknesses

Documented limitations from issue tracker, docs, or community reports. Cite source.

## 9. Sources

- [openai/swarm](https://github.com/openai/swarm) — observed 2026-06-14
