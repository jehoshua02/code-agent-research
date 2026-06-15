# Continue

_Last verified: 2026-06-14_

## 0. TL;DR

Continue is an IDE extension for VS Code and JetBrains that wires a self-hosted or cloud [LLM](../GLOSSARY.md#llm) directly into your editor — similar to GitHub Copilot but fully open-source and pointed at any model you choose. Pick it if you spend most of your time in VS Code or a JetBrains IDE and want AI completions and chat without leaving your editor or paying a SaaS subscription. The main catch is that the repository is archived as of 2026 (a final 2.0.0 was shipped but active development has stopped), so the [agentic loop](../GLOSSARY.md#agent-loop) is less mature than Aider's and future compatibility is uncertain.

## 1. What It Is

Continue is an Apache-2.0 TypeScript application from Continue Dev (continuedev/continue). Active. Open-source IDE extension (VS Code, JetBrains) for agentic coding with custom commands, models, and contexts.

## 2. Install

Platforms: any OS where VS Code or JetBrains IDEs run (macOS, Linux, Windows); the CLI is Node.js-based.

> **Note:** The `continuedev/continue` repository is read-only (archived) as of 2026. A final 2.0.0 release was published; it remains installable but is not actively maintained.

**VS Code extension** (primary):

```
# From VS Code Marketplace
ext install Continue.continue

# Or search "Continue" in the Extensions panel
```

Also available on the [OpenVSX Registry](https://open-vsx.org/extension/Continue/continue) for VS Code-compatible editors (e.g., VSCodium).

**CLI** (Node.js):

```bash
npm install -g @continuedev/cli
```

**JetBrains plugin**: Available via GitHub Releases; install `.zip` manually. The maintainers recommend the CLI over the JetBrains plugin going forward.

## 3. Interfaces

- **VS Code extension**: Chat sidebar, inline Edit mode, Autocomplete, and an Agent mode for autonomous development tasks.
- **JetBrains plugin**: Equivalent to the VS Code extension for IntelliJ-family IDEs; feature parity is lower than VS Code.
- **CLI**: Standalone terminal interface (`@continuedev/cli` on npm); works outside an IDE.
- No standalone web UI, no mobile app.
- Headless: the CLI can be scripted; the IDE extensions require a running IDE.

## 4. Model Compatibility

Continue is provider-agnostic and configurable. Supported providers documented in the project include:

- **Anthropic** (Claude), **OpenAI** (GPT-4o, etc.), **Google Gemini**, **Mistral**, **Cohere**, **AWS Bedrock**, **Azure OpenAI**, **Ollama** (local), **LM Studio**, **Llamafile**, and any OpenAI-compatible endpoint.

BYOK: yes — provider credentials are set in a `config.json` file per workspace. No bundled model; no provider lock-in.

## 5. Capabilities

Continue targets IDE-integrated coding assistance: inline autocomplete, chat over selected code, multi-file edits via Agent mode, and codebase-wide context retrieval through embeddings. It can read and write files within the IDE workspace and run terminal commands via Agent mode. No built-in browser tool or vision input; data analysis is limited to in-editor context.

## 6. MCP Support

Native MCP client support was added in v1.0 (late 2024). Continue can connect to any MCP server declared in `config.json` under the `mcpServers` key, exposing MCP tools as slash commands or context providers inside the IDE. Maturity is documented as stable for client consumption.

## 7. Extensibility

Extensibility lives in `~/.continue/config.json` (or a workspace-level override): custom slash commands (arbitrary prompts or TypeScript functions), context providers (pull in docs, repos, web pages, databases), and model providers are all config-driven. The SDK (`@continuedev/config-types`) allows TypeScript-based custom context providers and commands to be written as local packages and loaded via the config.

## 8. Documented Strengths

Documented strengths from maintainer docs, benchmarks, or independent reviews. Cite source.

## 9. Documented Weaknesses

Documented limitations from issue tracker, docs, or community reports. Cite source.

## 10. Sources

- [continuedev/continue](https://github.com/continuedev/continue) — observed 2026-06-14
