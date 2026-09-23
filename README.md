COINTRACE — AI-POWERED CRYPTOCURRENCY TRANSACTION RISK ANALYSIS

Smart India Hackathon 2026 — Problem Statement 26146


LIVE DEMO

https://cointrace-hazel.vercel.app/


PROBLEM

Cryptocurrency transactions can generate large volumes of data that are difficult to investigate manually.

Investigators may need to:

• Analyze large transaction datasets
• Identify unusual transaction behaviour
• Detect suspicious transaction patterns
• Prioritize potentially high-risk activity
• Understand the signals behind a detected anomaly

CoinTrace provides an automated analysis workflow that helps transform raw transaction data into investigation-oriented insights.


SOLUTION

CoinTrace accepts transaction data in CSV format and processes it through a machine-learning pipeline.

The system performs:

• Data parsing and validation
• Transaction feature engineering
• Machine-learning based anomaly detection
• Anomaly score generation
• Risk severity classification
• Priority alert generation
• Explainable analysis
• Interactive dashboard visualization


CORE WORKFLOW

Transaction CSV
       ↓
JSON Records
       ↓
Feature Engineering
       ↓
Isolation Forest
       ↓
Anomaly Score
       ↓
Risk Severity
       ↓
Explanation
       ↓
Investigation Dashboard


MACHINE LEARNING

CoinTrace uses an unsupervised anomaly-detection model based on Scikit-learn's Isolation Forest.

MODEL CONFIGURATION

Model: sklearn.ensemble.IsolationForest
Isolation Trees: 200
Random State: 26146
Contamination: 0.16

The model analyzes transaction and network/entity characteristics to identify behaviour that differs from the learned reference distribution.

FEATURE INDEPENDENCE

The following fields are not provided to the machine-learning model as input features:

• risk_score
• risk_level
• ground_truth
• Synthetic pattern labels

This prevents the model from directly learning predefined risk labels instead of detecting behavioural anomalies.


FEATURE ENGINEERING

CoinTrace derives transaction, network, and entity-level signals from the input data.

The ML pipeline uses 11 engineered transaction/network/entity features.

These features are used by the Isolation Forest model to identify unusual behavioural patterns.

The feature-engineering layer converts raw transaction records into the numerical representation required by the anomaly-detection model.


RISK ANALYSIS

After ML inference, CoinTrace converts anomaly information into investigation-oriented results.

PRIORITY ALERTS

Highlights transactions requiring attention and allows investigators to focus on potentially suspicious activity.

RISK CLASSIFICATION

Transactions are classified into risk-severity categories such as:

• High Risk
• Medium Risk
• Low Risk

EXPLAINABLE ANALYSIS

CoinTrace provides contextual explanations associated with detected signals instead of displaying only a numerical model output.

This makes the results easier to interpret during investigation.


INVESTIGATION DASHBOARD

The dashboard provides an interactive view of the analyzed transaction dataset.

Key areas include:

• Transaction overview
• Risk distribution
• Priority alerts
• Detection signals
• Explainable analysis
• Transaction-level information
• Interactive visualizations
• Investigation-oriented summaries

The objective is to turn raw transaction records into a more accessible investigation interface.


SYSTEM ARCHITECTURE

                         ┌──────────────────────┐
                         │   Transaction CSV    │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │   JSON Records       │
                         │   & Validation       │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │ Feature Engineering  │
                         │ 11 ML Features       │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │   Isolation Forest   │
                         │    200 Trees         │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │    Anomaly Score     │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │ Risk Severity &      │
                         │ Explainable Signals  │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │ Investigation        │
                         │ Dashboard            │
                         └──────────────────────┘


TECHNOLOGY STACK

FRONTEND

• HTML5
• CSS3
• JavaScript
• Interactive dashboard interface
• Data visualization

BACKEND

• Python
• FastAPI

MACHINE LEARNING

• Scikit-learn
• Isolation Forest
• Feature engineering
• Unsupervised anomaly detection

DATA

• CSV transaction data
• Synthetic CoinTrace reference dataset

DEPLOYMENT

• Vercel
• Python Functions
• FastAPI


PROJECT STRUCTURE

Cointrace/
│
├── api/
│   └── analyze.py
│
├── index.html
├── all.js
├── cointrace_sih26146_risk_aware_dataset.csv
├── requirements.txt
├── vercel.json
└── README.md


