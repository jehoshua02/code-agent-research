# Haystack agents

_Last verified: 2026-06-14_

## 0. TL;DR

Haystack Agents extends deepset's Haystack NLP pipeline framework with agentic, tool-using components — so agents are just another piece you plug into a Haystack pipeline alongside retrievers, readers, and rankers. Pick it if you're building [RAG](../GLOSSARY.md#rag-retrieval-augmented-generation) or document-processing pipelines and want agents as one composable step in that system. The main catch is that Haystack's pipeline abstraction adds overhead if you only need an agent and have no broader NLP pipeline to integrate with.

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

deepset-ai's RAG-and-pipelines framework with agentic features. Tools via `@tool` decorator (auto-schema from `Annotated` params), `create_tool_from_function`, or manual `Tool(...)`. `Agent` combines `ChatGenerator` + `ToolInvoker` in a loop bounded by `exit_conditions`. No formal planning; loop-based. Memory: in-context chat history; `state_schema` for structured state shared across tools (`inputs_from_state`/`outputs_to_state`). Multi-agent via wrapping agents as `Tool`/`ComponentTool`/`PipelineTool`; no dedicated orchestration class. HITL via `confirmation_strategies` — `BlockingConfirmationStrategy` with Strategy/Policy/UI layers; human can confirm/reject/modify with templated feedback. State persistence via pipeline **breakpoints** with snapshots (`{component}_{visit}_{ts}.json`), enabled by `HAYSTACK_PIPELINE_SNAPSHOT_SAVE_ENABLED=true`; resumable via `pipeline.run(data={}, pipeline_snapshot=snapshot)`; failed runs auto-snapshot. Observability with auto-tracing for OpenTelemetry, Datadog, Langfuse, MLflow, Weave, Jaeger; `HAYSTACK_CONTENT_TRACING_ENABLED` exposes I/O. Retry: `raise_on_tool_invocation_failure=False` lets LLM recover; snapshots enable resume. `AsyncPipeline` runs independents in parallel; `run`, `run_async`, `run_async_generator`; `concurrency_limit`. Source: docs.haystack.deepset.ai.

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
