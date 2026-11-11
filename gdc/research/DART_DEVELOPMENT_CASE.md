# DART: source-backed chronology development case

Created 2026-11-09. This case was selected and annotated by the same AI investigating the product. It is not held-out, independent annotation, or a model benchmark result.

## Assignment

Prepare a concise research chronology explaining how DART progressed from launch planning to impact and evidence of an altered orbit, through 2024-03-19. Distinguish physical events, announcements, estimates, and later reconstruction. Attach evidence and preserve important uncertainty. Do not describe a demonstration against a non-threatening target as interception of an incoming threat.

## Source packet status

The five source URLs and roles are in `dart_source_manifest.json`. `inspect_source_packet.py` fetched all five successfully (HTTP 200); all 11 selected phrase-presence checks passed. Three parser/normalization assertions run before fetching. Metadata and content hashes are in `dart_source_access_results.json`.

This is an access-checked source manifest, NOT a frozen article corpus. Full text is not stored. Raw hashes include site chrome and can change without a substantive article edit. The normalized-text hash also includes navigation. Hash mismatch alone must not be labeled a news update. Phrase presence confirms neither entailment nor source independence.

Only D05 exposed publication/modification times in the specific Open Graph metadata fields inspected. The four missing fields are not missing publication dates: the dates are visible on the pages. The parser is intentionally a narrow probe, not a production extractor.

Current pages have been inspected; exact historical page versions have not. Use the corpus for retrospective interpretation, not a proven simulation of what a reader could access on each historical day. Five NASA pages are also not five independent confirmations.

## Draft reviewer rubric

These are task-specific expected elements, not a universal ranking of DART milestones. An independent reviewer may add or contest them before any validation study. Requirements are conceptual: exact wording is not required, and alternative supported events should not be penalized simply because they were not anticipated.

| ID | Required distinction / content | Evidence | Error to detect |
|---|---|---|---|
| R01 | Planned launch and accomplished launch are different entries or explicitly different states | D01, D02 | Treating a schedule as proof of completion |
| R02 | Advisory contains a later editorial update | D01 | Assuming all current wording existed at original publication |
| R03 | Launch: November 24, 2021 at 01:21 EST, equivalent to November 23 at 22:21 PST | D01, D02 | Calling the local-date difference a contradiction |
| R04 | Target is Dimorphos, orbiting Didymos | D02, D03 | Swapping impacted moonlet and parent asteroid |
| R05 | Impact occurred September 26, 2022; current release displays September 27 | D03, D04 | Using page date as collision date |
| R06 | Impact confirmation does not itself quantify the orbital change | D03, D04 | Backdating later measurement to impact confirmation |
| R07 | October 11 report gives an initial 32-minute decrease with approximately two-minute uncertainty | D04 | Dropping the uncertainty or treating October 11 as collision time |
| R08 | March 2024 report describes a model-based reconstruction of post-impact orbital evolution | D05 | Treating research publication date as date of physical change |
| R09 | Distinguish improved knowledge from an evolving physical quantity | D04, D05 | Classifying every unequal number as a factual contradiction |
| R10 | Do not claim a threat to Earth was averted in this test | D01, D02, D03 | Turning future defensive potential into an actual rescue |

Optional for this assignment: deployment details, individual quotes, exact spacecraft dimensions, and broader planetary-defense history. They may be relevant for another brief. Omitting them is not automatically a failure here. The distinction illustrates why coverage must be conditioned on a task.

Do not grade factual assertions from the rubric alone. Review the cited source and any credible counterevidence. The rubric's role is defining the work, not replacing evidence.

## Expected handling of unresolved questions

- Exact historical wording of the prelaunch page: unknown without a suitable saved version. The editorial note supplies evidence of change, not the complete earlier text.
- Whether every potentially relevant public source has been found: unknown. This is a deliberately bounded packet.
- Subsequent mission developments after the assignment cutoff: outside scope, even if visible in current site navigation.
- Independent scientific confirmation: not established by collecting several NASA communications. A deeper assignment would inspect the underlying studies and provenance of their observations.

## What this case can test

Useful now: extraction format, reviewer rubric clarity, source/date separation, uncertainty preservation, handling of later interpretation, and accessibility without a paid scraper.

Not established: model failure frequency, superiority over a general model, professional time savings, open-web recall, extraction reliability across publishers, or a unique algorithm.

## Architecture implications, not inventions

Use an assertion record that can preserve source, observed page version, reporting time, event time/interval, attribution, and modality. Allow relations such as planned/completed, refines, and describes-a-later-state. These are existing modeling ideas. The question is whether implementing them improves the task enough to justify their extraction and review cost.

Keep evidence unavailable, evidence uninspected, and inspected-with-no-answer distinct. These states give the user different next actions. Do not automatically convert a missing answer into an allegation that an institution concealed something.

## Reproduce access check

Run `python inspect_source_packet.py --self-test` for local parser assertions, or `python inspect_source_packet.py` to fetch the manifest again and regenerate access metadata. A repeat overwrites only the generated results file; it does not reproduce an earlier page version. No model endpoint is called.
