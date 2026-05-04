# CodeBuddy (Tencent Cloud)

## What It Is

**Category:** Full-lifecycle AI coding assistant (IDE + plugin + CLI)
**Maker:** Tencent Cloud
**Released:** May 22, 2024 (plugin); July 2025 (IDE beta); September 2025 (CLI)
**Website:** https://www.codebuddy.ai

## Pricing

CodeBuddy uses a **credit-based** model. The IDE/plugin product and the CLI product have separate pricing structures.

### CodeBuddy IDE / Plugin (International)

| Tier | Price | Credits |
|---|---|---|
| Free | $0 | 250 credits / 2 weeks |
| Pro | $9.95/month (or $119.40/year) | 1,000 credits/month |
| Team | $40/seat/month | 1,000 credits/seat/month, pooled |

Add-on credit packages available for Pro and Team plans (e.g. 10,000 credits for $200 / 6 months).

### CodeBuddy (China / Enterprise)

Enterprise flagship: ¥198/user/month (raised from ¥78 in May 2026, ~154% increase).
Enterprise dedicated: ¥316/user/month (raised from ¥158).

Price increases in 2026 signal compute scarcity pressure across Tencent's AI product line.

## What It Does

### Core Features

**Code Completion (BuddyTab)**
- Context-aware inline completions across 200+ languages
- Real-time suggestions; multi-line and multi-file awareness

**Craft Mode (Autonomous Agent)**
- Describe a requirement in natural language; CodeBuddy plans, writes, and wires code across multiple files
- Handles dependency management, test generation, and deployment steps autonomously
- 50 free Craft credits per day on the free tier

**Plan Mode**
- Five-stage workflow: requirement clarification → solution design → review → step-by-step implementation → archival
- Generates full technical architecture and task breakdown before writing a single line of code
- Designed for complex features where direction must be set before execution

**Design-to-Code**
- Converts Figma mockups, hand-drawn sketches, and text descriptions into working UI code
- Claimed 99.9% layout fidelity for Figma imports
- Supports TDesign, MUI, and Shadcn component libraries

**Intelligent Code Review**
- Flags bugs, anti-patterns, and security vulnerabilities in real time
- Complies with MLPS Level 3 security standard; dual encryption using national cryptographic algorithms (relevant for Chinese enterprise deployments)

**Unit Test Generation**
- Auto-generates test cases including edge cases; integrates with Jest and other standard frameworks

**Technical Q&A / Chat**
- In-IDE chat interface; no context switching required
- Semantic codebase search via vector embeddings for "understand this codebase" queries

**One-Click Deployment**
- Built-in BaaS integration (Tencent CloudBase, Supabase)
- Ties into Tencent CODING DevOps suite for CI/CD

**WeChat Mini Program Support**
- Native integration with WeChat Developer Tools
- Supports WeChat Pay integration and game development workflows — unique to Tencent's ecosystem

### Supported Languages & Frameworks

200+ languages including Python, JavaScript, TypeScript, Java, C++, C#, Go, Rust, and more. Framework support spans React, React Native, Vue, Spring, Django, and others.

### Supported IDEs

15+ IDEs: VS Code (1.82+), Visual Studio 2022, IntelliJ IDEA (2022.2+), PyCharm, GoLand, CLion, PhpStorm, Android Studio, WeChat Developer Tools, Xcode.

## What It Doesn't Do

- **Weak on complex multi-file refactoring**: Cross-file dependency handling degrades on deeply nested codebases; requires requests to be broken into smaller scopes and results need independent validation.
- **Prompt-sensitive**: Vague inputs ("fix this code") yield generic suggestions. Specific, well-scoped prompts are required for useful output.
- **Not a replacement for specialized devops tooling**: Deployment and CI/CD capabilities are tightly coupled to Tencent's own cloud stack (CloudBase, CODING); limited usefulness on AWS/Azure/GCP-native pipelines.
- **Figma conversion requires manual refinement**: Complex charts and intricate layout elements still need additional manual instruction after conversion.
- **Limited global brand recognition**: Positioned primarily for Chinese market; international adoption trails GitHub Copilot and Cursor significantly.
- **No open-source core**: The underlying models and IDE are proprietary; community cannot contribute to or audit the core.
- **Context window unspecified in public docs**: Token limits per session not publicly documented for the IDE/plugin (CLI documentation is more complete).

## Architecture

### Deployment Forms

