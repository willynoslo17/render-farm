# Security Policy
- This repo contains only rendering code. No credentials are stored here; all keys live in encrypted GitHub Actions secrets.
- Workflows run only via `repository_dispatch` / `workflow_dispatch` (authorized token holders). No `pull_request_target`.
- Default GITHUB_TOKEN is read-only. Fork PR workflows require maintainer approval.
- Report vulnerabilities privately via GitHub Security Advisories ("Report a vulnerability"). Do not open public issues for security problems.
