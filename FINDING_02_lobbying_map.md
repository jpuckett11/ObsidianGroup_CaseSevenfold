# SEVENFOLD / FINDING 02
## The lobbying record: $4.96M, a 300:1 spending asymmetry, and a name that comes off the filings

**Status:** CONFIRMED from Senate LDA primaries. **Date:** 2026-08-27.
**Method:** `lda.senate.gov/api/v1/filings/`, issue-text search "kratom",
**all 298 rows across 12 pages**, deduplicated on `filing_uuid` (the API repeats a
filing once per lobbying activity, which inflates naive totals roughly 2x).
Raw pages held at `exhibits/kr_p1..12.json`.

**Instrument note.** Two errors were caught and corrected before these numbers were
used. The API silently caps `page_size` at 25, so an initial 4-page pull covered
only 275 of 298 rows and produced a false Stop Gas Station Heroin total of
$600,000. With page 12 recovered the true figure is $750,000. Any total in this
file reflects the complete 298-row corpus.

---

### 1. Disclosed kratom lobbying, all time

| Client | Disclosed | Registrant(s) |
|---|---|---|
| American Kratom Association | **$3,036,000** | 11 firms incl. McGuireWoods Consulting, Van Scoyoc, Michael Best Strategies, Upstream Consulting, David Carlucci Consulting |
| **Stop Gas Station Heroin LLC** | **$750,000** | Checkmate Government Relations |
| MIT45, Inc. | $500,000 | McGuireWoods Consulting, Ragnar Group |
| Global Kratom Coalition | $215,000 | **Troutman Strategies** |
| **Botanic Tonics LLC** | $200,000 | **Troutman Strategies** |
| Johnson Foods, LLC | $130,000 | Holland & Knight |
| Raben Group / Botanical Education Alliance | $40,000 | Valente & Associates |
| **Holistic Alternative Recovery Trust** | **$10,000** | Frost Brown Todd |
| Outpost Brands, LLC | $0 (registration) | Akin Gump Strauss Hauer & Feld |
| **End Kratom Addiction** | $0 (registration) | **Bob Good LLC** |
| **TOTAL (issue-text method)** | **$4,961,000** | |

> **SUPERSEDED 2026-08-27 by FINDING 12.** The issue-text search method
> undercounted by **$2,436,500**. Corrected total: **$7,397,500**. Four clients
> were invisible to it entirely, including a **$980,000** account at Miller
> Strategies and a **$290,000** Kratom Trade Association account at Holland &
> Knight. Use Finding 12 for all figures.

### 2. The escalation tracks the campaign

| Year | Disclosed |
|---|---|
| 2016 | $220,000 |
| 2017 | $251,000 |
| 2019-2021 | $500,000 combined |
| 2022 | $370,000 |
| 2023 | $470,000 |
| 2024 | $950,000 |
| **2025** | **$1,345,000** |
| **2026 (through Q2 only)** | **$855,000** |

### 3. The asymmetry

> **CORRECTED 2026-08-27, see Finding 08.** The split below originally placed
> MIT45 on the 7-OH-exposed side and flagged it as a judgment call. That was
> wrong. The Tampa Bay Times documents MIT45 as an AKA-endorsed "Kratom Consumer
> Champion" selling high-potency **mitragynine** extract (Super K tested at 367 mg
> per bottle). It belongs with the incumbents. Corrected figures:
>
> - leaf / pro-ban side: **$4,871,000**
> - organized 7-OH defense (HART alone): **$10,000**
> - **ratio: roughly 487 : 1**

**[I]** Superseded original reasoning, retained for audit: sorting clients by side
was called a judgment call, with MIT45 treated as ambiguous because it sells
extracts and its CEO was reported arranging FDA and HHS meetings. The original
figures were $4,371,000 vs $510,000, a ratio of 8.6:1.

The cleaner comparison needs no judgment call at all. **The Holistic Alternative
Recovery Trust exists specifically to defend 7-OH. It disclosed $10,000.** The
American Kratom Association alone outspent it about **300 to 1**.

**[I]** A regulatory fight this lopsided does not require a conspiracy to explain
the outcome. It requires only that one side could afford to be in the room.

### 4. The name comes off the filings

- **2022 Q4 - 2024 Q1:** Botanic Tonics LLC lobbies **under its own name** via
  Troutman Strategies. $200,000. Issues: FDA oversight of dietary supplements,
  H.R.9634 Federal Clarity for Kratom Consumers Act, Federal Kratom Consumer
  Protection Act (H.R. 5905 / S. 3039). Entities: FDA, House, Senate.
- **2024 Q2 - 2025 Q2:** the same registration continues but reports **$0 income**.
- **2025 Q3:** **Stop Gas Station Heroin LLC** appears via Checkmate Government
  Relations at **$150,000 in its first quarter**, reported as funded by Ross.

**[I]** The disclosed spending moves off the company's own name and into an opaque
LLC at the exact point the campaign changes objective, from protecting kratom to
banning a competing formulation. The vehicle's name does the argument's work: it
brands the *competitor* as heroin.

### 5. Escalation of who was lobbied

Stop Gas Station Heroin's own filings, quarter by quarter:

| Quarter | Amount | Government entities contacted |
|---|---|---|
| 2025 Q3 | $150,000 | House, Senate |
| 2025 Q4 | $300,000 | **FDA, HHS, House, Senate, White House Office** |
| 2026 Q1 | $150,000 | FDA, HHS, House, Senate, White House Office |
| 2026 Q2 | $150,000 | FDA, HHS, House, Senate, White House Office |

Registered lobbyists on the account: **Charles "Ches" McDowell**, Frederick
Vaughan, Caitlin Koury, Muhammad Rahim, Timothy Blanchat, Teresa Morgenstern.

**[I]** The White House Office enters the contact list in Q4 2025 and never leaves.
That is the same window in which the private Vance meeting was reported.

Corpus-wide agency contact counts: House 211, Senate 178, **FDA 67, HHS 51, White
House Office 45**, DEA 6, EOP 6, USDA 1.

> **CORRECTED 2026-08-27 by FINDING 14.** The claim below is WRONG. Botanicals
> for Better Health and Wellness, invisible to the issue-text search, lobbied
> **DEA directly**, plus **DOJ, OMB and the Executive Office of the President**,
> on a $980,000 engagement. The persuasion did reach the issuing agency.

**[I] SUPERSEDED:** DEA appears only 6 times across a decade of filings, and those are the 2016
filings opposing the original scheduling proposal. **The agency that actually
issued the 2026 Schedule I action is almost absent from the disclosed lobbying
record.** Either the persuasion ran through HHS and the White House rather than
DEA, which is what the contact pattern suggests, or it is not in these filings.

---

### 6. New threads

- **Global Kratom Coalition** shares Botanic Tonics' registrant. Identify its
  funders and whether it is a Ross-aligned vehicle.
- **"End Kratom Addiction"**, registered via **Bob Good LLC**. A former member of
  Congress lobbying the anti-kratom side. Identify the client behind it.
- **Outpost Brands, LLC** via Akin Gump. Registration only, no reported spend.
- **Frederick Vaughan** on the Checkmate account. Not named in any coverage
  reviewed. Identify prior government service.
- **Johnson Foods, LLC**, $130,000 via Holland & Knight. Unexplained.
- **David Carlucci** (56 activities) and **Robert Wasinger** (31) are the most
  active individual lobbyists in the corpus after the Haddows. Both warrant
  background checks for prior government positions.
