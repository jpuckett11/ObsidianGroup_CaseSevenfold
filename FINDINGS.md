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
| Vehicle | OGE nomination filing, March 2026 | [S], **the filing itself is NOT yet in our hands** |
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



















**2026-08-28, `REMEDIATION.md` s10, the principle underneath all of it.** In the
researcher's words: **"A unit is only as strong as its weakest member. So you
strengthen the weakest member. You do not discard them."** Stated as operational
logic rather than sentiment: removing the least capable component does not raise the
average, **it lowers the ceiling**, because everyone remaining learns what happens to
whoever falls behind next, and people who expect to be written off do not extend
themselves. Applied to **42.4 million untreated**, the response has been to schedule
one molecule at a time, **managing the consequences of the abandonment rather than
ending it.** Also added to the README.

**2026-08-29, Finding 49: Tennessee and West Virginia appropriated nothing, and Utah's
enforcement money alone would have treated 291 people.** **[P]** with a working
control. Ran the Finding 48 check on both states: **neither has an appropriations act
mentioning kratom.** The control matters because it is a negative, and Open States
indexes full bill text for all three states, with **Tennessee's HB 2631/SB 2690
"Appropriations, As enacted"** and **West Virginia's supplemental appropriations bills**
both surfacing on other terms. **The instrument works; the money is not there.**
**Tennessee is the sharper case:** Public Chapter 950 orders **every county medical
examiner to test every suspected overdose decedent for kratom**, and physicians to test
in suspected overdose and **neonatal abstinence syndrome**, and funds none of it. **An
unfunded mandate on county coroners**, where Utah appropriated $286,800 to courts and
$360,000 to crime labs for the same kind of cost. **West Virginia's fee revenue,
computed from the actual registry (418 products, 31 registrants): $83,600 + $9,300 =
~$92,900 a year, which treats fourteen people.** **[I]** The 11% privilege tax,
scaled from national market estimates by population share and **labelled soft**, yields
roughly **$756,000 to $1,162,000**, or **115 to 177 people**. **A FOIA to the WV Tax
Commissioner replaces that estimate with a fact.** **The honest answer to whether these
revenues could treat everyone is no**, and not close: WV's ~221,000 untreated would
cost ~$1.45 billion, so the tax covers 0.08%. **But that is the wrong comparison and it
lets the states off.** The right one: **Utah's $1,905,400 of kratom enforcement money
would put 291 people on methadone for a year, and the state spent it on crime labs,
prisons, parole and courts. The single Adult Probation and Parole line, $915,000, is
140 people, appropriated in the same session Utah let 940 people's worth of treatment
expire.** **Nobody had to find new money. The money was appropriated. It went somewhere
else.** Caveats stated: "people treated" is medication cost only and a real slot costs
more, and neither TN nor WV's general treatment appropriations are in this record.

**2026-08-29, Finding 48: Utah DID pay for its kratom law. $1,905,400 a year, to crime
labs, prisons, parole and courts.** **[P]** Utah H.B. 3 (2026), Enrolled Copy.
**Corrects Finding 43**, which said Utah regulated the molecule for free. The kratom
bill appropriates nothing; **the general appropriations act contains eight line items
each tagged "To implement the provisions of Kratom Adjustments (Senate Bill 45, 2026
General Session)."** Where it went: **Adult Probation and Parole $915,000**, **Prison
Operations $684,000**, **District Courts $286,800**, Board of Pardons and Parole
$13,600, **State Crime Labs $6,000 ongoing plus $360,000 one-time**. **Ongoing General
Fund to justice agencies: $1,905,400.** And the **Department of Agriculture and Food,
which actually runs the registry, was cut $120,600.** **Set that against Finding 43:
Utah's proposed FY27 appropriation for ALL opioid remediation is $1,600,000.** **Utah
budgeted more recurring money to police, imprison, supervise and prosecute around one
kratom statute than it budgeted for its entire opioid remediation programme. 1.19 to
1.** The largest single line, **$915,000, supervises people after conviction.** From
the same session, H.B. 8 sets what the state charges: **Kratom Product Registration
$475**, **Alkaloid Potency Testing $141**, pesticide $194, heavy metal $134, mycotoxin
$158. **The state charges $141 to test potency and cut the department that does the
testing.** **[I] Finding 42 with the general ledger attached: Utah did not decline to
spend, it spent $1.9M a year on probation officers, prison beds, courtrooms and a crime
lab.** **Method note: this was found because Open States indexes bill TEXT, so
appropriations acts surface on a kratom search. The budget sweep the investigator asked
for is now tractable, and Findings 44 and 46 should be treated as incomplete until the
same check is run for Tennessee and West Virginia.**

