---
name: "Smolagents"
maker: "HuggingFace"
license: "Apache-2.0"
license_category: "apache-2.0"
status: "active"
url: "https://github.com/huggingface/smolagents"
last_verified: "2026-06-14"
language: "Python"
supports_mcp: "native"
programming_model: "code-emitting"
best_for: ["coding", "research", "automation"]
notes: "CodeAgent emits Python as tool calls; sandbox (e2b/Docker) required in production."
---

# Smolagents

_Last verified: 2026-06-14_

## 0. TL;DR

Smolagents is a minimal HuggingFace Python framework where agents write and execute Python code as their "[tool](../GLOSSARY.md#tool) calls" rather than emitting JSON — making the action step very flexible and easy to debug. Pick it if you want a lightweight, code-first agent with excellent HuggingFace model support and don't need heavy scaffolding. The main catch is that executing arbitrary generated Python code requires a sandboxed environment (e2b or Docker) in production, which adds setup overhead.

## 1. What It Is

Smolagents is an Apache-2.0 Python framework from HuggingFace (huggingface/smolagents). Active. Minimal, code-first approach where agents emit Python code to execute rather than JSON tool calls.

## 2. Install

Python 3.10+ required; Linux, macOS, Windows supported.

```bash
pip install smolagents            # core only
pip install "smolagents[toolkit]" # core + common tools (web search, etc.)
```

Optional extras: `smolagents[litellm]` for LiteLLM integration, `smolagents[transformers]` for local HuggingFace model inference, `smolagents[e2b]` / `smolagents[docker]` for sandboxed code execution.

## 3. Model Compatibility

Highly model-agnostic via multiple model backends:

- `InferenceClientModel` — HuggingFace Inference API (50+ providers including Together, Fireworks, etc.)
- `LiteLLMModel` — 100+ providers via LiteLLM (Anthropic, OpenAI, Gemini, Cohere, etc.)
- `OpenAIModel` — direct OpenAI API or any OpenAI-compatible server (Ollama, vLLM, **OpenRouter** via `api_base="https://openrouter.ai/api/v1"`)
- `TransformersModel` — local HuggingFace models via `transformers`
- `AzureOpenAIModel`, `AmazonBedrockModel` for cloud providers

Source: [smolagents README](https://github.com/huggingface/smolagents).

## 4. Agent Capabilities

Minimal code-first agent library from HuggingFace. Two agent classes: `CodeAgent` (LLM writes Python tool calls, executes in sandbox) and `ToolCallingAgent` (JSON tool calls; `max_tool_threads` for parallel). Tools via `smolagents.Tool` subclass or `@tool`; collections from HF Hub or MCP (`ToolCollection.from_mcp`); imports from LangChain or Gradio. Planning: opt-in `planning_interval=N`; default ReAct loop with Thought/Code/Observation. Memory in-context only (`AgentMemory` of `TaskStep`/`ActionStep`/`PlanningStep`); `reset=False` preserves across `agent.run()` calls; no long-term store. Multi-agent via `managed_agents` — sub-agents appear as callable tools to a `CodeAgent` orchestrator. HITL minimal: `agent.interrupt()`, `final_answer_checks`, `GradioUI`. State persistence at definition level only: `agent.save()` / `from_folder()` / `push_to_hub()`. Observability via OpenTelemetry (`openinference-instrumentation-smolagents`) → Phoenix/MLflow/Langfuse. Retry: self-correction via error observations in `AgentMemory`; `max_steps` (20); sandboxed executors (`local`/`e2b`/`modal`/`docker`/`blaxel`). Primarily sync; `stream=True` returns a generator. Source: huggingface.co/docs/smolagents.

## 5. MCP Support

Native — `ToolCollection.from_mcp()` loads tools from any MCP server into a smolagents agent. Source: [smolagents tools reference](https://huggingface.co/docs/smolagents/reference/tools#smolagents.ToolCollection.from_mcp).

## 6. Programming Model

Imperative / code-first. The distinctive design is that `CodeAgent` emits Python code as its action language (rather than JSON tool calls), executes it in a sandboxed environment, and loops until done. The alternative `ToolCallingAgent` uses standard JSON tool calls if preferred. Logic lives entirely in Python; agents are constructed programmatically. Example:

```python
from smolagents import CodeAgent, WebSearchTool, LiteLLMModel

model = LiteLLMModel(model_id="anthropic/claude-sonnet-4-6-latest")
agent = CodeAgent(tools=[WebSearchTool()], model=model)
agent.run("Find the current price of gold.")
```

## 7. Documented Strengths

- **Code-as-actions is uniquely expressive.** `CodeAgent` emits Python code rather than JSON tool calls, enabling function nesting, loops, and conditionals in a single action step. The HuggingFace team reports CodeAgents use "30% fewer LLM steps and costs than classic ReAct-style JSON agents." Source: [HuggingFace smolagents docs](https://huggingface.co/docs/smolagents/en/index); [KDnuggets — Big Gains with smolagents](https://www.kdnuggets.com/big-gains-with-hugging-faces-smolagents).
- **Extremely minimal codebase.** Core agent logic fits in ~1,000 lines of code with minimal abstractions, making it easy to read, fork, and understand fully. Source: [GitHub — huggingface/smolagents README](https://github.com/huggingface/smolagents).
- **GAIA benchmark top performance.** A CodeAgent built on smolagents topped the GAIA leaderboard, demonstrating that open-source models with code-first agents can compete with top closed models. Source: [HuggingFace blog — "Our Transformers Code Agent beats the GAIA benchmark"](https://huggingface.co/blog/beating-gaia).
- **Native HuggingFace ecosystem integration.** `InferenceClientModel` provides direct access to 50+ Hub providers; tools, agents, and models are publishable and loadable from the Hub. Source: [smolagents README](https://github.com/huggingface/smolagents).

## 8. Documented Weaknesses

- **No built-in long-term or cross-session memory.** `AgentMemory` is in-context only; there is no built-in summarization or persistent store. Multiple open GitHub issues request this feature: [#694](https://github.com/huggingface/smolagents/issues/694), [#901](https://github.com/huggingface/smolagents/issues/901), [#1121](https://github.com/huggingface/smolagents/issues/1121).
- **Observability requires external tooling.** There is no first-party tracing dashboard; teams must wire up OpenTelemetry to Langfuse, Phoenix, or MLflow themselves. Source: [Langfuse — Observability for smolagents](https://langfuse.com/integrations/frameworks/smolagents).
- **Sandbox setup required for production code execution.** Running `CodeAgent` safely in production requires E2B, Docker, or Modal sandbox configuration, adding operational overhead. Source: [smolagents README — sandboxed executors](https://github.com/huggingface/smolagents).
- **Context grows unboundedly without intervention.** The framework has basic truncation but no automatic summarization; long-running agents accumulate history until context limits are hit, requiring custom management. Source: [ZenML blog — smolagents vs LangGraph](https://www.zenml.io/blog/smolagents-vs-langgraph).

## 9. Sources

- [huggingface/smolagents](https://github.com/huggingface/smolagents) — observed 2026-06-14
