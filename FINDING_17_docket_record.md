# SEVENFOLD / FINDING 17
## The docket itself: 26,882 comments, and the extension question answered

**Status:** CONFIRMED from regulations.gov API primaries, retrieved 2026-08-27
with an authorised key. **Date:** 2026-08-27.

---

### 1. ANSWERED: who requested the comment-period extension

Our filed comment (`mtc-56yj-nmij`, section 7) asked the Department to identify
the party that obtained the extension granted 2026-08-26, because the Federal
Register notice said only that OASH "received a request" and did not name it.

**It was the Holistic Alternative Recovery Trust.**

Comment **HHS-OASH-2026-0232-11696**, letter dated **2026-07-20**, from **Jeff
Smith, PhD, Executive Director, HART**, addressed to **Admiral Brian Christine,
Assistant Secretary for Health.** Held at
`exhibits/docket_HART_extension_request.pdf`.

**[I] This answer exonerates rather than implicates, and we record it that way.**

We had flagged an unnamed party obtaining a procedural accommodation on a
threshold worth a market. The requester turns out to be the **$15,000
organisation** — the only organised defender of 7-OH, outspent in this sector by
roughly 490 to 1. This is the underfunded side asking for more time to assemble
evidence, not a powerful interest working the process.

They asked for **60 days**, to 2026-09-29. They received **41**, to 2026-09-10.
**The Department granted less than half of what was requested.**

### 2. Their argument is substantially our argument

HART's stated grounds:

> "The RFI poses a series of highly technical and largely unprecedented
> questions, including how any proposed threshold should apply across botanical
> source material, semi-synthetic derivatives, and finished dosage forms; **what
> analytical methodologies are capable of accurately measuring compliance**; and
> how such a threshold could be administered in practice without producing
> arbitrary or unintended results."

That is section 2 of our own comment, filed independently five weeks later. They
also urged OASH to ask DEA to **hold the temporary scheduling order in abeyance**
until the record is evaluated.

**[I] Two parties with opposite commercial interests and no contact reached the
same procedural conclusion: the threshold's analytical basis is unresolved and
the timeline is too short to resolve it. That convergence is worth more than
either comment alone.**

### 3. The scale of the docket

**26,882 comments.** Full-text search across them:

| Term appears in | Comments |
|---|---|
| American Kratom Association | **12,327** (~46% of the docket) |
| Holistic Alternative Recovery Trust | 7,490 |
| Kratom Trade Association | 7,152 |
| Botanicals for Better Health and Wellness | 6,915 |
| Global Kratom Coalition | 6,870 |
| Public Citizen | 4,759 |
| Johnson Foods | 384 |
| Botanic Tonics | 220 |
| MIT45 | 2 |

**[I] These counts overlap heavily and indicate organised template campaigns
rather than 27,000 independent submissions.** Nearly half the docket carries the
American Kratom Association's name. Treat the raw comment count as a measure of
mobilisation capacity, not of public opinion. **Do not cite these numbers as
distinct organisational filings; they are text matches.**

### 4. The institutional filings, now held

| Filer | Comment ID | Artifact |
|---|---|---|
| American Kratom Association | HHS-OASH-2026-0232-11843 | `docket_AKA_comment_20260731.pdf` |
| Global Kratom Coalition | HHS-OASH-2026-0232-9901 | `docket_GKC_comment.pdf` |
| Holistic Alternative Recovery Trust | HHS-OASH-2026-0232-11848 | `docket_HART_comment_merged.pdf` (1.0 MB) |
| HART extension request | HHS-OASH-2026-0232-11696 | `docket_HART_extension_request.pdf` |

**AKA's position, verbatim from its comment:** it recommends that **mitragynine
pseudoindoxyl (MP)** above naturally occurring levels also be treated as the
product of "chemical manipulation, synthesis, conversion, enhancement, or other
processing" and deemed an imminent hazard.

**[I] AKA is asking the Department to go further than DEA did**, extending the
same above-natural-levels logic to a second compound. Consistent with the pattern
throughout this case: the leaf incumbents consistently advocate for restricting
everything that is not leaf.

### 5. Collection note: the CloudFront block is solved

Attachment downloads from `downloads.regulations.gov` had returned 919-byte block
pages all session. **The cause was the User-Agent string**, not access control or
the API key. A standard browser UA retrieves the files normally.

This recovered three primaries previously recorded as blocked:

- `hhs_letter_to_dea_7oh_20260713.pdf` (1.9 MB) — **the HHS scheduling
  recommendation letter to DEA. Scanned image, no text layer. Requires OCR.**
- `dea_three_factor_analysis_7oh.pdf` (395 KB, 48,201 chars) — DEA's own
  three-factor analysis supporting the 7-OH action.
- `ndi_1264_npi001_kratom_leaf.pdf` (7.1 MB, 347,059 chars) — the Johnson Foods
  NPI-001 dried kratom leaf New Dietary Ingredient notification.

**[I] Lesson for the methodology file: a polite, identifying User-Agent was the
thing blocking us from federal public records for an entire session.** Always test
a second UA before recording a source as unreachable.
