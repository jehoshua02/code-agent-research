---
name: "Pydantic AI"
maker: "Pydantic"
license: "MIT"
license_category: "mit"
status: "active"
url: "https://github.com/pydantic/pydantic-ai"
last_verified: "2026-06-14"
language: "Python"
supports_mcp: "native"
programming_model: "imperative"
best_for: ["coding", "automation", "data"]
notes: "Type-safe agent generics with FastAPI-style decorators; deep Logfire/OTel observability built in."
---

# Pydantic AI

_Last verified: 2026-06-14_

## 0. TL;DR

Pydantic AI is a Python agent framework from the Pydantic team that makes type safety a first-class concern — agent inputs, outputs, and [tool](../GLOSSARY.md#tool) results are all validated Pydantic models, and dependencies are injected like a proper application. Pick it if you care deeply about correctness, testability, and clean Python idioms, especially if you already use Pydantic elsewhere in your codebase. The main catch is that the structured/typed approach requires more upfront schema design compared to looser frameworks.

## 1. What It Is

Pydantic AI is an MIT-licensed Python framework from the Pydantic team (pydantic/pydantic-ai). Active. Brings type-safe, Pydantic-modeled inputs and outputs to agent construction, with dependency-injection-style design.

## 2. Install

Python 3.10+ required; Linux, macOS, Windows supported.

```bash
pip install pydantic-ai
```

Install provider extras as needed:

```bash
pip install "pydantic-ai[anthropic]"   # Anthropic
pip install "pydantic-ai[google]"      # Gemini
pip install "pydantic-ai[groq]"        # Groq
# OpenAI is included by default
```

## 3. Model Compatibility

Broad built-in provider support: OpenAI, Anthropic, Google Gemini, DeepSeek, Grok (xAI), Cohere, Mistral, Perplexity, Azure AI Foundry, Amazon Bedrock, Google Cloud, Ollama, LiteLLM (100+ providers), Groq, **OpenRouter**, Together AI, Fireworks AI, Cerebras, Hugging Face, GitHub, Heroku, Vercel, Nebius, OVHcloud, Alibaba Cloud, and SambaNova. Custom model backends are also supported. Source: [pydantic-ai README](https://github.com/pydantic/pydantic-ai).

## 4. Agent Capabilities

Type-safe agent framework using Pydantic models. Tools via `@agent.tool` (with `RunContext`), `@agent.tool_plain`, or `tools=` constructor; schemas auto-extracted from signatures + docstrings (Google/NumPy/Sphinx). Planning via pydantic-graph state machine and the "Deep Agents" tier (planning, file ops, sandboxed code, durable state). Memory: `result.new_messages()` / `result.all_messages()`; passed via `message_history=` to subsequent runs; `conversation_id` correlation; `ProcessHistory` preprocessor for token budget / summarization / redaction. Multi-agent via agent-as-tool (with usage propagation), programmatic hand-off, or pydantic-graph. HITL via Deferred Tools — `requires_approval=True`, raises `ApprovalRequired`, returns `DeferredToolRequests`, resolved with `DeferredToolResults` (`ToolApproved`/`ToolDenied`). State persistence via durable-execution integrations (Temporal, DBOS, Prefect, Restate). Observability: Pydantic Logfire (`logfire.instrument_pydantic_ai()`) + OpenTelemetry; routes to Langfuse / Weave / Arize / SigNoz. Retry: two systems — model-level via `ModelRetry` and `retries=` budget; HTTP/network via tenacity-based `RetryConfig`. Both sync (`run_sync`, `run_stream_sync`) and async (`run`, `run_stream`). Source: pydantic.dev/docs/ai.

## 5. MCP Support

Native — MCP is a built-in capability. Use `MCPServerStdio` / `MCPServerHTTP` to connect agents to MCP servers. Also exposed as an agent capability via `capabilities=[MCPCapability()]`. Source: [ai.pydantic.dev/mcp/overview](https://ai.pydantic.dev/mcp/overview).

## 6. Programming Model

Imperative / type-safe. Logic lives in Python code using a FastAPI-inspired decorator pattern. Agents are typed generics (`Agent[Deps, OutputType]`); tools are registered with `@agent.tool`; dynamic instructions with `@agent.instructions`; dependencies injected via `RunContext`. Agent definitions can also be expressed in YAML/JSON (no-code path). Supports both sync and async execution. Example:

```python
from pydantic_ai import Agent

agent = Agent("openai:gpt-4o", instructions="Be concise.")

@agent.tool
async def get_weather(ctx, city: str) -> str:
    """Return current weather for a city."""
    return f"Sunny in {city}"

result = agent.run_sync("What's the weather in Paris?")
print(result.output)
```

## 7. Documented Strengths

- **Full type safety at write-time**: Agent generics (`Agent[Deps, OutputType]`) and Pydantic-validated tool schemas catch mismatches in the IDE before runtime. Docs: [ai.pydantic.dev/overview](https://pydantic.dev/docs/ai/overview/).
- **First-class testability via dependency injection**: `RunContext` lets you swap real services for mocks; the same DI system powers evals. Docs: [ai.pydantic.dev/testing-evals](https://pydantic.dev/docs/ai/testing-evals/).
- **Tight Logfire/OTel observability**: `logfire.instrument_pydantic_ai()` provides trace-level token cost, latency, and failure data with zero extra code; routes to Langfuse, Weave, Arize, etc. Docs: [logfire.pydantic.dev/docs/ai-observability](https://logfire.pydantic.dev/docs/ai-observability/).
- **FastAPI-style ergonomics**: Decorator-driven tool registration and familiar Python idioms minimise learning curve for teams already using Pydantic/FastAPI. Docs: [ai.pydantic.dev/overview](https://pydantic.dev/docs/ai/overview/).

## 8. Documented Weaknesses

- **Upfront schema design cost**: Structured output and typed deps require more schema work than looser frameworks; barrier rises with complex nested models. Noted in community comparisons ([jangwook.net, 2026](https://jangwook.net/en/blog/en/python-ai-agent-library-comparison-2026/)).
- **Provider parity gaps**: Some backends (e.g. Bedrock) silently ignore settings like `top_k`; cross-provider behaviour is inconsistent. Open bug tracker: [github.com/pydantic/pydantic-ai/issues](https://github.com/pydantic/pydantic-ai/issues?q=is%3Aissue+is%3Aopen+label%3Abug).
- **Durable-execution non-determinism**: Temporal/DBOS replay can hit determinism violations due to tool-definition caching ordering; noted as a systemic design challenge in open issues.
- **Younger ecosystem**: Released late 2024; fewer third-party integrations and community recipes than LangChain. API surface still evolving. ([kunalganglani.com comparison, 2026](https://www.kunalganglani.com/blog/pydantic-ai-vs-langchain)).

## 9. Sources

- [pydantic/pydantic-ai](https://github.com/pydantic/pydantic-ai) — observed 2026-06-14
