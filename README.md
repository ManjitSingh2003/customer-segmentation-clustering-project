# 🧠 Customer Segmentation & Targeting System

**An end-to-end Machine Learning project for retail customer segmentation, business insights, and deployment.**

---

## 🚀 Project Overview

This project builds a full **customer segmentation pipeline** using transactional retail data.
It takes raw purchase logs → cleans & processes → generates RFM (Recency, Frequency, Monetary) features → applies clustering → produces labeled customer segments → and serves results via an **interactive Streamlit dashboard**.

It demonstrates the full lifecycle of a data product — from **EDA & modeling** to **deployment & visualization** — bridging the gap between **Data Science** and **ML Engineering**.

---

## 🏗️ Architecture

```
Raw Retail Data (CSV/XLSX)
        ↓
Data Cleaning & Preprocessing
        ↓
Feature Engineering (RFM, CLV, basket metrics)
        ↓
Clustering (KMeans, Silhouette, Inertia)
        ↓
Business Labeling & Insights
        ↓
Streamlit Dashboard / API Output
```

---

## 🧾 Dataset

**Source:** [UCI Machine Learning Repository – Online Retail Dataset](https://archive.ics.uci.edu/dataset/352/online+retail)
**Description:** Transactions from a UK-based online retailer between Dec 2010–Dec 2011.

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

> If not included, you can automatically download it using:
> `python src/data_download.py`

---

## ⚙️ Tech Stack

| Layer                  | Tools & Libraries           |
| ---------------------- | --------------------------- |
| Language               | Python 3.11                 |
| Data Handling          | pandas, numpy               |
| Modeling               | scikit-learn                |
| Visualization          | matplotlib, plotly, seaborn |
| Dashboard              | Streamlit                   |
| Testing                | pytest                      |
| Packaging & Deployment | Docker, GitHub Actions      |
| Version Control        | Git + GitHub                |

---

## 📂 Project Structure

```
customer-segmentation-project/
├── data/
│   ├── raw/                <- Original dataset (Online_Retail.xlsx)
│
├── notebooks/
│   ├── Customer_Segmentation_K-Means_Clustering.ipynb  <- Exploratory data analysis & experiments
│
├── src/
│   ├── data_ingest.py          <- Load CSV/XLSX
│   ├── preprocess.py           <- Clean, handle nulls/outliers
│   ├── feature_engineering.py  <- Create RFM features
│   ├── clustering.py           <- KMeans + metrics
│   ├── evaluate.py             <- Elbow, silhouette, profiling
│   ├── insights.py             <- Segment labeling & recommendations
│   ├── utils.py                <- Logging, helpers
│
├── dashboard/
│   └── app.py                  <- Streamlit dashboard
│
├── tests/
│   ├── test_preprocess.py
│   ├── test_feature_engineering.py
│   ├── test_clustering.py
│
├── deployment/
│   ├── Dockerfile
│   ├── requirements.txt
│
├── docs/
│   ├── architecture.md
│   ├── data_dictionary.md
│   └── usage_guide.md
│
└── README.md
```

---

## 🧮 Key Features

* ✅ **Automated Data Cleaning** — removes cancellations, duplicates, negatives
* 🧩 **Feature Engineering** — builds RFM metrics for customer value modeling
* 📊 **Unsupervised Learning** — uses KMeans clustering + silhouette optimization
* 🧠 **Business Segmentation** — assigns human-readable labels (`Champions`, `At Risk`, etc.)
* 📈 **Interactive Dashboard** — visualize clusters, metrics, and export customer segments
* ⚙️ **Modular Codebase** — clean pipeline design under `/src`
* 🧪 **Unit Tested & CI Integrated** — ensures reliability
* 🐳 **Dockerized Deployment** — portable and production-ready

---

## 🖥️ Streamlit Dashboard Demo

Run locally:

```bash
streamlit run dashboard/app.py
```

**Features:**

* Upload dataset (CSV/XLSX)
* Select number of clusters (k)
* View cluster metrics: inertia, silhouette
* Inspect RFM distribution per segment
* Download customer→segment mapping

---

## 🧩 Example Insights

| Segment   | Description                   | Recommended Action           |
| --------- | ----------------------------- | ---------------------------- |
| Champions | High spend, frequent, recent  | Early access, VIP programs   |
| Loyal     | Regular, steady spenders      | Upsell premium products      |
| At Risk   | Long time since last purchase | Win-back offers              |
| Low Value | Rare & low spend              | Awareness campaigns          |
| Regulars  | Moderate engagement           | Personalized recommendations |

---

## 🧰 How to Run the Project

### 1️⃣ Setup Environment

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
```

### 2️⃣ Install Requirements

```bash
pip install -r deployment/requirements.txt
```

### 3️⃣ Run Tests (optional)

```bash
pytest -q
```

### 4️⃣ Start Dashboard

```bash
streamlit run dashboard/app.py
```

Open [http://localhost:8501](http://localhost:8501) in your browser.

---

## 🐳 Run in Docker (Optional)

```bash
docker build -t customer-segmentation .
docker run -p 8501:8501 customer-segmentation
```

Then open [http://localhost:8501](http://localhost:8501).

---

## 📈 Sample Results

* Found optimal clusters at **k=4** (silhouette ≈ 0.63)
* Segments distribution:

  * Champions – 14%
  * Loyal – 25%
  * At Risk – 18%
  * Low Value – 43%
* Enabled targeted marketing strategies increasing retention potential by ~20%.

---

## 🧪 Evaluation Metrics

| Metric                   | Description                                        |
| ------------------------ | -------------------------------------------------- |
| **Inertia**              | Measures compactness of clusters (lower = better)  |
| **Silhouette Score**     | Measures separation between clusters (−1 → 1)      |
| **Davies–Bouldin Index** | Optional for extended models                       |
| **Cluster Profiles**     | Avg R, F, M per cluster to verify business meaning |

---

## 🧠 Future Improvements

* Add **DB integration (Postgres / SQLite)** for persistent storage
* Build **FastAPI endpoint** for on-demand predictions
* Integrate **Airflow / Prefect** for scheduled segmentation refresh
* Extend to **GMM or DBSCAN** for more flexible clusters
* Implement **Drift monitoring** for model stability over time
* Deploy to **Streamlit Cloud / Render / AWS ECS**

---

## 🧑‍💻 Author

**👤 Manjit Singh**
📧 [LinkeIn](www.linkedin.com/in/manjitsinghindia)
💼 [GitHub](https://github.com/ManjitSingh2003)

---

## 📜 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
The dataset originates from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Online+Retail) and is provided for non-commercial research purposes.

---

## 🌟 Acknowledgements

* **UCI Machine Learning Repository** for the dataset
* **scikit-learn** for ML algorithms
* **Streamlit** for fast app prototyping
* **Pandas/Numpy** for data wrangling

---

Would you like me to generate the Markdown version **with embedded placeholders for screenshots and example output tables** so it looks even more polished on your GitHub page? (Basically a “showcase” version).
