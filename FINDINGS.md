# CASE SEVENFOLD

**Obsidian Watch Group** · opened 2026-08-27 · Principal: Jay Puckett
**Subject:** Whether the federal Schedule I action against 7-hydroxymitragynine
(7-OH) was shaped to protect the market position of leaf-kratom products in which
serving federal officials hold financial interests.

**Status:** OPEN. Active collection. Nothing here is cleared for publication.

---

## Provenance key

Every claim below carries one of these. This is not decoration; it is the
difference between a finding and a rumour.

- **[P]** primary document, captured in `exhibits/`, sha256 in `exhibits/MANIFEST.tsv`
- **[S]** secondary reporting, outlet named
- **[I]** OWG inference, reasoning stated
- **[U]** unverified, needs a primary before it leaves this file

---

## 1. The short version

A sitting Secretary of Homeland Security holds a disclosed equity position of
**$500,001 to $1,000,000** in a leaf-kratom manufacturer. Before taking that
office, as a US Senator, he publicly fronted a federal enforcement push against
**7-OH**, a competing concentrated product class. That push has since become a DEA
temporary Schedule I action carrying a concentration threshold that **explicitly
exempts the product category he is invested in**. The manufacturer's founder is a
securities fraudster operating under a changed name who has moved **$1.73M** in
traceable federal political money, including **$1,000,000** to a PAC aligned with
the Health Secretary who co-announced the enforcement action.

The Senate Finance Committee's ranking member opened an inquiry into exactly this
on **2026-08-05**, with a **2026-08-31** response deadline.

---

## 2. The regulatory mechanism, which is the load-bearing fact

DEA issued two Notices of Intent on **2026-07-01**, published **2026-07-06**. [P]
`exhibits/fedreg_7oh_threshold_20260706.html`

- 7-OH **above a specified threshold** goes to Schedule I.
- Separately: mitragynine pseudoindoxyl, MGM-15, MGM-16 to Schedule I.
- The threshold is **0.05% 7-OH by dry weight**. [S]
- Natural kratom leaf below that threshold is **explicitly excluded**. [S]
- **Mitragynine** -- the plant's most abundant opioid alkaloid, and the active
  compound in leaf products -- is **not scheduled at all**. [S] Public Citizen

**[I] This is the whole case in one line.** The action is framed publicly as a
crackdown on kratom. It is in fact a crackdown on one *competing formulation* of
kratom, drawn at a concentration line that leaves the incumbent leaf-product
market untouched and removes its cheaper, more potent rivals from shelves.
Public Citizen, which supports scheduling BOTH alkaloids, calls the result a
crackdown that leaves most of the products blamed for deaths on sale. [S]

---

## 3. The official: Markwayne Mullin

Correct spelling is **Markwayne Mullin**, one word. R-OK. US Representative
OK-02 2013-2023, US Senator 2023-2026, **Secretary of Homeland Security** from
2026. [S]

| Item | Detail | Prov |
|---|---|---|
| Holding | Botanic Tonics, LLC (Broken Arrow, OK) | [S] |
| Range | **$500,001 - $1,000,000** | [S] |
| Vehicle | OGE nomination filing, March 2026 | [S] — **the filing itself is NOT yet in our hands** |
| Acquisition date | **UNKNOWN.** Reporting states the documents do not show when he invested | [S] |
| Public act | Appeared 2025-07-29 with RFK Jr. and FDA Commissioner Makary announcing federal action on 7-OH | [S] |
| Quote | "It's an addiction that's ruining lives... it's truly killing people" | [S] |
| Alleged act | Urged HHS officials to remove kratom harm warnings from the FDA website, both as senator and as DHS Secretary | [S] NYT |
| Response | DHS says he "follows all ethics and conflict of interest standards and has not lobbied for any individual or company" | [S] |

**Open items on Mullin, in priority order:**
1. Obtain the actual OGE Form 278e and his **ethics agreement**. Did he commit to
   divest? Did he? An unfulfilled divestiture commitment is a different and much
   sharper matter than a disclosed holding.
2. Establish the **acquisition date**. If the position predates 2025-07-29, the
   conflict existed at the podium.
3. His House and Senate annual disclosures 2013-2025. If Botanic Tonics never
   appeared there, either it was acquired late or it was under-reported. Both are
   worth knowing.

---

## 4. The founder: Jerry D. Cash, now J.W. "Jerry" Ross

