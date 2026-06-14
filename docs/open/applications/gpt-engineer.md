# GPT-Engineer

_Last verified: 2026-06-14_

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

What tasks it targets (coding, general, research, etc.). Tool use, file editing, shell, browser, vision, etc.

## 6. MCP Support

Native? Via adapter? Not supported?

## 7. Extensibility

Plugins, custom agents/commands, hooks, scripting. Where logic lives.

## 8. Documented Strengths

Documented strengths from maintainer docs, benchmarks, or independent reviews. Cite source.

## 9. Documented Weaknesses

Documented limitations from issue tracker, docs, or community reports. Cite source.

## 10. Sources

- [gpt-engineer-org/gpt-engineer](https://github.com/gpt-engineer-org/gpt-engineer) — observed 2026-06-14
