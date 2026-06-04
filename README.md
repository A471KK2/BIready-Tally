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
