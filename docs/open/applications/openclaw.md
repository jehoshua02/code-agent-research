# OpenClaw

_Last verified: 2026-06-14_

## 1. What It Is

OpenClaw is an MIT-licensed TypeScript application from the OpenClaw Foundation (openclaw/openclaw). Active, released November 2025. Cross-platform personal AI assistant ("Your own personal AI assistant. Any OS. Any Platform"); category is general-purpose agentic application with a skills-based extension model (a community Skills Registry catalogs 5,400+ skills).

## 2. Install

Platforms: macOS, Linux, Windows. Node.js 24 (recommended) or Node.js 22.19+ required.

```bash
# Recommended — guided onboarding installer
npm install -g openclaw@latest
openclaw onboard --install-daemon

# pnpm alternative
pnpm add -g openclaw@latest
```

`openclaw onboard` installs a system daemon (launchd on macOS, systemd on Linux) that keeps the Gateway running. Windows users can also use the [Windows Hub](https://docs.openclaw.ai/platforms/windows) native companion app for GUI-driven setup.

Docker is also supported: [docs.openclaw.ai/install/docker](https://docs.openclaw.ai/install/docker).

## 3. Interfaces

- **CLI**: Primary control plane — `openclaw gateway`, `openclaw message send`, `openclaw agent`, etc.
- **Companion apps**: Windows Hub (tray app + native chat + node mode), macOS menu bar app, iOS and Android apps (voice wake, Talk mode).
- **Live Canvas**: Agent-driven visual workspace (A2UI) on macOS.
- **Web surfaces**: Gateway exposes a web interface and remote access via Tailscale.
- **Multi-channel messaging**: WhatsApp, Telegram, Discord, Slack, Signal, iMessage, Microsoft Teams, Matrix, IRC, and 15+ more channels serve as conversational interfaces.
- Headless: yes — the Gateway daemon runs as a background service; CLI is fully scriptable.
- Multi-client/remote: yes — the Gateway can be exposed remotely (Tailscale or direct); multiple channels route to isolated agent workspaces.

## 4. Model Compatibility

OpenClaw supports multiple providers with a `<provider>/<model-id>` syntax in config. Documented providers include **OpenAI** (GPT-4o, Codex; primary sponsor) and "many providers and models." The docs reference [auth profile rotation and failover](https://docs.openclaw.ai/concepts/model-failover), implying support for Anthropic, Google, and others (exact list at [docs.openclaw.ai/concepts/models](https://docs.openclaw.ai/concepts/models)). BYOK: yes — provider credentials are stored in `~/.openclaw/openclaw.json`. No bundled model.

## 5. Capabilities

General-purpose assistant targeting coding (language-agnostic via provider model), shell execution, file editing, web browsing/search, and vision (when a multimodal model is configured). Multi-channel messaging surfaces (WhatsApp, Telegram, Discord, etc.) extend reach beyond the terminal. Data-analysis tasks are handled through shell and scripting skills in the community registry.

## 6. MCP Support

Native. OpenClaw ships with MCP support as a first-class integration; MCP servers can be registered via the Gateway config and are surfaced alongside built-in tools. No adapter layer required.

## 7. Extensibility

Skills are the primary extension unit: packaged TypeScript/JavaScript modules published to the community Skills Registry (5,400+ skills). Custom skills live in `~/.openclaw/skills/` or can be loaded from a local path in `openclaw.json`. Hooks and custom agents are configured in the same JSON file. The Gateway daemon and agent runtime are defined in the TypeScript source under `packages/`.

## 8. Documented Strengths

Documented strengths from maintainer docs, benchmarks, or independent reviews. Cite source.

## 9. Documented Weaknesses

Documented limitations from issue tracker, docs, or community reports. Cite source.

## 10. Sources

- [openclaw/openclaw](https://github.com/openclaw/openclaw) — observed 2026-06-14
- [openclaw.ai](https://openclaw.ai) — observed 2026-06-14
