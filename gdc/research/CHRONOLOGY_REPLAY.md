# Can a local reporter reconstruct what was known at each handoff?

Development protocol, recorded before generation. One East Palestine investigation, three nested cutoffs, not three independent stories. Same model, system prompt (including a warning about related links), row limit, and output budget. Each arm gets the same dated releases. The page arm includes paraphrased related material observed on the current pages; the body arm excludes it by construction. This evaluates the value of a perfect section boundary, not an implemented general-purpose extractor. Inputs are condensed researcher-made records, not original raw text or verified historical snapshots. No independent desk editor or other reporting source. Runs do not test unbiasedness.

Before reading answers, designate these minimum editorial milestones (each required only from its indicated cutoff onward):

- A: Feb 3 derailment with hazardous release or fires; June investigative hearing scheduled, not yet confirmed.
- B: replace hearing status with June hearing held; dockets available for reporting; June 25 meeting/vote still planned.
- C: meeting happened; attributable causal finding; attributable finding about the response decision; recommendations issued; distinguish published abstract from forthcoming full report.

At later cutoffs count the hearing's current status once, not the scheduling announcement and the confirmation separately. Denominators A=2, B=4, C=8 (incident, hearing held, dockets, board held, cause, response finding, recommendations, report status). Credit explicit facts only; date range vs exact day acceptable unless unsupported. Separately inspect every entry and question for hindsight, unsupported completion, and unsupported date precision. Do not reward predicting a future outcome. A future event can be mentioned as a plan. Missing milestone is not misinformation. No time-saved or professional-value claim possible from this replay.

Sources: NTSB [May 2023 hearing announcement](https://www.ntsb.gov/news/press-releases/Pages/NR20230524.aspx), [Feb 2024 board announcement](https://www.ntsb.gov/news/press-releases/Pages/NR20240206.aspx), [June 2024 findings](https://www.ntsb.gov/news/press-releases/Pages/NR20240625.aspx). See release bodies and related News separately. The February URL says 0206 but the displayed dateline is Feb 7; use the latter.

## Results and adjudication

Six successful calls; [raw answers, usage and request fingerprints](runs/chronology_replay_2026_11_11.jsonl). One generation per arm/cutoff; not blinded. Content-only judgment below separates missing milestones from incorrect citations. Scoring choice: contradictory status is not full credit; topics mentioned only inside questions are not delivered chronology entries.

| Cutoff | With related material | Release-body notes only |
|---|---|---|
| May 2023 | 1/2: incident; announces hearing but also narrates its second day and assigns an agenda for that day. | 2/2: incident and hearing plan; date field confusingly dates the announcement to the hearing itself. |
| Feb 2024 | 3/4: incident, docket, board plan. Hearing placed one year late. Board row also leaks both June findings. | 4/4 on content, but cites A for hearing completion where B is the confirmation. Says both later community meetings happened. Follow-up question assumes a bearing malfunction initiated the accident. |
| June 2024 | 6/8: incident, board held, cause, response finding, recommendations, abstract/full status. Hearing in wrong year; dockets omitted. | 5/8: incident, hearing, board held, cause, recommendations. Dockets omitted; response finding only in question; full report marked pending without mentioning available abstract. |

Both February briefs also append a February row after June. Even a maximum coverage score coexists with unpublishable mistakes. Do not sum these nested cutoffs into a performance statistic. In the June packet C refers to the response decision elliptically; this makes specificity harder and is a limitation of our condensation. The page arm had more text and repeated later findings, which may explain better final coverage. No evidence of general superiority for either arm.

[Review cue script](replay_lint.py) finds five row-level cues in February (two ordering, three future-occurrence phrases); no cues in May or June. It misses the most important leaked causal statement and wrong hearing year. It was written after seeing the answers. It is not an independent eval, a detector of all errors, or a publishing gate. Full local research unit suite: 21 passed. No production changes.

## What a better handoff could actually say

**Feb 7, 2024 — for the reporter taking over:** The June 2023 hearing is no longer just a calendar entry. The board now confirms it took place, and points to transcripts in the hearing docket. The separate accident docket has more than 1,800 pages. Next scheduled decision: June 25, when the board plans to vote on probable cause. Do not write that the board has attributed a cause on the strength of these releases. **Next reporting move:** pull the sworn testimony on the response decision and distinguish what witnesses said from what investigators have concluded. [NTSB release](https://www.ntsb.gov/news/press-releases/Pages/NR20240206.aspx)

**June 25 update:** Now attribute the bearing finding to the NTSB. Add its separate finding about the incident commander's decision and the incomplete and misleading information supplied to the commander. Link the available abstract; keep full-report publication as a watch item, not a completed event. [NTSB release](https://www.ntsb.gov/news/press-releases/Pages/NR20240625.aspx)

These are author-edited examples, not scored model outputs. Key product distinction: a later document can *confirm an earlier event* without making that confirmation available to the earlier reporter. Preserve both times and link the document that changes status. Never turn an absence in this packet into “nobody knew.”

**Prior art / pivot:** Broken historical context is not a new discovery. [Composite Memento temporal coherence](https://arxiv.org/abs/1402.0928) studies date mismatches between archived parent and embedded resources. Our observed mechanism is different: a current page's dated release and related-story text coexist in one extraction. Possible reusable deliverable: an as-of evidence audit for teams backtesting historical research agents. Keep as a pivot, not a second product.

**Next experiment:** Use a different institution and case, freeze source-body captures before annotation, and give both systems identical bodies. Compare a strong one-shot brief against updating a small ledger of event date, first supporting passage, status, and confirmation date. Show anonymous drafts to reviewers if available. Measure wrong-at-cutoff assertions, milestones missed, citation repairs, and minutes to sign-off. If a basic article extractor plus date sorting and the generic prompt matches that workflow on review effort, keep the simpler system.
