#!/usr/bin/env python3
"""
Watch Sixth Circuit docket 26-3648, Titan Logistics Group LLC v. Beth Tischler.

Why this docket: it is the appeal of the decision Judge Helmick relied on when he
enjoined Ohio SB 56 (Finding 41). The Sixth Circuit covers Ohio, Michigan, Kentucky
and TENNESSEE, so a holding on how far a state may go in regulating these products
would be binding law in the state that banned kratom outright (Finding 44).

Posture as of 2026-08-29: nature of suit 3950, Constitutional - State Statute.
Titan et al are APPELLEES, so the State lost below and is appealing.

Run from system cron, e.g. twice daily:
    17 7,19 * * *  /usr/bin/python3 /home/obsidian/case_sevenfold/tools/watch_ca6_26-3648.py

Writes state to tools/.ca6_26-3648.state and appends any change to
tools/ca6_26-3648_watch.log. Exits 0 on no change, 10 on change detected.
"""
import json, os, sys, time, urllib.request, urllib.error
from datetime import datetime

DOCKET_ID = 73669256
HERE = os.path.dirname(os.path.abspath(__file__))
STATE = os.path.join(HERE, ".ca6_26-3648.state")
LOG   = os.path.join(HERE, "ca6_26-3648_watch.log")
KEYFILE = "/home/obsidian/noname"   # line 6 = CourtListener token

def token():
    return open(KEYFILE, encoding="utf-8", errors="replace").read().splitlines()[5].strip()

def get(url, hdrs, tries=4):
    for i in range(tries):
        try:
            return json.load(urllib.request.urlopen(urllib.request.Request(url, headers=hdrs), timeout=90))
        except urllib.error.HTTPError as e:
            if e.code == 429:          # free tier resets about every 5 minutes
                time.sleep(310); continue
            raise
    return None

def main():
    H = {"Authorization": f"Token {token()}", "User-Agent": "OWG-watch/1.0"}
    dk = get(f"https://www.courtlistener.com/api/rest/v4/dockets/{DOCKET_ID}/", H)
    de = get(f"https://www.courtlistener.com/api/rest/v4/docket-entries/"
             f"?docket={DOCKET_ID}&order_by=-entry_number", H)
    rows = (de or {}).get("results") or []
    now = {
        "terminated":  dk.get("date_terminated") if dk else None,
        "last_filing": dk.get("date_last_filing") if dk else None,
        "max_entry":   max((r.get("entry_number") or 0) for r in rows) if rows else 0,
        "count":       len(rows),
        "newest":      " ".join((rows[0].get("description") or "").split())[:300] if rows else "",
    }
    old = {}
    if os.path.exists(STATE):
        try: old = json.load(open(STATE))
        except Exception: old = {}
    json.dump(now, open(STATE, "w"), indent=1)

    changed = [k for k in ("terminated", "last_filing", "max_entry", "count") if old.get(k) != now.get(k)]
    stamp = datetime.now().isoformat(timespec="seconds")
    if not old:
        line = f"{stamp}  BASELINE  entries={now['count']} max={now['max_entry']} last={now['last_filing']}"
    elif changed:
        line = (f"{stamp}  CHANGED {','.join(changed)}  entries={now['count']} "
                f"max={now['max_entry']} last={now['last_filing']} terminated={now['terminated']}\n"
                f"            newest: {now['newest']}")
    else:
        line = f"{stamp}  no change  entries={now['count']} last={now['last_filing']}"
    with open(LOG, "a") as f: f.write(line + "\n")
    print(line)

    # A termination date, or a decision-shaped entry, is the thing worth waking up for.
    if now["terminated"] or any(w in now["newest"].upper()
                                for w in ("OPINION", "JUDGMENT", "ORDER FILED", "AFFIRM", "REVERS", "ARGUMENT")):
        print("  >>> DECISION-SHAPED EVENT. Read the docket.")
        sys.exit(10)
    sys.exit(10 if changed and old else 0)

if __name__ == "__main__":
    main()
