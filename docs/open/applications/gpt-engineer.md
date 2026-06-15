# GPT-Engineer

_Last verified: 2026-06-14_

## 0. TL;DR

GPT-Engineer was an early one-shot [coding agent](../GLOSSARY.md#agent) that took a natural-language spec and generated a full project from scratch — an influential proof-of-concept that showed what [LLMs](../GLOSSARY.md#llm) could build end-to-end. The repository is archived and no longer maintained; its successor is lovable.dev (a commercial product). Do not start new projects on it, but it is worth knowing as the historical precursor to modern scaffold-generation agents.

## 1. What It Is

GPT-Engineer is an MIT-licensed Python application from Anton Osika (gpt-engineer-org/gpt-engineer). Archived. Early one-shot code-generation agent that took a natural-language spec and emitted a full project; became the precursor to lovable.dev.

## 2. Install

Platforms: macOS, Linux, Windows. Requires Python 3.10–3.12 (last version supporting 3.8–3.9 was 0.2.6). Docker also supported.

```bash
# Stable release via pip
python -m pip install gpt-engineer

# Development install
git clone https://github.com/gpt-engineer-org/gpt-engineer.git
cd gpt-engineer
poetry install
poetry shell
```

Docker and GitHub Codespaces options are also documented in the repo.

After install, set `OPENAI_API_KEY` (or configure another provider), create a project folder with a `prompt` file, then run:

```bash
gpte projects/my-new-project
```

## 3. Interfaces

- **CLI**: Single primary interface — the `gpte` binary. Run with a project directory argument; interactive only in the sense that it may ask clarifying questions during generation.
- Headless: runs non-interactively once a `prompt` file is present; suitable for scripting and benchmarking via the `bench` binary.
- No TUI, no web UI, no IDE extension, no mobile app.
- GitHub Codespaces: full browser-based environment available.

## 4. Model Compatibility

Defaults to **OpenAI** (GPT-4 and compatible models) via the OpenAI API. Also supports **Azure OpenAI** and **Anthropic** models. Local and open-source models are documented at [gpt-engineer.readthedocs.io/en/latest/open_models.html](https://gpt-engineer.readthedocs.io/en/latest/open_models.html) (e.g., WizardCoder). Vision-capable models can accept image inputs via `--image_directory`. BYOK: yes — set `OPENAI_API_KEY` or equivalent env var. No bundled model.

## 5. Capabilities

Targets one-shot code generation from a natural-language spec, producing entire project scaffolds. Supports any language the underlying LLM knows (Python, JavaScript, etc.). Writes files to disk; does not execute shell commands or browse the web. Vision input is supported when a vision-capable model is configured via `--image_directory`.

## 6. MCP Support

Not supported. GPT-Engineer is archived and predates MCP; no adapter or plugin mechanism exists.

## 7. Extensibility

Logic lives in Python modules under `gpt_engineer/`. Behaviour can be altered by subclassing `AI` or swapping prompt templates; the `bench` binary exposes a scripting surface for benchmarking. No plugin registry or hook system — extension requires forking the source.

## 8. Documented Strengths

Documented strengths from maintainer docs, benchmarks, or independent reviews. Cite source.

## 9. Documented Weaknesses

Documented limitations from issue tracker, docs, or community reports. Cite source.

## 10. Sources

- [gpt-engineer-org/gpt-engineer](https://github.com/gpt-engineer-org/gpt-engineer) — observed 2026-06-14
