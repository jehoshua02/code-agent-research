# Continue

_Last verified: 2026-06-14_

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

- [continuedev/continue](https://github.com/continuedev/continue) — observed 2026-06-14
