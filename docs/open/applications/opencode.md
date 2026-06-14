# OpenCode

_Last verified: 2026-06-14_

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

- [anomalyco/opencode](https://github.com/anomalyco/opencode) — observed 2026-06-14
