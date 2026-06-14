# Code Agent Research

Research and comparison of AI coding tools — agents, IDEs, extensions, and CLIs.

## Structure

```
docs/
  tools/              — One folder per tool, each with a README.md
    TEMPLATE.md       — Standard structure for tool docs
    antigravity/
    augment/
    claude-code/
    cline/
    codebuddy/
    codex/
    copilot/
    cursor/
    gemini-cli/
    hermes-agent/
    kilo/
    opencode/
    qwen-code/
    trae/
    windsurf/
    comparison/         — Tool comparison guides
  models/               — One folder per model family, each with a README.md
    TEMPLATE.md         — Standard structure for model docs
    claude/
    deepseek/
    gemini/
    gpt/
    grok/
    hunyuan/
    llama/
    qwen-coder/
    swe-1/
    comparison/         — Model comparison guides
```

## Tools Covered

| Tool | Type | Maker |
|------|------|-------|
| [Antigravity](docs/tools/antigravity/) | IDE (VS Code fork) | Google |
| [Augment](docs/tools/augment/) | IDE plugin + CLI + desktop | Augment Code |
| [Claude Code](docs/tools/claude-code/) | CLI agent | Anthropic |
| [Cline](docs/tools/cline/) | VS Code extension | Cline Bot Inc. |
| [CodeBuddy](docs/tools/codebuddy/) | IDE + plugin + CLI | Tencent |
| [Codex](docs/tools/codex/) | CLI agent + cloud agent | OpenAI |
| [Copilot](docs/tools/copilot/) | IDE plugin + cloud agent | GitHub/Microsoft |
| [Cursor](docs/tools/cursor/) | IDE (VS Code fork) | Anysphere |
| [Gemini CLI](docs/tools/gemini-cli/) | CLI agent | Google |
| [Hermes Agent](docs/tools/hermes-agent/) | Autonomous agent runtime | Nous Research |
| [Kilo](docs/tools/kilo/) | VS Code/JetBrains extension | Kilo Code |
| [OpenCode](docs/tools/opencode/) | CLI/TUI agent | Anomaly Co |
| [Qwen Code](docs/tools/qwen-code/) | CLI agent | Alibaba |
| [Trae](docs/tools/trae/) | IDE (VS Code fork) | ByteDance |
| [Windsurf](docs/tools/windsurf/) | IDE (VS Code fork) | Cognition AI |

## Models Covered

| Model Family | Maker | Open Weight | Self-Hostable |
|---|---|---|---|
| [Claude](docs/models/claude/) | Anthropic | No | No |
| [DeepSeek](docs/models/deepseek/) | DeepSeek | Yes (MIT) | Yes |
| [Gemini](docs/models/gemini/) | Google | No | No |
| [GPT](docs/models/gpt/) | OpenAI | No | No |
| [Grok](docs/models/grok/) | xAI | No | No |
| [Hunyuan](docs/models/hunyuan/) | Tencent | Partial | Partial |
| [Llama](docs/models/llama/) | Meta | Yes | Yes |
| [Qwen Coder](docs/models/qwen-coder/) | Alibaba | Yes (Apache 2.0) | Yes |
| [SWE-1](docs/models/swe-1/) | Windsurf/Codeium | No | No |

## Comparisons

- [Tool Comparison (May 3, 2026)](docs/tools/comparison/comparison-2026-05-03.md) — Feature matrix, deep-dives, decision guide
- [Model Comparison (May 3, 2026)](docs/models/comparison/comparison-2026-05-03.md) — Benchmarks, cost, self-hosting, head-to-head matchups

## Open Self-Hosted Survey

[docs/open/](docs/open/) — Survey of the open, free, self-hostable AI ecosystem: models, runtimes, agent frameworks, MCP servers, techniques. Task-agnostic (coding + research + writing + automation + data).
