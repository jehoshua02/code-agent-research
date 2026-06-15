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

Documented strengths from maintainer docs, benchmarks, or independent reviews. Cite source.

## 8. Documented Weaknesses

Documented limitations from issue tracker, docs, or community reports. Cite source.

## 9. Sources

- [huggingface/smolagents](https://github.com/huggingface/smolagents) — observed 2026-06-14