| Item | Detail | Prov |
|---|---|---|
| 2009 | SEC charges Jerry D. Cash, CEO and board chairman of Quest Resource Corp, with securities fraud; misappropriation; >$5M on an Oklahoma City mansion | [P] SEC LR-21087 + complaint PDF |
| 2010-11 | Sentenced to **108 months**, one count false Sarbanes-Oxley certification, plus $5M | [P] FBI Oklahoma City |
| ~2013-14 | Released; **changes name to J.W. Ross** | [S] |
| now | Founder, Botanic Tonics LLC; files with FEC from **Malibu / Los Angeles, CA** | [P] FEC |

**[I]** The name change is lawful and by itself proves nothing. Its significance
is that it decouples the public-facing founder of a company lobbying the federal
government from a federal securities-fraud conviction, and every outlet that
covered the influence campaign had to reconnect it manually.

---

## 5. The money, from FEC primaries

Identified on **employer = BOTANIC TONICS, occupation = FOUNDER**, not on name
alone. A bare "ROSS, JERRY" name query returns **1,331 rows** of unrelated
donors and must not be used. [P] `exhibits/fec_employer_botanic_tonics_schedA.json`

| Recipient | Amount | Prov |
|---|---|---|
| Republican National Committee (all 2026-02-17) | $443,000 | [P] |
| Kennedy Victory Fund 2024 (2025-01-02, 2025-02-05) | $161,800 | [P] |
| Team Kennedy (2023-09-19) | $6,600 | [P] |
| Libertarian National Committee | $41,300 | [P] |
| 10 state Libertarian / Free New Mexico parties | $77,973 | [P] |
| **Ross personal total** | **$730,673** | [P] |
| **Botanic Tonics LLC -> MAHA PAC (C00821439)** | **$1,000,000** | [P] `exhibits/fec_botanic_tonics_schedA.json` |
| **TRACEABLE FEDERAL TOTAL** | **$1,730,673** | [P] |

### The RNC contribution is the statutory ceiling, exactly [P]

The $443,000 is not a round number chosen by a donor. It is the **maximum an
individual may give a national party committee in one calendar year**, across all
four permitted accounts, under FEC's published 2025-2026 limits:

    main account          $ 44,300
    convention account    $132,900
    headquarters account  $132,900
    recount/legal account $132,900
                          --------
                          $443,000

Ross gave that sum on a single day, 2026-02-17, in four transactions matching
those four figures. FEC images `202603209853749439`, `...438`, `...743128`.

**Qualification we raise ourselves:** all four rows carry the memo
`PARTNERSHIP ATTRIBUTION` and three sit on the "Other Federal Receipts" line, so
the funds arrived through an entity and were attributed to Ross as a partner.
Whether they originated in personal accounts is **not established** [I].

See `FINDING_23_ross_money.md`.

### Two conflicts in the reporting, both now resolved against the primary

1. **$500K vs $1M to MAHA PAC.** Both were right. FEC shows **two** contributions
   of $500,000 each: **2026-03-04** and **2026-04-09**. Outlets writing in spring
   caught only the first tranche. [P]
2. **"~$162,000 to RFK Jr."** Confirmed. Kennedy Victory Fund 2024 receipts dated
   2025-01-02 and 2025-02-05 total **$161,800**. [P] Total across all
   Kennedy-affiliated committees including 2023 is **$168,400**.

### Unreported finding: the Libertarian cluster

**$119,273** to the Libertarian National Committee and ten state parties, dated
**2025-01-02** and **2025-02-05** -- the same two dates as the Kennedy money.
**[I]** Identical dates across a national committee and ten state committees is
the allocation signature of a **joint fundraising committee**, not eleven separate
decisions. Worth identifying the JFC. No outlet reviewed has reported this.

### The vehicle: MAHA PAC, and where traceability ends [P]

The $1,000,000 from Botanic Tonics LLC did not go to a candidate. It went to FEC
committee **C00821439**, whose registered name history is the finding:

    2022   PEOPLE'S PHARMA MOVEMENT
    2024   AMERICAN VALUES 2024      <- the RFK Jr. presidential super PAC
    2026   MAHA PAC

Same committee, same treasurer (Tony Lyons). Identity confirmed by its donors:
Timothy Mellon $25,003,300, Gavin de Becker $14,000,000, Nicole Shanahan
$4,000,000, all complete per-donor queries.

Botanic Tonics LLC is its **13th largest** itemized receipt of 834, and one of
only two corporate donors in the top fifteen.

**MAHA PAC's largest recurring outflow is $4,048,428 to MAHA ACTION, INC.**, a
**501(c)(4)**, EIN 994785075, Vienna VA [P IRS BMF], five of six transfers filed
as `CHARITABLE CONTRIBUTION`. A c4 does not disclose donors. That is where
itemized federal traceability stops.

