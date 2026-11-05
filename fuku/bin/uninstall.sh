#!/bin/zsh
LABEL="com.karnivall.fuku"
launchctl bootout "gui/$(id -u)/$LABEL" 2>/dev/null && echo "Fuku heartbeat stopped." || echo "Not running."
rm -f "$HOME/Library/LaunchAgents/$LABEL.plist"
