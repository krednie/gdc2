"""Read-only upstream audit; writes derived research results, never upstream text.

Run with Python 3.10+ (standard library only). No upstream code execution.
Use --revision SHA to reproduce the snapshot recorded in the results.
"""
import argparse
import ast
import calendar
import concurrent.futures
import datetime as dt
import hashlib
import json
import re
import urllib.request
from collections import Counter
from pathlib import Path

REPO = "Alibaba-NLP/CHRONOS"
MONTHS = {name.lower(): i for i, name in enumerate(calendar.month_name) if name}
MONTHS.update({name.lower(): i for i, name in enumerate(calendar.month_abbr) if name})
DATE_RE = re.compile(
    r"\b(?:(\d{1,2})(?:st|nd|rd|th)?[, ]+"
    r"(January|February|March|April|May|June|July|August|September|October|November|December)"
    r"[, ]+(\d{4})|"
    r"(January|February|March|April|May|June|July|August|September|October|November|December)"
    r"\s+(\d{1,2})(?:st|nd|rd|th)?[,]?\s+(\d{4}))\b", re.I
)


def fetch(url):
    request = urllib.request.Request(url, headers={"User-Agent": "AlithiaResearchAudit/0.1"})
    with urllib.request.urlopen(request, timeout=45) as response:
        return response.read()


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def precision(date_text):
    day = date_text.split("T")[0]
    try:
        if re.fullmatch(r"\d{4}-\d{2}-\d{2}", day):
            dt.date.fromisoformat(day)
            return "day"
        if re.fullmatch(r"\d{4}-\d{2}", day):
            dt.date.fromisoformat(day + "-01")
            return "month"
        if re.fullmatch(r"\d{4}", day):
            dt.date.fromisoformat(day + "-01-01")
            return "year"
    except ValueError:
        pass
    return "invalid_or_other"


def explicit_dates(sentence):
    dates = []
    for match in DATE_RE.finditer(sentence):
        day, month, year, month2, day2, year2 = match.groups()
        try:
            dates.append(dt.date(int(year or year2), MONTHS[(month or month2).lower()], int(day or day2)).isoformat())
        except ValueError:
            dates.append("INVALID_EXPLICIT_DATE")
    return dates


def inspect_topic(base, entry):
    topic, query, topic_id = entry
    url = f"{base}/data/open/{topic}/timelines.jsonl"
    raw = fetch(url)
    records = [json.loads(line) for line in raw.decode("utf-8").splitlines() if line.strip()]
    result = {"topic": topic, "query": query, "topic_id": topic_id, "url": url,
              "sha256": digest(raw), "reference_timelines": len(records), "rows": 0,
              "sentences": 0, "date_precision": Counter(), "multi_sentence_rows": 0,
              "rows_with_url_in_text": 0, "duplicate_dates": [], "order_inversions": [],
              "shape_errors": [], "date_text_flags": []}
    for ref_index, timeline in enumerate(records):
        previous = None
        seen = set()
        for row_index, row in enumerate(timeline):
            if not (isinstance(row, list) and len(row) == 2 and isinstance(row[0], str)
                    and isinstance(row[1], list) and all(isinstance(s, str) for s in row[1])):
                result["shape_errors"].append([ref_index, row_index])
                continue
            date_text, sentences = row
            result["rows"] += 1
            result["sentences"] += len(sentences)
            result["multi_sentence_rows"] += int(len(sentences) > 1)
            result["rows_with_url_in_text"] += int(any(re.search(r"https?://", s) for s in sentences))
            result["date_precision"][precision(date_text)] += 1
            date_key = date_text.split("T")[0]
            if date_key in seen:
                result["duplicate_dates"].append([ref_index, row_index, date_key])
            seen.add(date_key)
            if previous is not None and date_key < previous:
                result["order_inversions"].append([ref_index, row_index, previous, date_key])
            previous = date_key
            for sentence_index, sentence in enumerate(sentences):
                for explicit in explicit_dates(sentence):
                    if explicit != date_key:
                        result["date_text_flags"].append({"reference_index": ref_index,
                            "row_index": row_index, "sentence_index": sentence_index,
                            "row_date": date_key, "explicit_date": explicit,
                            "status": "candidate_only_not_adjudicated"})
    return result


def date_f1(pred, reference):
    pred, reference = set(pred), set(reference)
    if not pred or not reference:
        return {"precision": 0.0, "recall": 0.0, "f1": 0.0}
    overlap = len(pred & reference)
    p, r = overlap / len(pred), overlap / len(reference)
    return {"precision": p, "recall": r, "f1": 2*p*r/(p+r) if p+r else 0.0}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--revision")
    parser.add_argument("--output", default=str(Path(__file__).with_name("open_tls_audit_results.json")))
    args = parser.parse_args()
    revision = args.revision or json.loads(fetch(f"https://api.github.com/repos/{REPO}/commits/main"))["sha"]
    if not re.fullmatch(r"[0-9a-f]{40}", revision):
        raise ValueError("Expected a full commit SHA")
    base = f"https://raw.githubusercontent.com/{REPO}/{revision}"
    manifest = fetch(f"{base}/news_keywords.py")
    parsed = ast.parse(manifest.decode("utf-8"))
    assignment = next(n for n in parsed.body if isinstance(n, ast.Assign)
                      and any(isinstance(t, ast.Name) and t.id == "TARGET_KEYWORDS" for t in n.targets))
    entries = ast.literal_eval(assignment.value)["open"]
    topics, failures = [], []
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        jobs = {pool.submit(inspect_topic, base, entry): entry[0] for entry in entries}
        for future in concurrent.futures.as_completed(jobs):
            try:
                topics.append(future.result())
            except Exception as exc:
                failures.append({"topic": jobs[future], "error": f"{type(exc).__name__}: {exc}"})
    topics.sort(key=lambda x: x["topic_id"])
    counts = Counter()
    for topic in topics:
        counts.update(topic["date_precision"])
    summary = {"requested_topics": len(entries), "fetched_topics": len(topics),
               "failed_topics": len(failures), "date_precision": dict(counts)}
    for key in ("reference_timelines", "rows", "sentences", "multi_sentence_rows", "rows_with_url_in_text"):
        summary[key] = sum(t[key] for t in topics)
    for key in ("shape_errors", "duplicate_dates", "order_inversions", "date_text_flags"):
        summary[key] = sum(len(t[key]) for t in topics)
    apple = json.loads(fetch(f"{base}/data/open/Apple_2024.6.5/timelines.jsonl"))
    reference = [row[0].split("T")[0] for row in apple]
    repaired = ["2023-06-05" if day == "2024-06-05" else day for day in reference]
    counterexample = {"topic": "Apple_2024.6.5", "reference_date_count": len(set(reference)),
        "changed_date": {"original": "2024-06-05", "primary_source_supported": "2023-06-05"},
        "reference_clone": date_f1(reference, reference), "one_date_repair": date_f1(repaired, reference),
        "interpretation": "Constructed metric diagnostic; not a comparison of model outputs."}
    output = {"run_utc": dt.datetime.now(dt.timezone.utc).isoformat(), "repository": REPO,
              "revision": revision, "manifest_sha256": digest(manifest),
              "summary": summary, "failures": failures, "topics": topics,
              "date_metric_counterexample": counterexample}
    Path(args.output).write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"revision": revision, "summary": summary, "failures": failures,
                      "date_metric_counterexample": counterexample}, indent=2))


if __name__ == "__main__":
    main()
