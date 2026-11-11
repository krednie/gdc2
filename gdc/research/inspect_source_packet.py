"""Read bounded public source URLs; save metadata/hashes, not article copies.

No LLM calls, third-party dependencies, or upstream code execution.
An access probe is not a historical snapshot or a semantic entailment test.
"""
import argparse
import hashlib
import json
import re
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit
from urllib.request import Request, urlopen


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.hidden = 0
        self.text = []
        self.meta = {}

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag in {"script", "style"}:
            self.hidden += 1
        if tag == "meta":
            key = attrs.get("property", attrs.get("name", ""))
            if key in {"article:published_time", "article:modified_time", "og:title"}:
                self.meta[key] = attrs.get("content")

    def handle_endtag(self, tag):
        if tag in {"script", "style"}:
            self.hidden = max(0, self.hidden - 1)

    def handle_data(self, data):
        if not self.hidden:
            self.text.append(data)


def normalize(text):
    return re.sub(r"\s+", " ", text).strip().casefold()


def inspect(source):
    result = {"id": source["id"], "requested_url": source["url"],
              "retrieved_at_utc": datetime.now(timezone.utc).isoformat()}
    try:
        if urlsplit(source["url"]).hostname != "www.nasa.gov":
            raise ValueError("This bounded probe only permits www.nasa.gov URLs")
        request = Request(source["url"], headers={"User-Agent": "AlithiaResearchProbe/0.1"})
        with urlopen(request, timeout=30) as response:
            raw = response.read(4_000_001)
            if len(raw) > 4_000_000:
                raise ValueError("Response exceeded 4 MB limit")
            result.update(status=response.status, resolved_url=response.url,
                          content_type=response.headers.get("Content-Type"))
            encoding = response.headers.get_content_charset() or "utf-8"
        page = PageParser()
        page.feed(raw.decode(encoding, errors="replace"))
        text = normalize(" ".join(page.text))
        result.update(
            raw_bytes=len(raw), raw_sha256=hashlib.sha256(raw).hexdigest(),
            normalized_visible_text_sha256=hashlib.sha256(text.encode()).hexdigest(),
            metadata=page.meta,
            marker_presence={marker: normalize(marker) in text for marker in source["markers"]},
            historical_snapshot=False,
        )
    except Exception as exc:
        result["error"] = f"{type(exc).__name__}: {exc}"
    return result


def self_test():
    page = PageParser()
    page.feed('<meta property="article:published_time" content="2021-01-01">'
              '<script>hidden</script><p>32&nbsp; minutes <b>and</b> 42 seconds</p>')
    assert normalize(" ".join(page.text)) == "32 minutes and 42 seconds"
    assert page.meta["article:published_time"] == "2021-01-01"
    assert normalize("PLUS\n or\tminus") == "plus or minus"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", type=Path, default=Path(__file__).with_name("dart_source_manifest.json"))
    parser.add_argument("--output", type=Path, default=Path(__file__).with_name("dart_source_access_results.json"))
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    self_test()
    if args.self_test:
        print("3 parser/normalization assertions passed")
        return
    manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
    with ThreadPoolExecutor(max_workers=2) as pool:
        rows = list(pool.map(inspect, manifest["sources"]))
    output = {"case_id": manifest["case_id"], "kind": "access_and_marker_probe_not_model_evaluation",
              "results": rows}
    args.output.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    for row in rows:
        print(row["id"], row.get("status", row.get("error")), row.get("marker_presence", {}))
    print("Saved", args.output)


if __name__ == "__main__":
    main()
