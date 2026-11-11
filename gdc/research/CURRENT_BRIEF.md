# Alithia: current decision brief

Research navigation: [leverage map](leverage_map.json) and [watch-a-question decision memo](LEVERAGE_DECISION.md). New discriminator: a real official action can change one subscriber's answer but not another's.

Updated 2026-11-12. Start here; README.md is the chronological research notebook.

Newest: [desk patch prototype and retrieval check](DESK_PATCH_FINDINGS.md). The review queue works with curated proposals, not autonomous claim discovery. On two Starliner updates the first two paragraphs covered the chosen replacement evidence; the first two keyword-ranked paragraphs covered none. Keep lead-first as a baseline and test a different document form, including no-change items.

Previous: [Starliner paired trial](STARLINER_SHIFT_TRIAL.md). Same frozen passages, fresh vs carried draft. Neither won the one completed memory-active comparison. Test a cited replacement sentence plus a separate watch item with actual reviewers before investing in persistent draft memory.

Latest: [cutoff replay and handoff example](CHRONOLOGY_REPLAY.md). On a local accident investigation the model confused plans with completed events even when given only release-body notes. A more specific product test is an editor's dated handoff with explicit changes, confirmations and pending documents.

## What we are pursuing

A professional should be able to finish a useful, source-checkable chronology with fewer consequential omissions and less review work. This is a product hypothesis, not demonstrated product-market fit. The first customer segment and buyer are still unvalidated.

Do not promise omniscience or automatic immunity to propaganda. Scope the assignment, source universe, cutoff, and unresolved questions. Preserve attribution and uncertainty.

## Latest actual experiment

A live GPT-OSS 120B comparison through Groq completed six requests: generic versus explicit role-aware verification on the 12 existing development fixtures.

| Arm | Correct | Unsupported claims caught | False alarms | Missing predictions |
|---|---:|---:|---:|---:|
| Strong generic verifier | 12/12 | 6/6 | 0 | 0 |
| Explicit temporal/attribution checklist | 12/12 | 6/6 | 0 | 0 |

Input tokens were 1,091 versus 1,094. Completion tokens were 951 versus 910. Combined published-rate estimate: $0.00144435, not a verified account charge. Both arms used the same model and settings. The app's configured Llama model was not changed.

Interpretation: these simple fixtures establish no advantage for the checklist. Do not expand them into a claimed custom verifier breakthrough. They are previously authored examples with paraphrased evidence, not independent or held-out data, natural error prevalence, or a professional task evaluation. One run does not establish equivalence generally.

The initial inference attempt failed with HTTP 403. Read-only diagnostics isolated a client-header issue; an explicit research client identity succeeded. The failed attempt and successful run are retained separately, with no hidden retries.

Protocol: [VERIFIER_PILOT_PROTOCOL.md](VERIFIER_PILOT_PROTOCOL.md). Successful artifacts: `runs/verifier_pilot_live_identified_2026_11_10/`. Default runner behavior is dry-run. Six-call and completion-token limits, conservative cost reservation, strict prediction validation, and credential-safe logs are implemented.

## Concrete evidence accumulated

- **Application visibility:** the existing evidence formatter can produce a context that omits a displayed source. Reproduced in an isolated controlled fixture; no production error rate inferred.
- **Natural-output inconsistency:** a published historical summary reverses a relation its own fact list gets right. Checked against the original scanned source. This demonstrates a failure, not its generation-stage cause.
- **Coverage proxies:** more facts, longer summaries, and more cited pages misorder some outputs against published important-item judgments. Model-judged, small-sample reanalysis, not a universal predictor study.
- **Development dossier:** five accessible DART sources and a task rubric distinguish event occurrence, announcements, plans, and later interpretation. Current pages do not prove historical page versions.

## What is built, and what is not

Built outside the application: a bounded inference runner; seven runner tests; a whole-chunk evidence-accounting helper; twelve helper tests; and an executable comparison with the existing formatter.

The helper preserves content-version identity, records omissions, gives context offsets, and derives source cards only from presented chunks. It uses a character budget and greedy whole-chunk selection. It is a baseline, not a novel selection algorithm. Presented evidence is not automatically supporting or true.

Not built: a new app architecture, autonomous news platform, production integration, optimal evidence selector, or validated completeness estimator. No subscription purchased or application configuration changed.

## Decisions

1. Do not pursue generic temporal checking as our demonstrated technical advantage. The pilot provides no such evidence.
2. Keep chronology completion as a candidate workflow, with important omissions and total review effort as outcomes.
3. Use evidence accounting as instrumentation. It prevents misleading process claims but does not solve semantic completeness.
4. Test harder original-source and naturally occurring cases before adding verification complexity. Freeze cases before seeing outputs and obtain independent labels when possible.
5. Separate a useful product from a novel algorithm. Existing tools and papers already cover many proposed ingredients.

## Next experiment with highest information value

Use full original passages and natural generated outputs, including correct controls, across unseen event families. Compare a strong generic verifier against any proposed intervention at matched total budget. Evaluate omitted important events separately from wrong included claims. Keep a full-context baseline when documents fit.

For product evidence, observe a professional completing a real recurring assignment. Measure final work and voluntary reuse, not just perceived trust. The [review-effort study](REVIEW_EFFORT_STUDY.md) specifies the comparison without claiming recruitment has happened.

## Founder reflex

What would I want the AI to do now? Preserve the negative result, resist selling a fancy schema as a moat, and put the next unit of effort into a test that could change the build decision. Finding a ceiling is progress; renaming the same hypothesis is not.