**2026-08-29, Finding 47: only one company in America has to disclose anything about
7-OH, and the question is now before the Sixth Circuit.** **[P]** SEC full-text search
with a positive control, plus federal dockets. Collects the threads left open by
Findings 39 to 46. **The industry is private.** Checked every registrant behind the
thirty 7-OH products on West Virginia's registry: **Genrev Labs (210 mg), STNR
Creations (100 mg), The Empire Distribution (Dopium), Real Botanicals, Prof Whyte's are
all non-filers.** Control passes: LFTD returns CIK 0001391135. **SEC full-text search
for "7-hydroxymitragynine" returns 5 filings and every one is LFTD Partners.** "STNR
Creations" 0, "Dopium" 0, "Roxy Complex Alkaloid" 0. **[I] There is exactly one window
into this industry's finances and Finding 40 used it. The company selling 210 mg
tablets owes the public no accounting at all, and neither does the one selling a
product called Dopium. That is a structural answer, not a research failure.** **The
Ohio precedent is now on appeal.** *Titan Logistics Group LLC v. Tischler*,
3:26-cv-01300 (N.D. Ohio), the decision Judge Helmick relied on for the hemp TRO, is
before the **Sixth Circuit as 26-3648**, docketed 21 July 2026. **The Sixth Circuit
covers Ohio, Michigan, Kentucky and Tennessee**, so a ruling on state authority over
these products would be binding in **the state that banned kratom outright** (F44).
Flagged carefully as inference: these are hemp cases and F41 was corrected once for
blurring that line, but the doctrine is the same doctrine. **Two clocks converge:** the
Ohio **TRO expires 4 September**, the **comment period closes 10 September**, six days
apart, no connection claimed. **WV SB 534 obtained**: repeals and re-enacts Article 12F,
carries the Agricultural Fees Fund disposition over unchanged, and establishes **"a
licensing fund"** not a treatment fund. Finding 46 stands. **Torres settled**, final
approval and judgment 20 October 2025 before Judge Chhabria. Section 6 lists every
string that did not close and why.

**2026-08-29, Finding 46: West Virginia taxes kratom at 11 percent and spends every
dollar of it enforcing the kratom law.** **[P]** from the West Virginia Code. Third
state under the Finding 43 method. The article sits in **Chapter 19, AGRICULTURE**, not
the health code, and it is the same article that produces the 30-product 7-OH registry
in Finding 39. **§19-12F-7 levies "a privilege tax equal to 11 percent of the retail
sales price" of kratom, "in addition to all other applicable taxes"** and then forbids
the retailer from showing it: **"shall not be added by the retailer as a separate
charge or line item"** on any receipt. **The consumer pays it and is not permitted to
see it.** Disposition, §19-12F-7(f): **"All money received from the privilege tax...
shall be deposited into the Agricultural Fees Fund"**, which §19-12F-8 says is **"for
the use of the commissioner for administering and enforcing the provisions of this
article."** Same for the **$1,500** application fee, the **$300** annual fee and the
**$200 per product** across **450 products**. **Every revenue stream in the article
funds the article.** Checked across six sections: **treatment 0, substance abuse 0,
recovery 0, prevention 0, abatement 0**, with kratom throughout as control. What it
does build: **three state agencies plus state and local law enforcement conferring
monthly** (§19-12F-9) and criminal fines of $1,000, $5,000 and $10,000 (§19-12F-11).
**[I] Three states now, three different mechanisms, one result. Utah regulated and cut
treatment 74%. Tennessee prohibited and appropriated zero. West Virginia taxes it and
routes every dollar to enforcement. A state that prohibits, a state that regulates and
a state that taxes all built enforcement and none built care. West Virginia is the
sharpest because it is the only one that found money in kratom, and it spent it on
kratom enforcement.** **Sweep blocked and the blockers are recorded rather than worked
around:** LegiScan 403, **Open States needs a free API key we do not hold**, and
NASHP's settlement tracker turned out to be dated **05-17-24** and about governance
rather than spending, which was established only after pulling all 22 kratom states
from it. **An Open States key unblocks the statute half across all fifty states in one
pass.**

**2026-08-29, Finding 45: what pulling these people up would be worth. About $90B a
year, for about $13B, and it costs the same per person as treating kidney disease.**
**[I] ESTIMATE**, every input sourced, every step of arithmetic shown so it can be
checked or destroyed. Written as the constructive inverse of Finding 44 s6, which
priced doing nothing. **Nobody prices the upside, so we did.** Derived not assumed:
AAF's $702.1B lost output over 12.5B lost work hours gives **$56.17/hour, $112,336 per
worker-year**. Applied to **914,000 to 2,000,000** prime-age workers out of the labour
force due to opioids, at employment rates of 30 to 50 percent bracketing the 42.9
percent from a therapeutic-workplace trial: **$30.8B to $112.3B a year in output**.
Cost at **NIDA's own published prices**, methadone $6,552 or buprenorphine $5,980 per
patient per year: **$12.0B to $13.1B** for two million people. **Mid case ratio about
6.9 : 1.** AAF's separate framing needs no arithmetic from us: opioids cost **0.6
percentage points of annual real GDP growth**, 2.0 percent actual against 2.6 percent
counterfactual, **thirty percent faster growth**, roughly **$180B a year, recurring**.
**And the comparison that should end it, NIDA's own:** diabetes $3,560/yr, **kidney
disease $5,624/yr**, **opioid use disorder on methadone $6,552/yr**. Treating the
addiction costs about a thousand dollars a year more than treating the kidneys, and
nobody argues dialysis is a lifestyle choice. **Section 6 states where it is weak and
it is not decoration**: the labour data is opioid-specific and does not scale to the
42.4M all-SUD figure, it is 2015 vintage while this case is about stimulants, the 42.9
percent comes from one trial with 91 participants, output per worker is an aggregate so
step 3 is probably optimistic, drop-out is not modelled, and the $180B and $89.9B are
overlapping views that must not be added. **What survives: at the most pessimistic
corner tested, 914,000 people at 30 percent on the dearest drug, it is still $30.8B
returned for $12.9B spent, 2.4 : 1. The investment returns more than it costs at every
combination tried.** That is the finding, not the point estimate. **The argument was
never that this is unaffordable. Nobody had run the sum.**

