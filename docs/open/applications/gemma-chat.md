# Gemma Chat

_Last verified: 2026-06-14_

## 0. TL;DR

Gemma Chat is a local AI chat and [coding agent](../GLOSSARY.md#agent) for Apple Silicon Macs that runs Google's Gemma 4 model entirely on-device via MLX — no API key, no cloud, your data stays on your machine. Pick it if you are on a Mac with Apple Silicon, have already chosen Gemma as your [model](../GLOSSARY.md#model), and want a polished chat UI with agent capabilities without sending anything to a third-party server. The main catch is that it is Apple Silicon-only (no Intel Mac, no Linux, no Windows) and model-specific, so it is not the right choice if you want to swap between providers.

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

Targets local chat and project scaffolding (Build mode): generates multi-file codebases from a prompt in any language Gemma 4 supports, with a live preview canvas for web projects. No shell execution, file-system write access outside the preview sandbox, browser tool, or data-analysis environment. Vision is available when a multimodal Gemma 4 variant is selected.

## 6. MCP Support

Not supported. Gemma Chat is a self-contained Electron app with no plugin protocol or MCP integration documented.

## 7. Extensibility

No plugin or skill system. The app is intentionally minimal: behaviour is defined in the Electron/React source (`src/`). Customisation requires forking the repo and modifying the TypeScript source directly.

## 8. Documented Strengths

- **Fully offline after first download**: All inference runs locally via MLX-LM on Apple Silicon with no network dependency after the initial ~3 GB model pull — zero data leaves the machine. ([README](https://github.com/ammaarreshi/gemma-chat))
- **Live preview canvas for web projects**: Build mode streams generated files to a sandboxed preview pane that updates as the model types, giving instant visual feedback on scaffolded web projects. ([README](https://github.com/ammaarreshi/gemma-chat))
- **Hot-swappable model variants**: Four Gemma 4 sizes (E2B ~1.5 GB through 31B ~18 GB) are selectable at runtime without reinstalling, letting users trade speed for capability. ([README](https://github.com/ammaarreshi/gemma-chat))
- **Per-conversation sandbox isolation**: Each conversation runs in its own workspace, preventing file collisions between concurrent projects. ([README](https://github.com/ammaarreshi/gemma-chat))

## 9. Documented Weaknesses

- **Apple Silicon exclusive**: Requires macOS on Apple Silicon — no Intel Mac, Linux, or Windows support — eliminating it for most developer environments. ([README](https://github.com/ammaarreshi/gemma-chat))
- **Model loading failures on fresh install**: Multiple users report Gemma 4 models broken on fresh install and downloads stalling on the final file (issue #29, #27), with no automated recovery. ([issue tracker](https://github.com/ammaarreshi/gemma-chat/issues))
- **Port conflict with Ollama**: The MLX server binds port 11434 — the same default as Ollama — causing a collision that prevents launch when Ollama is already running. ([issue #7](https://github.com/ammaarreshi/gemma-chat/issues/7))
- **Agent loop capped at 40 rounds**: Autonomous Build-mode tasks are hard-limited to 40 back-and-forth rounds per user message, which may be insufficient for large or complex codebases. ([README](https://github.com/ammaarreshi/gemma-chat))

## 10. Sources

- [ammaarreshi/gemma-chat](https://github.com/ammaarreshi/gemma-chat) — observed 2026-06-14
