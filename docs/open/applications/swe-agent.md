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

- **State-of-the-art SWE-bench scores (open source)**: SWE-agent 1.0 with Claude 3.7 achieved SOTA on both SWE-bench full and SWE-bench Verified among open-source projects as of February 2025. ([swe-agent.com](https://swe-agent.com/latest/))
- **Single-YAML configurability**: The entire agent pipeline — tools, prompts, model — is governed by one YAML file, making ablation experiments and custom configurations straightforward for researchers. ([README](https://github.com/SWE-agent/SWE-agent))
- **Agent-computer interface (ACI) design**: Provides a purpose-built set of file-navigation and editing tools optimized for LLM use, rather than raw shell access — a design that proved reproducibly effective across multiple model families. ([README](https://github.com/SWE-agent/SWE-agent))
- **Open-weights SOTA variant**: SWE-agent-LM-32b achieved open-weights SOTA on SWE-bench, enabling researchers to study and fine-tune top-performing agentic behaviour. ([swe-agent.com](https://swe-agent.com/latest/))

## 9. Documented Weaknesses

- **Superseded by mini-swe-agent; in maintenance-only mode**: The project's own docs state "most of our current development effort is on mini-swe-agent" which "matches the performance of SWE-agent while being much simpler." New work should target the successor. ([swe-agent.com](https://swe-agent.com/latest/))
- **Local model incompatibilities cause error loops**: Users report that local models via Ollama (e.g., CodeLlama 13B) misinterpret Python tool calls as bash commands, triggering unrecoverable error loops. ([issue #1302](https://github.com/SWE-agent/SWE-agent/issues/1302))
- **Batch mode broken independently of single-run mode**: Issue tracker shows `sweagent run` succeeds while batch operations fail, suggesting divergent code paths with inadequate test coverage. ([issue #1247](https://github.com/SWE-agent/SWE-agent/issues/1247))
- **Heavy setup for non-benchmark use**: Requires Docker, Python 3.9+, and YAML configuration for each run — optimized for reproducible research tasks, not interactive developer workflows. ([README](https://github.com/SWE-agent/SWE-agent))

## 10. Sources

- [princeton-nlp/SWE-agent](https://github.com/princeton-nlp/SWE-agent) — observed 2026-06-14
