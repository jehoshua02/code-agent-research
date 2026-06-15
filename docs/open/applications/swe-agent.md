# SWE-agent

_Last verified: 2026-06-14_

## 0. TL;DR

SWE-agent is a research-grade [coding agent](../GLOSSARY.md#agent) from Princeton NLP, built specifically to solve real GitHub issues autonomously and score well on the SWE-bench benchmark — it's the tool academics and teams use to measure where [agentic loops](../GLOSSARY.md#agent-loop) actually stand today. Pick it if you are evaluating agent capabilities, running benchmarks, or need a rigorously designed agent-computer interface as a foundation for your own research. The main catch is that it's optimized for benchmark tasks rather than everyday interactive coding, so the setup is heavier and the UX is more research-lab than developer-tool.

## 1. What It Is

SWE-agent is an MIT-licensed Python application from Princeton NLP (princeton-nlp/SWE-agent). Active. Research-grade agent designed for the SWE-bench benchmark; uses a custom agent-computer interface to navigate and edit repositories.

## 2. Install

Platforms: macOS, Linux, Windows (via Docker or GitHub Codespaces). Python 3.9+ required; Docker recommended for the default sandbox backend.

```bash
# Clone and install
git clone https://github.com/SWE-agent/SWE-agent.git
cd SWE-agent
python -m pip install --upgrade pip && pip install --editable .

# Verify
sweagent --help
```

Optionally install Docker for local code evaluation and Node.js for the web-based GUI. GitHub Codespaces provides a zero-install browser environment.

> Note: active development has shifted to [mini-swe-agent](https://github.com/SWE-agent/mini-swe-agent), which matches SWE-agent's performance with much simpler code. SWE-agent is still maintained but primarily for research.

## 3. Interfaces

- **CLI** (`sweagent`): Primary interface; runs batch or single-instance tasks from the command line with a YAML config file.
- **Web GUI**: Optional browser-based interface; requires Node.js installed alongside the Python package.
- GitHub Codespaces: browser-based development environment available.
- No TUI, no IDE extension, no mobile app.
- Headless/non-interactive: yes — the CLI is designed for batch/automated runs (SWE-bench benchmarking).
- Remote: Docker backend runs sandboxed; cloud evaluation also supported.

## 4. Model Compatibility

SWE-agent supports all models accessible through [LiteLLM](https://docs.litellm.ai/docs/providers/), including:

- **Anthropic** (Claude Sonnet 4 — recommended), **OpenAI** (GPT-4o, o1-preview), **Together AI**, and any other LiteLLM-listed provider.
- **Local models**: any OpenAI-compatible endpoint via `api_base`; Ollama supported via LiteLLM's Ollama adapter.
- API keys set via `.env` file or `--agent.model.api_key` flag.

BYOK: yes. No bundled model; no provider lock-in. Model selection via `--agent.model.name`.

## 5. Capabilities

Targets software engineering tasks: navigating repositories, editing source files, and running shell commands inside a sandboxed Docker environment. Language-agnostic in practice — any language the underlying model understands. No browser/web tool, no vision support, and no interactive data-analysis environment; the agent-computer interface (ACI) exposes file search, view, edit, and bash execution.

## 6. MCP Support

Not supported in the main SWE-agent codebase. No MCP adapter is documented; the project predates MCP adoption and uses its own ACI tool schema.

## 7. Extensibility

Behaviour is configured via YAML files (`config/`) that define the agent pipeline, tool set, and prompt templates. New tools can be added by implementing a `Tool` subclass in Python under `sweagent/tools/`. The `mini-swe-agent` successor simplifies this further. No plugin registry; extension requires modifying source or supplying a custom config YAML.

## 8. Documented Strengths

Documented strengths from maintainer docs, benchmarks, or independent reviews. Cite source.

## 9. Documented Weaknesses

Documented limitations from issue tracker, docs, or community reports. Cite source.

## 10. Sources

- [princeton-nlp/SWE-agent](https://github.com/princeton-nlp/SWE-agent) — observed 2026-06-14
