# Trae

## What It Is

**Product category:** Standalone AI-native IDE (not a plugin/extension).
**Maker:** ByteDance (parent company of TikTok).
**Released:** January 20, 2025 (international); March 3, 2025 (Chinese domestic version).
**Name meaning:** "The Real AI Engineer."

## Pricing

**Pricing (international):**
- Free tier: limited completions per month, access to Claude 3.5 Sonnet and GPT-4o
- Pro: $3/month first month, then $10/month or $90/year ($7.50/month)
- Pro includes: 600 fast-queue requests + unlimited standard-queue requests, Claude 4, Gemini 2.5 Pro
- No enterprise pricing publicly listed as of mid-2025

## What It Does

### Core Modes
- **Chat mode:** Sidebar AI chat with context references (`#File`, `#Folder`, `#Code`, `#Workspace`)
- **Inline chat:** In-editor chat via `Cmd+I`
- **Builder mode:** Agentic project construction — plans architecture first, then executes ("think-before-doing")
- **SOLO mode:** Fully autonomous agent; takes a natural language idea, plans workflow, selects tools, executes end-to-end, produces production-ready code with documentation and structured architecture

### AI Capabilities
- Code completion with word-by-word acceptance (`Ctrl+→`) or full-line accept (`Tab`)
- Comment-driven generation (write description in comment, IDE implements it)
- Natural language debugging with step-by-step explanations
- Multi-file refactoring with automated testing loops
- Multimodal input: images, terminal output, Figma designs → UI components
- MCP (Model Context Protocol) support: 11,000+ MCP servers available via marketplace UI with one-click install

### Supported Languages (by usage share)
Vue, Python, JavaScript, HTML, Java, TypeScript. Specializes in front-end web and backend APIs. No language is explicitly unsupported — it inherits VS Code's language support.

### Supported Models (as of mid-2025)
- Free: Claude 3.5 Sonnet, GPT-4o
- Pro: Claude 4, Gemini 2.5 Pro
- Chinese domestic version: Doubao-1.5-pro, DeepSeek-R1, DeepSeek-V3
- Users can also add custom Anthropic, OpenAI, and Gemini API keys via settings

### Extensions & Integrations
- VS Code extension compatible — import existing VS Code settings and extensions directly
- MCP protocol for external tools (databases, cloud services, APIs)
- `.rules` configuration files for persistent agent behavior constraints (added in v1.3.0)
- WSL and SSH remote development (Debian/Ubuntu documented)

## What It Doesn't Do

- **No dedicated code review or bug-finding mode** — no structured review workflow
- **No custom AI rules system at launch** — `.cursor/rules` equivalent added only in v1.3.0; still less mature than Cursor's
- **Weak on very large codebases** — just-in-time context scanning breaks down past ~100,000 lines; no full upfront codebase indexing (manual indexing required for projects > 5,000 files)
- **No local-only/offline mode** — all AI calls go to cloud; no opt-out for telemetry
- **No team collaboration features** — no shared workspaces or org-level config
- **First-pass code accuracy lower than Cursor** — 78% vs Cursor's 87% in independent benchmarks
- **Limited model selection** (free tier: two models only)
- **No enterprise pricing or SLAs** published

**Privacy & Security concerns** — this warrants explicit coverage given documented findings:

- **Telemetry persists after opt-out:** Disabling telemetry in settings does not stop data transmission. In some analyses, opting out *increased* transmission frequency, suggesting the toggle is cosmetic.
- **Data collected:** Hardware specs, OS/architecture, usage patterns, persistent device identifiers, project and file path information, mouse/keyboard activity, JWT tokens, complete file contents during editing sessions.
- **Data retention:** Personal data retained 5 years after account closure per privacy policy.
- **Model training:** Terms of service permit using input content to train models and improve services.
- **No local mode:** No option to run fully offline or route only to self-hosted models.
- **ByteDance ownership:** Subject to Chinese data laws. Relevant for code under NDA, government/healthcare, or proprietary algorithms.
- **Community suppression:** Reported banning/muting of users raising privacy concerns on official channels.

**Practical guidance:** Do not use Trae for client code, proprietary algorithms, government/regulated-industry projects, or anything under NDA without legal review.

## Architecture

**Foundation:** VS Code fork — not an extension, a standalone editor with a redesigned interface built on the VS Code codebase.

**Platforms:** macOS (Apple Silicon and Intel), Windows 10/11. Linux not officially supported.

**Context indexing:** Just-in-time scanning (only files relevant to current task). Automatic for projects under 5,000 files; manual trigger required above that. Lower memory overhead (1.5 GB baseline RAM) but less deep comprehension than full-codebase indexers.

**CodeGraph:** Proprietary technology for understanding project-wide dependency graphs. Claimed 94% accuracy on cross-file dependency updates during refactoring.

