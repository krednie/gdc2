# Natural-output regression seeds

Inspected 2026-11-09. These examples come from published historical system outputs rather than deliberately corrupted statements. They are targeted findings, not a random sample, prevalence estimate, current-product evaluation, or new-model benchmark.

## NF01: summary and fact list disagree about ordering

Artifact: [public Initial Order evaluation packet](https://raw.githubusercontent.com/tomcardoso/watchdog/8cb766fa003f4bacd10f4a101f4b0f013596b35d/benchmarks/qualitative/packet-initial-order-2021-02-01.json), arm X. Packet SHA-256: `49a71125afcf2fc1fe2915d1b494ef0ea32f275d44c7956df367c7201dbb0880`.

The summary lists the Directors' Charge before the Administration Charge and says that listing is their priority order. A fact in the same output puts the Administration Charge first and the Directors' Charge second. This is an internal inconsistency, not just disagreement with a benchmark answer key.

I checked the underlying scanned order visually: printed page 12, paragraph 32 explicitly lists Administration first and Directors second. Thus the fact-list ordering agrees with this source and the summary ordering does not. This is a narrow textual comparison, not legal advice about enforcement or later proceedings.

Source PDF SHA-256: `e943be8173383b5d077a492401ce783a50e188cc5336547acd5090acb1d73408`. Local source: `source_review/laurentian_initial_order_2021_02_01.pdf`; reviewed image: `source_review/priority_page_12.png`. `render_order_evidence.py` reproduces the download and rendering. Text extraction returned no text for this scanned page, so visual inspection was necessary.

The public mapping labels arm X `sonnet-med`. Do not generalize to a model family or present current rankings. The artifact establishes conflicting output fields; it does not establish whether the summary was generated after the facts, whether the model internally represented the correct relation, or which stage caused the problem.

Product implication: a correct cited fact elsewhere does not make the delivered summary correct. Check the artifact users actually consume. A regression should compare relation direction as well as presence of entities and numbers.

## NF02: structurally empty extraction without a gap flag

The same packet's arm Z has zero key facts, a three-character placeholder summary, and a present but null `coverage_gap` field. The published mapping identifies this historical arm as `sonnet-high`.

`audit_published_packets.py` inspected all six mapped document packets at the pinned revision, totaling 18 arm-document outputs. Exactly one met the narrow predicate: fact list exists and is empty, with no truthy coverage-gap value. Result: `published_packet_audit_results.json`.

This reproduces the structure of a failure already discussed by the project's authors; it is not our discovery of an unknown bug. No inference calls, original run logs, billing, or current versions were reproduced. Nonempty fact lists do not imply adequate coverage, and this predicate would not catch selective omissions.

Product implication: track request success, parse success, extraction substance, semantic coverage, and final-output faithfulness separately. A transport-level success should not be displayed as completion of the user's research task.

## What follows, and what does not

These cases improve the experimental starting point over invented errors: one natural representation inconsistency independently checked against the document, plus one reproducible structural failure. They do not demonstrate a novel intervention, user demand, or superiority of Alithia.

Next discriminating comparison: generic source-to-output verification versus source-to-ledger plus ledger-to-deliverable checks at matched total cost. Count false alarms and human review time, not merely caught errors. Existing factuality checks and structured relation methods are serious baselines. If the generic check is enough, use it.

Keep examples developmental after inspecting them. A held-out test must use different documents/event families and independent labels. Do not tune a detector on the priority-order wording then report this case as evidence of generalization.
