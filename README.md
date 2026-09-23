CoinTrace

AI-Powered Cryptocurrency Transaction Risk Analysis

Smart India Hackathon 2026 — Problem Statement 26146

CoinTrace is an AI-powered cryptocurrency transaction risk analysis platform designed to identify suspicious transaction patterns, classify transaction risk, and generate explainable priority alerts through an interactive investigation dashboard.

The system combines machine learning, transaction feature engineering, risk analysis, and explainable alerts into a single web-based platform.

Live Demo

https://cointrace-hazel.vercel.app/

Problem

Cryptocurrency transactions generate large volumes of data that can be difficult to manually investigate.

Traditional investigation workflows may require analysts to:
1-Examine large transaction datasets

2-Identify unusual transaction behaviour

3-Detect suspicious entities and patterns

4-Prioritize high-risk transactions

5-Understand why a transaction was flagged
CoinTrace addresses this challenge by providing an automated risk-analysis workflow that helps investigators focus on transactions requiring greater attention.

Solution

CoinTrace processes transaction data through a machine-learning pipeline and converts raw transaction information into actionable investigation insights.

Core Workflow

Transaction CSV
       ↓
Data Validation
       ↓
Feature Engineering
       ↓
Machine Learning Model
       ↓
Anomaly Detection
       ↓
Risk Classification
       ↓
Priority Alerts
       ↓
Explainable Investigation Dashboard

Machine Learning

CoinTrace uses an unsupervised anomaly-detection approach based on Isolation Forest.

Model Configuration

Model: sklearn.ensemble.IsolationForest
Trees: 200
Random State: 26146
Contamination: 0.16

The model analyzes transaction and network/entity characteristics to identify behaviour that deviates from normal transaction patterns.

Feature Independence

The ML model does not use the following fields as input features
1-risk_score

2-risk_level

3-Ground-truth labels

4-Synthetic pattern labels
This prevents the model from simply learning predefined risk categories instead of detecting anomalous behaviour.

Feature Engineering

The system extracts transaction and entity-level signals from the input dataset.

Example feature categories include:
1-Transaction amount

2-Transaction frequency

3-Incoming/outgoing behaviour

4-Entity activity

5-Network characteristics

6-Transaction velocity

7-Behavioural patterns

8-Counterparty-related signals

These engineered features are supplied to the Isolation Forest model for anomaly detection.

Risk Analysis

Priority Alerts

Highlights transactions requiring attention and helps investigators focus on higher-risk activity first.

Risk Classification

Transactions are categorized into different risk levels such as:

1-High Risk

2-Medium Risk

3-Low Risk

Explainable Analysis

Instead of showing only a numerical prediction, CoinTrace provides contextual explanations describing the signals associated with a suspicious transaction.

Investigation Dashboard

CoinTrace provides an interactive dashboard containing:

1-Transaction overview

2-Risk distribution

3-Priority alerts

4-Detection signals

5-Explainable analysis

6-Transaction-level information

7-Visual analytics

8-Investigation-oriented summaries

The goal is to convert raw transaction records into an interface that can be understood quickly by an investigator.

System Architecture

                    ┌─────────────────────┐
                    │   Transaction CSV   │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Data Validation &   │
                    │ Feature Engineering │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │  Isolation Forest   │
                    │   ML Anomaly Model  │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Anomaly Score &     │
                    │ Risk Classification │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Priority Alerts &   │
                    │ Explainable Signals │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Investigation       │
                    │ Dashboard           │
                    └─────────────────────┘

Technology Stack

Frontend

•HTML5

•CSS3

•JavaScript

•Interactive dashboard components

•Data visualization

Backend

•Python

•FastAPI

•Machine Learning

•Scikit-learn

•Isolation Forest

•Feature engineering

•Anomaly detection

Data

•CSV-based transaction datasets

•Synthetic risk-aware reference dataset

Deployment

•Vercel

•Python Serverless Functions

Project Structure

Cointrace/
│
├── analyze.py
├── index.html
├── all.js
├── cointrace_sih26146_risk_aware_dataset.csv
├── requirements.txt
├── vercel.json
├── README.md
└── .gitignore

Local Setup

1. Clone the Repository

git clone https://github.com/realanshdev/Cointrace.git
cd Cointrace

2. Install Python Dependencies

python -m pip install -r requirements.txt

3. Run Using Vercel CLI

vercel dev

The frontend communicates with the Python ML analysis service through:

/api/analyze

Do not open index.html directly because the ML analysis requires the backend service.

Dataset

CoinTrace includes a synthetic risk-aware transaction dataset for demonstration and testing.

The dataset is designed to contain different transaction behaviours and risk patterns that allow the ML pipeline and dashboard to be demonstrated without depending on external blockchain APIs.

Dataset Workflow

CSV
 ↓
Validation
 ↓
Feature Extraction
 ↓
ML Inference
 ↓
Risk Analysis
 ↓
Dashboard

Privacy and Security

CoinTrace is designed as an analysis and investigation prototype.

The system:

Does not require cryptocurrency wallet credentials

Does not require private keys

Does not require exchange login credentials

Does not require blockchain wallet access

Does not require external transaction lookup services for the bundled demonstration dataset

The included dataset is synthetic and intended for demonstration purposes.

Deployment

CoinTrace can be deployed as a single Vercel project containing:

Frontend
   +
Python ML Analysis Service
   +
Machine Learning Pipeline

The frontend communicates with the ML analysis service through:

/api/analyze

This allows the frontend and backend functionality to be deployed as part of the same project.

Limitations

CoinTrace is currently a Smart India Hackathon prototype.

The current implementation primarily demonstrates the machine-learning and investigation workflow using synthetic/reference transaction data.

For a production-grade deployment, the system could be extended with:

Live blockchain data ingestion

Blockchain node/indexer integration

Graph-based transaction analysis

Entity clustering

Wallet/address intelligence

Historical behavioural profiling

Model monitoring and retraining

Role-based investigator access

Case management

Audit logging

Large-scale distributed processing

Future Scope

1. Real-Time Blockchain Monitoring

Integrate blockchain data sources to continuously monitor new transactions.

2. Graph-Based Investigation

Represent transactions and entities as graphs to identify complex money-flow relationships.

3. Advanced ML Models

Explore additional approaches such as autoencoders, graph neural networks, clustering, temporal anomaly detection, and ensemble models.

4. Investigator Collaboration

Add case creation, evidence management, investigator notes, audit trails, and report generation.

5. Scalable Architecture

Move from prototype-scale processing toward distributed transaction analysis capable of handling significantly larger datasets.

SIH Context

Event: Smart India Hackathon 2026

Problem Statement: 26146

Project: CoinTrace

CoinTrace demonstrates how machine learning and explainable analytics can be combined to assist cryptocurrency transaction investigation and risk prioritization.

Author

Ansh Shukla

Built for Smart India Hackathon 2026.

Disclaimer

CoinTrace is an educational and hackathon prototype.

Risk classifications and anomaly scores generated by the system should be treated as investigation-support signals, not as definitive evidence of financial crime or malicious activity.
