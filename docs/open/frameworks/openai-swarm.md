# OpenAI Swarm

_Last verified: 2026-06-14_

## 0. TL;DR

OpenAI Swarm is a tiny, now-deprecated Python library that demonstrated how [agents](../GLOSSARY.md#agent) can hand off control to one another using plain function returns — useful for learning the handoff pattern. Do not pick it for production; OpenAI itself replaced it with the OpenAI Agents SDK. Its value today is as a readable, ~300-line reference for understanding agent handoffs, not as a foundation to build on.

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

**Deprecated.** Educational/experimental; the README states it has been superseded by the OpenAI Agents SDK (openai-agents-python). Tools: plain Python functions auto-converted to Chat Completions schemas; can return strings, `Agent` (handoff), or `Result` (value + agent + context-vars). Planning: simple loop, no planning module; reasoning lives in `instructions`. Memory: stateless between `client.run()` calls; developer must persist `response.messages` / `response.agent` / `response.context_variables`. Multi-agent via explicit handoffs returning an `Agent`. HITL via `run_demo_loop` REPL utility; no built-in approval workflow. State persistence: none — developer manages. Observability: `debug=True`, streaming with `{"delim":"start"|"end"}` markers, `sender` field on messages. Retry: failures appended to chat history for LLM self-recovery; no automatic retry. Synchronous only. Source: github.com/openai/swarm; successor at github.com/openai/openai-agents-python.

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

_Note: Swarm is deprecated; strengths are framed in past tense as educational reference value._

- **Minimal, readable implementation of agent handoffs.** The entire orchestration loop was ~300 lines; the handoff pattern (a function returning an `Agent`) was the clearest published demonstration of how to transfer control between agents. Source: [openai/swarm README](https://github.com/openai/swarm).
- **Lightweight and easily testable.** The README noted that Swarm explored "patterns that are lightweight, scalable, and highly customizable by design," with all logic running client-side and no hidden state, making unit testing straightforward. Source: [openai/swarm README](https://github.com/openai/swarm).
- **Two-primitive model was easy to teach.** Just `Agent` (instructions + tool functions) and `handoff` (a function returning another `Agent`) made the mental model trivially graspable for people learning multi-agent patterns. Source: [openai/swarm README](https://github.com/openai/swarm).

## 8. Documented Weaknesses

- **Officially deprecated.** OpenAI's own README states: "Swarm is now replaced by the OpenAI Agents SDK, which is a production-ready evolution of Swarm." No further development is expected. Source: [openai/swarm README](https://github.com/openai/swarm).
- **Completely stateless.** The framework stored no state between `client.run()` calls; the developer was entirely responsible for persisting messages, agent reference, and context variables — unsuitable for any production use case with continuity requirements. Source: [openai/swarm README](https://github.com/openai/swarm).
- **Hardcoded to OpenAI Chat Completions API.** No support for non-OpenAI providers without overriding the underlying client; no native MCP support. Source: [openai/swarm README](https://github.com/openai/swarm).
- **No approval workflows or observability primitives.** Human-in-the-loop was limited to the `run_demo_loop` REPL; `debug=True` was the only observability option. Source: [openai/swarm README](https://github.com/openai/swarm).

## 9. Sources

- [openai/swarm](https://github.com/openai/swarm) — observed 2026-06-14
