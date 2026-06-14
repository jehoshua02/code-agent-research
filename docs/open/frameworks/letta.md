# Letta

_Last verified: 2026-06-14_

## 1. What It Is

Letta is an Apache-2.0 Python framework (letta-ai/letta), the rebrand of MemGPT. Active. Focuses on long-term persistent memory for agents via OS-style memory management — distinguishing between in-context, archival, and recall memory tiers.

## 2. Install

**Python SDK** (requires Python ≥3.9):

```bash
pip install letta-client
```

**TypeScript/Node.js SDK** (requires Node.js 18+):

```bash
npm install @letta-ai/letta-client
```

**CLI tool** (Letta Code, requires Node.js 18+):

```bash
npm install -g @letta-ai/letta-code
letta   # launches local agent
```

Letta runs agents against the Letta cloud API (API key from app.letta.com) or a self-hosted Letta server. Linux, macOS, Windows supported.

## 3. Model Compatibility

Model-agnostic. The Letta API accepts any model reference string in `provider/model` format. Supported providers include OpenAI, Anthropic, Google, and any OpenAI-compatible endpoint. The self-hosted Letta server also supports Ollama and local vLLM backends. Source: [Letta docs quickstart](https://docs.letta.com/quickstart); provider list at [leaderboard.letta.com](https://leaderboard.letta.com/).

## 4. Agent Capabilities

Tool use, planning, memory, multi-agent, human-in-the-loop, state persistence.

## 5. MCP Support

Not explicitly documented in the main README or core docs as of June 2026. The Letta server supports extensible tool APIs, but native MCP client integration is not listed as a feature. Verify at [docs.letta.com](https://docs.letta.com) for latest status.

## 6. Programming Model

Imperative / API-driven. Developers interact with agents through an HTTP API (or Python/TypeScript SDK wrappers). Agent configuration — memory blocks, tools, model — is passed as structured data on creation; subsequent interaction is via message-passing calls. No graph or DAG abstraction; the agent runtime handles looping and memory management internally. Example:

```python
from letta_client import Letta
client = Letta(api_key="...")
agent = client.agents.create(model="openai/gpt-4o", memory_blocks=[...], tools=["web_search"])
response = client.agents.messages.create(agent_id=agent.id, input="Hello!")
```

## 7. Documented Strengths

Documented strengths from maintainer docs, benchmarks, or independent reviews. Cite source.

## 8. Documented Weaknesses

Documented limitations from issue tracker, docs, or community reports. Cite source.

## 9. Sources

- [letta-ai/letta](https://github.com/letta-ai/letta) — observed 2026-06-14
