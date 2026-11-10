# Karnivall Agentic Company — home of Fuku

**Fuku** is Alvian's always-on AI co-founder, running on Claude Code. Alvian sets missions; Fuku owns the strategy and the execution.

## How it works
- **Identity & rules:** `CLAUDE.md` (Alvian owns §1–§4; Fuku evolves the bottom section)
- **Brain:** `fuku/`: MISSIONS, NOW, INBOX, OUTBOX, memory/, journal/, protocols/
- **Always-on:** a cloud routine runs `fuku/protocols/cloud_heartbeat.md` hourly, 07:00–22:00 WIB, against the GitHub repo, so Fuku works while the Mac is off. Quiet runs do groundwork or exit without a commit. (Optional local fallback: a macOS LaunchAgent running `fuku/bin/heartbeat.sh`; not installed.)
- **Self-learning:** reflect after every run → `memory/lessons.md` → weekly retro turns lessons into playbooks and upgrades Fuku's own rules, agents, and commands (logged in `fuku/CHANGELOG.md`)
- **Context:** a SessionStart hook loads Fuku's state into every session automatically
- **Guardrails:** Fuku can't edit `.claude/settings.json` or `fuku/bin/heartbeat.sh` (deny rules). Spending money, sending or publishing, and irreversible actions go to OUTBOX for your yes/no.

## Talk to Fuku
| You want to… | Do this |
|---|---|
| Give a mission | `/mission <goal>` in Claude Code, or edit `fuku/MISSIONS.md` |
| Leave a note async | Add to `fuku/INBOX.md` |
| See what he needs from you | `fuku/OUTBOX.md` → "Needs you" (max 3 asks; answer inline, e.g. "→ yes") |
| Get a briefing | `/status` |
| Correct him | `/feedback <what>` |
| Make him work now | `/heartbeat` |
| Force self-improvement | `/retro` |

## Local heartbeat setup (optional; the cloud routine already covers always-on)
1. In a terminal: `cd` into this folder and run `claude` once, then accept the "trust this folder" prompt.
2. `fuku/bin/install.sh` starts the hourly heartbeat. `fuku/bin/uninstall.sh` stops it.
3. Test: `fuku/bin/heartbeat.sh --force`, then check `fuku/runs/` and `fuku/journal/`.
4. If the log shows "Operation not permitted": macOS is blocking background access to ~/Documents. Give `/bin/zsh` and `~/.local/bin/claude` Full Disk Access (System Settings → Privacy & Security), or move this folder out of ~/Documents.
