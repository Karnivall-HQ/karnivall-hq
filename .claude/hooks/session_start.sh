#!/bin/zsh
# Injects Fuku's live state into every Claude Code session in this workspace.
ROOT="${CLAUDE_PROJECT_DIR:-$(cd "$(dirname "$0")/../.." && pwd)}"
F="$ROOT/fuku"
# Pull what cloud Fuku did since the last session (fast-forward only; never blocks the session)
if git -C "$ROOT" remote get-url origin >/dev/null 2>&1; then
  ( cd "$ROOT" && GIT_TERMINAL_PROMPT=0 git -c http.lowSpeedLimit=1000 -c http.lowSpeedTime=10 pull --ff-only -q origin main >/dev/null 2>&1 ) || echo "(git sync skipped: pull failed or diverged; resolve manually)"
fi
echo "=== FUKU STATE (auto-loaded) — you are Fuku; follow CLAUDE.md ==="
echo "Today: $(date '+%Y-%m-%d %A %H:%M')"
for f in NOW.md MISSIONS.md; do echo "\n--- fuku/$f ---"; sed -n '1,120p' "$F/$f"; done
echo "\n--- fuku/INBOX.md (new) ---"; sed -n '/^## New/,/^## Processed/p' "$F/INBOX.md" | sed '$d'
echo "\n--- fuku/OUTBOX.md (open) ---"; sed -n '/^## Open/,/^## Resolved/p' "$F/OUTBOX.md" | sed '$d' | head -60
echo "\n--- recent lessons ---"; grep '^- ' "$F/memory/lessons.md" | tail -15
LAST=$(ls -1 "$F/journal" 2>/dev/null | tail -1); [ -n "$LAST" ] && { echo "\n--- last journal ($LAST, tail) ---"; tail -25 "$F/journal/$LAST"; }
exit 0
