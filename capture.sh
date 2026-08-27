#!/usr/bin/env bash
# SEVENFOLD source capture. Fetches each URL to exhibits/ and records a sha256.
# Re-runnable: a non-empty existing capture is skipped so partial runs resume.
# Never deletes. Blocked/challenge pages are detected by CONTENT, not by byte size --
# an Akamai "Access Denied" body is 514 bytes and sailed past the old 500-byte floor.
set -uo pipefail
CASE=/home/obsidian/case_sevenfold
EX="$CASE/exhibits"; MAN="$EX/MANIFEST.tsv"
UA='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36'
: > "$MAN"; printf '#name\tstatus\turl\tsha256\n' >> "$MAN"
while IFS=$'\t' read -r name url; do
  [ -z "${name:-}" ] && continue
  case "$name" in \#*) continue;; esac
  out="$EX/${name}.html"
  if [ ! -s "$out" ]; then
    code=$(curl -sS -L -A "$UA" --max-time 45 -w '%{http_code}' -o "$out" "$url" 2>>"$CASE/capture.err") || code=000
  else
    code=cached
  fi
  sz=$(stat -c %s "$out" 2>/dev/null || echo 0)
  # Challenge/denial signatures seen in pass 1: Akamai, nginx 403, Cloudflare interstitial.
  if grep -qiE 'Access Denied|403 Forbidden|Just a moment\.\.\.|cf-browser-verification|Attention Required' "$out" 2>/dev/null || [ "$sz" -lt 1200 ]; then
    mkdir -p "$EX/_blocked"; mv "$out" "$EX/_blocked/${name}.blockpage.html" 2>/dev/null
    printf '%s\tBLOCKED(http=%s,bytes=%s)\t%s\t-\n' "$name" "$code" "$sz" "$url" >> "$MAN"
    echo "BLOCKED  $name"
  else
    h=$(sha256sum "$out" | cut -d' ' -f1)
    printf '%s\tOK(http=%s,bytes=%s)\t%s\t%s\n' "$name" "$code" "$sz" "$url" "$h" >> "$MAN"
    echo "ok       $name  $sz"
  fi
done < "$CASE/sources/urls.tsv"
