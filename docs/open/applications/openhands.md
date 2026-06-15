---
name: "OpenHands"
maker: "All Hands AI"
license: "MIT"
license_category: "mit"
status: "active"
url: "https://github.com/All-Hands-AI/OpenHands"
last_verified: "2026-06-14"
language: "Python"
interfaces: ["cli", "web-ui", "api"]
providers: ["anthropic", "openai", "google", "minimax", "ollama"]
supports_mcp: "native"
byok: true
focus: "agentic-coding"
hardware_tiers: ["any"]
best_for: ["coding", "research", "automation"]
notes: "Runs in sandboxed Docker; full browser + terminal environment; formerly OpenDevin."
---

# OpenHands

_Last verified: 2026-06-14_

## 0. TL;DR

OpenHands is a full [coding agent](../GLOSSARY.md#agent) platform that runs in a sandboxed Docker container and gives the [LLM](../GLOSSARY.md#llm) a browser, terminal, and file system — closer to a self-hosted junior developer than a chat assistant. Pick it if you want a web UI, strong sandboxing for safety, and an ambitious general-purpose [agentic loop](../GLOSSARY.md#agent-loop) that can tackle multi-step tasks end-to-end. The main catch is the Docker dependency and heavier setup compared to simpler CLI tools like Aider.

## 1. What It Is

OpenHands is an MIT-licensed Python application from All Hands AI (All-Hands-AI/OpenHands), formerly OpenDevin. Active. General-purpose agentic coding platform that runs in a sandboxed runtime; ships a web UI and CLI.

## 2. Install

Platforms: macOS, Linux, Windows. Docker recommended for the local GUI; the CLI requires Python 3.12+ and `uv`.

**CLI (OpenHands-CLI):**

```bash
# uv (recommended — Python 3.12 required)
uv tool install openhands --python 3.12

# Standalone binary
curl -fsSL https://install.openhands.dev/install.sh | sh
```

**Local GUI (Docker-based):**

```bash
docker run -it --rm -p 3000:3000 \
  -e SANDBOX_RUNTIME_CONTAINER_IMAGE=docker.all-hands.dev/all-hands-ai/runtime:0.43-nikolaik \
  docker.all-hands.dev/all-hands-ai/openhands:0.43
# then open http://localhost:3000
```

The `openhands` and `agent-server` Docker images are fully MIT-licensed.

**Cloud:** Free trial at [app.all-hands.dev](https://app.all-hands.dev) (requires GitHub/GitLab login; uses Minimax model by default).

## 3. Interfaces

- **CLI**: Interactive terminal agent (familiar to Claude Code / Codex users); supports IDE and CI pipeline integration; also runs in local browser via embedded server.
- **Local GUI**: Single-page React application with a REST API backend; self-hosted via Docker; single-user.
- **OpenHands Cloud**: Hosted web UI (multi-user, RBAC, Slack/Jira/Linear integrations, collaboration features; source-available).
- **Enterprise (self-hosted cloud)**: Kubernetes deployment in customer VPC; source-available, requires license.
- **SDK**: Composable Python library for building custom agents; scalable to thousands of parallel agents in the cloud.
- Headless/non-interactive: supported via SDK and CLI flags.
- No mobile app; no dedicated IDE extension (CLI works inside any IDE terminal).

## 4. Model Compatibility

OpenHands is model-agnostic. Any LLM supported by LiteLLM can be used, including:

- **Anthropic** (Claude), **OpenAI** (GPT-4o, o1), **Google** (Gemini), **Minimax** (default on cloud), **Ollama** (local), and any OpenAI-compatible endpoint.

BYOK: yes — API keys are supplied at setup time via the CLI wizard or environment variables (`LLM_API_KEY`, `LLM_MODEL`, `LLM_BASE_URL`). No bundled model; no provider lock-in.

## 5. Capabilities

OpenHands targets general software engineering: coding in any language, shell command execution, file reading and editing, and web browsing via a built-in browser tool (Playwright-backed). Vision input is supported when using a multimodal model. Data analysis and research tasks are within scope via the code-execution sandbox.

## 6. MCP Support

Native MCP support was added in late 2024 / early 2025. OpenHands can act as an MCP client, connecting to external MCP servers to consume additional tools. The integration is declared in the agent configuration; maturity is documented as experimental/beta.

## 7. Extensibility

Custom agents are written as Python classes implementing the `Agent` interface and placed in the `openhands/agenthub/` directory. Runtime tools (shell, browser, file ops) are registered at startup. The microagent system allows lightweight task-specific sub-agents to be defined in Markdown files under `.openhands/microagents/`. Hooks and event-bus listeners are available for platform integrations.

## 8. Documented Strengths

- **SWE-bench Verified #1 (open-source).** OpenHands reached 66.4% on SWE-bench Verified (5-attempt rollout with critic model) and is the only open-source agent in the top 10; also #1 on Multi-SWE-Bench across 8 languages ([blog, Apr 2025](https://www.openhands.dev/blog/sota-on-swe-bench-verified-with-inference-time-scaling-and-critic-model)).
- **Full-environment sandbox.** Gives the LLM a browser (Playwright), terminal, and filesystem inside Docker — enabling end-to-end tasks beyond code editing alone ([README](https://github.com/All-Hands-AI/OpenHands)).
- **Composable agent SDK.** Python `Agent` interface supports thousands of parallel agents and microagent sub-tasks, making it suitable for production pipelines ([arXiv:2511.03690](https://arxiv.org/pdf/2511.03690)).
- **70 K+ GitHub stars.** Strong community growth reflects broad adoption for research and production workflows ([GitHub](https://github.com/All-Hands-AI/OpenHands)).

## 9. Documented Weaknesses

- **Docker startup latency.** New users experience 1+ minute delays to pull the runtime image; even subsequent starts take ~15 s on modern hardware ([GitHub #2555](https://github.com/OpenHands/OpenHands/issues/2555), [#3644](https://github.com/OpenHands/OpenHands/issues/3644)).
- **Strong-model dependency.** Performance drops significantly without Claude 4.5 or GPT-4o; weaker models produce unreliable results, raising API cost concerns ([OpenHands Review 2026](https://vibecoding.app/blog/openhands-review)).
- **Agent loop repetition.** The agent sometimes repeats the same failing approach; Planning Mode (still beta) is occasionally ignored by the agent ([OpenHands Review 2026](https://vibecoding.app/blog/openhands-review)).
- **Docker networking edge cases.** In LAN/Docker deployments, agent-server containers fail to resolve `host.docker.internal`, blocking sandbox startup ([GitHub #12229](https://github.com/OpenHands/OpenHands/issues/12229)).

## 10. Sources

- [All-Hands-AI/OpenHands](https://github.com/All-Hands-AI/OpenHands) — observed 2026-06-14
