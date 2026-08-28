# SEVENFOLD / FINDING 22
## Where kratom industry money goes, and where it does not

**Status:** CONFIRMED from FEC primaries. **PARTIAL: three of five planned employer
queries completed before rate limiting.** **Date:** 2026-08-28.

---

### 1. Method

Queried FEC Schedule A by **contributor employer**, not by name. Employer fields
are self-reported by contributors and can be blank, abbreviated or inaccurate, so
these totals are **floors, not complete accounts**.

### 2. Botanic Tonics employees and founder

Previously established in Finding 12 and restated for the map:

| Recipient | Amount |
|---|---|
| Republican National Committee | $443,000 |
| Kennedy Victory Fund 2024 | $161,800 |
| Libertarian National Committee | $41,300 |
| Nine state Libertarian / Free New Mexico parties | $77,973 |
| **Team Kennedy** | **$6,600** |

### 3. MIT45 employees — NEW

| Recipient | Amount |
|---|---|
| **The Bergman Victory Committee** | **$35,100** |
| **BergmanForCongress** | **$31,800** |
| WinRed (conduit) | $19,951 |
| **Team Kennedy** | **$9,900** |
| STAR PAC | $3,300 |

**[I] Two findings here.**

**a. Both major kratom companies funded Robert F. Kennedy Jr.'s presidential
campaign.** Botanic Tonics' founder gave **$6,600** to Team Kennedy and **$161,800**
to Kennedy Victory Fund 2024. MIT45-employed contributors gave **$9,900** to Team
Kennedy. These are commercial rivals on opposite sides of the 7-OH question, and
both funded the same candidate, who became the Health Secretary who co-announced
the 7-OH enforcement action.

**b. MIT45-employed contributors directed roughly $67,000 to committees supporting
one member of Congress**, Rep. Jack Bergman (R-MI-01), across two committees. That
is a substantial concentration from a single company's employees toward a single
member. **We record the fact and assert nothing about it.** We have not examined
Rep. Bergman's legislative activity on kratom and make no claim that any exists.

### 4. A clean negative worth stating

**None of the eleven senators who signed the 18 March 2026 letter to Commissioner
Makary appear as recipients in any of the contribution records retrieved.**

Ricketts, Blumenthal, Shaheen, Crapo, Blackburn, Daines, Justice, Padilla, Britt,
Budd, Boozman. Not one appears.

**[I] This matters and it cuts in their favour.** Eleven senators wrote to FDA
arguing that scheduling 7-OH alone protects the wrong product, and the industry
money we can trace did not go to them. **Their letter is not compromised by the
funding record, and that makes it more useful, not less.**

**Caveat, stated plainly:** three employer queries completed, two were rate
limited (Checkmate Government Relations, Miller Strategies). Employer-field
searching also misses contributions where the field was left blank or a personal
capacity was used. **This is not a clearance. It is the absence of a hit in the
records retrieved.**

### 5. Also a negative

**"American Kratom Association" as contributor employer returns zero rows.** Its
staff do not appear to contribute under that employer designation. Given AKA's
$3,427,500 in disclosed lobbying, the absence of employee political giving under
its own name is notable but not in itself suspicious.

### 6. Not yet done

- **Checkmate Government Relations** and **Miller Strategies** employer queries,
  rate limited. Miller Strategies is the vehicle behind the **$980,000 Botanicals
  for Better Health and Wellness** account and Jeffrey Miller chaired the
  inaugural committee that received **$50,000** from that group.
- **The $50,000 inaugural committee donation** itself. Inaugural committees file
  with FEC and the filing carries a **filer address**, which is the most direct
  remaining route to BBHW's identity.
- **Secretary Mullin's own Senate campaign receipts**, tested against kratom
  employers.
- **Rep. Bergman's kratom-related legislative record**, if any.

**[I] All four need a free api.data.gov key. DEMO_KEY caps at 40 calls an hour and
has been the binding constraint on the money map for this entire investigation.**

---

## UPDATE 2026-08-28: the rate-limited queries are now complete

Finding 22 was published with a stated limitation: two of five planned employer
queries had not run because the FEC DEMO_KEY caps at 40 calls an hour. A full API
key was obtained and the remaining queries have been executed. **The limitation is
lifted. Nothing in the original finding required correction.**

### Completed queries

| Employer queried | Rows | Result |
|---|---|---|
| MILLER STRATEGIES | 2,870 | Republican fundraising firm, no kratom client identified |
| CHECKMATE GOVERNMENT RELATIONS | 51 | $750,000 kratom registrant (Stop Gas Station Heroin LLC) |
| BOTANIC TONICS | 37 | $730,673, see Finding 23 |
| MIT45 | 28 | confirms the original figures |

### Mullin's own receipts: a clean negative [P]

Every kratom-sector employer tested against **MULLIN FOR AMERICA (C00498345)**:

| Employer | Rows |
|---|---|
| Botanic Tonics | 0 |
| MIT45 | 0 |
| American Kratom Association | 0 |
| Johnson Foods | 0 |
| Della Terra | 0 |

**Control:** C00498345 has **22,978** itemized receipt rows. The endpoint returns
data for that committee, so the zeros above are genuine absences, not a broken
query.

No kratom company or trade association gave Markwayne Mullin's campaign anything.
That is now established as firmly as the holding in Finding 01 is established.
Both facts belong in any account of this case.

### A link tested and discarded

Two Holland & Knight lobbyists appear in Mullin's receipts: **Kathryn Lehman**
($500, 2022-06-21) and Gregory Louer ($500, 2022-08-09). Holland & Knight is the
registrant on the **$700,000 Johnson Foods** account (Finding 06), and Lehman is a
**named lobbyist on that account** [P, LDA filing detail]. Her contribution falls
in the same quarter the Johnson Foods engagement opened.

That looked like a connection. It does not survive its control test.

Pulling Lehman's complete Holland & Knight giving history by keyset pagination,
**345 itemized contributions across 137 distinct recipients** since the early
2000s, roughly ninety of them $500 gifts to House and Senate campaigns of both
parties' Republican caucus. Mullin's $500 is indistinguishable from the other
eighty-nine.

**We record this as a negative.** Routine lobbyist giving, no kratom signal. Had
we reported the first query without the second, we would have published a
connection that is not there.

### Method note for anyone reproducing this

`lda.senate.gov` now 301-redirects to `lda.gov`; requests without redirect
following return an nginx error page, not JSON. The FEC `per_page` parameter caps
below the requested value on some endpoints and offset paging silently drops rows,
so contributor histories must be pulled with **keyset pagination**
(`last_index` + `last_contribution_receipt_date`) and de-duplicated on `sub_id`.
An earlier pass at Lehman's history using a single 100-row page appeared to show
Mullin absent from her recipients. That was a truncation artifact, caught and
corrected before it reached any finding.