**2026-08-29, Finding 44: Tennessee's answer to a death was to criminalise the user and
delete kratom from the treatment title.** **[P]** Public Chapter 950, "Matthew
Davenport's Law," signed by Gov. Bill Lee, effective **1 July 2026**, named for a
Chattanooga man who died in 2024. **Possession of kratom is now a Class A misdemeanor
in Tennessee; sale is a Class C felony.** The definition reaches "any alkaloid or
alkaloid derivative... created by chemical synthesis or biosynthetic means" and
anything "substantially chemically equivalent." **The word "treatment" appears zero
times in the act; "kratom" appears 14, so the control works. Appropriation: $0.** The
companion bill, **HB 1647, would have made simple possession a Class D FELONY** and
sale a Class B felony, which is the range the debate occupied. **[S]** The regulatory
alternative, HB 2594, a Tennessee KCPA, never reached a floor vote. **Section 3 is the
one that matters: the act deletes ", including Kratom" from TCA 33-2-1404(a)(8)**,
which sits in **Title 33, Mental Health and Substance Abuse Services**, Part 14, the
licensing statute for **nonresidential substitution-based treatment centers for opiate
addiction**. **In the same act that made possession a crime, the legislature struck
kratom out of the opioid treatment clinic statute.** **[U] The text of (a)(8) before
deletion could not be obtained** (Justia 403, Casetext 410, FindLaw 403, LawServer
307), so what the phrase was attached to is unknown and not guessed at. **That single
subsection is the highest-value outstanding item here.** What the act does instead:
mandatory kratom testing in overdose autopsies, in toxicology for suspected overdose
and neonatal abstinence syndrome, and a drug-free-workplace definition. **Real data on
the dead, nothing for the living.** **THE SCALE, which is the investigator's point.**
Against the **$425.0 billion a year** estimated burden of opioid-related adverse events
and undertreatment (range $164.5B to $1,215.5B, DOI 10.3389/fpubh.2026.1824038):
Utah's entire expiring treatment line of **$6,161,003 is 0.0014%** of it, the
**$1,600,000** replacement is **0.00038%**, and **Tennessee's appropriation is 0%**.
**[I] These are not budget decisions at the scale of the problem, they are rounding.
And the $425 billion is not a proposal, it is what is already being spent on the
aftermath.**

**2026-08-29, Finding 43: Utah answered it. Same session, molecule regulated for free,
treatment cut by three quarters.** **[P]** from le.utah.gov. Finding 42 named this as
its decisive unresolved question and Utah is the file's best-documented state.
**S.B. 45 "Kratom Adjustments", signed 26 March 2026: "Money Appropriated in this
Bill: None," and the word "treatment" appears zero times** (kratom appears 93, so the
control works). H.B. 387 identical. **A regulatory bill not appropriating proves
nothing, so we checked the budget.** In FY24 Utah appropriated **$7,061,033 ongoing**
to opioid remediation and **it expires at the end of FY26**. The expiring programmes:
PATH treatment for pregnant individuals **$933,333**, ED/urgent care MOUD induction
**$1,200,000**, **MOUD in jails $1,000,000** which the state's own document says has
**"no other funding"**, FQHC OUD treatment access **$1,300,000**, prevention
**$2,627,700**. Total **$6,161,003**. Proposed replacement: **$1,600,000**. A **74
percent** cut. On **5 March 2026** the Executive Appropriations Committee **rescinded**
grants of **$150,000 to Fit to Recover** and **$100,000 to the School of Addiction
Recovery**, and cut **Jacky's Recovery Support Services from $269,900 to $100,000**,
**$419,900 removed from three recovery organisations in one sitting**. And the money is
not gone but locked: **$543 million over 17 years**, with HB 10 (2025) restricting
future spending to **interest only**. **The steelman is stated in the finding:** an
endowment is a defensible design. **What it does is fund a person in 2041 and not the
one in the jail programme now.** Chronology is stated precisely because the cuts came
**before** the July poison control alert and death, and **no causal claim is made.**
Corrects Finding 42 in one direction too: **Utah does fund treatment**, just less of it,
in the same months it regulated a product for nothing and won a federal lawsuit about
it. One state; twelve to seventeen other KCPA states unchecked, and the method now
takes an hour.

**2026-08-29, Finding 42: every government in this file acted on the molecule. None of
them acted on a person.** **[I] SYNTHESIS**, no new primary evidence, built on Findings
32, 34, 35, 36, 37, 39 and 41. **Drafted to complicate the reading that representatives
do not represent, and corrected by the investigator before it was published.** The
first draft credited four state legislatures for acting. **Every action it credited was
about a molecule.** Utah banned a combination product, West Virginia refused a
registration, Missouri and Ohio restricted an intoxicant. **None is help for a person
with a substance use disorder**, and crediting them was crediting the thing Finding 34
showed does not work. **The corrected claim is harder: they do act, at every level, and
the person is the object of none of it.** The mechanism is not free versus expensive,
because Utah spent real money defending its statute. **It is that governments will
spend on control and not on care.** Four states absorbed federal litigation to stop a
sale; the cheapest care instrument in the file, a cap that cost **$68 a head** to make
effective (F35), took twenty-five years and is still half fixed, and the safe harbour
Congress ordered is twenty months late. **[S]** Roughly **13 to 18 states** have a KCPA
and about **10 ban outright**, so this is the national picture rather than four unusual
states, **which makes it worse.** The finding names its own decisive gap: **we have not
checked whether any of those states funded treatment in the same session**, and that
absence needs a control before section 3 stands.

