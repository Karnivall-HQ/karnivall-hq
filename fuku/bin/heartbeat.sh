#!/bin/zsh
# Fuku's heartbeat: one autonomous work cycle. Invoked by launchd (or manually).
set -u
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
F="$ROOT/fuku"
source "$F/config.sh"
export PATH="$HOME/.local/bin:/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:$PATH"

HOUR=$((10#$(date +%H)))
if [[ "${1:-}" != "--force" ]] && (( HOUR < ACTIVE_HOUR_START || HOUR >= ACTIVE_HOUR_END )); then exit 0; fi

# Single-instance lock (stale after MAX_RUN_MINUTES+15)
LOCK="$F/runs/.lock"
if ! mkdir "$LOCK" 2>/dev/null; then
  if [[ -n $(find "$LOCK" -maxdepth 0 -mmin +$((MAX_RUN_MINUTES+15)) 2>/dev/null) ]]; then rm -rf "$LOCK"; mkdir "$LOCK"; else exit 0; fi
fi
trap 'rm -rf "$LOCK"' EXIT

mkdir -p "$F/runs"
LOG="$F/runs/$(date +%Y-%m-%d_%H%M).log"
PROMPT="Heartbeat $(date '+%Y-%m-%d %H:%M %A'). You are Fuku, running autonomously. Follow fuku/protocols/heartbeat.md exactly."

ARGS=(-p "$PROMPT" --permission-mode auto --permission-prompts none --model "$FUKU_MODEL" --effort "$FUKU_EFFORT" -n "fuku-heartbeat")
[[ -n "$MAX_BUDGET_USD" ]] && ARGS+=(--max-budget-usd "$MAX_BUDGET_USD")

cd "$ROOT"
echo "### heartbeat start $(date)" > "$LOG"
claude "${ARGS[@]}" >> "$LOG" 2>&1 &
PID=$!
( sleep $((MAX_RUN_MINUTES*60)); kill -TERM $PID 2>/dev/null && echo "### killed: exceeded ${MAX_RUN_MINUTES}m" >> "$LOG" ) &
WATCH=$!
wait $PID; RC=$?
kill $WATCH 2>/dev/null
echo "\n### heartbeat end $(date) rc=$RC" >> "$LOG"

if [[ "$NOTIFY" == "1" ]]; then
  MSG=$(grep -E '^NOTIFY:' "$LOG" | tail -1 | sed 's/^NOTIFY:[[:space:]]*//; s/["\\]//g' | cut -c1-180)
  (( RC != 0 )) && MSG="Heartbeat failed (rc=$RC). See ${LOG:t}"
  [[ -n "$MSG" ]] && osascript -e "display notification \"$MSG\" with title \"Fuku\" sound name \"Glass\"" 2>/dev/null
fi

find "$F/runs" -name '*.log' -mtime +14 -delete 2>/dev/null
exit 0
