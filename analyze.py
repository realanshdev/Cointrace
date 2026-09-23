import json, math, os
from collections import Counter
import numpy as np
from sklearn.ensemble import IsolationForest


def arr(v):
    if isinstance(v, list): return v
    try: return json.loads(v) if v else []
    except Exception: return []


def feature_rows(records):
    ip_freq = Counter(str(r.get('src_ip','')) for r in records)
    country_freq = Counter(str(r.get('country','Unknown')) for r in records)
    wallet_freq = Counter()
    parsed=[]
    for r in records:
        ins=arr(r.get('input_addresses')); outs=arr(r.get('output_addresses'))
        wallet_freq.update(ins); wallet_freq.update(outs)
        parsed.append((r,ins,outs))
    X=[]
    for r,ins,outs in parsed:
        try: ts=float(__import__('datetime').datetime.fromisoformat(str(r.get('timestamp','')).replace('Z','+00:00')).timestamp())
        except: ts=0
        import datetime
        d=datetime.datetime.fromtimestamp(ts, datetime.timezone.utc)
        hour=d.hour; dow=d.weekday()
        amounts=arr(r.get('output_amounts'))
        in_amounts=arr(r.get('input_amounts'))
        amount=sum(float(x or 0) for x in amounts) or sum(float(x or 0) for x in in_amounts)
        fee=float(r.get('fee') or 0)
        src_port=float(r.get('src_port') or 0)
        X.append([
            math.log1p(max(0,amount)), math.log1p(max(0,fee)*10000),
            math.log1p(max(1,len(ins))), math.log1p(max(1,len(outs))),
            math.log1p(ip_freq[str(r.get('src_ip',''))]), math.log1p(wallet_freq[ins[0]] if ins else 1),
            math.log1p(country_freq[str(r.get('country','Unknown'))]), src_port,
            math.sin(hour/24*math.pi*2), math.cos(hour/24*math.pi*2), dow
        ])
    return np.asarray(X,dtype=float), parsed


def train_reference():
    path=os.path.join(os.path.dirname(os.path.dirname(__file__)),'cointrace_sih26146_risk_aware_dataset.csv')
    import csv
    with open(path,newline='',encoding='utf-8') as f: records=list(csv.DictReader(f))
    X,_=feature_rows(records)
    model=IsolationForest(n_estimators=200, contamination=0.16, random_state=26146, n_jobs=1, max_samples=min(256,len(X)))
    model.fit(X)
    s=model.decision_function(X)
    return model, float(np.percentile(s,2)), float(np.percentile(s,98))

MODEL, CAL_LOW, CAL_HIGH = train_reference()


from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="CoinTrace ML API", version="1.0")

class AnalyzeRequest(BaseModel):
    records: list[dict]

@app.get("/api/health")
def health():
    return {"ok": True, "service": "CoinTrace ML API", "model": "sklearn IsolationForest"}

@app.post("/api/analyze")
def analyze(payload: AnalyzeRequest):
    try:
        records=payload.records
        if not isinstance(records,list) or not records:
            raise HTTPException(status_code=400, detail="records must be a non-empty array")
        X,parsed=feature_rows(records)
        decision=MODEL.decision_function(X)
        preds=MODEL.predict(X)
        # Lower Isolation Forest decision scores are more anomalous.
        scores=np.clip((CAL_HIGH-decision)/(CAL_HIGH-CAL_LOW)*100,0,100)
        out=[]
        for i,(r,ins,outs) in enumerate(parsed):
            ip=str(r.get('src_ip','')); country=str(r.get('country','Unknown'))
            amount=sum(float(x or 0) for x in arr(r.get('output_amounts'))) or sum(float(x or 0) for x in arr(r.get('input_amounts')))
            score=int(round(float(scores[i])))
            severity='High' if preds[i] == -1 else ('Medium' if score >= 40 else 'Low')
            clues=[]
            if sum(1 for rr in records if str(rr.get('src_ip',''))==ip)>=4: clues.append('IP reuse')
            if len(outs)>=4: clues.append('fan-out')
            if len(ins)>=4: clues.append('fan-in')
            if amount>=5: clues.append('large amount')
            reason='ML anomaly · '+' + '.join(clues[:2]) if clues else 'ML anomaly score'
            out.append({**r,
                'mlScore':score,'riskScore':score,'anomaly':score,'severity':severity,
                'mlRawScore':round(float(decision[i]),6),'mlModel':'sklearn IsolationForest',
                'mlFeatures':{'amount':amount,'inputs':len(ins) or 1,'outputs':len(outs) or 1,
                              'ipReuse':sum(1 for rr in records if str(rr.get('src_ip',''))==ip),
                              'walletReuse':1,'fee':float(r.get('fee') or 0)},
                'mlExplanation':('Isolation Forest marked this transaction anomalous from its multivariate feature vector.' if preds[i]==-1 else 'Isolation Forest found this transaction close to the learned reference population.'),
                'reason':reason,'signalDesc':('Isolation Forest anomaly score from 11 transaction/network/entity features.'),
                'signalBasis':'sklearn Isolation Forest feature space','pattern':'ML-derived'
            })
        return {'ok':True,'model':{'name':'sklearn IsolationForest','estimators':200,'features':11,'trained_on':'CoinTrace synthetic reference dataset','contamination':0.16},'rows':out}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
