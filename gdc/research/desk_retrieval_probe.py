"""Zero-model baseline: rank a new release's paragraphs against a standing sentence."""
import json
import math
import re
from collections import Counter
from pathlib import Path


def tokens(text):
    stop=set("a an the and its to in is are with on of at as for".split())
    return [t for t in re.findall(r"[a-z0-9]+",text.lower()) if t not in stop]


def rank(query, paragraphs):
    # Standard BM25, k1=1.2, b=0.75, calculated only within the incoming release.
    docs={key:Counter(tokens(text)) for key,text in paragraphs.items()}
    mean=sum(sum(tf.values()) for tf in docs.values())/len(docs)
    scores={}
    for key,tf in docs.items():
        score=0
        for term in set(tokens(query)):
            df=sum(term in t for t in docs.values())
            scale=math.log(1+(len(docs)-df+0.5)/(df+0.5))
            score+=scale*tf[term]*2.2/(tf[term]+1.2*(0.25+0.75*sum(tf.values())/mean))
        scores[key]=score
    return sorted(scores,key=lambda k:(-scores[k],k))


if __name__=="__main__":
    root=Path(__file__).resolve().parent
    fix=json.loads((root/"starliner_desk_fixture.json").read_text(encoding="utf-8"))
    packet=json.loads((root/fix["packet"]).read_text(encoding="utf-8"))
    for release in packet[1:]:
        for row in fix["story"]:
            order=rank(row["text"],release["passages"])
            print(release["date"],row["id"]," ".join(order))
    for release, sentence, proposal in zip(packet[1:],fix["story"][:2],fix["proposals"]):
        expected=set(proposal["refs"])
        lead=list(release["passages"])[:2]
        lexical=rank(sentence["text"],release["passages"])[:2]
        print("fixed two-paragraph budget",release["date"],{
            "lead": [lead,len(set(lead)&expected),len(expected)],
            "bm25": [lexical,len(set(lexical)&expected),len(expected)]})