BACKEND API

The machine-learning inference service is implemented using FastAPI.

ENDPOINT

POST /api/analyze

The endpoint receives transaction data, performs feature engineering and ML inference, and returns the analysis results used by the frontend dashboard.

The frontend communicates with the API using the same-origin /api/analyze route.

Because the frontend and Python service are deployed as part of the same Vercel project, a separate backend URL or CORS configuration is not required for the deployed application.


LOCAL SETUP

1. CLONE THE REPOSITORY

git clone https://github.com/realanshdev/Cointrace.git
cd Cointrace


2. INSTALL DEPENDENCIES

python -m pip install -r requirements.txt


3. RUN LOCALLY WITH VERCEL

vercel dev

After the development server starts, open the local Vercel URL in your browser.

Do not open index.html directly because the dashboard requires the Python ML API.


DATASET

CoinTrace includes a synthetic risk-aware reference dataset for demonstration and testing.

The dataset is used by the Python ML service during startup to train the Isolation Forest model.

The system can also analyze uploaded transaction CSV files through the dashboard.

DATASET PROCESSING

CSV Dataset
     ↓
Record Parsing
     ↓
Feature Engineering
     ↓
Isolation Forest
     ↓
Anomaly Detection
     ↓
Risk Analysis
     ↓
Dashboard


OFFLINE AND SIH DEMONSTRATION

The machine-learning model and feature-engineering pipeline execute inside the Python runtime.

The core analysis does not require:

• Blockchain APIs
• Cloud AI services
• External transaction lookup services
• Cryptocurrency wallet credentials
• Private keys

The included synthetic dataset allows the complete ML workflow to be demonstrated without requiring live blockchain data.

Vercel deployment provides the web-based demonstration, while the same FastAPI application can be run locally for an offline demonstration.


PRIVACY AND SECURITY

CoinTrace is designed as an analysis and investigation prototype.

The application does not require:

• Cryptocurrency wallet credentials
• Private keys
• Exchange login credentials
• Blockchain wallet access

The bundled dataset is synthetic and intended for demonstration purposes.


DEPLOYMENT

CoinTrace is designed to run as a single Vercel project.

                  CoinTrace
                      │
          ┌───────────┴───────────┐
          │                       │
          ▼                       ▼
   Static Frontend          Python API
   HTML/CSS/JS             FastAPI
                                  │
                                  ▼
                         Machine Learning
                         Isolation Forest

The frontend communicates with:

/api/analyze

This same-origin architecture keeps the frontend and ML service within the same deployed application.


LIMITATIONS

CoinTrace is currently a Smart India Hackathon prototype.

The current implementation demonstrates the machine-learning and investigation workflow using a synthetic reference dataset and uploaded transaction data.

For a production-grade deployment, the platform could be extended with:

• Live blockchain data ingestion
• Blockchain node or indexer integration
• Graph-based transaction analysis
• Entity clustering
• Wallet and address intelligence
• Historical behavioural profiling
• Continuous model monitoring
• Automated model retraining
• Investigator authentication
• Case management
• Audit logging
• Large-scale distributed processing


FUTURE SCOPE

REAL-TIME BLOCKCHAIN MONITORING

Integrate blockchain data sources to continuously monitor new transactions.

GRAPH-BASED INVESTIGATION

Represent transactions and entities as graphs to identify complex money-flow relationships.

ADVANCED MACHINE LEARNING

Explore additional approaches such as:

• Autoencoders
• Graph Neural Networks
• Clustering
• Temporal anomaly detection
• Ensemble anomaly-detection models

INVESTIGATOR COLLABORATION

Future versions can include:

• Case creation
• Evidence management
• Investigator notes
• Audit trails
• Report generation

SCALABLE ARCHITECTURE

The system can be extended from prototype-scale processing to distributed transaction analysis capable of handling significantly larger datasets.


SIH CONTEXT

Event: Smart India Hackathon 2026

Problem Statement: 26146

Project: CoinTrace

CoinTrace demonstrates how machine learning and explainable analytics can be combined to assist cryptocurrency transaction investigation and risk prioritization.


AUTHOR

Ansh Shukla

Built for Smart India Hackathon 2026.


DISCLAIMER

CoinTrace is an educational and hackathon prototype.

Risk classifications and anomaly scores generated by the system should be treated as investigation-support signals and not as definitive evidence of financial crime or malicious activity.
