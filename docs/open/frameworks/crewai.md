---
name: "CrewAI"
maker: "crewAI Inc."
license: "MIT"
license_category: "mit"
status: "active"
url: "https://github.com/crewAI-Inc/crewAI"
last_verified: "2026-06-14"
language: "Python"
supports_mcp: "native"
programming_model: "role-based"
best_for: ["automation", "research", "writing"]
notes: "YAML/Python hybrid config; LLM routing via LiteLLM (100+ providers)."
---

# CrewAI

_Last verified: 2026-06-14_

## 0. TL;DR

CrewAI is a Python framework for assembling a "crew" of role-playing [agents](../GLOSSARY.md#agent) — researcher, writer, reviewer — that collaborate on a shared goal. Pick it if you like a high-level, role-centric mental model and want to get a multi-agent [workflow](../GLOSSARY.md#workflow) running quickly with minimal boilerplate. The main catch is limited control over the underlying agent loop, which can make debugging surprising behavior harder.

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

- **Intuitive role-based mental model.** Defining an agent's role, goal, and backstory maps directly to how teams actually work; community benchmarks report getting to a working prototype "roughly 40 percent faster than graph-based alternatives." Source: [designrevision.com — AI Agent Frameworks Compared 2026](https://designrevision.com/blog/ai-agent-frameworks).
- **Minimal boilerplate for multi-agent pipelines.** YAML config + `@CrewBase` decorators wire agents to tasks without manual graph construction; `hierarchical` process adds a manager agent with one flag. Source: [CrewAI docs — Crews](https://docs.crewai.com/concepts/crews).
- **Broad LLM coverage via LiteLLM.** 100+ providers accessible through a uniform interface without additional adapter packages. Source: [CrewAI docs — LLM Connections](https://docs.crewai.com/how-to/LLM-Connections/).
- **Built-in memory with semantic retrieval.** Unified LanceDB-backed memory with recency/semantic/importance weights and per-crew scoping requires no external vector DB setup. Source: [CrewAI docs — Memory](https://docs.crewai.com/concepts/memory).

## 8. Documented Weaknesses

- **Limited fine-grained loop control.** CrewAI's "structured, role-based approach may not suit organizations needing highly specialized or unconventional agent behaviors," and fine-grained customization is harder than in frameworks like LangGraph. Source: [latenode.com — CrewAI 2025 review](https://latenode.com/blog/ai-frameworks-technical-infrastructure/crewai-framework/crewai-framework-2025-complete-review-of-the-open-source-multi-agent-ai-platform).
- **No built-in production monitoring or error recovery.** The review notes "absence of built-in monitoring, error recovery, and scaling mechanisms," requiring teams to add these independently. Source: [latenode.com — CrewAI 2025 review](https://latenode.com/blog/ai-frameworks-technical-infrastructure/crewai-framework/crewai-framework-2025-complete-review-of-the-open-source-multi-agent-ai-platform).
- **Scaling coordination complexity.** As crews grow, "maintaining clear role definitions and ensuring smooth communication between agents becomes increasingly challenging," demanding significant architectural upfront work. Source: [latenode.com — CrewAI 2025 review](https://latenode.com/blog/ai-frameworks-technical-infrastructure/crewai-framework/crewai-framework-2025-complete-review-of-the-open-source-multi-agent-ai-platform).
- **Struggles with smaller open-source models.** Function-calling features have documented difficulties with 7B-parameter models due to precise instruction-adherence limitations. Source: [latenode.com — CrewAI 2025 review](https://latenode.com/blog/ai-frameworks-technical-infrastructure/crewai-framework/crewai-framework-2025-complete-review-of-the-open-source-multi-agent-ai-platform).

## 9. Sources

- [crewAI-Inc/crewAI](https://github.com/crewAI-Inc/crewAI) — observed 2026-06-14
