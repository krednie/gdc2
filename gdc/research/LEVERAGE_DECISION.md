# Watch a question, not a topic

Read one local neighborhood with `python gdc/research/query_leverage.py change_gate`. Source links point back to the original notebook, competing product, paper or official record. This is a hand-curated index for selective reading, not a model-generated discovery or a measurement of token savings. The installed Graphify repository connector was identifiable but no callable repository tool or authorized index was exposed in this session. No upload or remote indexing performed.

## A real discriminator: one record, two subscribers

In [NYC's outdoor dining bill record](https://legistar.council.nyc.gov/LegislationDetail.aspx?ID=5400747&GUID=9E913589-73E9-4618-B773-B0A6B45BAD92) the committee and council both approved the measure on August 3, 2023. On August 16 the record lists a mayoral hearing, a signing scheduled, and a signature. Consider two deliberately narrow questions: Q1 “Has the council approved this version?” and Q2 “Has the mayor signed this version?”

| Selected action on version C | Q1 warrants positive update? | Q2 warrants positive update? |
|---|---|---|
| Committee approved | No | No |
| Council approved | Yes | No |
| Council sent to mayor | No new answer | No |
| Mayor held hearing | No new answer | No |
| Signing scheduled | No new answer | No |
| Mayor signed | No new answer | Yes |

Six selected rows × two questions = 12 opportunities to send a positive alert; two are warranted under these definitions. A notify-on-every-mention policy would interrupt ten extra times. This is a worked counterexample, not a measured product precision, historical notification timing, or estimate of citywide alert traffic. The action record does not establish when the website first made each row public; same-day dates are not timestamps. Signature is not necessarily the effective date of a particular provision. A different question, such as “is a signing scheduled?”, legitimately changes the labels.

## Technical leverage hypothesis

For a structured source start with (jurisdiction, matter ID, version, question, deciding body, action). Exact match and idempotent notifications are the baseline. Record action date and first observed time separately. A signature is supported by a signature record, not by any row carrying a pass flag. Send changed/ambiguous rows to a model only when needed. When the feed goes dark, report unknown coverage; silence must not imply nothing happened. [Official Legistar schema](https://webapi.legistar.com/Help/Api/GET-v1-Client-Events-EventId-EventItems_AgendaNote_MinutesNote_Attachments) documents action text and pass flags. Direct NYC API access returned HTTP 403, token required; this example used the public council record instead. Do not budget as though every city offers a free API.

The research frontier is narrower than “temporal RAG.” [TIDE](https://arxiv.org/abs/2608.08512) already tests resolving which text applies; [LiveSearchBench](https://arxiv.org/abs/2511.01409) already starts from structured changes. A potentially useful addition is the reverse task: hold a source event fixed, vary the standing question, and test when the system must abstain. Include adjacent but wrong bodies, superseded versions, missing sources, duplicate delivery and effective-date questions. Hard negatives have a useful structure and can be generated cheaply; a reviewer must still adjudicate ambiguity.

## Business leverage hypothesis

[Curate](https://www.curatesolutions.com/local-governments) already advertises a local-government research feed and custom alerts. Broad policy monitoring is a crowded starting point. First candidate buyer to investigate: a trade-publication editor maintaining a municipal policy tracker for subscribers. Their deliverable is an existing table or brief, not another dashboard. Sell a reviewed row change with evidence; do not start by competing on geographic breadth. The same evaluation data could become a secondary product for agent teams, but no buyer or willingness to pay is established for either.

Economics: the relevant denominator is cost per **accepted, supported change**, including human triage, data access and model cost. Count missed changes separately so a silent system cannot win. Distribution hypothesis: offer a patch feed into a publication's existing tracker rather than asking every reporter to adopt a destination. No customer access, integrations or commercial rights are assumed.

## Next go/no-go

Freeze several measures in a second jurisdiction before designing its rules; hold out that jurisdiction for transfer. Compare all-mentions, exact official action/body rules, and rules plus model fallback. Measure warranted-change recall, false alerts per 100 watched question-events, unsupported edit rate, and model calls per accepted change. If rules alone work, ship rules for that source and reserve research for unstructured minutes. If every city needs expensive custom mapping, narrow distribution to a single high-value beat or drop the approach. Validate actual professional time and repeat use separately.
