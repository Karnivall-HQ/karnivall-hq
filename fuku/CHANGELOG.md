# CHANGELOG — changes to Fuku's own system

- 2026-11-05 · Bootstrap: constitution (CLAUDE.md), brain files, heartbeat, protocols, subagents, commands.

- 2026-11-05: Added "always use emojis in chat" rule (with emoji key) to CLAUDE.md §6, at Alvian's request, so it applies to every session in this folder.
- 2026-11-05: Cloud Fuku prep. Turned the workspace into a git repo (.gitignore excludes runs/logs/.env), added fuku/protocols/cloud_heartbeat.md, and made session_start.sh fast-forward pull from origin/main so local sessions see what cloud Fuku did.
- 2026-11-05: Cloud Fuku went live. Created the private repo github.com/alvianlim/karnivall-hq, installed gh CLI at ~/.local/bin/gh (logged in as alvianlim), and created routine trig_01NGMFnv9BpvRp1jQjkAwUVJ (cron `0 0-15 * * *` UTC = hourly 07–22 WIB, Opus, default connectors incl. Meta Ads). Test run verified: it pushed straight to main.
- 2026-11-05: Ads are now propose-only (Alvian's rule). Added it to the CLAUDE.md Evolving rules, memory/alvian.md, and the M-001 constraints/strategy. Closed both OUTBOX ad-change decisions. The cloud routine's Meta Ads connector is limited to 44 read-only tools (permitted_tools); enforcement will be verified on the next run.
- 2026-11-05: Learned Meta's ads algorithm from 17 docs Alvian provided. Added `fuku/knowledge/meta-ads/` (sources + notes) and the playbook `fuku/memory/playbooks/meta-ads-algorithm.md` (12 rules checked against Fab data), plus an Evolving rule in CLAUDE.md to read it before any Meta ads work.
