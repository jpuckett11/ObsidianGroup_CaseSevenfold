# SEVENFOLD / FINDING 12
## Corrected lobbying corpus: $7,397,500, a $2.44M undercount in our own earlier work

**Status:** CONFIRMED from Senate LDA primaries. **Supersedes the totals in
Finding 02 and Finding 08.** **Date:** 2026-08-27.

---

### 1. What we got wrong and why

Findings 02 and 08 reported **$4,961,000** in disclosed kratom lobbying. That
figure came from a search on the LDA **issue-text** field for the term "kratom".

**That method systematically missed any filing that avoided the word.** Johnson
Foods' filings describe the work as "raising awareness about company's product
pipeline" and "FDA regulation of dietary supplements". They never say kratom. We
recorded that account as $130,000. **It is $700,000.**

Re-querying the entire corpus by **client name** instead, then merging and
deduplicating on `filing_uuid`, and stripping client-name false positives (Raben
Group filings for The Mentor Network, the Fisheries Survival Fund, and an
unrelated Columbia University match):

**199 unique filings. $7,397,500.** A **+$2,436,500** revision.

**[I] Methodological lesson worth carrying to other cases: searching a disclosure
system by subject term measures what filers chose to call the work, not what the
work was.** Always re-run by party name.

### 2. Corrected totals

| Client | Disclosed | Registrant(s) |
|---|---|---|
| American Kratom Association | **$3,427,500** | 11+ firms incl. McGuireWoods Consulting, Van Scoyoc, Michael Best, Corcoran Partners, David Carlucci Consulting, Kountoupes Denham Carr & Reid, First Amendment Partners |
| **Botanicals for Better Health and Wellness** | **$980,000** | **Miller Strategies, LLC** |
| Stop Gas Station Heroin LLC | $750,000 | Checkmate Government Relations |
| **Johnson Foods, LLC** | **$700,000** | Holland & Knight |
| MIT45, Inc. | $500,000 | McGuireWoods Consulting, Ragnar Group |
| Global Kratom Coalition | **$335,000** | Troutman Strategies, **BGR Government Affairs** |
| **Kratom Trade Association** | **$290,000** | **Holland & Knight** |
| Botanic Tonics LLC | $200,000 | Troutman Strategies |
| **Outpost Brands, LLC** | **$160,000** | Akin Gump Strauss Hauer & Feld |
| Raben Group for Botanical Education Alliance | $40,000 | Valente & Associates |
| **Holistic Alternative Recovery Trust** | **$15,000** | Frost Brown Todd |
| End Kratom Addiction | $0 | Bob Good LLC |
| **TOTAL** | **$7,397,500** | |

### 3. By year

| Year | Disclosed |
|---|---|
| 2016 | $140,000 |
| 2017 | $318,000 |
| 2018 | $514,000 |
| 2019 | $180,000 |
| 2020 | $150,000 |
| 2021 | $185,000 |
| 2022 | $612,500 |
| 2023 | $860,500 |
| 2024 | $1,052,500 |
| **2025** | **$2,070,000** |
| **2026 (through Q2 only)** | **$1,315,000** |

### 4. Four entities that were invisible

**Botanicals for Better Health and Wellness -- $980,000 via Miller Strategies,
LLC.** Now the **second largest spender in the entire fight.** Miller Strategies
is **Jeff Miller**, the Trump fundraiser previously known in this case only for
routing **$50,000** to the Trump inaugural committee. That $50,000 was the visible
edge of a nearly one-million-dollar account. **Funders of this entity: unknown.
Priority target.**

**Kratom Trade Association -- $290,000 via Holland & Knight.** Appears in no
reporting reviewed. Means **Holland & Knight carries two kratom clients totalling
$990,000**, not one. **Membership and funders: unknown. Priority target.**

**Johnson Foods, LLC -- $700,000, not $130,000.** See Finding 06; this reframes
the paid study as one leg of a $700,000 campaign rather than an isolated conflict.

**Outpost Brands, LLC -- $160,000 via Akin Gump**, previously recorded at $0
(registration only). Unidentified.

### 5. The asymmetry, restated on corrected numbers

The **Holistic Alternative Recovery Trust**, the only organized defender of 7-OH,
disclosed **$15,000**.

- American Kratom Association alone outspends it **228 : 1**.
- The full leaf/pro-restriction side outspends it by roughly **490 : 1**.

**[I] Restated because it survives every correction we have made: this was never a
contested rulemaking. One side could afford to be in the room and the other could
not.**

### 6. Still to pull

- **Funders of Botanicals for Better Health and Wellness** and the **Kratom Trade
  Association**. Two seven-figure-adjacent vehicles with no public membership.
- **BGR Government Affairs** on the Global Kratom Coalition account, newly visible.
- **LD-203 semi-annual contribution reports** for every registrant above. Those
  disclose the political giving of the firms and their individual lobbyists, and
  we have not touched them.
