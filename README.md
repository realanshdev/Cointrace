# CoinTrace — SIH 26146

CoinTrace is a Vercel-ready investigation dashboard with a **real Python/scikit-learn Isolation Forest ML service**.

## Actual ML model

- Model: `sklearn.ensemble.IsolationForest`
- 200 isolation trees
- deterministic `random_state=26146`
- contamination: 0.16
- 11 transaction/network/entity features
- trained on the bundled synthetic CoinTrace reference dataset at Python function startup
- inference is performed by the Python `/api/analyze` endpoint
- the model never receives `risk_score`, `risk_level`, `ground_truth`, or synthetic pattern labels as features

Pipeline:

`CSV → JSON records → feature engineering → sklearn IsolationForest → anomaly score → severity → explanation → dashboard/graph`

## Vercel

Vercel serves the static frontend and Python API from the same project. Vercel's current Python deployment model supports Python functions under `api/`; this project uses FastAPI in `api/analyze.py`. citeturn0search3

Deploy with Vercel from this folder. The frontend calls the same-origin `/api/analyze` route, so no separate backend URL or CORS setup is required.

## Local

```bash
python -m pip install -r requirements.txt
vercel dev
```

Then open the local Vercel URL and load a CSV. Do not open `index.html` directly because the real ML API is required.

## Offline / SIH note

The ML model and feature engineering execute locally inside the Python runtime when the project is run locally. No blockchain API, cloud AI service, or external transaction lookup is required. Vercel deployment is for the web demo; for a fully offline Linux demo, run the same FastAPI application locally with the included dependencies.
