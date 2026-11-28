#!/usr/bin/env bash
# Sweep live files for stale values after a re-scope or a revised number.
# Usage: fuku/bin/sweep.sh "<old value>" ["<old value 2>" ...]
# Searches NOW.md, OUTBOX.md (Open section only), fab_advertising/{reports,creatives}, fuku/bin.
# Journal and lessons are history and are not searched. Exit 0 = no hits, 1 = hits found, 2 = usage.
set -u
cd "$(dirname "$0")/../.." || exit 2
[ $# -ge 1 ] || { echo "usage: $0 \"<old value>\" [...]" >&2; exit 2; }
hits=0
for v in "$@"; do
  echo "== \"$v\""
  out=$(grep -rnF -- "$v" fuku/NOW.md fab_advertising/reports fab_advertising/creatives fuku/bin 2>/dev/null | grep -v '^fuku/bin/sweep.sh:')
  open=$(awk '/^## Open/{f=1} /^## Parked/{f=0} f' fuku/OUTBOX.md | grep -nF -- "$v" | sed 's/^/fuku\/OUTBOX.md(Open):/')
  all=$(printf '%s\n%s\n' "$out" "$open" | sed '/^$/d')
  if [ -n "$all" ]; then echo "$all" | cut -c1-220; hits=$((hits + $(echo "$all" | wc -l))); else echo "   (none)"; fi
done
echo "total hits: $hits"
[ "$hits" -eq 0 ]
