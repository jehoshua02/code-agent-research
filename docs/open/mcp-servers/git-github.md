# Git / GitHub

_Last verified: 2026-06-14_

## 0. TL;DR

A Git/GitHub [MCP](../GLOSSARY.md#mcp-model-context-protocol) server lets an agent inspect commits, diffs, and branches, or create pull requests and manage issues — without shelling out to the `git` CLI directly. Use one when the agent needs to participate in a code-review workflow, automate PR creation, or reason about repository history. The main catch: write operations (commit, push, PR creation) are irreversible, so scope the agent's permissions carefully and review its actions before merging.

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

**Token leakage** is the primary risk for hosted-platform servers: `GITHUB_PERSONAL_ACCESS_TOKEN` and `GITLAB_PERSONAL_ACCESS_TOKEN` are long-lived credentials with broad scope (classic PATs grant org-wide write access). If the token appears in debug logs, error messages, or is embedded in a repository accidentally committed by the agent, it provides full API access until manually revoked.

**Force-push to protected branches** can occur if the agent misidentifies the target branch. The GitHub API and local `git push --force` do not ask for confirmation; a single misdirected call can overwrite or delete history on `main` or a release branch, with no undo if the remote is the only copy.

**Committing secrets** is a structural risk: an agent writing files and then calling `git_add` + `git_commit` may include `.env` files, private keys, or API credentials that happened to be in the working tree. The git server has no secret-scanning step; the commit lands and is immediately in history even if pushed and then deleted (it remains in reflog and forks).

**Scope over-provisioning** compounds all of these: a classic PAT with `repo` scope grants read/write access to every repository the token owner can access — far beyond the single repo the agent is working in. A compromised agent session or prompt injection can exploit this to exfiltrate code from unrelated private repositories.

**Mitigation:** use fine-grained PATs scoped to the minimum required repository and permissions; enable branch protection rules (require PRs, disallow force-push) on important branches; run secret-scanning (e.g., `git-secrets`, `trufflehog`) in a pre-commit hook or CI step; rotate tokens regularly.

## 7. Documented Strengths

Documented strengths from maintainer docs or community reports. Cite source.

## 8. Documented Weaknesses

Documented limitations from issue tracker or community reports. Cite source.

## 9. Sources

- [modelcontextprotocol/servers — git](https://github.com/modelcontextprotocol/servers/tree/main/src/git) — observed 2026-06-14
