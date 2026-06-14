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

Tool use, planning, memory, multi-agent, human-in-the-loop, state persistence.

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
