# Open Interpreter

_Last verified: 2026-06-14_

## 0. TL;DR

Open Interpreter lets an [LLM](../GLOSSARY.md#llm) write and execute code directly on your machine — think of it as ChatGPT's Code Interpreter but running locally against your own files, APIs, and system. Pick it if you need a general-purpose [agent](../GLOSSARY.md#agent) for data wrangling, automation, or system tasks rather than pure software development. The main catch is the AGPL-3.0 license and the fact that it executes arbitrary code on your machine, so you need to be comfortable reviewing what it runs before approving.

## 1. What It Is

Open Interpreter is a Python application from the OpenInterpreter org (OpenInterpreter/open-interpreter), AGPL-3.0. Active. Lets LLMs execute code locally to perform general tasks; effectively a code-execution agent for any data or system task.

## 2. Install

Platforms: macOS, Linux, Windows. Requires Python 3.

```bash
# From GitHub (latest)
pip install git+https://github.com/OpenInterpreter/open-interpreter.git

# PyPI (stable)
pip install open-interpreter
```

Also runnable in Google Colab (interactive demo available). A desktop app with early access is in development ([signup](https://0ggfznkwh4j.typeform.com/to/G21i9lJ2)).

## 3. Interfaces

- **CLI**: Primary interface; run `interpreter` after install to start an interactive ChatGPT-like REPL in the terminal.
- **Python API**: Import and use programmatically (`from interpreter import interpreter`); supports streaming, message history save/restore, and custom system messages.
- **Desktop app (early access)**: Native app in development; signup required.
- No TUI, no IDE extension, no hosted web UI.
- Headless: supported via Python API — pass messages directly to `.chat(message)` without launching interactive mode.
- Remote: runs over SSH as a standard Python process.

## 4. Model Compatibility

Open Interpreter uses [LiteLLM](https://docs.litellm.ai/docs/providers/) to connect to language models, giving access to virtually all major providers:

- **OpenAI** (GPT-4o, GPT-3.5-turbo — default), **Anthropic** (Claude 2+), **Cohere** (Command Nightly), **Google**, and any model listed in LiteLLM's provider registry.
- **Local models**: Any OpenAI-compatible server (LM Studio, Jan.ai, Ollama, Llamafile) via `--api_base` and a dummy key. `--local` flag sets a local-friendly context window automatically.

```bash
interpreter --model claude-2 --api-key anthropic=<key>
interpreter --api_base "http://localhost:1234/v1" --api_key fake_key
```

BYOK: yes. No bundled model; no provider lock-in.

## 5. Capabilities

Open Interpreter executes code in Python, JavaScript, Shell, and other languages locally to accomplish tasks: file manipulation, data analysis, chart generation, web scraping, and system automation. It can browse the web by generating and running browser-control code. Vision is supported when using a multimodal model (image paths or screenshots can be passed as messages).

## 6. MCP Support

Not natively supported. MCP integration is not documented; the project predates MCP's wide adoption and uses its own tool-call loop rather than the MCP protocol.

## 7. Extensibility

Behaviour is customised via the Python API: set `interpreter.system_message`, `interpreter.llm.model`, `interpreter.computer.languages` to add/remove language kernels, and `interpreter.tools` to register custom tools. Custom language kernels can be added as Python classes. No plugin registry or hook system; scripting is done by wrapping the Python API directly.

## 8. Documented Strengths

Documented strengths from maintainer docs, benchmarks, or independent reviews. Cite source.

## 9. Documented Weaknesses

Documented limitations from issue tracker, docs, or community reports. Cite source.

## 10. Sources

- [OpenInterpreter/open-interpreter](https://github.com/OpenInterpreter/open-interpreter) — observed 2026-06-14
