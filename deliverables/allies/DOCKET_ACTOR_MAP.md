# DOCKET ACTOR MAP — HHS-OASH-2026-0232
### Organisations that put a name on the record

**Method and its limit, stated first.** The regulations.gov list endpoint does not
return the `organization` field; only per-comment detail records do, and fetching
27,053 of those is not feasible. Organisation names were therefore extracted from
the `title` field across the **first 5,000 comments**, which is the maximum the API
will page through.

**This is a sample of roughly the earliest fifth of the docket, not a census.**
Thirteen organisation-shaped submitters were found. More exist beyond the
pagination cap.

---

## Recovery, prevention and public health — potential allies

| Comment | Organisation |
|---|---|
| `-7588` | **Awakening Recovery, Inc.** — recovery homes; reports residents overdosing on 7-OH (Finding 33) |
| `-3269` | **The Megan House Foundation, Inc.** |
| `-3259` | **7 Hope Alliance Foundation** |
| `-4017` | **Carter County Drug Prevention Coalition** |

**These are the approach targets.** They chose to be public, they work with the
affected population, and none of them is selling anything.

## Law enforcement

| Comment | Organisation |
|---|---|
| `-3234` | **Kentucky Narcotic Officers' Association** |

## Industry and trade

| Comment | Organisation |
|---|---|
| `-3256` | **Outpost Brands, LLC** — **also appears in the Senate LDA kratom lobbying corpus** (Finding 12) |
| `-1563` | Lifted Liquids, Inc. |
| `-0006` | Hodas High Life Vape & Tobacco LLC |
| `-4062` | DATCS, LLC (drug and alcohol testing compliance) |

**Outpost Brands is the one to note.** A company that appears as a client in the
lobbying record also filed a public comment. That is entirely lawful and entirely
ordinary. It is recorded because this case tracks who is present in both places.

## Free-market advocacy organisations

| Comment | Organisation |
|---|---|
| `-0827` | **Consumer Choice Center** |
| `-1293` | **Reason Foundation** |
| `-0804` | **Taxpayers Protection Alliance** |

**[I] Three free-market policy organisations filing on a single drug-scheduling
docket is a pattern worth noticing, not a finding.** We have not examined their
funding and make no claim about it. Recorded so that anyone assessing the
composition of this docket can see it. **Their comment IDs are given so a reader can
read what they actually argued rather than assume.**

## Other

| Comment | Organisation |
|---|---|
| `-0806` | GUNN LAW GROUP |
| `-2734` | Powell IT Services |

---

## What this map is for

The docket is overwhelmingly **individual** commenters. In 5,000 comments, thirteen
organisations. The rest are people writing in their own names about their own lives.

**That is worth stating plainly.** This is not an astroturf docket. It is mostly
real people, and the industry presence in it is small and identifiable.

## Open

- **The remaining ~22,000 comments** are beyond the pagination cap. A date-windowed
  crawl could reach them.
- **Approach drafted, not sent:** Awakening Recovery, Inc.,
  `APPROACH_awakening_recovery.txt`.
- **Approach SENT 2026-08-29:** Northwest Alabama Mental Health Center, a public
  non-profit CMHC serving Fayette, Lamar, Marion, Walker and Winston counties, whose
  service line includes chemical dependency. Text at `EMAIL_nwamhc.txt`. It offers
  the case file free, warns that a person can present having overdosed on a product
  whose label lists no opioid, and asks only for aggregate observation, explicitly
  no names and nothing identifiable.
