# Letta

_Last verified: 2026-06-14_

## 0. TL;DR

Letta (formerly MemGPT) is a Python framework built around the idea that agents need persistent, structured [memory](../GLOSSARY.md#memory) — it splits memory into in-context, archival, and recall tiers so agents can remember things across many conversations. Pick it if long-term user or task memory is the central requirement of your application. The main catch is that Letta's architecture requires running a Letta server (cloud or self-hosted), adding operational complexity compared to a simple library.

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

Stateful agent framework (MemGPT successor) focused on long-term memory. Tools in four categories: server-tool sandbox, client-side execution, built-in (web search, fetch, code interpreter), MCP (stdio/HTTP/SSE). Planning is emergent from agent loop; supervisor-worker pattern is canonical. Memory is the core feature — four-layer hierarchy: in-context Memory Blocks (XML-prepended, agent-mutable via `memory_rethink`/`memory_replace`), out-of-context Archival Memory (semantic vector search), Files (read-only ≤5 MB), External RAG. All state persisted to DB; nothing lost on context eviction. Multi-agent via shared memory blocks, message passing, five patterns (supervisor-worker, parallel, round-robin, producer-reviewer, hierarchical). HITL: any tool can `require_approval`; emits `approval_request_message`; user approves/denies with feedback. State: persistent DB, Runs/Steps API tracks every invocation; ADE UI for inspection. Observability: per-run trace/usage/messages sub-resources, fine-grained stop reasons. Retry: not built-in; surfaced via stop_reason. Background-mode async (`create_async`) survives disconnects via `run_id`+`seq_id` cursor pagination. Source: docs.letta.com.
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

- **OS-inspired tiered memory is the core differentiator.** Core (RAM-like), Recall (cache-like), and Archival (cold storage) tiers let agents self-edit what they remember, supporting "effectively unlimited memory" for multi-week or multi-thousand-turn tasks. Source: [vectorize.io — Mem0 vs Letta 2026](https://vectorize.io/articles/mem0-vs-letta); [atlan.com — Best AI Agent Memory Frameworks 2026](https://atlan.com/know/best-ai-agent-memory-frameworks-2026/).
- **Transparent memory inspection.** The Agent Development Environment (ADE) lets developers inspect memory state across all three tiers and monitor tool calls in real time, which the review calls "genuinely useful for understanding why an agent made a particular memory decision." Source: [vectorize.io — Mem0 vs Letta 2026](https://vectorize.io/articles/mem0-vs-letta).
- **Integrated stateful runtime.** The Letta server manages the agent loop, tool execution, state persistence, and memory together, eliminating friction between memory management and the rest of agent logic. Source: [Letta docs — quickstart](https://docs.letta.com/quickstart).
- **Background async mode survives disconnects.** `create_async` with `run_id`+`seq_id` cursor pagination lets long-running tasks continue even if the client disconnects. Source: [Letta docs — async runs](https://docs.letta.com).

## 8. Documented Weaknesses

- **Architectural lock-in.** Adopting Letta means "rewriting not just your memory layer but your entire agent infrastructure," making it a significant commitment that is difficult to reverse. Source: [vectorize.io — Mem0 vs Letta 2026](https://vectorize.io/articles/mem0-vs-letta).
- **Every memory operation costs inference tokens.** The agent must reason about what to store on each turn; this active-paging approach adds latency and token cost compared to passive extraction approaches. Source: [vectorize.io — Mem0 vs Letta 2026](https://vectorize.io/articles/mem0-vs-letta).
- **Requires running a server.** The Letta architecture mandates a Letta Cloud or self-hosted Letta server with a database backend; there is no simple "import and call" library mode. Source: [Letta docs quickstart](https://docs.letta.com/quickstart).
- **No published independent benchmark results.** Letta has not published LongMemEval scores, making objective performance comparison with alternatives impossible. Source: [vectorize.io — Mem0 vs Letta 2026](https://vectorize.io/articles/mem0-vs-letta).

## 9. Sources

- [letta-ai/letta](https://github.com/letta-ai/letta) — observed 2026-06-14
