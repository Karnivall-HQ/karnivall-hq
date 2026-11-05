# CHANGELOG — changes to Fuku's own system

- 2026-11-05 · Bootstrap: constitution (CLAUDE.md), brain files, heartbeat, protocols, subagents, commands.

- 2026-11-05: Added "always use emojis in chat" rule (with emoji key) to CLAUDE.md §6, at Alvian's request, so it applies to every session in this folder.
- 2026-11-05: Cloud Fuku prep. Turned the workspace into a git repo (.gitignore excludes runs/logs/.env), added fuku/protocols/cloud_heartbeat.md, and made session_start.sh fast-forward pull from origin/main so local sessions see what cloud Fuku did.
- 2026-11-05: Cloud Fuku went live. Created the private repo github.com/alvianlim/karnivall-hq, installed gh CLI at ~/.local/bin/gh (logged in as alvianlim), and created routine trig_01NGMFnv9BpvRp1jQjkAwUVJ (cron `0 0-15 * * *` UTC = hourly 07–22 WIB, Opus, default connectors incl. Meta Ads). Test run verified: it pushed straight to main.
