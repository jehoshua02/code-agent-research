# Git / GitHub

_Last verified: 2026-06-14_

## 1. What It Is

MCP servers in this category expose Git and GitHub/GitLab operations — clone, diff, status, commit, PR, issues. Agents need them for any code-review or repository-management workflow. Notable: git (official reference, Anthropic) for local repos; community github and gitlab servers for hosted platforms.

## 2. Capability

**Local git (Anthropic reference `mcp-server-git`)** — operates on a repository path on disk:

- **git_status** — show working-tree status
- **git_diff_unstaged** / **git_diff_staged** — show unstaged or staged changes
- **git_diff** — compare branches or commits
- **git_add** — stage files
- **git_commit** — create a commit
- **git_reset** — unstage all staged changes
- **git_log** — display commit history with optional date filtering
- **git_create_branch** — create a new branch from a base branch
- **git_checkout** — switch branches
- **git_show** — display a commit's contents and diff
- **git_branch** — list local, remote, or all branches

**Hosted-platform servers (community `github`, `gitlab`)** — wrap the GitHub/GitLab REST APIs and additionally expose: list/create/update pull requests, list/create issues, search repositories, create/delete branches, read file contents via the API, and manage releases.

## 3. Install

Anthropic reference (`mcp-server-git`) is Python-based:

```
uvx mcp-server-git --repository /path/to/repo
```

Or via Docker:

```
docker run --rm -i --mount type=bind,src=/path,dst=/path mcp/git
```

Community GitHub server is Node.js:

```
npx -y @modelcontextprotocol/server-github
```

Host install is standard for local git operations. Docker is appropriate for CI or ephemeral environments; mount the repository path into the container.

## 4. Transport

stdio for all reference and major community implementations. The process is spawned by the MCP client.

## 5. Auth

- **Local git server**: no credential-based auth; access is controlled by filesystem permissions on the repository path
- **GitHub server**: requires a `GITHUB_PERSONAL_ACCESS_TOKEN` environment variable (classic PAT or fine-grained token); scopes depend on the operations used (repo, issues, pull_requests)
- **GitLab server**: requires a `GITLAB_PERSONAL_ACCESS_TOKEN` environment variable

## 6. Security Considerations

Sandboxing, allowlists, common footguns.

## 7. Documented Strengths

Documented strengths from maintainer docs or community reports. Cite source.

## 8. Documented Weaknesses

Documented limitations from issue tracker or community reports. Cite source.

## 9. Sources

- [modelcontextprotocol/servers — git](https://github.com/modelcontextprotocol/servers/tree/main/src/git) — observed 2026-06-14
