# Shell

_Last verified: 2026-06-14_

## 1. What It Is

MCP servers in this category run commands in a shell on behalf of the agent. Agents need them to invoke build systems, package managers, tests, or any CLI tool not exposed through a dedicated server. No Anthropic reference (deliberately, due to risk). Notable community: mcp-server-commands and similar; usually paired with allowlists and sandboxing.

## 2. Capability

Exposes one or more tools that spawn processes on the host machine. Operations vary slightly by implementation but typically include:

- **run_process** (mcp-server-commands) — run a command via the system's default shell (`command_line` mode) or directly as an executable (`argv` mode); returns stdout and stderr as text; supports passing stdin content
- **execute_command** / **run_shell** (mcp-shell-server and similar) — run an arbitrary shell command and capture combined output

Some implementations expose multiple tools for common patterns (read file, list directory) layered on top of shell execution.

## 3. Install

Community servers; no Anthropic reference implementation. The most common is the npm-published `mcp-server-commands`:

```
npx mcp-server-commands
```

Python-based alternatives (e.g., `mcp-shell-server`) install via:

```
uvx mcp-shell-server
```

**Host vs container:** Shell servers by definition execute on whichever machine the process runs. For any meaningful sandboxing, run inside a container with restricted mounts and no network or with an allowlist of permitted commands. Running on the host directly exposes all tools available to the server's user account.

## 4. Transport

stdio. The server process is spawned by the MCP client; JSON-RPC flows over stdin/stdout. HTTP wrapping is possible via adapters such as `mcpo` but is not the default for any major shell server.

## 5. Auth

No credential-based auth. Permissions are entirely dictated by the OS user running the server process. Most implementations warn explicitly against running with elevated privileges (e.g., sudo). Some clients (Claude Desktop) prompt for human approval of each command invocation.

## 6. Security Considerations

Sandboxing, allowlists, common footguns.

## 7. Documented Strengths

Documented strengths from maintainer docs or community reports. Cite source.

## 8. Documented Weaknesses

Documented limitations from issue tracker or community reports. Cite source.

## 9. Sources

- [PulseMCP — command execution servers](https://www.pulsemcp.com/servers?q=shell) — observed 2026-06-14
