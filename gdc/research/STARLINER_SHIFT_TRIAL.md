# Two returns, three desk handoffs

Pre-run design, 12 November 2026. [Frozen packet](runs/starliner_body_packet.json) contains the first seven nonempty WordPress article paragraphs of each of three current NASA releases, plus URL, displayed publication date, capture time, and HTML hash. Excludes related-news panels. Not proof of what a historical page displayed. No third-party reporting represented.

Conditions: same cumulative passages, same handoff schema and materiality instruction, same model and generation limit. Fresh writes from scratch. Carry also receives its own preceding four-row handoff, explicitly not evidence. This compares a lightweight persistent draft, not a database or a pure memory ablation: short arm-specific instructions differ; carry gets extra input tokens. Six calls maximum, no retry, local cumulative estimated reservation $0.025. First cutoff has no previous draft: calibration only. Do not pool these repeated cutoffs as independent cases.

Predefined required handoff facts:

- August: decision about uncrewed return (not a landing); crew remains on station with later Dragon/Crew-9 return planned; capsule return targeted for early September.
- September: preserve August decision; actual uncrewed landing September 6 local (not release date September 7); crew remains aboard station, February return still a plan.
- March: preserve August decision; September uncrewed landing; Wilmore and Williams actually return March 18 via Crew-9 Dragon; distinguish earlier February expectation from realized March date.

Score explicit coverage in dated rows or change line. Separately note wrong temporal status, ordering, and insufficient row citations (can the cited paragraphs support the material parts without searching the rest?). Distinguish needed source repairs from style preferences. Author audit, not blind or independent. No sign-off time available. Do not estimate time saved from token counts. Prefer fresh if carry does not improve substantive quality.

## Observations

[Raw run](runs/starliner_shift_trial.jsonl). Four successful drafts; the fifth call (fresh, March) returned HTTP 429; the sixth was not sent. The stop policy stands. March is unscored for both. There is only one successful paired cutoff where memory was active.

| As of | Fresh draft | Carry draft |
|---|---|---|
| Aug 24 | 3/3 required items. Its change line adds that all required engineering fixes were finished. D1P5 describes tests and reviews, not completion of all repairs. Delete this assertion. | 2/3. Omits how the astronauts are expected to return. Adds an unsupported mid-2024 launch window to the docking-port constraint (D1P7); change line says only “updated.” No prior draft yet. |
| Sept 7 | 2/3. Right landing, right pending crew return. Dates the uncrewed-return decision June 6, when the technical problems were identified. Its cited D2P6 explicitly says weeks of work preceded the decision. | 2/3. Right August decision and Sept 6 landing. Carries an engineering row and a still-present-tense September target forward; no row tells the next shift that the two astronauts are still expecting a February trip with Crew-9. |

For September the crew-plan item credits the fresh draft's planned return plus its statement that the pair remain on station; the incorrect date on that decision fails the separate decision item. Both preserve a prospective capsule target without clearly flagging it as superseded. Both August drafts use the release date as an exact engineering-work date without explicit passage support. These counts are about explicitly specified milestones, not factual precision or quality scores. The carry draft preserved the correct August date; that is not proof memory caused the improvement. September carry used 1,830 input tokens versus fresh's 1,589; no review-time inference.

**New product test: protect the edit, not just the timeline.** Fresh's August rows describe analyses and tests; the unsupported “fixes” assertion enters in the sentence aimed directly at the reporter. A check on dated rows alone would miss it. A source-bearing replacement sentence and a separate pending-items list may be more useful than preserving four polished rows. Both should be editable without rewriting the whole page.

### Example handoff cards (author-edited, not model outputs)

**Sept 7:** Replace “Starliner is expected back in early September” with “The capsule landed without a crew in New Mexico on Sept 6 local time.” [Confirmation: September release, paragraph 1](https://www.nasa.gov/news-release/nasa-boeing-welcome-starliner-spacecraft-to-earth-close-mission/). Keep on watch: Wilmore and Williams are still on station; February is their projected Crew-9 return, not an accomplished flight (same release, paragraph 6).

**March 18:** Replace “the astronauts are expected to return in February” with “Wilmore and Williams returned March 18 aboard Crew-9's Dragon.” [Confirmation: March release, paragraphs 1–2](https://www.nasa.gov/news-release/welcome-home-nasas-spacex-crew-9-back-on-earth-after-science-mission/). Retain the September capsule landing as a separate historical event. Do not invent an explanation for the change from February to March: this packet does not trace every intervening schedule change.

### A cheaper decision before another model run

Use the two September drafts as anonymous candidates for a five-minute desk exercise. Hand a reviewer the August story lead and the August/September releases. Ask for (1) the one sentence they would replace, (2) the paragraph that authorizes the replacement, (3) what they would keep watching. Record actual time, substantive edits and source opens; alternate presentation order across reviewers. Ask what tool or artifact they last used for a real comparable handoff. Do not infer recurring demand from a hypothetical “would you use it?” If the ordinary source-and-notes workflow is as fast and accurate, don't build a memory subsystem on this evidence.
