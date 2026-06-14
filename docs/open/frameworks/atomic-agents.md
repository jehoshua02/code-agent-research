# Atomic Agents

_Last verified: 2026-06-14_

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

**Pass C research deferred** — research agent hit session limit before completing. Composable atomic-component agent framework (BrainBlend-AI/atomic-agents). Atomic single-responsibility blocks (input/output schemas, system prompts, agent class). Apply remaining capability detail in next pass; see project README for current information.

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
