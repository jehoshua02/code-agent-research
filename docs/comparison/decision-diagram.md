# Decision Diagram: Choosing an AI Coding Tool
**May 3, 2026**

## Flowchart

```mermaid
flowchart TD
    START([What kind of developer are you?]) --> INTERFACE{Where do you work?}

    INTERFACE -->|Terminal / CLI| CLI_PATH
    INTERFACE -->|IDE / Editor| IDE_PATH
    INTERFACE -->|Both / Flexible| BOTH_PATH

    %% === CLI PATH ===
    CLI_PATH{Is open source important?}
    CLI_PATH -->|Yes| CLI_OSS{Need fully self-hosted<br/>including the model?}
    CLI_PATH -->|No| CLI_CLOSED{What matters most?}

    CLI_OSS -->|Yes — air-gap / privacy| QWEN([Qwen Code])
    CLI_OSS -->|No — open source CLI,<br/>cloud inference is fine| CLI_OSS_CLOUD{Biggest priority?}

    CLI_OSS_CLOUD -->|Free tier / low cost| GEMINI([Gemini CLI])
    CLI_OSS_CLOUD -->|Max model flexibility| OPENCODE([OpenCode])
    CLI_OSS_CLOUD -->|GitHub integration| CODEX([Codex CLI])

    CLI_CLOSED -->|Best benchmark scores /<br/>hardest tasks| CLAUDE([Claude Code])
    CLI_CLOSED -->|Free tier /<br/>budget conscious| GEMINI

    %% === IDE PATH ===
    IDE_PATH{Do you want a new editor<br/>or keep your current one?}
    IDE_PATH -->|New AI-native editor| IDE_FORK{Biggest priority?}
    IDE_PATH -->|Keep VS Code / JetBrains| EXTENSION_PATH

    IDE_FORK -->|Best AI features /<br/>background agents| CURSOR([Cursor])
    IDE_FORK -->|Proprietary SWE models /<br/>codebase visualization| WINDSURF([Windsurf])
    IDE_FORK -->|Free tier /<br/>zero cost| FREE_IDE{Privacy concerns ok?}

    FREE_IDE -->|Yes — ByteDance telemetry ok| TRAE([Trae])
    FREE_IDE -->|No — prefer Google| ANTIGRAVITY([Antigravity])

    %% === EXTENSION PATH ===
    EXTENSION_PATH{What matters most?}
    EXTENSION_PATH -->|Enterprise / team /<br/>GitHub integration| COPILOT([GitHub Copilot])
    EXTENSION_PATH -->|Model freedom /<br/>open source| EXT_OSS{VS Code only ok?}
    EXTENSION_PATH -->|Large codebase /<br/>multi-repo| AUGMENT([Augment Code])
    EXTENSION_PATH -->|Full lifecycle /<br/>WeChat / China market| CODEBUDDY([CodeBuddy])

    EXT_OSS -->|Yes — VS Code only| CLINE([Cline])
    EXT_OSS -->|Need JetBrains too| KILO([Kilo Code])

    %% === BOTH PATH ===
    BOTH_PATH{What's the use case?}
    BOTH_PATH -->|Long-lived personal agent /<br/>cross-session memory| HERMES([Hermes Agent])
    BOTH_PATH -->|Daily coding —<br/>IDE + terminal flexibility| BOTH_DAILY{Budget?}

    BOTH_DAILY -->|Free / cheap| OPENCODE
    BOTH_DAILY -->|Will pay for best| BEST_COMBO{Prefer Anthropic<br/>or multi-model?}

    BEST_COMBO -->|Anthropic models| CLAUDE
    BEST_COMBO -->|Multi-model choice| CURSOR

    %% === STYLING ===
    classDef tool fill:#2d6a4f,stroke:#1b4332,color:#fff,font-weight:bold
    classDef decision fill:#264653,stroke:#2a9d8f,color:#fff
    classDef start fill:#e76f51,stroke:#f4a261,color:#fff,font-weight:bold

    class START start
    class INTERFACE,CLI_PATH,CLI_OSS,CLI_OSS_CLOUD,CLI_CLOSED,IDE_PATH,IDE_FORK,FREE_IDE,EXTENSION_PATH,EXT_OSS,BOTH_PATH,BOTH_DAILY,BEST_COMBO decision
    class CLAUDE,OPENCODE,GEMINI,CODEX,QWEN,CURSOR,WINDSURF,TRAE,ANTIGRAVITY,COPILOT,CLINE,KILO,AUGMENT,CODEBUDDY,HERMES tool
```

## Quick Reference

Can't follow the diagram? Start here:

| If you... | Use |
|---|---|
| Want the best autonomous agent, cost no object | **Claude Code** |
| Live in the terminal, want open source + free | **Gemini CLI** |
| Live in the terminal, want max model choice | **OpenCode** |
| Want the most polished AI IDE experience | **Cursor** |
| Want an AI IDE with proprietary SWE models | **Windsurf** |
| Want a free AI IDE and accept ByteDance telemetry | **Trae** |
| Want a free AI IDE from Google | **Antigravity** |
| Already use VS Code/JetBrains, want the market leader | **GitHub Copilot** |
| Want open-source extension, model freedom, VS Code | **Cline** |
| Want open-source extension + JetBrains support | **Kilo Code** |
| Have a massive multi-repo enterprise codebase | **Augment Code** |
| Need full lifecycle + WeChat ecosystem | **CodeBuddy** |
| Need fully self-hosted, air-gapped, open-weight models | **Qwen Code** |
| Want GitHub-native automation (issue → PR) | **Codex** |
| Want a long-lived personal agent with memory | **Hermes Agent** |
