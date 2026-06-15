# Tool use / function calling

_Last verified: 2026-06-14_

## 0. TL;DR

Tool use (function calling) is the foundational capability that turns a chat model into an agent: instead of making something up, the model emits a structured call to a real function, gets the result back, and continues from there. Every other agentic technique — [ReAct](../GLOSSARY.md#react), [RAG](../GLOSSARY.md#rag), plan-and-execute — assumes tool use is already in place. The main catch: the model decides when and how to call tools, so vague tool descriptions or overlapping tool names produce bad calls.

## 1. What It Is

Tool use (a.k.a. function calling) is the pattern where the model emits structured tool-call requests that a runtime intercepts, executes, and returns results from, rather than fabricating answers from memory. Toolformer (Schick et al., 2023) is an early survey; modern providers expose it via API-level structured calls.

## 2. Problem It Solves

LLMs have a frozen knowledge cutoff and no mechanism to take actions or read live state. Without tool access, a model asked to check current weather, execute a calculation, query a database, or send an email must either fabricate a plausible-sounding answer or refuse. Even when trained knowledge covers the domain, the model cannot act on the world.

## 3. How It Works

The model is given a list of tool definitions (name, description, parameter schema) in the prompt or API request. When the model determines a tool call is needed, it emits a structured response (typically JSON) specifying the tool name and arguments instead of a prose answer. The runtime intercepts this, executes the actual function, and returns the result as a new message. The model then continues generating with the real result in context. Standardized by OpenAI's function calling spec (2023) and the Anthropic tool use API.

```
tools = [{"name": "search", "description": "...", "parameters": {...}}]
response = llm(messages, tools=tools)
if response.tool_call:
    result = dispatch(response.tool_call.name, response.tool_call.args)
    messages.append(tool_result(result))
    response = llm(messages, tools=tools)
return response.content
```

## 4. When To Use

Use tool use whenever the task requires live data (search, stock prices, weather), computation (code execution, calculators), or side effects (sending email, writing to a database). It is the correct primitive for grounding an LLM in the real world.

## 5. When Not To Use

Skip tool use for pure text generation tasks where no external data or action is needed — it adds latency and API complexity. If the model doesn't support structured output, reliable tool call parsing requires fragile regex. Avoid it on paths where every millisecond matters and the overhead of a round-trip to an external service is unacceptable.

## 6. Implementations

- **OpenAI API** — `functions` / `tools` parameter; automatic parsing of `tool_calls` in the response
- **Anthropic API** — `tools` parameter with `tool_use` / `tool_result` content blocks
- **LangChain** — `Tool`, `StructuredTool`, and toolkit abstractions; integrates with hundreds of pre-built tools
- **LlamaIndex** — `FunctionTool` and `QueryEngineTool`; tools are first-class in agent abstractions
- **MCP (Model Context Protocol)** — standardized server/client protocol for exposing tools across runtimes and models

## 7. Sources

- [Toolformer: Language Models Can Teach Themselves to Use Tools (Schick et al., 2023)](https://arxiv.org/abs/2302.04761) — observed 2026-06-14
