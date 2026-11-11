# First live verifier pilot

2026-11-10, recorded before live calls. User authorized continuing and building research tools after the request for a capped configured-provider evaluation.

Question: does an explicit role checklist outperform a strong generic evidence-verification instruction on the 12 existing development fixtures? This is a smoke test and a possible ceiling check, not novel-method validation.

Same configured model, source evidence, claim order, temperature, seed, reasoning effort, and output cap. Six requests: two arms by three source groups. Randomized fixed request order. Labels, error classes, and manually supplied semantic roles are withheld from prompts. Evidence remains researcher paraphrase, not original passages. One run; no threshold tuning or retries. Checklist specificity and prompt wording differ, so this does not isolate a causal mechanism or match exact input token counts.

Scores: valid coverage, confusion counts, correct/planned, accuracy on valid outputs. Failed/missing requests are shown explicitly, not silently discarded. Empty, truncated, duplicate-ID, wrong-type, or missing-ID predictions fail validation. Account token usage is recorded when supplied. No claims about independent annotation, held-out accuracy, professional usefulness, or statistical significance.

Interpretation fixed beforehand: if both arms solve these cases, the fixtures do not establish an advantage for extra structure; move to harder natural-output and original-source cases rather than celebrating a tie as a novel system. If one differs, inspect errors without treating one small run as robust superiority.

Controls: dry-run default; explicit execute switch; no app imports; no model substitution; no automatic retries; max six calls and 1,536 completion tokens each; a conservative bytes-based input reservation with a local $0.02 gate using verified published rates. This is not an account-level billing limit. No subscriptions, account changes, tools, or web search are invoked by the model. Only public researcher-authored fixtures are transmitted. Credentials read only for the configured Groq route and never written to artifacts.

Documentation checked: [Groq API](https://console.groq.com/docs/api-reference), [Groq model rates](https://console.groq.com/docs/models), and [OpenAI gpt-oss model](https://developers.openai.com/api/docs/models/gpt-oss-120b). Provider implementation details come from Groq; OpenAI's model documentation does not establish Groq account access or billing.

Pre-execution amendment: the configured model is `llama-3.3-70b-versatile`; its current provider listing gives enterprise/contact-sales pricing. The dry-run stopped before any request. Use an explicit `--model openai/gpt-oss-120b` research override for both arms, with published pricing, rather than guess the configured model's rate. No application configuration change or automatic fallback. This is therefore a GPT-OSS pilot, not a measurement of Alithia's currently configured model.

Transport amendment before any predictions: the first completion attempt returned HTTP 403 and stopped the run. A read-only model-list request with Python's default client identity also returned 403 with error marker 1010. An explicit, honest `AlithiaResearch/0.1` User-Agent received HTTP 200 and confirmed GPT-OSS 120B availability. A fresh run uses that header; the original failed run remains preserved. No credentials or account settings changed, no proxy rotation, and no automatic inference retries. Total attempted completion requests across both runs can therefore be seven, including the initial rejected request. Total local reservation remains below $0.02; billing is not independently confirmed.
