# mcp-agent

_Last verified: 2026-06-14_

## 0. TL;DR

mcp-agent is a minimal Python framework specifically for building agents that consume [MCP](../GLOSSARY.md#mcp-model-context-protocol) servers as their primary [tool](../GLOSSARY.md#tool) source — it handles MCP server lifecycle, connection management, and basic orchestrator-worker patterns out of the box. Pick it if your agent is MCP-native from the start and you want the simplest possible wrapper rather than a full-featured framework. The main catch is low activity since early 2026, which raises questions about long-term maintenance.

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

LastMile AI's minimal MCP-native framework. Tools come **only** from configured MCP servers (`server_names=[...]` per agent); custom tools via `@app.tool`/`@app.async_tool`; tools discovered at runtime via `agent.list_tools()`. Augmented LLMs (`OpenAIAugmentedLLM`, etc.) handle tool dispatch in `generate_str`/`generate_structured`. Planning: composable factory helpers — `create_orchestrator()` (orchestrator-workers), `create_router_llm()`/`create_router_embedding()` (routing with confidence), `create_parallel_llm()` (fan-out/fan-in), `create_deep_orchestrator()` (long-horizon), `create_evaluator_optimizer_llm()` (iterative refinement), `create_intent_classifier_llm()`, `create_swarm()` (handoffs). Memory: short-term auto-retained across `generate_str` calls; long-term via Temporal durable execution (no dedicated vector store). Multi-agent via factories + agents-as-MCP-servers (server-of-servers). HITL: `context.request_human_input(HumanInputRequest)` or low-level Temporal signal (`wait_for_signal`/`signal_workflow`); CLI `mcp-agent cloud workflows resume`. State persistence: Temporal's replay model — deterministic workflow code re-executes after crashes, non-determinism offloaded to activities; one-config-line switch from asyncio to Temporal. Observability: structured logging in `mcp_agent.config.yaml`, OpenTelemetry, `TokenCounter` with watcher API, Temporal Web UI. Retry: Temporal per-activity retry policies via YAML (pattern matching, non-retryable error types per provider); asyncio mode has none. Async-first only — no sync API. Source: docs.mcp-agent.com.

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

- **MCP-native from the ground up**: All tools come from MCP servers; connection lifecycle is managed automatically; no adapter layer needed for any MCP-compliant server. Source: [github.com/lastmile-ai/mcp-agent README](https://github.com/lastmile-ai/mcp-agent).
- **Temporal durable execution with zero code change**: Switching `execution_engine: temporal` in config gives pause/resume, per-activity retry policies, and human-input signals without modifying workflow code. Docs: [github.com/lastmile-ai/mcp-agent/examples/temporal](https://github.com/lastmile-ai/mcp-agent/tree/main/examples/temporal).
- **Batteries-included agentic patterns**: Factory helpers implement all of Anthropic's "Building Effective Agents" patterns (orchestrator-workers, router, evaluator-optimizer, map-reduce, swarm) as one-liners. Source: [github.com/lastmile-ai/mcp-agent README](https://github.com/lastmile-ai/mcp-agent).
- **Minimal abstraction surface**: Thin wrapper with explicit Python wiring; no graph DSL or config graph to learn; suitable for teams that want full control. Source: [medium.com/@hanieh_74136 developer guide 2025](https://medium.com/@hanieh_74136/the-developers-guide-to-ai-agent-frameworks-in-2025-mcp-native-vs-traditional-approaches-e6c74027f220).

## 8. Documented Weaknesses

- **Low activity since early 2026**: Last commit was January 25, 2026; no releases since; long-term maintenance is uncertain. Source: [github.com/lastmile-ai/mcp-agent/commits](https://github.com/lastmile-ai/mcp-agent/commits/main).
- **Security issues in deploy tooling**: `deploy` command imports project `main.py` in-process (arbitrary code execution risk); API keys printed in plain text to terminal on deploy. Open issues #669, #670: [github.com/lastmile-ai/mcp-agent/issues](https://github.com/lastmile-ai/mcp-agent/issues).
- **Async-only, no sync API**: No `run_sync` or blocking wrappers; callers must use asyncio throughout. Docs: [github.com/lastmile-ai/mcp-agent README](https://github.com/lastmile-ai/mcp-agent).
- **Silent partial failures in server discovery**: `get_capabilities_task` returns exception objects inside the `ServerCapabilities` dict on partial server failure rather than raising. Open bug #671: [github.com/lastmile-ai/mcp-agent/issues/671](https://github.com/lastmile-ai/mcp-agent/issues/671).

## 9. Sources

- [lastmile-ai/mcp-agent](https://github.com/lastmile-ai/mcp-agent) — observed 2026-06-14