**[I] and a limit we impose on ourselves:** every observed transfer to the c4 is
dated on or before **2026-02-02**, and Botanic Tonics' first $500,000 is
**2026-03-04**. Their money cannot be traced into those transfers and we do not
claim it. See `FINDING_24_the_pipeline.md`.

### Timing that needs no interpretation

- **2025-12** DOJ drops the seizure case against Botanic Tonics. [S]
- **2026-03-04** Botanic Tonics sends MAHA PAC its first $500,000. [P]
- **2026-03** Mullin nominated to DHS; the stake becomes public. [S]
- **2026-04-09** Second $500,000. [P]
- **2026-07-01** DEA moves on 7-OH only. [P]

---

## 6. The lobbying apparatus

| Entity | Detail | Prov |
|---|---|---|
| **Stop Gas Station Heroin** | Opaque group funded by Ross. The name itself is the message discipline: it makes the *competitor* the villain | [S] |
| **Checkmate Government Relations** | Retained by the above. Reported quarters: Q3'25 $150K, Q4'25 $300K, Q1'26 $150K | [S] |
| | **ARITHMETIC CONFLICT:** those quarters sum to **$600,000**, but one summary asserts $750,000. Unresolved. Check LDA filings directly | [U] |
| **Ches McDowell IV** | Principal. Close to the president's elder sons. Firm employs a **nephew of RFK Jr.** and the **son of Chris LaCivita** (Trump 2024 co-campaign manager) | [S] |
| Other registered lobbyists | Caitlin Koury, Usman Rahim, Luke Blanchat, Teresa Morgenstern | [S] |
| **Jeff Miller** | Trump fundraiser, retained by "Botanicals for Better Health and Wellness"; that group gave **$50,000** to the Trump inaugural committee | [S] |
| **Ryan Niddel** | CEO, Diversified Botanics / MIT45. Hired a Trump campaign lobbyist post-inauguration, arranged FDA and HHS meetings | [S] |

---

## 7. Other officials in the frame

**No second official with a disclosed equity stake has been identified yet.**
Mullin is so far unique in that respect. The others are connected by money flow
or by act, which is a different and weaker category, and must be written that way.

| Official | Connection | Category | Prov |
|---|---|---|---|
| **Robert F. Kennedy Jr.**, HHS Sec | $168,400 from Ross to his committees; $1M from Botanic Tonics to the aligned MAHA PAC (run by ally **Tony Lyons**); co-announced the 7-OH action; called Ohio Gov. DeWine | money + act | [P]/[S] |
| **JD Vance**, VP | Private meeting with Ross and McDowell; headlined a Ross-hosted fundraiser Feb 2026; $443K to RNC around it | access | [S] |
| **Mike DeWine**, Ohio Gov | Planned a **full** kratom ban Aug 2025; after a Kennedy call, narrowed it to 7-OH only | act | [S] |
| **Ashley Moody**, Sen (R-FL) | Intervened to end a Tampa event when RFK Jr. was asked if he was "in the pocket of Feel Free". **No financial tie identified** | act | [S] |
| **Marty Makary**, FDA Comm | Co-announced the action | act | [S] |
| **Ron Wyden**, Sen (D-OR) | **Adversarial.** Opened the Finance inquiry 2026-08-05 | oversight | [P] |
| Brett Giroir, Scott Gottlieb | Historical: Gottlieb recommended Schedule I 2018, Giroir rescinded it | context | [S] |

**Collection still open:** FEC sweep on MIT45, Diversified Botanics, CBD American
Shaman, Stop Gas Station Heroin and Checkmate employers was **blocked by rate
limit, not returned empty**. Do not read the absence of results as absence of
money.

---

## 8. The harm record, kept separate from the money

Stating these plainly because the market fight tends to bury them.

- **26 deaths** over five years where a coroner attributed death to
  **mitragynine** -- the alkaloid that is *not* being scheduled. Toxicologists
  estimate hundreds more. [S] Public Citizen, 2026-08-03
- **5,200+** overdose decedents 2020-2024 with kratom in their system. [S] NYT
- **Kevin Oliveira**, 32, dead 2025-04-21, Tequesta FL. ME cited high blood
  mitragynine. Feel Free Classic bottles present. [S]
- **Wyatt Wheeler**, dead Oct 2022, six weeks after starting a kratom extract. [S]
- *Torres v. Botanic Tonics*, class action over undisclosed kratom content,
  settled **$8.75M**. **Date conflict:** one source says 2024, another Oct 2025.
  Unresolved. [S]

