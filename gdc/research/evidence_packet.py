"""Research-only evidence accounting. Not a truth verifier or app integration.

Whole supplied chunks only. Character budget matches the existing app's unit;
production token budgets require model-specific tokenization separately.
"""
from dataclasses import dataclass, asdict
import hashlib
import json


@dataclass(frozen=True)
class Evidence:
    url: str
    title: str
    text: str
    observed_at: str | None = None

    @property
    def content_hash(self):
        return hashlib.sha256(self.text.encode("utf-8")).hexdigest()

    @property
    def evidence_id(self):
        return hashlib.sha256((self.url + "\0" + self.content_hash).encode()).hexdigest()


def pack_evidence(items, max_characters=6000):
    if type(max_characters) is not int or max_characters < 0:
        raise ValueError("Budget must be a nonnegative integer")
    blocks, presented, omitted, duplicates = [], [], [], []
    seen = set()
    used = 0
    for position, item in enumerate(items):
        if not isinstance(item, Evidence) or not all(isinstance(x, str) for x in (item.url, item.title, item.text)):
            raise ValueError("Invalid evidence record")
        metadata = {"id": item.evidence_id, "url": item.url, "title": item.title,
                    "observed_at": item.observed_at, "content_sha256": item.content_hash,
                    "input_position": position}
        if item.evidence_id in seen:
            duplicates.append(metadata)
            continue
        seen.add(item.evidence_id)
        if not item.text.strip():
            omitted.append({**metadata, "reason": "empty_text"})
            continue
        # JSON keeps metadata/body boundaries explicit; it does not prevent prompt injection.
        block = json.dumps({"evidence_id": item.evidence_id, "title": item.title,
                            "url": item.url, "text": item.text}, ensure_ascii=False)
        separator = "\n" if blocks else ""
        required = len(separator) + len(block)
        if used + required > max_characters:
            omitted.append({**metadata, "reason": "budget", "required_additional_characters": required})
            continue
        start = used + len(separator)
        used += required
        blocks.append(block)
        presented.append({**metadata, "context_start": start, "context_end": used,
                          "status": "presented_not_verified"})
    context = "\n".join(blocks)
    assert len(context) == used <= max_characters
    return {"context": context, "budget_characters": max_characters,
            "used_characters": used, "presented": presented,
            "omitted": omitted, "duplicates": duplicates,
            "source_cards": [{"evidence_id": r["id"], "url": r["url"], "title": r["title"],
                              "status": r["status"]} for r in presented],
            "limitations": ["Presented does not mean understood, supporting, or true.",
                            "Whole-chunk retention does not establish complete source extraction.",
                            "Greedy packing is a baseline, not an optimal relevance policy."]}
