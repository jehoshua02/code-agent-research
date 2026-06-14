# Haystack agents

_Last verified: 2026-06-14_

## 1. What It Is

Haystack Agents refers to the agentic features of Haystack from deepset (deepset-ai/haystack, Apache-2.0, Python). Active. Extends Haystack's pipeline framework for NLP and RAG with tool-using and multi-step agentic components.

## 2. Install

Python 3.10+ required; Linux, macOS, Windows supported. Also available as a Docker image.

```bash
pip install haystack-ai
```

Nightly pre-releases:

```bash
pip install --pre haystack-ai
```

Provider-specific integrations are in [haystack-core-integrations](https://github.com/deepset-ai/haystack-core-integrations) and installed separately.

## 3. Model Compatibility

Model- and vendor-agnostic via a component integration system. Core integrations include: OpenAI, Anthropic, Mistral, Cohere, Hugging Face (Inference API and local), Azure OpenAI, AWS Bedrock, Google AI, and local models. OpenRouter is reachable via the OpenAI-compat component with a custom `api_base`. Source: [Haystack README](https://github.com/deepset-ai/haystack).

## 4. Agent Capabilities

Tool use, planning, memory, multi-agent, human-in-the-loop, state persistence.

## 5. MCP Support

Via companion tool — [Hayhooks](https://github.com/deepset-ai/hayhooks) can expose Haystack pipelines as MCP servers. Haystack pipelines themselves can also consume MCP tools. Source: [Haystack README tip block](https://github.com/deepset-ai/haystack#features).

## 6. Programming Model

Declarative pipeline / graph-based. Agents and pipelines are composed of named `Component` objects (each with typed inputs/outputs) wired together into a `Pipeline` graph. Logic lives in Python component classes; pipeline topology is defined programmatically or serializable to YAML. Agentic loops are built by connecting a generator component to tool-calling components with conditional routing. Example sketch:

```python
from haystack import Pipeline
from haystack.components.generators.chat import OpenAIChatGenerator
from haystack.components.agents import ToolCallingAgent

pipeline = Pipeline()
pipeline.add_component("agent", ToolCallingAgent(chat_generator=OpenAIChatGenerator(), tools=[...]))
result = pipeline.run({"agent": {"messages": [ChatMessage.from_user("Hello")]}})
```

## 7. Documented Strengths

Documented strengths from maintainer docs, benchmarks, or independent reviews. Cite source.

## 8. Documented Weaknesses

Documented limitations from issue tracker, docs, or community reports. Cite source.

## 9. Sources

- [deepset-ai/haystack](https://github.com/deepset-ai/haystack) — observed 2026-06-14