**Performance:** ~1.2s average code completion response. Code completion latency reduced 60% moving from Agent 1.0 to SOLO architecture.

**Telemetry infrastructure:** Connections to multiple ByteDance domains including `mon-va.byteoversea.com` (telemetry), `maliva-mcs.byteoversea.com` (config/heartbeat), `api.trae.ai`, `api-sg-central.trae.ai`, `bytegate-sg.byteintlapi.com`. Data sent every ~30 seconds including during idle. Uses binary MessagePack format alongside JSON. Persistent device ID via SHA-256 hardware hash survives reinstallation.

## Key Differentiators

1. **SOLO mode:** Among the highest autonomous task completion rates in independent tests (75.2% on real-world tasks). Competes directly with Devin/Claude Code style agents.
2. **MCP marketplace:** Polished one-click UI for installing MCP servers — more user-friendly than Cursor or Windsurf.
3. **Price:** Free tier is the most aggressive in the market. Pro is $10/month vs Cursor's ~$20-40/month.
4. **Multimodal input:** Image and video → code workflows (e.g., Figma-to-code, video context) are built-in, not third-party.
5. **Chinese language support:** Native Mandarin UI and models (Doubao, DeepSeek) in the domestic version. Most competitors are English-first.
6. **Resource efficiency:** Lightest RAM footprint among major AI IDEs at 1.5 GB baseline.

## Ideal Use Cases

- **Solo developers and indie hackers** who want a full AI IDE without paying $20+/month
- **Rapid prototyping and MVPs** — SOLO mode can scaffold a full CRUD app with backend, UI, and deployment from a single prompt
- **Small-to-medium projects** under 100,000 lines
- **Frontend/backend web development** in Vue, Python, JavaScript
- **Resource-constrained machines** — low RAM footprint
- **Non-English-speaking developers** — particularly strong Chinese language support
- **Teams experimenting with agentic workflows** via MCP integrations

**Not ideal for:**
- Large monolithic codebases requiring deep cross-file comprehension
- Organizations with strict data sovereignty or NDA requirements (see privacy concerns above)
- Teams needing enterprise SLAs, compliance documentation, or SOC 2

## Community & Ecosystem

**Adoption (2025 annual report):**
- 6 million+ total registrations
- 1.6 million+ monthly active users
- ~200 countries and regions
- ~60 million sessions in 2025; ~500 million queries; ~100 billion lines of code generated
- Daily token consumption grew ~700% in the second half of 2025
- SOLO mode used by 44% of international users, 30% of domestic users

**Open source status:** Closed source. The editor is built on the open-source VS Code codebase but Trae itself is proprietary.

**Extension ecosystem:** Inherits VS Code's extension marketplace. 11,000+ MCP servers supported. `.rules` files for agent configuration (v1.3.0+).

**Community channels:** Discord (official). Note: users reporting privacy concerns have been muted on Discord and the word "track" was added to an automated blacklist triggering 7-day mutes.

## Sources

- [Trae official site](https://www.trae.ai/)
- [Trae pricing page](https://www.trae.ai/pricing)
- [TRAE SOLO mode](https://www.trae.ai/solo)
- [Trae IDE v1.3.0 MCP & .rules announcement](https://traeide.com/news/6)
- [Trae 2025 annual report — 1.6M MAU](https://news.aibase.com/news/24099)
- [Trae paid subscription launch with Claude 4 support](https://www.aibase.com/news/18413)
- [Builder.io: Cursor vs Trae comparison](https://www.builder.io/blog/cursor-vs-trae)
- [Skywork: Trae AI IDE Review 2025 — features, pricing, privacy](https://skywork.ai/blog/trae-ai-ide-review-2025-features-pricing-privacy-comparison/)
- [Skywork: Trae vs Cursor 2025](https://skywork.ai/blog/trae-ai-ide-review-2025-cursor-alternative/)
- [Zoer.ai: Trae vs Cursor vs Windsurf 2026](https://zoer.ai/posts/zoer/trae-cursor-windsurf-ai-ide-comparison-2026)
- [Unit 221B: Trae data collection analysis](https://blog.unit221b.com/dont-read-this-blog/unveiling-trae-bytedances-ai-ide-and-its-extensive-data-collection-system)
- [The Register: Trae telemetry continues after opt-out](https://www.theregister.com/2025/07/28/bytedance_trae_telemetry/)
- [Cybernews: ByteDance Trae data harvesting](https://cybernews.com/security/bytedance-ai-coding-tool-trae-data-collection/)
- [TechRadar: ByteDance AI tool caught collecting user data](https://www.techradar.com/pro/security/bytedance-ai-tool-caught-spying-on-users)
- [DigitalOcean: Trae free AI code editor overview](https://www.digitalocean.com/community/tutorials/trae-free-ai-code-editor)
- [DataCamp: Trae AI guide with examples](https://www.datacamp.com/tutorial/trae-ai)
