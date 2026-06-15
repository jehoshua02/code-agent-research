# Aider

_Last verified: 2026-06-14_

## 0. TL;DR

Aider is a [coding agent](../GLOSSARY.md#agent) you run in your terminal that pair-programs with you over your git history, turning every LLM edit into a real commit so you always have a clean undo path. Pick it if you want git-native pair programming, deep repo-wide context, and a mature [agentic loop](../GLOSSARY.md#agent-loop) that has been battle-tested across many [LLM](../GLOSSARY.md#llm) providers. The main catch is that it's a CLI-only tool — there's no built-in GUI, so if you prefer clicking over typing it may feel spartan.

## 1. What It Is

Aider is an Apache-2.0 Python application from Aider-AI / Paul Gauthier (Aider-AI/aider). Active. Agentic coding CLI that pair-programs over git, applying edits as commits with strong support for repo-wide context.

## 2. Install

Platforms: macOS, Linux, Windows. Requires Python 3.9+.

```bash
# Recommended (bootstraps into an isolated environment)
python -m pip install aider-install
aider-install

# Direct pip install
python -m pip install aider-chat

# pipx (isolated)
pipx install aider-chat
```

After install, run `aider` from inside a git repository. Pass API keys via environment variables or `--api-key` flags.

## 3. Interfaces

- **CLI**: Primary interface; interactive REPL in the terminal with `/commands` for control.
- **"Watch" mode for IDE integration**: Aider monitors files for AI-comment triggers (`# AI: ...`), letting any editor drive it passively without a plugin.
- No dedicated TUI beyond the interactive CLI prompt, no web UI, no IDE extension, no mobile app.
- Headless/non-interactive: supported via `--yes` flag and message piping for CI scripting.
- Remote: not built-in; can run over SSH as a standard terminal process.

## 4. Model Compatibility

Aider supports virtually any LLM via its own provider abstraction. Confirmed providers include:

- **Anthropic** (Claude 3.5/3.7 Sonnet — recommended), **OpenAI** (GPT-4o, o1, o3-mini), **DeepSeek** (R1, Chat V3), **Google Gemini**, **OpenRouter**, **Azure OpenAI**, **Cohere**, **Ollama** (local), **LM Studio**, and any OpenAI-compatible endpoint.

BYOK: yes — each provider requires its own API key set via env var or `--api-key <provider>=<key>`. No bundled model; no provider lock-in. Ranks models on its own leaderboard at [aider.chat/docs/leaderboards](https://aider.chat/docs/leaderboards/).

## 5. Capabilities

Aider specialises in multi-file coding tasks across any language (strong defaults for Python, JavaScript/TypeScript, Go, Rust, and others). It edits files directly in the local git working tree and commits changes automatically; it can run shell commands via `/run` and `/test`. No built-in browser, web-fetch, or vision tool; data analysis is limited to what the LLM can do over pasted or referenced file content.

## 6. MCP Support

Not natively supported as of the last verified date. MCP integration is not documented in aider's official docs; no adapter is shipped. Community workarounds (wrapping aider behind an MCP server) exist but are unofficial.

## 7. Extensibility

Aider is extended primarily through its `.aider.conf.yml` config file (model selection, editor format, conventions) and `--system-prompt` / `--edit-format` flags. Custom `/commands` can be defined via scripting the CLI. A Python API (`from aider.coders import Coder`) allows embedding aider in larger pipelines; there is no official plugin system or hook architecture.

## 8. Documented Strengths

- **SWE-bench Lite SOTA (26.3%).** Aider reached state-of-the-art on SWE-bench Lite in May 2024, surpassing the previous leader (Amazon Q, 20.3%); uses a repo-map via static analysis rather than RAG ([aider.chat/2024/05/22/swe-bench-lite](https://aider.chat/2024/05/22/swe-bench-lite.html)).
- **Git-native workflow.** Every edit is committed automatically with a sensible message; undo is a plain `git revert`. Linting and tests run on every change ([README](https://github.com/Aider-AI/aider)).
- **Broad model leaderboard.** Maintains a live polyglot coding leaderboard across 225 Exercism exercises in 6 languages; top model (GPT-5 high) scores 88.0% ([aider.chat/docs/leaderboards](https://aider.chat/docs/leaderboards/)).
- **46 K+ GitHub stars and active releases.** Consistent weekly releases; large contributor base signals sustained community maintenance ([GitHub](https://github.com/Aider-AI/aider)).

## 9. Documented Weaknesses

- **No MCP support.** MCP integration is not documented; community workarounds are unofficial ([§6 above](#6-mcp-support)).
- **Security: untrusted repo config execution.** Opening an untrusted repository auto-executes commands from `.aider.conf.yml` without confirmation ([GitHub issues](https://github.com/aider-ai/aider/issues)).
- **Cannot delete files.** The agent can create files but not delete them, a gap in file-manipulation capability that surprises users ([GitHub issues](https://github.com/aider-ai/aider/issues)).
- **API rate-limit handling.** Rate-limit errors from Anthropic and other providers lack automatic backoff, causing silent failures in long sessions ([GitHub issues and Dispatch Report](https://thedispatch.ai/reports/1385/)).

## 10. Sources

- [Aider-AI/aider](https://github.com/Aider-AI/aider) — observed 2026-06-14
