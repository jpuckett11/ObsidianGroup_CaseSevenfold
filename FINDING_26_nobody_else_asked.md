# SEVENFOLD / FINDING 26
## Twenty-seven thousand people commented. Nobody raised the corynantheidine gap.

**Status:** CONFIRMED from the regulations.gov API, with the search instrument
itself tested before any count was trusted.
**Analyst:** Aegis, for Obsidian Watch Group. **Date:** 2026-08-28.

---

### 1. The docket is not small

**27,053 comments** on HHS-OASH-2026-0232 as of 2026-08-28. This is a heavily
commented docket with real public engagement, not an empty room.

That matters for what follows. A question nobody asked on a docket with a hundred
comments is unremarkable. A question nobody asked on a docket with twenty-seven
thousand is a gap in the public record.

### 2. Test the instrument before trusting a single number

The regulations.gov `searchTerm` filter **does not phrase-match. It OR-matches**,
and the difference destroys any multi-word count.

Proof, run in the same session:

| Query | Comments |
|---|---|
| `Florida` | 273 |
| `corynantheidine` | 1 |
| `Florida corynantheidine zzqnonsense` | **274** |

274 is exactly 273 + 1. Multi-word queries return the **union**, not the phrase.

**Two figures produced earlier in this analysis were therefore wrong and are
withdrawn before publication:** "Florida emergency rule" appeared as 3,768 and is
meaningless, and "manufacturability" appeared as 1,008 because the index stems and
was matching *manufacturing*. Neither is used below.

**Control:** `zzqnonsensecontrolstring` returns **0**. The filter genuinely
filters, so the zeros below are real absences.

**Only single, rare, unstemmed words are used from here.**

### 3. What nobody said [P]

| Term | Comments |
|---|---|
| **9-hydroxycorynantheidine** | **0** |
| **corynanthe** | **0** |
| **Mitradyne** | **0** |
| **Atallah** | **0** |
| **divestiture** | **0** |
| corynantheidine | **1** |

**The single corynantheidine hit is not this argument.** It is one commenter
listing plant alkaloids and their receptor activity in passing:

> "Such as Corynoxeine: Calcium channel blocker, Corynantheidine (rauhimbine): an
> α1-adrenergic and α2-adrenergic..."

Nobody connected the compound to the scope of the action. Nobody named the second
scaffold. Nobody mentioned the manufacturing patents. Nobody named the scientist
who co-authored the study FDA relies on while working for a leaf-kratom company.

### 4. What people did say, stated so the contrast is honest [P]

The public is neither ignorant nor asleep on this docket:

| Term | Comments | What it shows |
|---|---|---|
| threshold | 6,697 | The 0.05% figure is heavily contested |
| Kruegel | 17 | Commenters cite the real 2016 J Am Chem Soc paper |
| buprenorphine | 142 | Personal accounts of dependence and treatment |
| Huestis | 13 | The cited literature is being read |
| Mullin | 36 | **The financial holding is already public** |
| Makary | 3 | |
| fermentation | 2 | |
| scaffold | 7 | Stemmed; sampled text did not contain the word. Treat as unreliable |

**We are not the only people who noticed the holding.** Thirty-six commenters
raise Mullin, one describing the investment in a competitor directly. That part of
this case is already in public circulation and this finding says so plainly rather
than claiming credit for it.

**"Botanic" returns 221, and that number is not usable.** The sampled match was
"Shaman Botanical," a different company. Partial matching inflates it.

### 5. What is actually unique to this case, stated narrowly

Two things, and only two:

1. **The corynantheidine scaffold gap.** Zero of 27,053. Comment `mtc-q9zv-dase`
   is the only place in this docket where anyone argues that every covered
   substance sits on one chemical scaffold while a second scaffold in the same
   plant is uncovered, that Florida named it and the federal instruments did not,
   and that two patent families already claim how to manufacture it.

2. **The phantom citation.** Seventeen commenters cite *Kruegel et al. 2016*.
   FDA's own assessment carries an in-text citation to **"(Kruegel et al., 2019)"**
   that appears nowhere in its reference list, and it is the citation attached to
   the content-by-weight discussion underlying the threshold. Comment
   `mtc-56yj-nmij` is the only one asking the Department to identify it.

Everything else in this case, including the holding, the lobbying and the captured
evidence base, is either already raised by others or is documentation of things
others have asserted less precisely.

### 6. Why this is the argument for filing rather than posting

Twenty-seven thousand people told the Department what they think. The Department
must review that record.

Inside it, two questions exist exactly once, and both are ours. Neither depends on
anyone finding this case interesting, sharing it, or believing the investigator.
They sit in the administrative record with tracking numbers attached, and they
will still be sitting there when the comment period closes on 10 September 2026.

**That is what a filing is for.** It is the one channel in this entire
investigation that does not require a single person to care.

### 7. Method, for anyone reproducing this

- `filter[docketId]`, **not** `filter[commentOnId]`. The latter returns 0 for this
  docket and looks like a real negative. It is not.
- `page[size]` must be **5 or greater**; smaller values return HTTP 400.
- `searchTerm` OR-matches and stems. **Single rare words only**, and read a sample
  of the matched text before believing any count.
- Run a nonsense-string control every time.
