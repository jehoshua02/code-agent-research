# CrewAI

_Last verified: 2026-06-14_

## 1. What It Is

CrewAI is an MIT-licensed Python framework from crewAI Inc. (crewAI-Inc/crewAI) for role-based multi-agent crews. Active. Emphasizes assigning agents distinct roles (researcher, writer, etc.) collaborating on a shared goal.

## 2. Install

Python >=3.10 and <3.13 required; Linux, macOS, Windows supported. CrewAI uses [uv](https://docs.astral.sh/uv/) internally for project management.

```bash
pip install crewai
# With optional built-in tools (search, scraping, etc.):
pip install "crewai[tools]"
```

Scaffold a new project:

```bash
crewai create crew my_project
```

## 3. Model Compatibility

CrewAI routes all LLM calls through [LiteLLM](https://litellm.ai/), giving access to 100+ providers via a uniform interface: OpenAI, Anthropic, Google Gemini, Mistral, Cohere, AWS Bedrock, Azure OpenAI, Groq, Ollama (local), LM Studio, vLLM (OpenAI-compat), and OpenRouter. Default is the OpenAI API; switch via `llm` parameter on each `Agent`. Source: [CrewAI LLM Connections docs](https://docs.crewai.com/how-to/LLM-Connections/).

## 4. Agent Capabilities

Role-based multi-agent crew framework. Tools via `BaseTool` subclass or `@tool` decorator; 30+ built-in tools via `pip install 'crewai[tools]'`; tools attached per-agent. Planning: crew-level via `planning=True` (`AgentPlanner` injects step plan), agent-level via `reasoning=True` (per-step reflection); processes `sequential` or `hierarchical`. Memory unified via LanceDB at `./.crewai/memory`; recency/semantic/importance weights; hierarchical scopes; non-blocking writes. Multi-agent via Sequential/Hierarchical processes, `allow_delegation=True`, task `context=[other_task,...]`. HITL via task-level `human_input=True` (pauses before output), `before_kickoff_callbacks`/`after_kickoff_callbacks`, `task_callback`. State persistence: `checkpoint=True` on Crew, configurable `CheckpointConfig`; resume via `crewai replay -t <task_id>`. Observability: `verbose`, per-agent/crew `step_callback`, OpenTelemetry via `tracing` param. Retry: `max_retry_limit` (default 2), `max_iter` (20), task guardrails with `guardrail_max_retries` (3). Both sync (`kickoff`) and async (`akickoff`, `akickoff_for_each`). Source: docs.crewai.com.
## 5. MCP Support

Native — `crewai-tools` provides an `MCPServerTool` that connects to MCP servers (stdio or SSE) and exposes their tools to CrewAI agents. Source: [CrewAI docs — MCP Server Tool](https://docs.crewai.com/tools/mcp-server-tool).

## 6. Programming Model

Declarative / code-hybrid. Agents and tasks are defined in YAML config files (`agents.yaml`, `tasks.yaml`); the crew orchestration and tool wiring live in Python via the `@CrewBase`, `@agent`, `@task`, and `@crew` decorators. Logic is split: what an agent does goes in YAML; how tasks connect and what tools they use goes in Python. Supports sequential and hierarchical process flows. Example structure:

```
config/agents.yaml   ← roles, goals, backstories
config/tasks.yaml    ← task descriptions and expected outputs
crew.py              ← Python glue: instantiates agents/tasks, defines process
main.py              ← entry point
```

## 7. Documented Strengths

Documented strengths from maintainer docs, benchmarks, or independent reviews. Cite source.

## 8. Documented Weaknesses

Documented limitations from issue tracker, docs, or community reports. Cite source.

## 9. Sources

- [crewAI-Inc/crewAI](https://github.com/crewAI-Inc/crewAI) — observed 2026-06-14
