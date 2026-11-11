"""Capture three public releases; paired fresh-vs-carry handoff trial. Exclusive outputs."""
import argparse
import hashlib
import json
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from urllib.request import Request, urlopen, build_opener
from run_verifier_eval import credentials, ENDPOINT, NoRedirect, sha

ROOT = "https://www.nasa.gov/news-release/"
DOCS = [
    ("2024-08-24","nasa-decides-to-bring-starliner-spacecraft-back-to-earth-without-crew"),
    ("2024-09-07","nasa-boeing-welcome-starliner-spacecraft-to-earth-close-mission"),
    ("2025-03-18","welcome-home-nasas-spacex-crew-9-back-on-earth-after-science-mission"),
]

class Paragraphs(HTMLParser):
    def __init__(self):
        super().__init__()
        self.rows=[]
        self.current=None
    def handle_starttag(self,tag,attrs):
        if tag=="p" and "wp-block-paragraph" in dict(attrs).get("class","").split():
            self.current=[]
    def handle_data(self,data):
        if self.current is not None: self.current.append(data)
    def handle_endtag(self,tag):
        if tag=="p" and self.current is not None:
            self.rows.append(" ".join("".join(self.current).split()))
            self.current=None

def capture():
    docs=[]
    for i,(date,slug) in enumerate(DOCS,1):
        url=ROOT+slug+"/"
        with urlopen(Request(url,headers={"User-Agent":"AlithiaResearch/0.1"}),timeout=30) as r:
            data=r.read()
        parser=Paragraphs()
        parser.feed(data.decode())
        rows=[r for r in parser.rows if r][:7]
        if not rows: raise ValueError("No article paragraphs")
        docs.append(dict(date=date,url=url,html_hash=hashlib.sha256(data).hexdigest(),
                         collected=datetime.now(timezone.utc).isoformat(),
                         passages={f"D{i}P{j}":s for j,s in enumerate(rows,1)}))
    return docs

COMMON=("Prepare a science desk handoff as of the last release. Cover the status of the "
        "Starliner capsule and its two original astronauts' returns. Distinguish a decision, "
        "a target and a completed event. Include the material timeline and what a reporter "
        "can newly say, not background trivia. Use only the dated passages. Give up to four "
        "rows ordered by event time. Each row has event date (or target window), compact "
        "statement, status, and the passage IDs supporting that exact status. "
        'JSON only: {"entries":[{"when":"...","statement":"...","status":"...","sources":["..."]}],"change":"..."}')

def trial(docs,stream):
    key=credentials()[0]
    if not key: raise ValueError("no credential")
    prior=None
    spent=0
    opener=build_opener(NoRedirect())
    for i in range(3):
        records=[{"published":d["date"],"passages":d["passages"]} for d in docs[:i+1]]
        for arm in (("fresh","carry") if i!=1 else ("carry","fresh")):
            user={"records":records}
            if arm=="carry" and prior is not None: user["previous_draft"]=prior
            instruction=COMMON+(" Reconcile the previous draft, if provided, with the sources. It is not evidence."
                                if arm=="carry" else " Draft from scratch and review against the sources.")
            payload=dict(model="openai/gpt-oss-120b",temperature=0,seed=731,reasoning_effort="low",
                         max_completion_tokens=1350,response_format={"type":"json_object"},
                         messages=[{"role":"system","content":instruction},{"role":"user","content":json.dumps(user)}])
            spent+=((len(json.dumps(payload).encode())+512)*0.15+1350*0.60)/1e6
            if spent>0.025: raise ValueError("batch reservation exceeded")
            req=Request(ENDPOINT,data=json.dumps(payload).encode(),headers={"User-Agent":"AlithiaResearch/0.1",
                  "Accept":"application/json","Content-Type":"application/json","Authorization":"Bearer "+key})
            row=dict(arm=arm,cutoff=records[-1]["published"],request_hash=sha(payload),source_hash=sha(records))
            try:
                with opener.open(req,timeout=40) as r: result=json.load(r)
                c=result["choices"][0]
                ans=json.loads(c["message"]["content"])
                if c["finish_reason"]!="stop" or not isinstance(ans["entries"],list): raise ValueError("invalid answer")
                if arm=="carry": prior=ans
                row.update(status="ok",answer=ans,usage={k:result["usage"][k] for k in ("prompt_tokens","completion_tokens")})
            except Exception as exc:
                row.update(status="error",error=type(exc).__name__,code=getattr(exc,"code",None))
            stream.write(json.dumps(row,ensure_ascii=False)+"\n");stream.flush()
            print(i+1,arm,row["status"],flush=True)
            if row["status"]!="ok": return

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("mode",choices=["capture","execute"]);p.add_argument("packet",type=Path)
    p.add_argument("--out",type=Path)
    a=p.parse_args()
    if a.mode=="capture":
        docs=capture()
        with a.packet.open("x",encoding="utf-8") as f: json.dump(docs,f,indent=2,ensure_ascii=False)
    else:
        docs=json.loads(a.packet.read_text(encoding="utf-8"))
        if not a.out or [(d["date"],d["url"]) for d in docs]!=[(v,ROOT+s+"/") for v,s in DOCS]:
            raise SystemExit("expected fixed public packet and new output file")
        with a.out.open("x",encoding="utf-8") as f: trial(docs,f)
