# Cycle 3: finish the chronology, not just generate it

Research decision brief, 2026-11-03. Status: proposed product experiment, not validated fit. Read alongside README.md for completed diagnostics and source limits.

## Founder decision

Keep the ambition of an exceptionally useful chronology. Stop treating a custom graph, uncertainty checker, or clever retrieval loop as the product thesis. The relevant question is whether a professional can finish a concrete research task with fewer important omissions and less checking than with existing tools.

Working positioning to test:

> Turn a bounded set of records about a developing event into a reviewable chronology: what happened, what is only claimed or planned, what supports each entry, and which important questions the available evidence still cannot answer.

This is not a promise to know everything. Scope, cutoff, excluded sources, and unresolved questions belong in the output. Unknown is an acceptable result. An official source establishes an attributable statement and sometimes direct evidence; official status alone does not establish every underlying claim as true.

## Product fit before architecture

First user hypothesis: a reporter or research analyst assembling a background chronology for a specific assignment from public records and reporting. Select actual recurring tasks rather than treating all journalists and analysts as one market. Buyer, frequency, available budget, and switching friction remain unknown.

Trigger: a new assignment requires understanding the sequence behind an event, not merely reading the latest article. Deliverable: a chronology that can be checked, amended, and exported into the user's existing writing workflow. The meaningful success event is a usable completed dossier, not a pleasing summary or time spent in our interface.

Start with document-rich public investigations or institutional decisions as an evaluation setting. This is an access choice, not a claim that incident reporting is the best market. War-news coverage adds disputed access, multilingual evidence, operational safety, and potentially serious identity harms before we know the basic workflow works. Do not infer identities of casualties or present unconfirmed causes as established facts.

Do not first build a general public destination, autonomous article writer, or replacement for original reporting. Interviews, unavailable documents, and firsthand verification can remain necessary.

## What the evidence changes

