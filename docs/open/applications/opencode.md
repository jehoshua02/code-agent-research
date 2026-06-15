# OpenCode

_Last verified: 2026-06-14_

## 0. TL;DR

OpenCode is a [coding agent](../GLOSSARY.md#agent) you run in your terminal that reads your codebase, edits files, and runs commands for you — think GitHub Copilot but with a full [agentic loop](../GLOSSARY.md#agent-loop) instead of single completions. Pick it if you want a polished TUI experience, support for 75+ [LLM](../GLOSSARY.md#llm) providers, and don't want to be locked into one IDE or cloud vendor. The main catch is that it's TypeScript-based rather than Python, so the plugin ecosystem is smaller than Aider's.

## 1. What It Is

OpenCode is an MIT-licensed TypeScript application from Anomaly (anomalyco/opencode, formerly redirected from sst/opencode). Active. Agentic coding CLI/TUI with headless mode and IDE integrations; provider-agnostic across 75+ LLM providers.

## 2. Install

Platforms: macOS, Linux, Windows. Node.js runtime required. The repo moved from `sst/opencode` to `anomalyco/opencode` (redirects automatically).

```bash
# Curl installer (any OS)
curl -fsSL https://opencode.ai/install | bash

# npm / pnpm / bun / yarn
npm i -g opencode-ai@latest

# macOS/Linux (Homebrew, recommended — always up to date)
brew install anomalyco/tap/opencode

# Windows
scoop install opencode
choco install opencode

# Arch Linux
sudo pacman -S opencode          # stable
paru -S opencode-bin             # AUR latest

# mise (any OS)
mise use -g opencode
```

A desktop app (BETA) is also available for download at [opencode.ai/download](https://opencode.ai/download) for macOS (Apple Silicon and Intel), Windows (x64), and Linux (`.deb`, `.rpm`, `.AppImage`). macOS Homebrew cask: `brew install --cask opencode-desktop`.

## 3. Interfaces

- **TUI**: Interactive terminal UI (primary experience); runs in any terminal.
- **CLI**: Headless / non-interactive mode available for scripting and CI.
- **Desktop app (BETA)**: Native wrapper for macOS, Windows, and Linux.
- No dedicated IDE extension, web UI (browser-hosted), or mobile app.
- Remote/multi-client: not documented; the TUI is single-session per invocation.

## 4. Model Compatibility

Provider-agnostic via a built-in provider registry covering 75+ LLM providers. Confirmed providers include Anthropic (Claude), OpenAI, Google Gemini, AWS Bedrock, Azure OpenAI, OpenRouter, Ollama (local), and any OpenAI-compatible endpoint. BYOK: yes — users supply API keys via environment variables or a config file. No bundled model; no provider lock-in.

## 5. Capabilities

OpenCode targets agentic coding across any language supported by the chosen LLM. It can read and write files, run shell commands, and apply multi-file edits within a repo. Vision input is model-dependent (supported when the provider model accepts image tokens); no built-in browser or web-fetch tool is documented.

## 6. MCP Support

Native MCP support is built in. OpenCode ships as an MCP server itself (exposing its agent as an MCP tool) and can consume external MCP servers via its config file, enabling tool composition with any MCP-compatible tool provider.

## 7. Extensibility

Configuration lives in a project-level or user-level `opencode.json` / `opencode.toml`. Custom providers and models are added via the provider registry config. MCP servers are declared as tool providers in config; no plugin API or scripting hook system beyond that is documented.

## 8. Documented Strengths

Documented strengths from maintainer docs, benchmarks, or independent reviews. Cite source.

## 9. Documented Weaknesses

Documented limitations from issue tracker, docs, or community reports. Cite source.

## 10. Sources

- [anomalyco/opencode](https://github.com/anomalyco/opencode) — observed 2026-06-14
