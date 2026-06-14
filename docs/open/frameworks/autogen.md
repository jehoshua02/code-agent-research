# AutoGen

_Last verified: 2026-06-14_

## 1. What It Is

AutoGen is a CC-BY-4.0 Python framework from Microsoft (microsoft/autogen) for building multi-agent conversation systems. Active. Models problems as multiple specialized agents exchanging messages, with optional human-in-the-loop.

## 2. Install

Python 3.10+ required; Linux, macOS, Windows supported.

**Note:** AutoGen is now in maintenance mode. Microsoft recommends new projects use [Microsoft Agent Framework](https://github.com/microsoft/agent-framework). Existing AutoGen users can continue with the packages below.

```bash
# AgentChat + OpenAI extension
pip install -U "autogen-agentchat" "autogen-ext[openai]"

# Optional: no-code GUI
pip install -U autogenstudio
```

Extras: `autogen-ext[azure]`, `autogen-ext[anthropic]`, `autogen-ext[ollama]`, etc.

## 3. Model Compatibility

Supports any OpenAI-compatible endpoint plus provider-specific extensions. First-party extensions in `autogen-ext` cover: OpenAI, Azure OpenAI, Anthropic, Ollama (local), Google Gemini, AWS Bedrock, Mistral, and vLLM (via OpenAI-compat). OpenRouter is reachable via the OpenAI client pointed at `https://openrouter.ai/api/v1`. Source: [AutoGen models docs](https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/tutorial/models.html).

## 4. Agent Capabilities

Tool use, planning, memory, multi-agent, human-in-the-loop, state persistence.

## 5. MCP Support

Native — built into `autogen-ext` via `McpWorkbench` and `StdioServerParams`. Connect to any MCP server (stdio or SSE) and expose its tools directly to agents. Multiple MCP servers can be combined in a list. Source: [AutoGen README MCP example](https://github.com/microsoft/autogen#mcp-server).

```python
from autogen_ext.tools.mcp import McpWorkbench, StdioServerParams
async with McpWorkbench(server_params) as mcp:
    agent = AssistantAgent("agent", model_client=client, workbench=mcp)
```

## 6. Programming Model

Imperative / event-driven. Logic lives in Python code using the layered API: Core (message passing, distributed runtime), AgentChat (opinionated high-level agents and teams), Extensions (provider integrations). Agents are defined by subclassing or instantiating `AssistantAgent`, wired into teams (`RoundRobinGroupChat`, `SelectorGroupChat`) or direct handoffs. Control flow is explicit Python; no separate config files required (though AutoGen Studio offers a no-code GUI). Example:

```python
from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient

agent = AssistantAgent("helper", model_client=OpenAIChatCompletionClient(model="gpt-4o"))
result = await agent.run(task="Summarize the news.")
```

## 7. Documented Strengths

Documented strengths from maintainer docs, benchmarks, or independent reviews. Cite source.

## 8. Documented Weaknesses

Documented limitations from issue tracker, docs, or community reports. Cite source.

## 9. Sources

- [microsoft/autogen](https://github.com/microsoft/autogen) — observed 2026-06-14
