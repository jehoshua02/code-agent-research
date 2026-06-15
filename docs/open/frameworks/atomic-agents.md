# Atomic Agents

_Last verified: 2026-06-14_

## 0. TL;DR

Atomic Agents is a Python framework built around the idea of composing small, single-responsibility building blocks — each "atomic" component handles one thing and has strictly typed Pydantic inputs and outputs via [Instructor](https://python.useinstructor.com/). Pick it if you want a clean, testable architecture where agent behavior emerges from composing small focused units rather than configuring a large monolithic class. The main catch is that it requires Python 3.12+ and the composable style demands more upfront design discipline compared to just writing a quick agent script.

## 1. What It Is

Atomic Agents is an MIT-licensed Python framework (BrainBlend-AI/atomic-agents). Active. Builds agents from small composable atomic components, emphasizing single-responsibility blocks over monolithic agent classes.

## 2. Install

Python 3.12+ required; Linux, macOS, Windows supported.

```bash
pip install atomic-agents
```

Provider SDKs are installed via [Instructor](https://python.useinstructor.com/) extras:

```bash
pip install instructor[anthropic]    # Anthropic
pip install instructor[groq]         # Groq
pip install instructor[google-genai] # Gemini
# OpenAI included by default
```

The CLI tool "Atomic Assembler" is installed with the package.

## 3. Model Compatibility

All inference is mediated through [Instructor](https://python.useinstructor.com/), which wraps provider SDKs and enforces structured (Pydantic-typed) outputs. Supported providers include: OpenAI, Anthropic, Google Gemini, Groq, Mistral, Cohere, Fireworks AI, and any OpenAI-compatible endpoint (Ollama, vLLM, **OpenRouter**). Source: [Instructor integrations docs](https://python.useinstructor.com/integrations/); [Atomic Agents README](https://github.com/BrainBlend-AI/atomic-agents).

## 4. Agent Capabilities

Composable single-responsibility framework built on Instructor + Pydantic. Tools are plain Python functions registered via the framework's CLI ("Atomic Assembler"); each tool is a downloadable atomic unit with its own input/output schema. No formal planning module — composition is explicit in Python; multi-step behavior emerges from chaining `AtomicAgent[InputSchema, OutputSchema]` instances via schema matching. Memory: `ChatHistory` object passed to `AgentConfig` is the short-term in-process store; no built-in long-term/vector memory layer — RAG and persistence are external concerns. Multi-agent: agents chain by output→input schema (deterministic pipeline) or one agent can register another as a tool; no built-in orchestrator/handoff primitive. HITL not built-in; handled at the application layer between `agent.run()` invocations. State persistence: `ChatHistory` can be serialized to dict/JSON and reloaded; no checkpointer or durable execution integration. Observability: relies on Instructor's tracing; OpenInference + OpenTelemetry support via the broader Instructor ecosystem; no dedicated tracing layer. Retry / error handling: Instructor's automatic retries on Pydantic validation failure (default 3) — the model is re-prompted with the validation error until output parses; tool-level retries are application code. Sync and async both supported via `agent.run()` and `agent.run_async()`; structured streaming via `agent.run_stream()` for OpenAI/Anthropic-compat providers. Source: [Atomic Agents README](https://github.com/BrainBlend-AI/atomic-agents), [Instructor docs](https://python.useinstructor.com/).

## 5. MCP Support

Not supported natively. No MCP integration found in the repository or documentation as of June 2026. Source: review of [BrainBlend-AI/atomic-agents](https://github.com/BrainBlend-AI/atomic-agents).

## 6. Programming Model

Imperative / composable-component model. Logic lives entirely in Python. The core building block is `AtomicAgent[InputSchema, OutputSchema]`, a typed generic that takes an Instructor-backed client, a system prompt generator, and a chat history. Agents are chained by passing the output schema of one as the input of the next ("schema chaining"). Context providers inject dynamic data into the system prompt at runtime. No graph abstraction; composition is explicit Python. Example:

```python
from atomic_agents import AtomicAgent, AgentConfig, BasicChatInputSchema
from atomic_agents.context import SystemPromptGenerator
import instructor
from openai import OpenAI

agent = AtomicAgent[BasicChatInputSchema, MyOutputSchema](
    config=AgentConfig(
        client=instructor.from_openai(OpenAI()),
        model="gpt-4o",
        system_prompt_generator=SystemPromptGenerator(background=["You are helpful."]),
    )
)
response = agent.run(BasicChatInputSchema(chat_message="Hello!"))
```

## 7. Documented Strengths

Documented strengths from maintainer docs, benchmarks, or independent reviews. Cite source.

## 8. Documented Weaknesses

Documented limitations from issue tracker, docs, or community reports. Cite source.

## 9. Sources

- [BrainBlend-AI/atomic-agents](https://github.com/BrainBlend-AI/atomic-agents) — observed 2026-06-14