| Alternative | Evidence inspected | Consequence for us |
|---|---|---|
| Watchdog | [Official repository overview](https://github.com/tomcardoso/watchdog): cited document facts, timelines, connections, contradiction review | A document-to-investigation workspace is already being built. Need task-level comparison; no claim its accuracy is known |
| Feedly | [Engineering explanation](https://feedly.com/engineering/posts/reducing-clustering-latency): event clustering and near-duplicate removal | Aggregation and deduplication are baseline capabilities, not a distinctive thesis |
| Event Registry | [Help page](https://help.eventregistry.org/event-details-reporting-timeline/): article publication activity | Clearly distinguish reporting time from event occurrence; do not infer the whole platform lacks event intelligence |
| General AI plus source folder | Strong practical baseline, not evaluated here | A careful prompt and existing model may be sufficient; this baseline must be allowed to win |
| Timeline and factuality research | AMRFact, TimelineAgent, DTELS, ATC; see notebook | Existing methods already cover many proposed ingredients. Novelty must reside in a demonstrated unresolved problem or improvement |

Workflow evidence is encouraging but limited. The [2025 interview study](https://arxiv.org/html/2503.16011v1) supports the importance of collection, documentation, and verification; its eight-person sample and video elicitation cannot validate our specific product. Customer claims require direct observation of actual work.

## The narrower research question

Under a fixed collection and review budget, can a system reduce consequential chronology omissions while keeping unsupported assertions and verification effort acceptably low?

Separate three possible failures:

1. **Acquisition:** the necessary record was not retrieved or cannot be accessed.
2. **Interpretation:** the record was available but the system misunderstood time, actor, attribution, conditions, or event identity.
3. **Selection:** the system understood an event but excluded it despite its importance to the user's task.

This decomposition matters: improving the verifier cannot recover an unseen record, and adding more records can increase review burden without improving the deliverable. It is an experimental decomposition, not a new scientific theory.

The candidate intervention is a task-specific evidence checklist linked to chronology entries and unresolved questions. Each suggested next document must name the question it could resolve. The basic mechanism overlaps with Active Timeline Completion and classical coverage optimization. A contribution would require evidence that the intervention improves outcomes beyond these baselines, not a new label for gap questions.

Completeness has three distinct meanings: coverage of a supplied collection, coverage of a declared source universe, and coverage of reality. Only the first is directly measurable in the initial experiment. Do not translate a high score there into an open-web completeness guarantee.

## Cheapest discriminating experiment

No new model spend is authorized or assumed. Preparing cases is possible now; comparing model outputs requires an explicitly available execution route. Existing authored fixtures are development material only.

### Data and controls

- Choose six public event families for a feasibility pilot: two development, four held out. This is a small pilot, not adequate statistical evidence for broad superiority.
- Keep Apple, Boeing MAX, and Starliner as development examples because we have already inspected their failures. Do not reuse them as surprising held-out successes.
- Give each family an explicit research question and cutoff. Collect a bounded packet of primary records plus selected reporting with source URL, retrieval time, document date, version hash, and access status.
- Preserve attribution. A company's account, a regulator's decision, and a reporter's inference are different evidence types even when the sentences look similar.
- Have a reviewer who did not create system outputs identify essential events and supporting spans. Preserve ambiguous labels and disagreement. Without independent review, label results developmental, not validation.
- Freeze the packet and rubric before predictions. Audit candidate reference events missing from the original rubric through blinded adjudication; otherwise a better system can be penalized for finding something the annotator overlooked.
- Source version uncertainty is explicit. A current page is not proof of the exact text available at a historical cutoff. Start prospective replay from saved versions if retrospective availability cannot be established.

### Matched arms

| Arm | Method | What it tests |
|---|---|---|
| A | General model, strong chronology prompt, same source packet and citation requirement | Whether a standard model already solves the task |
| B | Same model plus explicit actor/time/modality checks | Whether structure adds value beyond ordinary verification |
| C | Same model plus evidence-question coverage and targeted follow-up within the packet | Whether omission reduction justifies extra cost |

Compare within equal total token and tool budgets, including extraction, retries, verification, and rejected candidates. Also report unconstrained cost-quality curves, so equal budget does not hide useful but more expensive behavior. Give A a comparable revision opportunity. If all source text fits in context, include a full-context baseline; do not handicap it with unnecessary retrieval.

Separate an oracle-support condition (known relevant passages) from end-to-end retrieval. Otherwise a retrieval advantage may be incorrectly credited to reasoning. If reproducing ATC is infeasible, label an inspired baseline honestly; do not call it the published system.

### Measures

Primary outcome: reviewer minutes to produce an acceptable final chronology, with essential-event coverage and unsupported-assertion rate reported alongside it. If no independent reviewer is available, do not replace this with AI-estimated minutes.

Also record citation-support accuracy, time-role and actor errors, unresolved-question accuracy, duplicate entries, inference usage, and latency. Report absolute counts and event-level variability. Hundreds of assertions from four stories are not hundreds of independent event samples.

Abstention is not automatically success: an empty chronology has few unsupported claims but no useful coverage. A longer chronology is not automatically success either. Report the coverage/error/review-effort tradeoff without collapsing everything into a convenient single number.

Provisional engineering gate, chosen before outputs: pursue further if the candidate gives a material review-time reduction (target 25%) without losing essential-event coverage or increasing unsupported assertions on the pilot. This is a founder-set decision threshold, not an industry standard or statistical guarantee. A larger independent test is needed before external claims.

Reject or narrow if the generic baseline matches it; if the checklist mostly creates irrelevant questions; if extra checking eats the time saved; or if inaccessible records dominate failures. In the last case investigate acquisition as the bottleneck rather than adding reasoning machinery.

## Product validation, distinct from method evaluation

No outreach has been performed. Before building a full platform, observe three to five consenting professionals on a recent recurring assignment. Ask for public or redacted artifacts, not confidential source material.

Questions should reconstruct behavior: What was the last chronology you made? Which records did you inspect? What did you almost miss? How did you decide you had enough? What did the editor or client send back? How often do you repeat this? Who can authorize spending?

Run a task-based comparison, not a feature-pitch survey. Then look for voluntary reuse on a second task, retained/exported work, corrections made, and actual purchase intent from a plausible buyer. These are early signals, not proof of product-market fit. If the task is rare, a reusable utility or integration may fit better than a subscription platform.

## Economics without invented pricing

Per-dossier variable cost = retrieval/extraction + model input/output + storage + retries + human review/support. Record each term even when locally subsidized. Track failed-source attempts separately: scrape success and usable-evidence yield are not the same metric.

Customer value hypothesis = time saved on a required task plus fewer costly omissions. Do not assign a salary, hourly rate, or willingness to pay without evidence. If review consumes most effort, token optimization may barely affect delivered cost. If acquisition dominates, hosted scraping might help availability but will not establish evidence quality or demand.

An open benchmark or audit tool remains a credible student outcome if commercial demand fails. Conversely, a useful integration can be commercially valuable without a novel algorithm. Choose the route from results, not prestige.

## Founder reflex and next action

If I were accountable for this venture, I would want the AI to stop us from confusing a literature gap with a buyer, a clever schema with a moat, or a synthetic diagnostic with a measured improvement.

Next executable research work: assemble one bounded source packet and a reviewer-facing task rubric, then identify an actual no-new-spend prediction route. Keep the corpus interface independent of the scraper. Do not build the full platform or spend on extraction until this reveals whether acquisition, interpretation, or selection is the dominant failure.

Side pivot retained: reusable evaluation of task-conditioned evidence coverage. Its potential value is making omissions visible to tool builders. Novelty, annotation affordability, and adopter demand remain unproven. It must compete with established summarization coverage and human-evaluation methods.
