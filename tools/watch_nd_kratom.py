#!/usr/bin/env python3
"""
Watch North Dakota HB 1628 and SB 2408, 69th Legislative Assembly, 2nd special session.

Why these two: they are Finding 54. HB 1628 regulates kratom and carries the ONLY
kratom appropriation in the country, $20,000 to Health and Human Services for a
public awareness campaign and a website. SB 2408 puts 7-OH and its analogs on
Schedule I and appropriates nothing. Both are heard 2026-09-01 in Special Ad Hoc
Policy and together 2026-09-02 at 10:30 in Joint Policy, room Pioneer.

That makes this the cleanest live test of the case's remediation claim: states fund
enforcement and not treatment. The single most informative outcome is an AMENDMENT
that adds money to SB 2408 or strips it from HB 1628, so this watcher does not just
diff the action list. It re-reads the current bill text and counts the
appropriation language directly.

Run from cron, four times a day while the special session sits:
    23 6,11,16,21 * * *  /usr/bin/python3 /home/obsidian/case_sevenfold/tools/watch_nd_kratom.py

State goes to tools/.nd_kratom.state, changes append to tools/nd_kratom_watch.log.
Both match the tools/*.log and tools/.*.state ignore rules, so cron never dirties
the tree. Exits 0 on no change, 10 on change.
"""
import json, os, re, subprocess, sys, tempfile, urllib.request
from datetime import datetime

API   = "https://ndlegis.gov/api/assembly/69-2025/data/bills.json"
BILLS = ("1628", "2408")
UA    = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) OWG-watch/1.0"}
HERE  = os.path.dirname(os.path.abspath(__file__))
STATE = os.path.join(HERE, ".nd_kratom.state")
LOG   = os.path.join(HERE, "nd_kratom_watch.log")

# ndlegis serves a single ~8MB blob for the whole assembly; there is no per-bill
# endpoint, so we pull it once and index rather than fetching twice.
def fetch_json(url):
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=180) as r:
        return json.load(r)

def money(url):
    """Download a bill version and report what appropriation language it contains.

    This is the point of the watcher. A bill gaining or losing an appropriation is
    not visible in the action list, only in the text, so we read the text."""
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=120) as r:
            pdf = r.read()
    except Exception as e:
        return {"error": str(e)[:120]}
    with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as f:
        f.write(pdf); path = f.name
    try:
        txt = subprocess.run(["pdftotext", "-layout", path, "-"],
                             capture_output=True, text=True, timeout=90).stdout
    finally:
        os.unlink(path)
    # "penalt" is the control: it is present in both bills, so if it drops to zero
    # the extraction broke and the appropriation count cannot be trusted either.
    return {
        "appropriat": len(re.findall(r"appropriat", txt, re.I)),
        "penalt_control": len(re.findall(r"penalt", txt, re.I)),
        "dollars": sorted(set(re.findall(r"\$[\d,]+", txt)))[:8],
        "chars": len(txt),
    }

def snapshot():
    d = fetch_json(API)
    out = {"api_last_updated": d.get("last_updated"), "bills": {}}
    for num in BILLS:
        b = d.get("bills", {}).get(num) or {}
        acts = b.get("actions") or []
        vers = b.get("versions") or []
        # ndlegis puts a flat document_url on each version; the LAST entry is the
        # current text, so an amendment appears as a new element with a new lc_number.
        url = None
        for v in vers:
            if str(v.get("document_url", "")).endswith(".pdf"):
                url = v["document_url"]
        out["bills"][num] = {
            "status": b.get("current_status"),
            "passed": b.get("passed"),
            "last_action": b.get("last_action"),
            "lc_numbers": [v.get("lc_number") for v in vers],
            "actions": len(acts),
            "latest_action": (acts[-1].get("description") if acts else None),
            "latest_action_date": (acts[-1].get("date") if acts else None),
            "hearings": [f"{h.get('date')} {(h.get('committee') or {}).get('name')} {h.get('room')}"
                         for h in (b.get("hearings") or [])],
            "versions": len(vers),
            "version_url": url,
            "text": money(url) if url else None,
        }
    return out

def main():
    now = snapshot()
    old = {}
    if os.path.exists(STATE):
        try: old = json.load(open(STATE))
        except Exception: old = {}
    json.dump(now, open(STATE, "w"), indent=1)

    lines = []
    for num in BILLS:
        n = now["bills"][num]; o = (old.get("bills") or {}).get(num, {})
        if not o:
            continue
        for k in ("status", "passed", "last_action", "lc_numbers",
                  "actions", "latest_action", "hearings", "versions"):
            if o.get(k) != n.get(k):
                lines.append(f"  {num}: {k}: {o.get(k)} -> {n.get(k)}")
        ot, nt = (o.get("text") or {}), (n.get("text") or {})
        # the headline event: money appearing or disappearing
        if ot.get("appropriat") != nt.get("appropriat"):
            lines.append(f"  *** {num}: APPROPRIATION LANGUAGE {ot.get('appropriat')} -> "
                         f"{nt.get('appropriat')} (control penalt={nt.get('penalt_control')})")
        if ot.get("dollars") != nt.get("dollars"):
            lines.append(f"  *** {num}: dollar figures {ot.get('dollars')} -> {nt.get('dollars')}")
        if nt.get("penalt_control") == 0:
            lines.append(f"  !! {num}: control term absent, text extraction suspect, do not trust counts")

    if lines and old:
        stamp = datetime.now().astimezone().isoformat(timespec="seconds")
        with open(LOG, "a") as f:
            f.write(f"\n=== {stamp} CHANGE\n" + "\n".join(lines) + "\n")
        print(f"CHANGE {stamp}"); print("\n".join(lines))
        sys.exit(10)
    print("no change" if old else "baseline written")
    sys.exit(0)

if __name__ == "__main__":
    main()
