---

# 🧠 Customer Segmentation & Targeting System

**An End-to-End Machine Learning Pipeline for Retail Customer Analytics**

![Project Overview Banner](docs/screenshots/overview.png)

---

## 🚀 Overview

This project automates **customer segmentation** using **unsupervised machine learning** to help retailers identify high-value customers, re-engage dormant ones, and optimize marketing strategies.

Built entirely in **Python**, this pipeline ingests raw transactional data → cleans and engineers features (RFM metrics) → clusters customers using **KMeans** → labels segments with business-friendly names → and exposes results through an interactive **Streamlit dashboard**.

This is a **production-style, end-to-end data science project** built for real-world deployment — complete with modular code, tests, Docker, and CI/CD.

---

## 🎯 Business Objective

Retailers often spend heavily on marketing without understanding **which customers are worth targeting**.
This project provides a data-driven segmentation system that enables:

* 🎯 **Personalized marketing** for different customer segments
* 💰 **Reduced customer churn** by identifying “At Risk” users early
* 📈 **Increased retention** by focusing on loyal and high-value customers
* 🔄 **Automated updates** for continuous segmentation refresh

---

## 🧾 Dataset

**Source:** [UCI Machine Learning Repository – Online Retail Dataset](https://archive.ics.uci.edu/ml/datasets/Online+Retail)
**Description:** 541,909 transactions from a UK-based online retailer between Dec 2010–Dec 2011.

| Column      | Description                 |
| ----------- | --------------------------- |
| InvoiceNo   | Unique invoice number       |
| StockCode   | Product code                |
| Description | Product name                |
| Quantity    | Quantity of product ordered |
| InvoiceDate | Date of transaction         |
| UnitPrice   | Price per unit              |
| CustomerID  | Unique customer identifier  |
| Country     | Country of customer         |

> If the dataset isn’t included, it can be auto-downloaded using
> `python src/data_download.py`

---

## ⚙️ Tech Stack

| Category             | Tools / Libraries           |
| -------------------- | --------------------------- |
| **Language**         | Python 3.11                 |
| **Data Handling**    | pandas, numpy               |
| **Modeling**         | scikit-learn                |
| **Visualization**    | matplotlib, seaborn, plotly |
| **Dashboard**        | Streamlit                   |
| **Testing**          | pytest                      |
| **Containerization** | Docker                      |
| **Automation / CI**  | GitHub Actions              |
| **Version Control**  | Git + GitHub                |

---

## 🧩 Project Architecture

```
                ┌─────────────────────────┐
                │ Raw Retail Data (CSV)   │
                └──────────┬──────────────┘
                           │
             ┌─────────────▼─────────────┐
             │ Data Cleaning & Validation│
             └─────────────┬─────────────┘
                           │
             ┌─────────────▼─────────────┐
             │ RFM Feature Engineering   │
             └─────────────┬─────────────┘
                           │
             ┌─────────────▼─────────────┐
             │ KMeans Clustering + Eval  │
             └─────────────┬─────────────┘
                           │
             ┌─────────────▼─────────────┐
             │ Segment Labeling & Insights│
             └─────────────┬─────────────┘
                           │
             ┌─────────────▼─────────────┐
             │ Streamlit Dashboard / API │
             └───────────────────────────┘
```

---

## 📂 Repository Structure

```
customer-segmentation-project/
├── data/
│   ├── raw/                <- Original dataset (Online_Retail.xlsx)
│   ├── processed/          <- Cleaned/feature-engineered data
│
├── notebooks/
│   ├── EDA_and_Modeling.ipynb  <- Exploratory & model development
│
├── src/
│   ├── data_ingest.py          <- Load raw data
│   ├── preprocess.py           <- Clean transactional data
│   ├── feature_engineering.py  <- Create RFM metrics
│   ├── clustering.py           <- Run KMeans, save model
│   ├── evaluate.py             <- Evaluate clustering
│   ├── insights.py             <- Label segments + actions
│   ├── utils.py                <- Helpers & logging
│
├── dashboard/
│   └── app.py                  <- Streamlit web app
│
├── tests/                      <- Unit tests
├── deployment/                 <- Docker + requirements
├── docs/                       <- Architecture, data dictionary, screenshots
└── README.md
```

---

## 🖥️ Streamlit Dashboard

**Launch locally:**

```bash
streamlit run dashboard/app.py
```

Then open [http://localhost:8501](http://localhost:8501)

![Dashboard Screenshot](docs/screenshots/dashboard.png)

### Key Features:

* Upload CSV/XLSX file of transactions
* Choose number of clusters (`k`) dynamically
* View inertia & silhouette metrics
* Inspect RFM values per segment
* Download labeled customer segment file (`customer_segments.csv`)

---

## 📊 Example Results

| Metric           | Value        |
| ---------------- | ------------ |
| Optimal k        | 4            |
| Silhouette Score | 0.63         |
| Inertia          | 18,530.42    |
| Dataset Size     | 541,909 rows |

**Segment Distribution Example:**

| Segment   | % of Customers | Avg Recency | Avg Frequency | Avg Monetary | Strategy                      |
| --------- | -------------- | ----------- | ------------- | ------------ | ----------------------------- |
| Champions | 14%            | 10 days     | 12            | £1500        | VIP programs, loyalty rewards |
| Loyal     | 25%            | 22 days     | 8             | £980         | Upsell premium items          |
| At Risk   | 18%            | 110 days    | 5             | £620         | Win-back emails               |
| Low Value | 43%            | 240 days    | 2             | £200         | Discount campaigns            |

![Cluster Visualization](docs/screenshots/clusters.png)

---

## 🧪 Evaluation Metrics

| Metric                | Description                                    |
| --------------------- | ---------------------------------------------- |
| **Inertia**           | Within-cluster sum of squares (lower = better) |
| **Silhouette Score**  | Cluster separation metric (−1 → 1)             |
| **Elbow Plot**        | Helps select optimal k                         |
| **Cluster Profiling** | Mean R/F/M values per segment                  |

![Elbow Plot](docs/screenshots/elbow_plot.png)

---

## 🧠 Insights & Business Recommendations

| Segment       | Description                 | Recommended Actions           |
| ------------- | --------------------------- | ----------------------------- |
| **Champions** | Frequent, high-value buyers | Early access, loyalty perks   |
| **Loyal**     | Consistent spenders         | Upsell complementary products |
| **At Risk**   | Haven’t purchased recently  | Win-back campaigns            |
| **Low Value** | Low frequency and spend     | Awareness offers              |
| **Regulars**  | Moderate value              | Personalized recommendations  |

---

## 🧰 Run the Project Locally

### 1️⃣ Create Environment

```bash
python -m venv .venv
.venv\Scripts\activate   # (Windows)
# or
source .venv/bin/activate  # (macOS/Linux)
```

### 2️⃣ Install Dependencies

```bash
pip install -r deployment/requirements.txt
```

### 3️⃣ Run Tests

```bash
pytest -q
```

### 4️⃣ Launch the Dashboard

```bash
streamlit run dashboard/app.py
```

---

## 🐳 Run via Docker (Optional)

```bash
docker build -t customer-segmentation .
docker run -p 8501:8501 customer-segmentation
```

Then visit [http://localhost:8501](http://localhost:8501)

---

## 🧱 CI/CD Workflow

The repo includes a basic **GitHub Actions** workflow (`.github/workflows/ci.yml`) that:

* Installs dependencies
* Runs unit tests
* Validates build
  You can extend this to deploy automatically on Streamlit Cloud or Render.

---

## 🔮 Future Enhancements

* Integrate **PostgreSQL/SQLite** for persistent data storage
* Add **FastAPI microservice** for online segment prediction
* Build **automated retraining pipeline** (Airflow/Prefect)
* Add **drift monitoring** for segment stability
* Extend to **DBSCAN / GMM** clustering for flexible segments
* Deploy on **AWS / GCP / Azure**

---

## 👤 Author

**Manjit Singh**
📧 itsmanjit20@gmail.com
💼 [GitHub Profile](https://github.com/ManjitSingh2003)

---

## 📜 License

Licensed under the **MIT License**.
Dataset © UCI Machine Learning Repository, used for non-commercial research purposes.

---

## 🌟 Acknowledgements

* [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Online+Retail) for dataset
* [Streamlit](https://streamlit.io) for dashboarding
* [scikit-learn](https://scikit-learn.org/) for clustering tools
* [pandas](https://pandas.pydata.org/) & [numpy](https://numpy.org/) for data manipulation

---
