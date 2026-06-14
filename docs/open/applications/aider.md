# Aider

_Last verified: 2026-06-14_

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

- [Aider-AI/aider](https://github.com/Aider-AI/aider) — observed 2026-06-14
