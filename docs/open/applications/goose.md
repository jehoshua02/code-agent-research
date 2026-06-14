# Goose

_Last verified: 2026-06-14_

## 1. What It Is

Goose is an Apache-2.0 Rust application originally from Block (block/goose), now under the Linux Foundation's AAIF (aaif-goose/goose). Active. General-purpose open-source AI agent with extensible toolkit and MCP support.

## 2. Install

Platforms: macOS, Linux, Windows. Built in Rust. The repo moved from `block/goose` to `aaif-goose/goose` under the Linux Foundation's AAIF.

**Desktop app** (macOS, Linux, Windows): download from [goose-docs.ai/docs/getting-started/installation](https://goose-docs.ai/docs/getting-started/installation).

**CLI**:

```bash
curl -fsSL https://github.com/aaif-goose/goose/releases/download/stable/download_cli.sh | bash
```

Also available via system package managers (Repology tracks packaging status across distros).

## 3. Interfaces

- **Desktop app**: Native GUI for macOS, Linux, and Windows; primary graphical interface.
- **CLI**: Full terminal interface for scripting and terminal workflows.
- **API**: Embeddable API surface for integrating Goose into other applications.
- No dedicated IDE extension or mobile app.
- Headless: yes — CLI supports non-interactive / scripted use.
- Multi-client: not documented in README; the desktop app and CLI are independent.

## 4. Model Compatibility

Goose works with 15+ providers out of the box:

- **Anthropic** (Claude), **OpenAI** (GPT-4o, etc.), **Google** (Gemini), **Ollama** (local), **OpenRouter**, **Azure OpenAI**, **AWS Bedrock**, and more.
- Existing ChatGPT, Claude, and Gemini subscriptions can be used via [ACP (Agent Connectivity Protocol)](https://goose-docs.ai/docs/guides/acp-providers) — BYOK or subscription-based.
- 70+ extensions via MCP.

BYOK: yes. No bundled model; no provider lock-in. Provider credentials configured at setup.

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

- [block/goose](https://github.com/block/goose) — observed 2026-06-14
