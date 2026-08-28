#!/usr/bin/env bash
# Sync the working case to the public mirror.
#
# README.md and .gitignore are DELIBERATELY DIFFERENT between the two trees:
# the private README is marked NOT FOR PUBLICATION and names respondents/.
# A sync on 2026-08-28 overwrote the public README with the private one and
# deleted the public .gitignore. Both are excluded below. Do not remove them.
#
# --delete is intentional so retractions propagate, which is why the two
# exclusions above matter.
#
# CONSEQUENCE, learned 2026-08-29: because README.md is excluded, edits made to the
# PRIVATE README never reach the public repo. A link to REMEDIATION.md was added to
# the private README and silently never published. If you add anything to a README,
# add it to BOTH trees by hand.
set -euo pipefail
SRC=/home/obsidian/case_sevenfold
DST=/home/obsidian/case_sevenfold_public

rsync -a --delete \
  --exclude='.git' --exclude='.gitignore' --exclude='README.md' \
  --exclude='respondents/' --exclude='*_INTERNAL.md' --exclude='FINDING_13A*' \
  --exclude='deliverables/clinical/' --exclude='deliverables/wyden/' --exclude='deliverables/foia/*_FILED.txt' \
  --exclude='exhibits/tbt_*.html' --exclude='exhibits/inquirer_*.html' \
  --exclude='exhibits/statnews_*.html' --exclude='exhibits/nutraingredients_*.html' \
  --exclude='exhibits/senate_annual_*.html' --exclude='exhibits/ptr_*.html' \
  --exclude='exhibits/_blocked/' --exclude='exhibits/fara_partial/' \
  --exclude='*.err' --exclude='.opened' --exclude='deliverables/_*.html' \
  "$SRC/" "$DST/"

# Leak gate. Refuse to leave a dirty tree containing restricted markers.
# ADDR is assembled at runtime so this script is not itself a copy of the address.
ADDR="680 North""ridge"
cd "$DST"
if git status --porcelain | awk '{print $NF}' | while read -r f; do
     [ -f "$f" ] && grep -ilE "NOT FOR PUBLICATION|${ADDR}|respondents/" "$f" 2>/dev/null
   done | grep -q .; then
  echo "LEAK GATE TRIPPED: restricted marker in a synced file. Nothing committed." >&2
  exit 1
fi
echo "sync clean"
