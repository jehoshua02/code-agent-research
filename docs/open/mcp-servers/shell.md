# Shell

_Last verified: 2026-06-14_

## 0. TL;DR

A shell [MCP](../GLOSSARY.md#mcp-model-context-protocol) server lets an agent run arbitrary commands on the host machine — build tools, package managers, test runners, or any CLI. Use one when you need the agent to do things no dedicated server covers, like running `npm test` or invoking a custom script. The main catch: shell access is the highest-risk tool category; always pair it with an allowlist of permitted commands and run inside a container or sandbox.

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

**Arbitrary command execution** is the defining risk: a shell server that accepts free-form command strings gives the agent (and any prompt injected into its context) full OS access under the server process's user account. A single injected instruction — `rm -rf ~` or a curl-pipe-sh — executes without recourse.

**Prompt injection** amplifies this: content the agent reads from external sources (web pages, documents, untrusted tool outputs) can contain instructions that the model treats as legitimate requests to run destructive or exfiltrating commands.

**Allowlist bypass** is the next failure mode. Implementations that restrict to a list of permitted executables are still vulnerable to argument injection (e.g., `git` is allowed, but `git config --global core.sshCommand 'curl ...'` is not), shell metacharacter smuggling (`; rm -rf`), and PATH manipulation if the allowed binary resolves differently at runtime.

**Mitigation:** treat shell MCP servers as a last resort; prefer category-specific servers (filesystem, git) for scoped operations; enforce an allowlist at both the binary and argument level; run inside a container with `--network none` and a read-only root filesystem; require human-in-the-loop approval for each invocation.

## 7. Documented Strengths

- **Universal reach**: because it executes arbitrary shell commands, a single shell server can substitute for dozens of purpose-built MCP servers — build tools, package managers, test runners, linters — without requiring separate integrations ([mcp-server-commands README](https://github.com/g0t4/mcp-server-commands)).
- **Zero integration overhead**: any CLI tool the host already has installed is immediately available to the agent without writing adapter code or a new MCP server.
- **stdin/stdout passthrough**: implementations like `mcp-server-commands` support piped input and capture both stdout and stderr, enabling composable UNIX pipelines within a single tool call.
- **Flexible sandboxing options**: operators can layer OS-level controls (Docker `--network none`, seccomp, read-only rootfs) around a shell server to enforce a narrower threat surface while retaining broad command coverage.

## 8. Documented Weaknesses

- **Highest attack surface of any MCP category**: Anthropic deliberately ships no reference shell server; the MCP security guidance calls arbitrary-execution servers the primary prompt-injection escalation vector ([MCP security docs](https://modelcontextprotocol.io/docs/concepts/security)).
- **Allowlist bypass is routine**: argument injection (`git config --global …`), shell metacharacter smuggling (`;`, `&&`), and PATH hijacking can all circumvent binary-level allowlists, as documented in community threat-model discussions.
- **Frequently blocklisted in enterprise deployments**: ops teams routinely disable shell MCP servers entirely rather than attempt to harden them, limiting their practical use to trusted local-dev environments.
- **No structured output**: raw stdout is returned as a string; agents must parse unstructured CLI output rather than consuming typed data, making responses fragile across tool versions.

## 9. Sources

- [PulseMCP — command execution servers](https://www.pulsemcp.com/servers?q=shell) — observed 2026-06-14