**2026-08-29, Finding 41: the industry is not winning on preemption. It is winning
where states wrote protectionist laws.** **[P]** Ohio TRO order and Missouri complaint,
obtained and hashed. **Neither case is about kratom** (Missouri: kratom 0, hemp 189;
Ohio TRO: kratom 0). They are in this file because **Lifted Liquids is a plaintiff in
both**, the same company behind the Roxy 7-OH tablets in Finding 39. **Ohio SB 56 let a
company hold a licence only if its products were "sourced, manufactured, and
distributed solely within Ohio."** Judge Jeffrey J. Helmick granted a TRO on **7 August
2026**, extended 19 August to **4 September**, on Commerce Clause discrimination, and
stated the governing rule: **"absent discrimination, a State may exclude from its
territory, or prohibit the sale therein."** Ohio's brief **"does not substantively
respond"** to the motion. **Missouri HB 2641 has the identical defect**, products legal
"only if such products are grown and manufactured entirely in Missouri." **Set against
Utah, which banned combination products for everyone, wrote nothing about where they
are made, and WON on state police powers (Finding 37).** **[I] The recommendation this
finding exists to make: a state should restrict the product on its terms and write
nothing about where it is made. The in-state licensing clause is not the price of
protecting the public, it is the thing that loses the case.** Worth more to the
officials being sued than anything else here.

**2026-08-29, Finding 40: a public filing prices the stake at half of revenue, and
warns of bankruptcy.** **[P]** LFTD Partners Inc. (ticker
**LIFD**, CIK 0001391135) is the parent of **Lifted Made**, the registrant behind the
**Roxy** 7-OH tablets on West Virginia's list (Finding 39). Because it is public, it
must disclose. Its **Form 10-Q filed 14 August 2026** says the scheduling proposals
"could materially restrict or prohibit the manufacture, distribution, and sale of
certain kratom-derived products sold by the Company and **materially reduce the
Company's revenue, potentially by approximately half or more**," and that it booked an
**inventory reserve of $1,434,458** against kratom-derived inventory. **That is the
number this case did not have.** The same filing discloses the company suing states:
**Missouri Governor Mike Kehoe, AG Catherine Hanaway and Health Director Sarah Wilson**
over HB 2641 (16 July 2026), and Ohio officials over SB 56 (30 July 2026), on
**preemption, Dormant Commerce Clause and vagueness**, **the same theories Botanic
Tonics used against West Virginia (Finding 38) and Utah (Finding 37).**

**CORRECTED 2026-08-29, same day.** The Missouri and Ohio complaints were pulled and
read, and **neither is a kratom case.** Missouri HB 2641 is hemp (**kratom 0 hits,
hemp 189**); the Ohio SB 56 TRO order is intoxicating hemp (**kratom 0 hits**). **The
four-state kratom playbook was our claim, built on the 10-Q's litigation note without
reading the pleadings, and it was wrong.** What the documents support: **the kratom
suits are two, both Botanic Tonics (WV and Utah)**, and the same preemption theory is
run by **Lifted Liquids in two more states on hemp**. The tool is industry-standard
across intoxicant categories, which is weaker than what we said. **The kept fact is
the split outcome: Utah DENIED the kratom injunction on 4 May 2026 on state police
powers, while Ohio GRANTED a hemp TRO on 7 August 2026, extended 19 August to 4
September.** An Ohio statute is enjoined right now and a Utah one is not. An
Agriculture Commissioner sued **personally for damages**, a sitting Governor, two
Attorneys General. **The argument in all of them is that the federal line is the only
line a state may draw**, which would make the July 2026 rule, one molecule scheduled
and the leaf excluded, a ceiling and a floor at once. **[I] Convergent strategy, not
proven concert**; the two companies are rivals and Finding 38 has one naming the
other's products.

**Addendum the same day, and it corrects our own tone.** The filings put numbers to
"half or more" and they are not what this case expected. **H1 2026 net sales
$17,863,400 against cost of goods sold of $18,918,247, so gross profit of NEGATIVE
$1,054,847.** Revenue down about 28% since 2023. **Accumulated deficit $34,444,821**
and the filing states in terms that "**Bankruptcy of the Company at some point in the
future is a possibility.**" Non-hemp products, the segment containing kratom, are
**$9,137,589 or 51%** of H1 sales and **grew** as a share while hemp fell, though
non-hemp is not a synonym for kratom-derived and the finding says so. **[I] A company
with negative gross profit and a written bankruptcy warning, litigating against state
officials, is not
acting from strength.** Desperation explains the litigation volume at least as well as
confidence does, and **this case should stop implying the second without evidence.**
It sharpens rather than blunts the public-health point: a distressed seller with
negative margins has every reason to move volume, and Finding 39 shows the volume is
210 mg, 150 mg and 100 mg, one line branded **Dopium**. Botanic Tonics is private and
its finances are not in this record at all.

