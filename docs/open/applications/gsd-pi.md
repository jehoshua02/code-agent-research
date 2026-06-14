# GSD-PI

_Last verified: 2026-06-14_

> **Borderline inclusion.** Below the ★1,000 adoption threshold (★626 as of 2026-06-14) but recent (created May 2026) and a candidate for the "distinct contribution" criterion. Revisit in 3 months when adoption stabilizes.

## 1. What It Is

GSD-PI (open-gsd/gsd-pi, npm: `@opengsd/gsd-pi`) is an MIT-licensed TypeScript application. Active, baselined at 1.0.0 in 2026. Local-first agentic coding application — TUI/web agent that plans, implements, verifies, and tracks work via a milestones/slices/tasks workflow with worktree-aware Git automation, multi-provider model routing, and an extension surface for skills/tools/commands. Distinct in organizing long-horizon autonomous work around a structured project workflow under `.gsd/` rather than ad-hoc conversation.

## 2. Install

Platforms: macOS, Linux, Windows. Node.js required (managed by the package).

```bash
# Guided installer (recommended — walks through provider and project setup)
npx @opengsd/gsd-pi@latest

# CI / scripted (non-interactive)
npx @opengsd/gsd-pi@latest --yes

# Direct global install via npm
npm install -g @opengsd/gsd-pi@latest

# pnpm global install
pnpm setup && exec $SHELL -l && pnpm dlx @opengsd/gsd-pi@latest
```

After install, run `gsd` in a project directory. State is stored under `.gsd/`. Subsequent upgrades: `gsd upgrade`.

## 3. Interfaces

- **TUI**: Primary interface; interactive terminal UI launched by `gsd`.
- **Web UI**: Optional; launch with `gsd --web` for a visual control plane when a browser-based dashboard is preferred.
- **Desktop Studio app** (`studio/` in the repo): optional companion for project oversight.
- **CLI slash commands**: `/gsd auto`, `/gsd quick "..."`, `/gsd status`, `/gsd config`, etc., used within the TUI session.
- No IDE extension, no mobile app.
- Headless: auto-mode (`/gsd auto`) runs autonomously through plan/implement/verify cycles without human input at each step.
- Remote: not documented; runs locally.

## 4. Model Compatibility

GSD-PI is multi-provider with configurable per-phase model routing. The README explicitly mentions:

- **Anthropic** (Claude Opus 4.8 as a named supported model), and "the provider your team already uses" as the selection criterion.

The GSD provider setup docs reference a providers guide ([docs/user-docs/providers.md](https://github.com/open-gsd/gsd-pi/blob/main/docs/user-docs/providers.md)); the web configurator at [pi.opengsd.net](https://pi.opengsd.net) helps choose a provider. BYOK: yes — credentials are entered during the guided install flow. No bundled model; no provider lock-in.

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

- [open-gsd/gsd-pi](https://github.com/open-gsd/gsd-pi) — observed 2026-06-14
- [opengsd.net](https://www.opengsd.net) — observed 2026-06-14
- [@opengsd/gsd-pi on npm](https://www.npmjs.com/package/@opengsd/gsd-pi) — observed 2026-06-14
