# Customer Segmentation & Targeting System

An end-to-end data product that ingests retail transactions, engineers RFM features,
clusters customers, generates business insights, and exposes an interactive dashboard.

## Architecture
- Data Ingestion → Preprocessing → Feature Engineering (RFM) → Clustering & Evaluation → Insights → Streamlit Dashboard

```mermaid
flowchart LR
  A[Raw Retail Data (CSV/XLSX)] --> B[Preprocess & Clean]
  B --> C[Feature Engineering (RFM, totals)]
  C --> D[Clustering (KMeans)]
  D --> E[Evaluation & Labeling]
  E --> F[Insights Report]
  E --> G[Streamlit Dashboard]
```

## Quickstart

```bash
# 1) Create environment
python -m venv .venv
source .venv/bin/activate  # on Windows: .venv\Scripts\activate

# 2) Install deps
pip install -r deployment/requirements.txt

# 3) Run dashboard
streamlit run dashboard/app.py
```

Upload the **Online Retail** dataset (CSV or XLSX) from UCI during runtime.

## Project Layout
```
customer-segmentation-project/
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
│   ├── EDA.ipynb
│   └── Model_Experiments.ipynb
├── src/
│   ├── data_ingest.py
│   ├── preprocess.py
│   ├── feature_engineering.py
│   ├── clustering.py
│   ├── evaluate.py
│   ├── insights.py
│   ├── utils.py
│   └── __init__.py
├── dashboard/
│   └── app.py
├── deployment/
│   ├── requirements.txt
│   └── Dockerfile
├── tests/
│   ├── test_preprocess.py
│   ├── test_feature_engineering.py
│   └── test_clustering.py
├── docs/
│   ├── architecture.md
│   ├── data_dictionary.md
│   └── usage_guide.md
├── .github/workflows/
│   └── ci.yml
├── .gitignore
├── LICENSE
└── README.md
```

## Notes
- The app produces a downloadable CSV of customer → cluster label.
- Replace the demo heuristics in `insights.py` with business-specific rules when you have domain inputs.
