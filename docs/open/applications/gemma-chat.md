# Gemma Chat

_Last verified: 2026-06-14_

## 1. What It Is

Gemma Chat (ammaarreshi/gemma-chat) is an MIT-licensed TypeScript application. Active. Local AI chat + coding agent for Apple Silicon powered by Google's Gemma 4 via MLX, with Ollama support. Model-specific by design — the user has already chosen Gemma; the application is optimized around that choice.

## 2. Install

Platform: macOS on Apple Silicon only. Requirements: Python 3.10–3.13, Node 20+.

```bash
git clone https://github.com/ammaarreshi/gemma-chat-public.git
cd gemma-chat-public
npm install
npm run dev
```

First launch auto-provisions a Python venv, installs MLX-LM, and downloads the model (~3 GB). Build a distributable `.dmg` with `npm run dist`. See [../README.md](../README.md#4-deployment-notes) for general reader-facing deployment context.

## 3. Interfaces

Desktop app (Electron + React 19 + TypeScript + Tailwind). No CLI, TUI, or API surface. Chat and Build modes in a single window with a live preview canvas for generated projects.

## 4. Model Compatibility

Bundled Gemma 4 via MLX-LM (local venv, Apple Silicon only). Four variants selectable at runtime: Gemma 4 E2B (~1.5 GB), Gemma 4 E4B (~3 GB, recommended), Gemma 4 27B MoE (~8 GB), Gemma 4 31B (~18 GB). Model-specific — no general OpenAI-compat or Ollama backend; Gemma only.

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

- [ammaarreshi/gemma-chat](https://github.com/ammaarreshi/gemma-chat) — observed 2026-06-14