**2026-08-29, Finding 39: a state registry, dated six weeks after scheduling, lists
thirty 7-OH products by name. The biggest is 210 mg.** **[P]** West Virginia
Department of Agriculture, **"Registered Kratom Products v 08/14/2026"**, 450 rows,
obtained and hashed. The DEA action issued **1 July 2026**. This list postdates it by
six weeks and contains **thirty products with "7-OH" in the product name**: **7Rox Max
210mg** and **7Rox Super 150mg** (Genrev Labs), **STNR and 7 Seas 100mg**, **Real
Botanicals 7-Hydro 30mg 7-OH Shot**, **Prof Whyte's Kplex 20mg**, and **Dopium 10mg**
in six flavours. **Finding 18 established a federal absolute limit of 1.00 mg per
article.** It also **corroborates Finding 38**: Botanic Tonics alleged in a sworn
complaint that West Virginia registered Roxy 7-OH tablets while refusing *feel free*,
and the registry shows exactly that. **Six Roxy Complex Alkaloid rows at 16mg and
20mg, registrant Lifted Made, and *feel free* appears nowhere in 450 rows.** The
finding states plainly what it does not claim: a label figure is not an assay,
registration is not approval, and administrative lag is a sufficient explanation for
the timing. **The next step is to buy a 210mg tablet and assay it**, which is under
$100 and would settle it.

**2026-08-29, Finding 38: a competitor named the state-licensed 7-OH products, under
oath.** **[P]** *Botanic Tonics LLC v. Kent Leonhardt*, 2:25-cv-00680 (S.D. W. Va.),
complaint filed 19 Nov 2025, 21pp, obtained. **West Virginia's Agriculture
Commissioner was sued in his INDIVIDUAL CAPACITY for compensatory damages** under
**42 U.S.C. 1983**, on Dormant Commerce Clause, Supremacy Clause and Fourteenth
Amendment theories, by counsel including **Jonathan W. Emord**. The complaint alleges
the Department "has authorized the following products which include
**7-hydroxymitragynine synthetic concentrates at levels established in the scientific
literature to create morphine-like effects and dependencies**," then lists ten by
brand and dose, and says that "**for not a single one of these applicants did the
Department demand proof of safety of any kind.**" Recorded as an adverse party's
assertion, since BT is a commercial rival of the products it names, and **checked
against the state registry the same day** (Finding 39). The case ended after five
docket entries with no responsive pleading.

**2026-08-29, Finding 37: the company sued the Utah agency that later warned the
public about a death.** **[P]** *Botanic Tonics, LLC v. Kelly Pherson*, 2:26-cv-267
(D. Utah). **Botanic Tonics and the Global Kratom Coalition sued four Utah officials**
to block Utah's Kratom Regulation Act: **Kelly Pherson, Commissioner of the Utah
Department of Agriculture and Food**, his deputy **Amber Brown**, division director
**Bradon Forsyth**, and **Attorney General Derek Brown**. Filed 31 March 2026.
**That is the same department that, on 30 July 2026, warned the public about
mislabeled Buzzers Cat's Claw tablets in the matter where a Utah County death was
reported** (Finding 29). Judge Howard C. Nielson Jr. **DENIED the injunction on 4 May
2026**, holding that "the historic police powers of the States were not to be
superseded." **A state may regulate this category more tightly than the federal
government does.** The filings also show *feel free* in **321 Utah stores** with a deal
for **852 more nationwide**, and that it is reached because it is a combination
product: "feel free plainly does not qualify as pure leaf kratom because it is mixed
with kava root." The industry also argued against scheduling **mitragynine
pseudoindoxyl**, one of the four compounds Utah Poison Control named in July.
**Botanic Tonics is plaintiff in at least eight federal actions**, including a
**42 U.S.C. 1983** suit against **West Virginia Agriculture Commissioner Kent
Leonhardt**, and the Utah appeal is live at the Tenth Circuit. **[I]** The line the
federal rule drew in July is the line the company had been litigating for since March.

**2026-08-29, Finding 36: the government won, then walked away twelve days later.**
CourtListener opened up and produced the primary document `FINDING_03` had recorded as
blocked. **[P] On 10 December 2025 the court DENIED Botanic Tonics' motion to dismiss**
the forfeiture action, holding that *"the Amended Complaint survives"* and that the
facts *"support a reasonable belief that, if proven, the Government would be able to
successfully meet its burden."* Gelpí, Circuit Judge, sitting by designation. That
motion had been pending **two years and seven months**. **[S] Twelve days later, on 22
December 2025, the government filed a Notice of Dismissal without prejudice**, sourced
only to the claimant's own press release, and labelled as such. **[P] And the operative
amended complaint alleges what nobody in this case had seen: the United States told a
federal court that KRATOM ITSELF, the leaf, was "adulterated within the meaning of 21
U.S.C. 342(f)(1)(B)"**, citing *"addiction, and liver toxicity."* Not 7-OH. The seized
articles were 250,000 bottles of feel free, capsules, and bulk leaf powder. **The
company then announced the dismissal as regulators recognising leaf versus synthetic,
and six months later the federal rule drew exactly that line.** This complicates our own
thesis and the finding says so: the failure here is not that the government did not act.
It acted, prevailed, and abandoned it. Exhibits hashed in `exhibits/litigation/`.

