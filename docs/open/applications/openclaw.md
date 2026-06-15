# OpenClaw

_Last verified: 2026-06-14_

## 0. TL;DR

OpenClaw is a cross-platform personal AI assistant (released November 2025) built around a community Skills Registry of 5,400+ skills — think of it as a general-purpose [agent](../GLOSSARY.md#agent) you extend by installing skills rather than writing plugins from scratch. Pick it if you want a breadth-first assistant that can handle coding, research, and everyday automation through a rich extension ecosystem rather than a coding-only tool. Being new and niche, the skills registry quality varies widely and the community is still small, so expect more rough edges than in mature tools like Aider or OpenHands.

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

- **Massive multi-channel reach**: Supports 22+ messaging platforms (WhatsApp, Telegram, Discord, Slack, iMessage, Teams, Signal, Matrix, etc.) as conversational interfaces, enabling AI access from any device without a dedicated app. ([README](https://github.com/openclaw/openclaw))
- **Skills Registry breadth**: The community ClawHub registry catalogues 44,000+ skills (as of early 2026), providing ready-made integrations for a wide range of tasks without custom coding. ([VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills))
- **Multi-provider failover and auth rotation**: Native support for credential rotation and automatic failover between providers when rate limits are hit — documented as a first-class feature. ([docs.openclaw.ai](https://docs.openclaw.ai/concepts/model-failover))
- **Persistent Gateway daemon**: Runs as a system service (launchd/systemd), surviving reboots and enabling always-on automation and scheduled tasks without a running terminal. ([README](https://github.com/openclaw/openclaw))

## 9. Documented Weaknesses

- **Supply-chain risk in Skills Registry**: The ClawHavoc campaign (February 2026) found 341 malicious skills distributed via ClawHub; broader scanning flagged 7.6% of 31,000+ audited skills as risky. ([DataCamp blog](https://www.datacamp.com/blog/what-is-openclaw))
- **Security CVEs with high severity**: Over 60 security advisories filed since launch, including CVE-2026-32922 (CVSS 9.9) and CVE-2026-25253 (CVSS 8.8); 220,000+ instances were publicly internet-reachable at peak. ([DataCamp blog](https://www.datacamp.com/blog/what-is-openclaw))
- **Unexpected token costs**: Each heartbeat, tool call, and sub-task step is a separate API call; users frequently report bills far higher than anticipated for multi-step automations. ([DataCamp blog](https://www.datacamp.com/blog/what-is-openclaw))
- **Setup complexity not beginner-friendly**: Requires terminal proficiency, file-permission knowledge, API key management, and daemon configuration; 3,500+ open issues and 3,200+ open PRs reflect ongoing rough edges at scale. ([DataCamp blog](https://www.datacamp.com/blog/what-is-openclaw); [issue tracker](https://github.com/openclaw/openclaw/issues))

## 10. Sources

- [openclaw/openclaw](https://github.com/openclaw/openclaw) — observed 2026-06-14
- [openclaw.ai](https://openclaw.ai) — observed 2026-06-14
