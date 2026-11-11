"""Offline editor review queue. Assertions are supplied, not inferred or published."""
import argparse
import hashlib
import json
from datetime import date
from pathlib import Path


def fingerprint(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def index_packet(docs):
    index = {}
    for doc in docs:
        for pid, body in doc["passages"].items():
            if pid in index:
                raise ValueError("duplicate passage ID")
            index[pid] = {"text": body, "url": doc["url"], "published": doc["date"]}
    return index


def review(story, proposals, passages, cutoff):
    boundary = date.fromisoformat(cutoff)
    ids = [s["id"] for s in story]
    if len(set(ids)) != len(ids):
        raise ValueError("duplicate sentence ID")
    if len({p["id"] for p in proposals}) != len(proposals):
        raise ValueError("duplicate proposal ID")
    # Never assume that two stories about a vehicle and its passengers refer to
    # the same return. Join on a curator-supplied event key, not shared words.
    result = []
    for s in story:
        candidates = [p for p in proposals if p["event"] == s["event"]
                      and date.fromisoformat(p["available"]) <= boundary]
        cards, issues = [], []
        for p in candidates:
            refs = []
            for pid, digest in p["refs"].items():
                entry = passages.get(pid)
                if (not entry or fingerprint(entry["text"]) != digest
                        or entry["published"] > p["available"]):
                    issues.append([p["id"], "missing, changed or not-yet-available passage"])
                    break
                refs.append(dict(id=pid, **entry))
            else:
                if not refs or not p["text"].strip():
                    issues.append([p["id"], "empty evidence or replacement"])
                elif fingerprint(s["text"]) != p["before_hash"]:
                    issues.append([p["id"], "editor has a different sentence version"])
                elif p["text"] == s["text"]:
                    continue
                else:
                    cards.append({"proposal": p["id"], "replacement": p["text"], "sources": refs})
        state = ("needs_review" if issues or len(cards) > 1 else
                 "proposed_edit" if cards else "no_proposed_edit")
        result.append(dict(sentence=s["id"], original=s["text"], event=s["event"],
                           state=state, candidates=cards, issues=issues))
    return result


def render(rows):
    parts = []
    for r in rows:
        parts.extend([f"## {r['sentence']} — {r['state']}", "", r["original"], ""])
        for card in r["candidates"]:
            parts.extend(["Proposed: " + card["replacement"], ""])
            for s in card["sources"]:
                parts.extend([f"[{s['id']} · {s['published']}]({s['url']})", "", "> " + s["text"], ""])
        for pid, reason in r["issues"]:
            parts.extend([f"Review {pid}: {reason}", ""])
    return "\n".join(parts)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("fixture", type=Path)
    parser.add_argument("--as-of", required=True)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    fixture = json.loads(args.fixture.read_text(encoding="utf-8"))
    packet = json.loads((args.fixture.parent / fixture["packet"]).read_text(encoding="utf-8"))
    rows = review(fixture["story"], fixture["proposals"], index_packet(packet), args.as_of)
    print(json.dumps(rows, ensure_ascii=False, indent=2) if args.json else render(rows))