**2026-08-28, Finding 35: the cap was real, and the agency blamed for it said it
never imposed it.** Contingency management is the one SUD treatment with a
dose-response curve. A federal limit held it at **$15 per incentive, $75 per patient
per year**. The only head-to-head magnitude trial, **Petry 2004** (DOI
10.1111/j.1360-0443.2003.00642.x), ran arms at **$80 and $240**: *"Patients in the
$240 CM condition achieved more abstinence than patients in the standard
condition."* **The $80 arm did not**, and $80 is the closest experimental analogue
to the cap. The effective floor is roughly **$250 per 12-week course**. **[P] But
Petry's patients actually earned $36 and $68 on average**, the arm that worked cost
**$68 a head, under the cap it violated.** The cap bound on the size of the available
prize, not on spending, so **the saving was near zero and the cost was the entire
effect.** **[P] And it was never required:** OIG stated in the preamble to its 2020
rule (85 FR 77,684 at 77,791-92) that its nominal-value policy **"does not impose a
$75 annual limit on CM incentives."** SAMHSA kept $75 until **January 2025**, then
raised it to **$750**. Still half fixed: $750 exceeds the safe harbor (**$623 for
2026**), the safe harbor excludes the gift cards SAMHSA mandates, and it reaches
only SOR/TOR grants, not Medicaid, where California's pilot stops at **$599, set
under the IRS 1099 threshold, a tax boundary standing in for a clinical one.**
**[P] That $599 is OIG Advisory Opinion 22-04's ceiling**, OIG approved
cash-equivalent CM incentives at $599/yr for one company, in an opinion that says it
**"cannot be relied upon by any other person"** and turns on the requestor **not
billing any federal health care program.** So the only federal sign-off on CM at a
working dose is unavailable to any clinic billing Medicaid.
**Congress ordered a safe harbor** in the CAA 2023, due **29 Dec 2024**; OIG opened
**RIN 0936-AA13** for August 2024. **It has never published**, verified by RIN
against the Federal Register with controls (AA10 = 3 docs, AA15 = 1, AA16 = 1,
**AA13 = 0**). Closes the open item flagged in `REMEDIATION.md` s5.

**2026-08-28, Finding 34: Congress DID act, and it did not work.** The
**Mainstreaming Addiction Treatment Act removed the X-waiver**, the barrier the field
named for a decade. Two evaluations find **no effect**: "no differences in either the
level or trend of buprenorphine prescribers" (DOI 10.1016/j.amepre.2026.108508) and
"no change in the total buprenorphine prescriptions per month" (DOI
10.1016/j.acepjo.2025.100246), because "**structural barriers persist**." **[I] The
barrier was never the waiver.** The reframe: the failure is not refusal to act, it is
that **the actions taken were the ones that cost nothing.** Repealing a registration
requirement is free; so is scheduling a molecule. Funding capacity and contingency
management at effective levels is not, and has not been tried. Meanwhile premature
mortality from drug use disorders is **rising** in high-income countries (Lancet GBD
2025).

**2026-08-28, Finding 33: the recovery field is on this docket and it is split.**
**Awakening Recovery, Inc.** (`-7588`), a named nonprofit running recovery homes,
reports residents arriving **having overdosed on 7-OH** and asks for Schedule I. A
recovery professional filing as **"A, R"** (`-18012`) argues **"recovery is fostered
through treatment, stability, and human connection, not through expanding criminal
penalties."** Same population, opposite asks, neither wrong. Her framing appears in
**13 of 27,053 comments**. **She reached the remediation argument six weeks before we
did and the case says so.** She filed under initials; **we have not tried to identify
her and will not.**

**2026-08-28, Finding 32: the letter that did not mention the people.** Eleven US
Senators, 18 March 2026, to the FDA Commissioner. **537 words. Twelve references to
enforcement and scheduling. Zero to treatment, recovery or access to care**, the
lone "clinic" match is `mayoclinic.org` in a footnote URL. Their only expansion
beyond the pending action was to ask the Commissioner "to consider **scheduling the
whole kratom leaf**." **None of the eleven took industry money** (F22), so this is
not a corruption finding. It is a record of what unbought legislators wrote about,
while 42.4 million untreated Americans sat in the federal government's own survey.
**Reproducible in five minutes with the PDF and a search box.**

**2026-08-28, Finding 31: they published the arbitrage themselves.** The
manufacturer's own homepage states it "**figured out a way to extract an indole
alkaloid from the Cat's Claw plant to mirror the effects of popular kratom
products**," producing "a **non-kratom product with kratom-like effects**," and a
retailer states the rationale outright: "**Cat's Claw is a recognized botanical and
is not a controlled substance, so Buzzers ship nationwide**." Marketed as "clarity,
focus, and high-functioning energy." **A state poison control centre names the same
brand in connection with multiple severe overdoses and a death.** Sold as an upper,
killing people as an opioid. Both brands Utah named, Buzzers and Homiez, are sold
from the same site. **Five pages captured and SHA-256 hashed 2026-08-28 before they
change.**

**2026-08-28, Finding 30: it is all still on the shelf, and stays there.** The
three federal instruments reach **four substances, all on the mitragynine
scaffold**. **9-hydroxycorynantheidine** (a major human metabolite of the controlled
substance), **corynoxine** (a mu-opioid **full agonist**), and **corynoxine B**
(which retail products are documented as being built around) are reached by none of
them, **and nothing in any instrument brings them in later**. On the day 7-OH is
controlled, the substitutes remain lawful to manufacture and sell. Florida's
emergency rule and Utah's pure-leaf-only law are both **stricter than the federal
instrument**. No purchase is needed to establish any of this; it is the rule text
read against the compound list.

**2026-08-28, `REMEDIATION.md` s6 added on European rehabilitation evidence, and
it cuts both ways.** EUDA reports **56% of clients entering European drug treatment
are unemployed** and recommends housing, education and vocational training
**embedded in treatment early**, while stating in its own words that "**evidence is
sparse**." Against that, a propensity-matched study
(DOI 10.1177/0306624X231159886) found that after controlling for selection bias,
**vocational certificates alone produced no difference in any outcome.** The
document publishes the null result, and concludes that a certificate is not an
occupation and that **the gap in the literature is a funding gap, not a finding.**

