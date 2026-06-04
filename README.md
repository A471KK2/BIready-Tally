# 📊 BIReady Tally

Transform raw Tally exports into clean, standardized, analytics-ready datasets.

BIReady Tally is a Streamlit-based data preparation and business analytics platform designed to convert raw Tally ERP exports into structured, validated, and business intelligence (BI) ready datasets. The application automates data cleaning, anomaly detection, KPI generation, and export workflows, helping businesses reduce manual effort and accelerate reporting.

---

## 🚀 Features

### 📁 Tally Data Import

* Upload CSV, XLS, or XLSX Tally exports
* Automatic data ingestion and validation
* Supports large datasets

### 🧹 Data Cleaning & Standardization

* Column name normalization
* Date format standardization
* Currency field cleaning
* Missing value handling
* Master data normalization

### 🔍 Anomaly Detection

Identify common accounting and transaction issues:

* Duplicate invoices
* Negative balances
* Missing GST information
* Zero-value invoices
* Future-dated transactions

### 📈 Business Analytics Dashboard

Generate key business metrics instantly:

* Total Revenue
* Procurement Cost
* Gross Profit
* Profit Margin
* Total Invoices
* Unique Customers/Hospitals

### 📊 Interactive Visualizations

* Monthly Revenue Trend
* Payment Mode Distribution
* State-wise Revenue Analysis
* Top Revenue-Contributing Customers

### 💡 AI-Powered Business Insights

Automatically generated business observations based on:

* Revenue performance
* Customer behavior
* Regional trends
* Transaction anomalies

### 📤 Export Center

Export cleaned datasets in:

* CSV
* Parquet

Ready for:

* Power BI
* Tableau
* Python Analytics
* Data Warehouses

---
## 🖥️ Offline Power BI Integration

BIReady Tally is designed as an **offline-first analytics workflow**.

The Streamlit application performs data cleaning, validation, anomaly detection, KPI generation, and dataset preparation. The prepared dataset is then consumed by a local Power BI dashboard template for advanced reporting and visualization.

### Why Offline?

Power BI Desktop (`.pbix`) files cannot be opened directly from a deployed Streamlit application because Power BI Desktop must be installed on the user's machine.

For this reason:

* ✅ Data cleaning and preparation can be performed through BIReady Tally.
* ✅ Cleaned datasets are automatically exported in BI-ready format.
* ✅ Power BI dashboards can be refreshed locally using the exported dataset.
* ❌ Power BI Desktop cannot be launched from the deployed Streamlit Cloud application.
* ❌ `.pbix` files cannot be executed inside a web browser.

---

## 📊 Power BI Dashboard Workflow

The Power BI integration follows the workflow below:

```text
Raw Tally Export
       │
       ▼
BIReady Tally
(Data Cleaning & Validation)
       │
       ▼
Cleaned CSV Dataset
       │
       ▼
Power BI Desktop
       │
       ▼
Interactive Business Dashboard
```

---

## ⚙️ Power BI Setup Procedure

### Step 1 — Process Data

1. Launch BIReady Tally.
2. Upload the Tally Export file.
3. Review KPIs and data quality metrics.
4. Export the cleaned dataset.

Output:

```text
cleaned_tally_data.csv
```

---

### Step 2 — Open Power BI Dashboard

Open the provided dashboard template:

```text
powerbi/templates/Tally_Dashboard.pbix
```

Requirements:

* Power BI Desktop installed
* Microsoft Windows operating system

---

### Step 3 — Replace Dataset

Copy the exported file:

```text
cleaned_tally_data.csv
```

into:

```text
powerbi/datasets/
```

or update the Power BI data source path to the exported CSV location.

---

### Step 4 — Refresh Dashboard

Inside Power BI Desktop:

```text
Home → Refresh
```

Power BI will reload the latest cleaned dataset.

---

### Step 5 — Analyze Insights

The dashboard automatically updates:

* Revenue KPIs
* Profitability Metrics
* State-wise Analysis
* Payment Mode Analysis
* Customer/Hospital Performance
* Business Trends

---

## ⚠️ Deployment Limitation

When BIReady Tally is deployed on Streamlit Community Cloud:

* Power BI Desktop integration is disabled.
* The "Open Power BI Dashboard" feature is available only when running locally.
* Exported CSV files can still be downloaded and imported into Power BI Desktop manually.

This limitation exists because Power BI Desktop is a local Windows application and cannot be executed from cloud-hosted Streamlit environments.

---

## 🛠️ Technology Stack

### Frontend

* Streamlit

### Data Processing

* Pandas
* NumPy

### Visualization

* Plotly

### Analytics

* Custom KPI Engine
* Anomaly Detection Engine

### Utilities

* Loguru
* OpenPyXL
* Streamlit AgGrid

---

## 📂 Project Structure

```text
BIReady-Tally/
│
├── streamlit_app.py
│
├── engine/
│   ├── analytics/
│   │   ├── anomaly_detector.py
│   │   ├── dashboard_analytics.py
│   │   └── insight_engine.py
│   │
│   └── transformers/
│       ├── data_pipeline.py
│       └── export_engine.py
│
├── data/
│   ├── raw/
│   └── exports/
│
├── logs/
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/BIReady-Tally.git
cd BIReady-Tally
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate virtual environment:

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run streamlit_app.py
```

---

## 📷 Dashboard Modules

### Dashboard

Interactive preview of cleaned data with filtering and export options.

### Analytics

Business KPI visualizations and performance charts.

### Insights

Automatically generated business insights and observations.

### Export

Download analytics-ready datasets for downstream reporting tools.

---

## 🎯 Use Cases

* Business Reporting
* Financial Data Preparation
* Tally ERP Data Cleaning
* BI Dashboard Preparation
* Data Quality Validation
* Accounting Data Analysis

---

## 🔮 Future Enhancements

* AI-powered data correction suggestions
* Automated report generation
* Power BI direct connector
* Predictive analytics
* Multi-company data consolidation
* Scheduled data refresh workflows

---

## 👨‍💻 Author

**Kunal R. Kothe**

Data Science | AI/ML | Business Intelligence | Analytics Engineering

---

## ⭐ Support

If you found this project useful, consider giving it a star on GitHub.

It helps support future development and improvements.
