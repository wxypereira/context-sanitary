# Security Policy — context-sanitary

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 0.1.x   | 🟢 Supported       |
| < 0.1   | 🔴 Not supported   |

## Reporting a Vulnerability

**Please open a GitHub Issue** using the provided "Security Vulnerability" issue template (or label the issue with `security` / `vulnerability`).

1. Open an issue on this repository, select the **Security Vulnerability** template (or add the `security` label), and include: description, reproduction steps, impact, and affected version.
2. Maintainers will acknowledge within 5 business days.
3. After fix and release, the report is credited in `CHANGELOG.md` (unless anonymity is requested).

**Do not** send vulnerability details via email or private messages — use the GitHub Issue tracker with the security label so the process is transparent and auditable.

## Secret Handling Rules

- **Never commit secrets.** API keys (`HONCHO_API_KEY`, `MEM0_API_KEY`, `SUPERMEMORY_API_KEY`) belong only in local `.env`, never in the repository.
- `.env.example` must contain **empty keys only** (template, no values).
- `.env` is in `.gitignore` and must not be included in PRs.
- Before opening a PR, run `python3 scripts/check_pr.py` (with `--fix` if needed) to catch placeholders, stale URLs, and accidental artifacts (`__pycache__/`, `.env`).

## Scope

- `scripts/sanitary_purge.py` writes **only** to local user directories (`~/.ai-memory/wiki/`, `~/ObsidianVault/`, `~/.hermes/`) or as configured via `VAULT_PATH`. No data exfiltration: the `honcho` / `mem0` / `supermemory` providers are **experimental stubs** and make no network calls in this version.
- Runtime dependencies: Python 3.8+ standard library only (no auto-downloads). The Node wrapper (`bin/context-sanitary.js`) simply invokes local `python3` / `python`.