**2026-08-28, `REMEDIATION.md` given the scale, from the government's own survey.**
2024 NSDUH: **48.4M** with a substance use disorder, **52.6M** needed treatment,
**10.2M** received it. Of the 10.2M, **4.2M had no disorder**, so only **6.0M with a
disorder were treated** and **42.4 million received nothing, 87.6%**. Larger than the population
of California. And 48.4M is an undercount by construction: SAMHSA's own notes say
the measures "do not capture disorders arising solely from the use of **IMF**",
illegally made fentanyl, and it is a household survey that structurally misses the
homeless and incarcerated. Annual economic burden **$425.0 billion**
(DOI 10.3389/fpubh.2026.1824038). Also added: contingency management shows a
**dose-response relationship between magnitude and immediacy of reward and
effectiveness** (DOI 10.1016/j.ypmed.2023.107647).

**2026-08-28, FIFTH comment FILED. Tracking `mtd-izm8-ql4p`.** Reports that the
substitution earlier comments warned of **has already occurred**: the Utah Poison
Control alert of 22 July 2026, the Utah death linked to mislabelled Buzzers-brand
Cat's Claw tablets, and lawful products built on **corynoxine B**, a mu-opioid full
agonist nothing covers. Argues **the label is the evasion**. States expressly that
OWG does not seek restriction of genuine cat's claw and would oppose it.

**2026-08-28, Finding 29 CORRECTS Finding 28. The substitution already happened.**
The **Utah Poison Control Center** (22 July 2026) warns of smoke-shop products sold
as **"Cat's Claw"** causing "life-threatening opioid overdose, dependence, or
withdrawal," naming **Buzzers** and **Homiez** brands, adulterated with **7-OH,
mitragynine pseudoindoxyl, MGM-15 or MGM-16** and not labelled as containing them.
A **death** was linked to Buzzers-brand Cat's Claw tablets on 30 July 2026.
Separately, a recovery community documents products **lawfully built on corynoxine
B** to dodge the 7-OH scheduling. **Finding 28's reassurance is retracted:** it
measured the plant and concluded about the products. See Finding 29 s6 for the full
account of the error.

**2026-08-28, Finding 28: the rule's boundary is a genus name.** **Corynoxine is
a mu-opioid receptor FULL agonist** (ACS Chem Neurosci 2021, DOI
10.1021/acschemneuro.1c00149) and it has been isolated from ***Uncaria tomentosa***,
cat's claw (J Chromatogr A 2015, DOI 10.1016/j.chroma.2015.02.028), sold as an
unregulated dietary supplement. *Mitragyna* and *Uncaria* are neighbouring genera in
tribe Naucleeae and their alkaloid lists overlap heavily.
**This is NOT a warning about cat's claw.** The same paper reports corynoxine shows
**attenuated respiratory depression versus morphine**, the authors caution these
alkaloids are "unlikely to play the majority role", and we have no concentration
data and no harm signal. We do not ask for it to be scheduled and would oppose that
on this evidence. The finding is about **scope**: the action reaches one scaffold in
one species while the pharmacology spans two scaffolds across two genera.
**ANSWERED 2026-08-28 and it cuts against our own lead:** a 500 mg bark capsule
carries about **0.65 mg of the entire tetracyclic class**, under the 1.00 mg the
government treats as significant for one scheduled compound; bark is a 6:1
pentacyclic chemotype and the trade already selects away from the tetracyclics; and
LDA shows **zero** filings on cat's claw or *Uncaria* against controls of 1,910 and
298. **There is no cat's claw problem and this case says so.**

**2026-08-28, FOURTH comment FILED. Tracking `mtd-holx-p7i5`.** Corrects our own
third comment. Puts on the federal record that **9-hydroxycorynantheidine is a
major circulating human metabolite of the substance being scheduled**, that **10 g
of ordinary unenhanced leaf already equals the 1.00 mg absolute limit** against
FDA's own data, and that **the rule never defines "article"**, so forty pressed
pills at 0.9 mg each are individually compliant and deliver 36 mg in one bag.

**2026-08-28, Findings 27 and the Finding 18 addendum, both filed as a fourth
comment.** **9-hydroxycorynantheidine is a major circulating human metabolite of
mitragynine** (Kanumuri 2026, clinical, DOI 10.1080/13880209.2026.2715806), not the
"minor plant alkaloid" our own third comment called it. In rats it is a **major**
metabolite while **7-OH is minor** (Chiang 2025, DOI 10.1021/acsptsci.4c00277,
labelled as animal data). Separately, the rule's absolute limit turns on the word
**"article", which the rule never defines**: forty pressed pills at 0.9 mg each are
individually compliant and deliver 36 mg in a bag. And against FDA's own leaf data,
**10 g of average leaf already equals the 1.00 mg absolute limit.**

**2026-08-28, Finding 26: nobody else asked.** Of **27,053** comments on
HHS-OASH-2026-0232, **zero** mention 9-hydroxycorynantheidine, corynanthe,
Mitradyne, Atallah or divestiture. One mentions corynantheidine, in a passing
alkaloid list. The two questions unique to this case in that entire record are the
**corynantheidine scaffold gap** (`mtc-q9zv-dase`) and the **phantom "(Kruegel et
al., 2019)" citation** in FDA's own assessment (`mtc-56yj-nmij`). Stated honestly:
**36 commenters already raise the Mullin holding**, so that part is not ours alone.