CodeBuddy is the first product in China (by Tencent's claim) to offer all three deployment forms simultaneously:

| Form | Description |
|---|---|
| **Plugin** | Installs into VS Code or JetBrains IDEs; traditional developer-led, AI-assisted model |
| **IDE** | Standalone full-stack workbench built on Tencent CloudStudio technology; covers design through deployment |
| **CLI (CodeBuddy Code)** | Terminal agent; Node.js 18.0+ required; executes file edits, runs tests, manages dependencies via natural language commands |

### Models

- **Primary**: Tencent Hunyuan (Yuanbao Code Large Model) — Tencent's proprietary LLM, tuned specifically for code
- **Secondary**: DeepSeek V3 / R1 — integrated for additional reasoning capability
- **Additional**: Claude and ChatGPT listed as switchable backends in the IDE (multi-model flexibility is a stated differentiator)
- **Hunyuan 3 (Hy3)**: Tencent's MoE 295B model, integrated into CodeBuddy as it released in 2026

### Protocols & Integrations

- **MCP (Model Context Protocol)**: First Chinese coding assistant to implement MCP. Connects 30+ external tools (Git, npm, databases, APIs) via STDIO, SSE, and HTTP transports. Configuration scoped at user, project, and local levels.
- **ACP (Agent Communication Protocol)**: CodeBuddy Code v2.0 (January 2026) added ACP support for agent-to-agent orchestration.
- **LSP (Language Server Protocol)**: Configured via `.lsp.json` for per-language server integration.
- **Plugin SDK**: Open SDK released in v2.0; plugins composed of commands (slash), skills (auto-invoked), and hooks (event-driven). Marketplace supports GitHub repos, HTTP servers, and local directories.

### Security & Compliance

- MLPS Level 3 compliant
- Dual encryption using Chinese national cryptographic algorithms (SM2/SM4)
- Private deployment option available for enterprise customers

## Key Differentiators

1. **Full lifecycle in one product**: Requirement doc generation → design mockup → code → test → deploy. Competitors (Copilot, Cursor) stop at code; CodeBuddy extends into design and deployment.
2. **Tencent ecosystem integration**: WeChat Mini Programs, WeChat Pay, Tencent CloudBase, CODING DevOps — no competitor has this stack.
3. **First MCP implementation in China**: Standardized external tool integration before any domestic competitor.
4. **Dual-model architecture (Hunyuan + DeepSeek)**: Leverages Tencent's proprietary model alongside the strongest open-weight code model available.
5. **Enterprise-proven internally**: 12,000 Tencent engineers use it in production; 43%+ of Tencent's internal code is AI-generated via CodeBuddy.
6. **Free tier generous vs. competitors**: Free daily Craft credits with no credit card; Pro at $9.95/month undercuts Cursor Pro ($20) and GitHub Copilot Pro ($10) in credit-per-dollar terms.
7. **Three-form coverage**: Plugin + standalone IDE + CLI in one product family — matches Cursor (IDE only) plus Claude Code (CLI only) plus Copilot (plugin only), all from one vendor.

## Ideal Use Cases

- **Chinese enterprise development teams** needing on-premise/private deployment with MLPS compliance and national cryptographic standards.
- **WeChat Mini Program or WeChat ecosystem developers** — no other AI coding assistant has native Weixin Developer Tools integration.
- **Product managers and designers** using the full-lifecycle IDE form to go from sketch/Figma → deployed prototype without switching tools.
- **Greenfield projects** where Craft Mode's multi-file autonomous generation shines; less suited to navigating large legacy codebases.
- **Teams already on Tencent Cloud** (CloudBase, CODING, Tencent meetings) where one-click deployment and DevOps integration add genuine value.
- **Developers in China** where latency and data residency requirements favor domestic infrastructure.

## Community & Ecosystem

**Adoption (as of early 2026)**
- 12,000 engineers inside Tencent use CodeBuddy daily
- 50+ external enterprises on the platform
- Named to *2025 Top 100 Global AI Applications* list

**Open Source Status**
- Proprietary; not open source
- Plugin SDK (released January 2026) is open, allowing third-party plugin development
- MCP support means any public MCP server can extend CodeBuddy's tool access

**Extensibility**
- Plugin marketplace: GitHub-hosted, HTTP-served, or local plugins
- Skills, commands, and hooks cover the main extension points
- LSP configuration for custom language servers

**International Expansion**
- International pricing and domain (codebuddy.ai) launched alongside domestic (copilot.tencent.com)
- Marketed globally but community and documentation still skew toward Chinese developers
- JetBrains Marketplace listing (plugin ID 24379) indicates active global distribution channel

**Versioning & Momentum**
- Shipped from plugin (May 2024) → Craft agent (April 2025) → MCP support (May 2025) → IDE beta (July 2025) → CLI (September 2025) → CLI v2.0 with ACP + open SDK (January 2026)
- Rapid cadence; major capability additions every 2-3 months
- Price increases in 2026 suggest transition from growth-at-all-costs to unit economics focus

## Sources

- [CodeBuddy Introduction — Official Docs](https://www.codebuddy.ai/docs/ide/Introduction)
- [CodeBuddy Pricing — Official Docs](https://www.codebuddy.ai/docs/ide/Account/pricing)
- [CodeBuddy Plan Mode — Official Docs](https://www.codebuddy.ai/docs/ide/Features/Plan-Mode)
- [CodeBuddy MCP Documentation](https://www.codebuddy.ai/docs/cli/mcp)
- [CodeBuddy Plugin System](https://www.codebuddy.ai/docs/cli/plugins)
- [Baidu Wiki — CodeBuddy](https://baike.baidu.com/en/item/CodeBuddy/1432154)
- [Tencent CodeBuddy Review — Skywork AI](https://skywork.ai/blog/tencent-codebuddy-a-new-kind-of-ai-coding-partner/)
- [Tencent Launches CodeBuddy CLI — AIBase](https://www.aibase.com/news/21148)
- [China's Cursor: Tencent Launches CodeBuddy — AIBase](https://www.aibase.com/news/18038)
- [CodeBuddy IDE In-Depth Review — Medium](https://medium.com/@lcxfs1991/in-depth-review-of-tencents-new-codebuddy-ide-a-revolutionary-upgrade-for-developer-experience-465845c4bc63)
- [Tencent Cloud Hikes AI Coding Prices — BigGo Finance](https://finance.biggo.com/news/vQ5Y050BtCxy99G5l4m1)
- [CodeBuddy IDE — codebuddyide.net](https://codebuddyide.net/)
- [Tencent Cloud CodeBuddy — JetBrains Marketplace](https://plugins.jetbrains.com/plugin/24379-tencent-cloud-codebuddy)
