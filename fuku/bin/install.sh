#!/bin/zsh
# Installs Fuku's always-on heartbeat as a macOS LaunchAgent.
set -e
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
source "$ROOT/fuku/config.sh"
LABEL="com.karnivall.fuku"
PLIST="$HOME/Library/LaunchAgents/$LABEL.plist"
chmod +x "$ROOT/fuku/bin/"*.sh "$ROOT/.claude/hooks/"*.sh
mkdir -p "$HOME/Library/LaunchAgents" "$ROOT/fuku/runs"
cat > "$PLIST" <<PL
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0"><dict>
  <key>Label</key><string>$LABEL</string>
  <key>ProgramArguments</key><array><string>/bin/zsh</string><string>$ROOT/fuku/bin/heartbeat.sh</string></array>
  <key>StartInterval</key><integer>$((HEARTBEAT_MINUTES*60))</integer>
  <key>RunAtLoad</key><false/>
  <key>EnvironmentVariables</key><dict><key>PATH</key><string>$HOME/.local/bin:/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin</string><key>HOME</key><string>$HOME</string></dict>
  <key>StandardOutPath</key><string>$ROOT/fuku/runs/launchd.out</string>
  <key>StandardErrorPath</key><string>$ROOT/fuku/runs/launchd.err</string>
</dict></plist>
PL
launchctl bootout "gui/$(id -u)/$LABEL" 2>/dev/null || true
launchctl bootstrap "gui/$(id -u)" "$PLIST"
echo "Fuku heartbeat installed: every ${HEARTBEAT_MINUTES}m between ${ACTIVE_HOUR_START}:00 and ${ACTIVE_HOUR_END}:00."
echo "Trigger now:  launchctl kickstart gui/$(id -u)/$LABEL"
echo "Logs:         $ROOT/fuku/runs/"