**[I]** Both sides of this commercial fight are selling an opioid. The
documented body count attaches substantially to the leaf/mitragynine products
that the scheduling action leaves on the shelf. Any OWG output must not read as
a defence of 7-OH.

---

## 9. What would break this case

Written down deliberately, so we test it instead of confirming it.

1. **If Mullin acquired the stake after 2025-07-29**, the podium appearance was
   not conflicted at the time and the story narrows sharply. **We do not know the
   acquisition date.** This is the single most important open fact.
2. **If his ethics agreement required and achieved divestiture**, the present-tense
   conflict may be resolved even though the historical one is not.
3. **A 0.05% threshold may be defensible on pharmacology alone.** If the science
   independently supports that line, "the threshold was drawn to spare the
   incumbent" collapses to coincidence. Needs a toxicologist's read of the DEA
   record, not our assertion.
4. **Public-health merit.** 7-OH concentrates genuinely are far more potent. A
   corrupt process and a defensible outcome can coexist.

---

## FILED

**2026-08-27 — Public comment filed to docket HHS-OASH-2026-0232** (HHS OASH,
Request for Information on the 7-OH scheduling threshold).
**Comment Tracking Number: `mtc-56yj-nmij`.** Eight sections, 2,268 words,
submitted as `OWG_Comment_HHS-OASH-2026-0232.pdf`. Status: submitted, pending
agency review and posting. Comment period closes 2026-09-10.

## 10. Next actions

- [ ] Obtain Mullin's **OGE Form 278e and ethics agreement** (OGE / Senate HSGAC nomination record)
- [ ] Mullin House + Senate annual disclosures 2013-2025, test for prior Botanic Tonics reporting
- [x] ~~Resume the blocked **FEC employer sweep**~~ **DONE 2026-08-28**, full API key obtained. Findings 22 update + 23
- [x] ~~Identify the **joint fundraising committee**~~ **Kennedy Victory Fund 2024**, allocating outward to the LNC and state parties. Finding 23 s4
- [x] ~~Settle the $600K vs $750K conflict~~ **$750,000**, Checkmate Government Relations for Stop Gas Station Heroin LLC. Confirmed again 2026-08-28 against the full 298-filing corpus
- [ ] **Atallah's Botanic Tonics start date** vs the Feb 2024 publication. FEC places him there by 2025-09-30 and at JUUL Labs through Jan 2021; the gap is unresolved. Finding 06 addendum
- [x] ~~**Patent search: 9-hydroxycorynantheidine synthesis routes.**~~ **DONE 2026-08-28. `FINDING_25_the_patents.md`.** 18 documents name the compound; two claim manufacture. **Mitradyne Corporation** (EP4538367, priority 2023-09-20) claims the cell-free C9 hydroxylase producing it, in a claim adjacent to its claim for the 7-OH enzyme. **CB Therapeutics** (US2025/0179544, priority 2023-12-01) claims recombinant-cell production of corynanthe-type alkaloids and names it. The compound is an **intermediate on the biosynthetic route to mitragynine**, so any enzymatic mitragynine facility passes through it
- [~] **Mitradyne Corporation.** PARTIAL, 2026-08-28. All four inventors are **University of Guelph, Molecular and Cellular Biology**: Casaretto, Akhtar, Rothstein, Soubeyrand, who co-author the group's own **cell-free synthesis** papers on cannabis metabolites, matching claim 11. Agent is Dehns, London. Controlled negatives: no SEC filings, **zero** Canadian federal grants (nonsense-string control returns 0, empty returns 1,193,970), no web presence. **The Ontario registration itself was NOT obtained**: MRAS is decommissioned, Canada's Business Registries WAF-blocks, and the Corporations Canada federal search failed its own control, so no conclusion on federal incorporation. Finding 25 addendum
- [ ] **Ontario Business Registry search for Mitradyne** (free but needs an interactive session): registration number, incorporation date, directors
- [ ] Whether the **University of Guelph** holds an interest via its commercialisation office
- [ ] Identify the **partnership or LLC** behind the `PARTNERSHIP ATTRIBUTION` memo on the $443,000
- [ ] Constituent letter to **Sen. Blackburn (TN)**, who signed the 2026-03-18 letter and takes no industry money
- [ ] **PACER**: *Torres v. Botanic Tonics*; the 2023 in-rem seizure action and its Dec 2025 dismissal. The dismissal docket may state a reason
- [ ] Obtain the **Wyden letters** themselves, all three
- [ ] Re-capture the five **blocked sources** (DEA, Public Citizen x2, congress.gov, Missouri Independent) via an alternate path
- [ ] Determine whether Botanic Tonics itself sells any product above the 0.05% line
