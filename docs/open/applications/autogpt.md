# AutoGPT

_Last verified: 2026-06-14_

## 0. TL;DR

AutoGPT was the first viral autonomous-[agent](../GLOSSARY.md#agent) project — it showed the world that you could hand an [LLM](../GLOSSARY.md#llm) a goal and let it plan and act in a loop without human hand-holding at every step. Today the original self-prompting loop is still there, but the project has evolved into a hosted platform tier (Polyform Shield licensed) that dominates the roadmap; the MIT core agent is largely a foundation for that cloud service. Pick AutoGPT if you want to experiment with the historical blueprint of autonomous agents or try the managed platform; go to Aider or OpenHands if you want a focused, actively developed open-source coding agent.

## 1. What It Is

AutoGPT is a Python application from Significant Gravitas (Significant-Gravitas/AutoGPT), MIT for the core agent and Polyform Shield for the platform tier. Active. Early autonomous-agent project that pioneered iterative goal pursuit with self-prompting.

## 2. Install

Platforms: Linux (Ubuntu 20.04+), macOS (10.15+), Windows 10/11 with WSL2. Docker + Docker Compose required for the platform; Node.js 16+, npm 8+, and Git also needed.

```bash
# macOS/Linux — one-line installer (recommended)
curl -fsSL https://setup.agpt.co/install.sh -o install.sh && bash install.sh

# Windows (PowerShell)
powershell -c "iwr https://setup.agpt.co/install.bat -o install.bat; ./install.bat"

# Manual: clone + Docker Compose
git clone https://github.com/Significant-Gravitas/AutoGPT.git
cd AutoGPT
# follow https://agpt.co/docs/platform/getting-started/getting-started
```

Minimum hardware: 4-core CPU, 8 GB RAM, 10 GB storage. The classic stand-alone agent (outside `autogpt_platform/`) can be run via the `./run` CLI without Docker.

## 3. Interfaces

- **Web UI (platform)**: Low-code Agent Builder for connecting blocks into workflows; Workflow Management; Deployment Controls; Agent Marketplace; Monitoring & Analytics.
- **CLI (classic)**: `./run agent start` / `./run benchmark` for the original stand-alone agent and Forge-based agents.
- **Agent protocol REST API**: Agents expose a standard agent-protocol API, usable by the CLI frontend and third-party clients.
- **Cloud-hosted beta**: [app.agpt.co](https://app.agpt.co) (closed beta as of 2026-06-14; waitlist open).
- No dedicated TUI, IDE extension, or mobile app.
- Headless: classic agent can run non-interactively; platform agents are triggered by external sources and run continuously.

## 4. Model Compatibility

The platform is designed for OpenAI GPT-4/o-series models (primary). The classic agent also supports Anthropic Claude and Azure OpenAI via configuration. OpenAI-compatible endpoints and open/local models are possible with additional setup (documented in the classic agent's open-models guide). BYOK: yes — API keys are set via `.env` file. No bundled model; the platform tier has stronger coupling to OpenAI by default.

## 5. Capabilities

AutoGPT targets general autonomous task execution: web search and browsing, file reading and writing, shell command execution (classic agent), and code generation. The platform edition focuses on multi-step workflow automation via visual block graphs rather than raw coding. Vision and data analysis capabilities depend on the underlying model.

## 6. MCP Support

Not supported natively. MCP is not referenced in AutoGPT's official documentation as of the last verified date. The platform uses its own block-based tool abstraction; MCP integration would require a custom block or adapter.

## 7. Extensibility

The platform is extended through custom blocks (Python classes registered in the block registry under `autogpt_platform/`). The classic Forge-based agent supports plugin-style skills. Workflow logic lives in the visual Agent Builder (web UI) and is serialised as a graph in the platform database; scripted agents are written against the Forge SDK.

## 8. Documented Strengths

- **Pioneered the autonomous agent paradigm.** Released two weeks after GPT-4 (March 2023), AutoGPT was the first project to demonstrate LLM goal-pursuit loops, catalysing the entire autonomous-agent ecosystem ([vibeagentmaking.com](https://vibeagentmaking.com/blog/autogpt-got-100k-stars-and-then-what/)).
- **183 K GitHub stars.** Remains one of the most-starred AI repositories on GitHub, reflecting its historical influence and ongoing community interest ([Tencent Cloud comparison, 2026](https://www.tencentcloud.com/techpedia/144032)).
- **Visual low-code Agent Builder.** The 2024 platform redesign introduced a block-graph workflow UI, making multi-step automation accessible without coding ([agpt.co docs](https://agpt.co/docs/platform/getting-started/getting-started)).

## 9. Documented Weaknesses

- **Original loop deprecated for platform.** The self-prompting loop has been superseded by the Polyform-licensed platform; the MIT core agent is largely unmaintained as a standalone tool ([vibeagentmaking.com](https://vibeagentmaking.com/blog/autogpt-got-100k-stars-and-then-what/)).
- **Compound reliability failure.** An ~85% per-step success rate yields only ~20% end-to-end success over 10 steps; agents frequently hallucinate and enter infinite loops ([vibeagentmaking.com](https://vibeagentmaking.com/blog/autogpt-got-100k-stars-and-then-what/)).
- **Heavy API costs.** Recursive GPT-4 calls ($0.03–0.06/1 K tokens) stack quickly; model-switching to GPT-3.5 collapsed performance ([vibeagentmaking.com](https://vibeagentmaking.com/blog/autogpt-got-100k-stars-and-then-what/)).
- **Eclipsed by focused alternatives.** Community reviews note AutoGPT has been "largely eclipsed" by tools like CrewAI and OpenHands that offer more predictable multi-agent workflows ([vibeagentmaking.com](https://vibeagentmaking.com/blog/autogpt-got-100k-stars-and-then-what/)).

## 10. Sources

- [Significant-Gravitas/AutoGPT](https://github.com/Significant-Gravitas/AutoGPT) — observed 2026-06-14