**See [`CONTACT_LOG.md`](CONTACT_LOG.md)** for every approach to an official or
agency and what came back. Short version: the state consumer division acknowledged
in **23 seconds** with a reference number, the federal docket issues a tracking
number for every comment, FDA refused on a channel technicality but wrote back with
the correct route, and the **Senate personal office issues no reference number of
any kind** while its phone line routes callers back to the same form. Response time
tracks whether an office has a duty to answer, not the quality of the material.

**2026-08-28, Constituent submission to Sen. Marsha Blackburn (R-TN)**, via her
web form, two messages. Carries the corynantheidine gap, Mitradyne's claims 5, 6,
8 and 11 for independent verification, and the three scope questions. Raises the
Mullin holding once, with the sequencing that matters: **the nominee disclosure
was filed 2026-03-17 and she signed the Makary letter 2026-03-18, one day later.**
Opens with the finding that favours her, that she has taken nothing from this
industry. No tracking number is issued; the confirmation page is the receipt.
**Note: an earlier email to `senator@blackburn.senate.gov` returned 550 User
Unknown. There is no email route to a Senate office.**

**2026-08-28, Tennessee Division of Consumer Affairs complaint SENT and
ACKNOWLEDGED.** Reference **`104939`**, acknowledged 23 seconds after sending.
Tennessee Consumer Protection Act, Tenn. Code Ann. §§ 47-18-101 et seq.

**CORRECTION 2026-08-28, the FDA FOIA was never filed.** It was recorded as SENT
on 2026-08-27. FDA replied that it **does not accept FOIA requests by email** and
must be filed through `accessdata.fda.gov` or `foia.gov`. The entry has been moved
out of FILED. A send that leaves the outbox is not a filing.

**2026-08-28, THIRD comment filed to docket HHS-OASH-2026-0232**, the
corynantheidine gap. **Comment Tracking Number: `mtc-q9zv-dase`.** Five-page
attachment, 1,251 words, box text 4,995 of 5,000 characters. Argues every covered
substance sits on the mitragynine scaffold while **9-hydroxycorynantheidine sits
on the corynantheidine scaffold and is covered by nothing**, and puts the
manufacturing evidence from Finding 25 on the federal record: Mitradyne's
EP 4 538 367 claims 5, 6, 8 and 11 quoted verbatim, CB Therapeutics'
US 2025/0179544, and the fact that the compound is an intermediate on the route to
mitragynine. Fifth requested action asks whether scope was set on **natural
abundance rather than manufacturability**. Status: submitted, pending agency
review.

**2026-08-27, Public comment filed to docket HHS-OASH-2026-0232** (HHS OASH,
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
- [x] ~~Whether the **University of Guelph** holds an interest~~ **CHECKED 2026-08-28. No evidence of one.** Guelph's IP policy of 2014-06-05 makes inventions **creator-owned**, assignment to the university voluntary, so a faculty spin-out filing in its own name is the ordinary path. The patent says "University" **0 times** in 90,613 characters, with no funding, NSERC or government-rights language. **But the work used university facilities**: live plants in controlled chambers, material authenticated by **Dr. Carole Ann Lacroix**, Collections Manager of the Guelph herbarium, voucher No. 102033 deposited there. No disclosed interest while the work ran through its facilities. Finding 25 addendum 2
- [x] ~~USPTO assignment records~~ **OBTAINED 2026-08-28** via ODP key. **Reel 68665 frame 517**, recorded 2024-09-23: the four inventors assigned directly to **Mitradyne Corporation**. One conveyance, **no University of Guelph, no security interest, no third party**. Control: Guelph is first applicant on **122** US applications, so it patents heavily and its absence here is a choice under its creator-owned policy. Same lab also runs **ATLAS365** (via NuMed Naturals, Guelph) and a Van Gelder-held filing; Guelph appears in none. Finding 25 addendum 4
- [ ] **[I] Mitradyne pays "Regular Undiscounted" USPTO fees while ATLAS365, Van Gelder and CB Therapeutics all claim Small entity.** Status is lost by licensing to a non-small entity; universities/non-profits still qualify as small. Mundane explanation is counsel inattention. **Signal, not a finding.** Worth re-checking against later filings
- [ ] **Ontario Business Registry search for Mitradyne** (free, needs a browser). Returns **directors**. Now the only cheap route that could still change the Guelph answer
- [ ] **EPO OPS credentials** (free, email only, non-paying tier) for European Register transfers on EP4538367
- [ ] **NOTE: Mitradyne holds no granted US patent.** 18/891,491 is pending; a Restriction/Election Requirement issued 2026-08-14. Do not describe it as patented
- [ ] EPO Register applicant-history / transfers for EP24201792 (403 from this host)
- [ ] Identify the **partnership or LLC** behind the `PARTNERSHIP ATTRIBUTION` memo on the $443,000
- [ ] Constituent letter to **Sen. Blackburn (TN)**, who signed the 2026-03-18 letter and takes no industry money
- [ ] **PACER**: *Torres v. Botanic Tonics*; the 2023 in-rem seizure action and its Dec 2025 dismissal. The dismissal docket may state a reason
- [ ] Obtain the **Wyden letters** themselves, all three
- [ ] Re-capture the five **blocked sources** (DEA, Public Citizen x2, congress.gov, Missouri Independent) via an alternate path
- [ ] Determine whether Botanic Tonics itself sells any product above the 0.05% line
