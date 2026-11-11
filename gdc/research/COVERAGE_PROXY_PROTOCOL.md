# Coverage proxy audit protocol

Registered locally 2026-11-09 before calculating these comparisons. This is exploratory reanalysis of an existing small evaluation collection, not an independent model experiment.

Question: on the six published Watchdog qualitative packets, do cheap output-size signals order outputs the same way as the published important-item coverage judgments?

Known before registration: the Initial Order packet includes an empty arm; its other two arms have 17 and 21 facts. Some individual item labels have been inspected. Prior author summaries have also been read. This is not blinded or free of prior knowledge.

Data: all six packet/judgment pairs listed by mapping.json at revision `8cb766fa003f4bacd10f4a101f4b0f013596b35d`. No packet exclusion based on outcome. Save input hashes. Model names are unnecessary to the hypothesis; report anonymous per-document arms.

Outcome: fraction of items in the packet's important-item category labeled `verbatim` or `credited` by the published judge. These are externally supplied model-judge labels, not ground truth. Report strict `verbatim`-only sensitivity as well. Do not confuse coverage with factual precision or source validity.

Proxies fixed before comparison: number of key facts; summary character length; number of distinct positive integer page citations in key facts. A page-span count is not proof of reading the document, and raw output size can be inflated by irrelevant content.

Comparison: for each document, compare every pair of its three outputs. Count concordant, discordant, proxy-tied, and outcome-tied orderings. Report the conditional concordance among pairs tied on neither quantity, with denominators. Repeat excluding pairs involving empty fact lists. No pooled correlation across different-sized documents, no p-values from treating dependent pairs as independent observations, no accuracy or confidence guarantee.

Record at least one discordant example if any exist. Failure criterion for using a proxy as a completion certificate: any such inversion disproves a deterministic ordering guarantee on this set. High agreement would still not validate a runtime completeness certificate or imply causal improvement from generating more facts.

Interpretation limits: six related legal/financial documents, three historical arms per document, model-judged labels, selection of qualitative rather than all evaluation items, no replication. Purpose is choosing which cheap diagnostic not to trust blindly, not estimating an industry-wide effect.

## Executed result

`audit_coverage_proxies.py` fetched all six packet/judgment pairs and recorded hashes in `coverage_proxy_results.json`. All expected important-item labels were found and passed the allowed-label check. Five pair-classification branches were separately tested successfully.

With both `verbatim` and `credited` treated as coverage hits:

| Proxy | Concordant pairs | Discordant pairs | Proxy-only ties | Outcome-only ties | Total |
|---|---:|---:|---:|---:|---:|
| Number of facts | 10 | 5 | 0 | 3 | 18 |
| Summary character length | 9 | 6 | 0 | 3 | 18 |
| Distinct cited pages | 9 | 5 | 1 | 3 | 18 |

Excluding the two comparisons involving the empty output leaves 16 pairs. Concordant counts drop to 8, 7, and 7 respectively; the discordant counts remain 5, 6, and 5. Thus these disagreements are not explained solely by the empty-output outlier. Under strict `verbatim`-only scoring, all three proxies still show inversions; this sensitivity analysis does not validate the judge labels themselves.

Concrete example, `annual-financial-report-19-20`: arm X contains 49 facts and receives credit for 7/9 important items; arm Y contains 61 facts and receives credit for 3/9. Its longer summary also does not rescue the ranking. The nine items are this packet's qualitative important-item slice, not all possible important information in the document. Credit comes from the published model judge, not our independent annotation.

Conclusion supported: more output and broader page citation do not deterministically imply better task-specific coverage in these published artifacts. These signals can still be useful warning features; this study does not show they are useless. No calibrated completeness estimator, human review-time improvement, population failure rate, or new model ranking has been established.

Product consequence: avoid displaying a completeness badge based on fact count, output length, or citation spread. Show those as process diagnostics and keep task-coverage judgments separate. Next necessary evidence is independently adjudicated coverage on unseen event families; optimizing this six-document sample would not establish generalization.
