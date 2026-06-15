# OpenHands

_Last verified: 2026-06-14_

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

Documented strengths from maintainer docs, benchmarks, or independent reviews. Cite source.

## 9. Documented Weaknesses

Documented limitations from issue tracker, docs, or community reports. Cite source.

## 10. Sources

- [All-Hands-AI/OpenHands](https://github.com/All-Hands-AI/OpenHands) — observed 2026-06-14
