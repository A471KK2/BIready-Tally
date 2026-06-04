# import streamlit as st
# import pandas as pd
# import plotly.express as px
# import os
# import sys

# from pathlib import Path
# from loguru import logger

# # =====================================================
# # FIX PYTHON IMPORT PATH
# # =====================================================

# sys.path.append(
#     str(Path(__file__).resolve().parent.parent)
# )

# # =====================================================
# # IMPORTS
# # =====================================================

# from engine.transformers.data_pipeline import (
#     run_cleaning_pipeline
# )

# from engine.analytics.anomaly_detector import (
#     detect_anomalies
# )

# from engine.analytics.dashboard_analytics import (
#     calculate_dashboard_metrics
# )

# from engine.analytics.insight_engine import (
#     generate_business_insights
# )

# from engine.analytics.data_quality_engine import (
#     calculate_data_quality_scores
# )

# from engine.transformers.export_engine import (
#     ensure_export_directories,
#     generate_export_filename
# )
# from streamlit_option_menu import option_menu

# # =====================================================
# # PAGE CONFIG
# # =====================================================

# st.set_page_config(
#     page_title="Tally Smoothener",
#     page_icon="📊",
#     layout="wide"
# )

# # =====================================================
# # LOGGER SETUP
# # =====================================================

# Path("logs").mkdir(exist_ok=True)

# log_path = Path("logs/app.log")

# logger.add(
#     log_path,
#     rotation="1 MB",
#     retention="5 days",
#     level="INFO",
#     enqueue=True
# )

# # =====================================================
# # PAGE TITLE
# # =====================================================

# st.title("📊 Tally Data Smoothener")

# st.markdown(
#     """
#     Upload messy Tally exports and transform them into
#     clean Power BI-ready datasets.
#     """
# )

# # =====================================================
# # SIDEBAR CONTROLS
# # =====================================================

# st.sidebar.title("⚙️ Dashboard Controls")

# show_column_info = st.sidebar.checkbox(
#     "📌 Column Information",
#     value=False
# )

# show_primary_key = st.sidebar.checkbox(
#     "🆔 Primary Key Validation",
#     value=False
# )

# show_anomalies = st.sidebar.checkbox(
#     "🚨 Anomaly Detection",
#     value=False
# )

# show_business_charts = st.sidebar.checkbox(
#     "📊 Business Intelligence Charts",
#     value=False
# )

# show_ai_insights = st.sidebar.checkbox(
#     "🧠 AI Business Insights",
#     value=False
# )

# show_data_preview = st.sidebar.checkbox(
#     "📄 Data Preview",
#     value=False
# )

# # =====================================================
# # FILE UPLOADER
# # =====================================================

# uploaded_file = st.file_uploader(
#     "📂 Upload Excel or CSV File",
#     type=["xlsx", "xls", "csv"]
# )

# # =====================================================
# # FILE PROCESSING
# # =====================================================

# if uploaded_file:

#     try:

#         logger.info(
#             f"File uploaded: {uploaded_file.name}"
#         )

#         # =====================================================
#         # READ FILE
#         # =====================================================

#         if uploaded_file.name.endswith(".csv"):

#             df = pd.read_csv(uploaded_file)

#         else:

#             df = pd.read_excel(uploaded_file)

#         logger.info(
#             "File read successfully."
#         )

#         # =====================================================
#         # CLEANING PIPELINE
#         # =====================================================

#         cleaned_df = run_cleaning_pipeline(df)

#         logger.info(
#             "Cleaning pipeline completed successfully."
#         )

#         # =====================================================
#         # INTERACTIVE FILTERING
#         # =====================================================

#         filtered_df = cleaned_df.copy()

#         # -----------------------------------------------------
#         # DATE FILTER
#         # -----------------------------------------------------

#         if "invoice_date" in filtered_df.columns:

#             filtered_df["invoice_date"] = pd.to_datetime(
#                 filtered_df["invoice_date"],
#                 errors="coerce"
#             )

#             min_date = filtered_df[
#                 "invoice_date"
#             ].min()

#             max_date = filtered_df[
#                 "invoice_date"
#             ].max()

#             if (
#                 pd.notnull(min_date)
#                 and pd.notnull(max_date)
#             ):

#                 date_range = st.sidebar.date_input(
#                     "📅 Invoice Date Range",
#                     value=(min_date, max_date)
#                 )

#                 if len(date_range) == 2:

#                     start_date, end_date = date_range

#                     filtered_df = filtered_df[
#                         (
#                             filtered_df["invoice_date"]
#                             >= pd.to_datetime(start_date)
#                         )
#                         &
#                         (
#                             filtered_df["invoice_date"]
#                             <= pd.to_datetime(end_date)
#                         )
#                     ]

#         # -----------------------------------------------------
#         # STATE FILTER
#         # -----------------------------------------------------

#         if "state" in filtered_df.columns:

#             states = sorted(
#                 filtered_df["state"]
#                 .dropna()
#                 .unique()
#             )

#             selected_states = st.sidebar.multiselect(
#                 "🗺️ Select States",
#                 options=states,
#                 default=states
#             )

#             filtered_df = filtered_df[
#                 filtered_df["state"]
#                 .isin(selected_states)
#             ]

#         # -----------------------------------------------------
#         # HOSPITAL FILTER
#         # -----------------------------------------------------

#         if "hospital_name" in filtered_df.columns:

#             hospitals = sorted(
#                 filtered_df["hospital_name"]
#                 .dropna()
#                 .unique()
#             )

#             selected_hospitals = st.sidebar.multiselect(
#                 "🏥 Select Hospitals",
#                 options=hospitals,
#                 default=hospitals
#             )

#             filtered_df = filtered_df[
#                 filtered_df["hospital_name"]
#                 .isin(selected_hospitals)
#             ]

#         # -----------------------------------------------------
#         # PAYMENT MODE FILTER
#         # -----------------------------------------------------

#         if "payment_mode" in filtered_df.columns:

#             payment_modes = sorted(
#                 filtered_df["payment_mode"]
#                 .dropna()
#                 .unique()
#             )

#             selected_payment_modes = st.sidebar.multiselect(
#                 "💳 Payment Modes",
#                 options=payment_modes,
#                 default=payment_modes
#             )

#             filtered_df = filtered_df[
#                 filtered_df["payment_mode"]
#                 .isin(selected_payment_modes)
#             ]

#         # -----------------------------------------------------
#         # PRODUCT FILTER
#         # -----------------------------------------------------

#         if "product_name" in filtered_df.columns:

#             products = sorted(
#                 filtered_df["product_name"]
#                 .dropna()
#                 .unique()
#             )

#             selected_products = st.sidebar.multiselect(
#                 "📦 Products",
#                 options=products,
#                 default=products
#             )

#             filtered_df = filtered_df[
#                 filtered_df["product_name"]
#                 .isin(selected_products)
#             ]

#         # -----------------------------------------------------
#         # GLOBAL SEARCH
#         # -----------------------------------------------------

#         search_query = st.sidebar.text_input(
#             "🔎 Global Search"
#         )

#         if search_query:

#             filtered_df = filtered_df[
#                 filtered_df.astype(str)
#                 .apply(
#                     lambda row:
#                     row.str.contains(
#                         search_query,
#                         case=False
#                     ).any(),
#                     axis=1
#                 )
#             ]

#         # =====================================================
#         # SUCCESS MESSAGE
#         # =====================================================

#         st.success(
#             "✅ File loaded and cleaned successfully."
#         )

#         # =====================================================
#         # DATASET METRICS
#         # =====================================================

#         st.subheader("📊 Dataset Metrics")

#         col1, col2, col3, col4 = st.columns(4)

#         col1.metric(
#             "Rows",
#             filtered_df.shape[0]
#         )

#         col2.metric(
#             "Columns",
#             filtered_df.shape[1]
#         )

#         col3.metric(
#             "Missing Values",
#             int(filtered_df.isnull().sum().sum())
#         )

#         col4.metric(
#             "Filtered Rows",
#             filtered_df.shape[0]
#         )

#         # =====================================================
#         # BUSINESS KPI DASHBOARD
#         # =====================================================

#         st.subheader(
#             "📈 Business Intelligence Dashboard"
#         )

#         dashboard_metrics = calculate_dashboard_metrics(
#             filtered_df
#         )

#         kpi1, kpi2, kpi3 = st.columns(3)

#         kpi4, kpi5, kpi6 = st.columns(3)

#         kpi1.metric(
#             "💰 Total Revenue",
#             f"₹ {dashboard_metrics['total_revenue']:,.2f}"
#         )

#         kpi2.metric(
#             "🏭 Procurement Cost",
#             f"₹ {dashboard_metrics['procurement_cost']:,.2f}"
#         )

#         kpi3.metric(
#             "📈 Gross Profit",
#             f"₹ {dashboard_metrics['gross_profit']:,.2f}"
#         )

#         kpi4.metric(
#             "📊 Profit Margin",
#             f"{dashboard_metrics['profit_margin']:.2f}%"
#         )

#         kpi5.metric(
#             "🧾 Total Invoices",
#             dashboard_metrics["total_invoices"]
#         )

#         kpi6.metric(
#             "🏥 Unique Hospitals",
#             dashboard_metrics["unique_hospitals"]
#         )

#         # =====================================================
#         # BUSINESS INTELLIGENCE CHARTS
#         # =====================================================

#         if show_business_charts:

#             # -------------------------------------------------
#             # MONTHLY REVENUE TREND
#             # -------------------------------------------------

#             try:

#                 if (
#                     "invoice_date" in filtered_df.columns
#                     and "credit_amount" in filtered_df.columns
#                 ):

#                     revenue_df = filtered_df.copy()

#                     revenue_df["invoice_date"] = (
#                         pd.to_datetime(
#                             revenue_df["invoice_date"],
#                             errors="coerce"
#                         )
#                     )

#                     revenue_df = revenue_df.dropna(
#                         subset=["invoice_date"]
#                     )

#                     revenue_df["month"] = (
#                         revenue_df["invoice_date"]
#                         .dt.strftime("%Y-%m")
#                     )

#                     monthly_revenue = (
#                         revenue_df
#                         .groupby("month")["credit_amount"]
#                         .sum()
#                         .reset_index()
#                     )

#                     st.subheader(
#                         "📊 Monthly Revenue Trend"
#                     )

#                     revenue_chart = px.line(
#                         monthly_revenue,
#                         x="month",
#                         y="credit_amount",
#                         markers=True,
#                         title="Monthly Revenue"
#                     )

#                     st.plotly_chart(
#                         revenue_chart,
#                         use_container_width=True
#                     )

#             except Exception as e:

#                 st.error(
#                     f"Revenue chart error: {e}"
#                 )

#             # -------------------------------------------------
#             # PAYMENT MODE DISTRIBUTION
#             # -------------------------------------------------

#             try:

#                 if "payment_mode" in filtered_df.columns:

#                     payment_mode_df = (
#                         filtered_df["payment_mode"]
#                         .value_counts()
#                         .reset_index()
#                     )

#                     payment_mode_df.columns = [
#                         "payment_mode",
#                         "count"
#                     ]

#                     st.subheader(
#                         "💳 Payment Mode Distribution"
#                     )

#                     payment_chart = px.pie(
#                         payment_mode_df,
#                         names="payment_mode",
#                         values="count",
#                         hole=0.4
#                     )

#                     st.plotly_chart(
#                         payment_chart,
#                         use_container_width=True
#                     )

#             except Exception as e:

#                 st.error(
#                     f"Payment chart error: {e}"
#                 )

#             # -------------------------------------------------
#             # STATE-WISE REVENUE
#             # -------------------------------------------------

#             try:

#                 if (
#                     "state" in filtered_df.columns
#                     and "credit_amount" in filtered_df.columns
#                 ):

#                     state_sales = (
#                         filtered_df
#                         .groupby("state")["credit_amount"]
#                         .sum()
#                         .reset_index()
#                     )

#                     st.subheader(
#                         "🗺️ State-wise Revenue"
#                     )

#                     state_chart = px.bar(
#                         state_sales,
#                         x="state",
#                         y="credit_amount",
#                         title="Revenue by State"
#                     )

#                     st.plotly_chart(
#                         state_chart,
#                         use_container_width=True
#                     )

#             except Exception as e:

#                 st.error(
#                     f"State chart error: {e}"
#                 )

#             # -------------------------------------------------
#             # TOP HOSPITALS
#             # -------------------------------------------------

#             try:

#                 if (
#                     "hospital_name" in filtered_df.columns
#                     and "credit_amount" in filtered_df.columns
#                 ):

#                     top_hospitals = (
#                         filtered_df
#                         .groupby("hospital_name")[
#                             "credit_amount"
#                         ]
#                         .sum()
#                         .sort_values(ascending=False)
#                         .head(10)
#                         .reset_index()
#                     )

#                     st.subheader(
#                         "🏥 Top Hospitals by Revenue"
#                     )

#                     hospital_chart = px.bar(
#                         top_hospitals,
#                         x="hospital_name",
#                         y="credit_amount",
#                         title="Top 10 Hospitals"
#                     )

#                     st.plotly_chart(
#                         hospital_chart,
#                         use_container_width=True
#                     )

#             except Exception as e:

#                 st.error(
#                     f"Hospital chart error: {e}"
#                 )

#         # =====================================================
#         # COLUMN INFORMATION
#         # =====================================================

#         if show_column_info:

#             st.subheader("📌 Column Information")

#             column_info = pd.DataFrame({

#                 "Column": filtered_df.columns,

#                 "Data Type": [
#                     str(dtype)
#                     for dtype in filtered_df.dtypes
#                 ],

#                 "Missing Values": (
#                     filtered_df.isnull()
#                     .sum()
#                     .values
#                 )

#             })

#             st.dataframe(
#                 column_info,
#                 use_container_width=True
#             )

#         # =====================================================
#         # PRIMARY KEY VALIDATION
#         # =====================================================

#         if show_primary_key:

#             st.subheader(
#                 "🆔 Primary Key Validation"
#             )

#             duplicate_keys = filtered_df[
#                 "primary_key"
#             ].duplicated().sum()

#             if duplicate_keys == 0:

#                 st.success(
#                     "✅ All primary keys are unique."
#                 )

#             else:

#                 st.warning(
#                     f"⚠️ {duplicate_keys} duplicate primary keys detected."
#                 )

#             st.dataframe(
#                 filtered_df[["primary_key"]].head(),
#                 use_container_width=True
#             )

#         # =====================================================
#         # ANOMALY DETECTION
#         # =====================================================

#         anomalies = detect_anomalies(filtered_df)

#         if show_anomalies:

#             st.subheader("🚨 Anomaly Detection")

#             anomaly_col1, anomaly_col2 = st.columns(2)

#             anomaly_col3, anomaly_col4 = st.columns(2)

#             duplicate_invoice_count = len(
#                 anomalies["duplicate_invoices"]
#             )

#             anomaly_col1.metric(
#                 "Duplicate Invoices",
#                 duplicate_invoice_count
#             )

#             negative_balance_count = len(
#                 anomalies["negative_balances"]
#             )

#             anomaly_col2.metric(
#                 "Negative Balances",
#                 negative_balance_count
#             )

#             missing_gst_count = len(
#                 anomalies["missing_gst"]
#             )

#             anomaly_col3.metric(
#                 "Missing GST Records",
#                 missing_gst_count
#             )

#             zero_value_count = len(
#                 anomalies["zero_value_invoices"]
#             )

#             anomaly_col4.metric(
#                 "Zero Value Invoices",
#                 zero_value_count
#             )

#         # =====================================================
#         # DATA QUALITY SCORING
#         # =====================================================

#         st.subheader(
#             "📋 Enterprise Data Quality Scores"
#         )

#         quality_scores = calculate_data_quality_scores(
#             filtered_df,
#             anomalies
#         )

#         q1, q2, q3 = st.columns(3)

#         q4, q5, q6 = st.columns(3)

#         q1.metric(
#             "📦 Completeness",
#             f"{quality_scores['completeness_score']}%"
#         )

#         q2.metric(
#             "🧩 Consistency",
#             f"{quality_scores['consistency_score']}%"
#         )

#         q3.metric(
#             "📜 Compliance",
#             f"{quality_scores['compliance_score']}%"
#         )

#         q4.metric(
#             "🚨 Anomaly Score",
#             f"{quality_scores['anomaly_score']}%"
#         )

#         q5.metric(
#             "📊 BI Readiness",
#             f"{quality_scores['bi_readiness_score']}%"
#         )

#         q6.metric(
#             "🏆 Overall Quality",
#             f"{quality_scores['overall_quality_index']}%"
#         )

#         # =====================================================
#         # QUALITY INTERPRETATION
#         # =====================================================

#         overall_quality = quality_scores[
#             "overall_quality_index"
#         ]

#         if overall_quality >= 90:

#             st.success(
#                 "✅ Dataset quality is enterprise-grade."
#             )

#         elif overall_quality >= 75:

#             st.info(
#                 "📈 Dataset quality is good for BI analytics."
#             )

#         elif overall_quality >= 60:

#             st.warning(
#                 "⚠️ Dataset quality is moderate."
#             )

#         else:

#             st.error(
#                 "🚨 Dataset quality is poor."
#             )

#         # =====================================================
#         # AI BUSINESS INSIGHTS
#         # =====================================================

#         if show_ai_insights:

#             st.subheader(
#                 "🧠 AI Business Insights"
#             )

#             insights = generate_business_insights(
#                 filtered_df,
#                 dashboard_metrics,
#                 anomalies
#             )

#             for insight in insights:

#                 st.info(insight)

#         # =====================================================
#         # DATA PREVIEW
#         # =====================================================

#         if show_data_preview:

#             st.subheader(
#                 "📄 Cleaned Data Preview"
#             )

#             st.dataframe(
#                 filtered_df.head(20),
#                 use_container_width=True
#             )

#         # =====================================================
#         # EXPORT ENGINE
#         # =====================================================

#         st.subheader(
#             "⬇️ Export Cleaned Dataset"
#         )

#         ensure_export_directories()

#         # -----------------------------------------------------
#         # EXPORT CSV
#         # -----------------------------------------------------

#         csv_filename = generate_export_filename(
#             "cleaned_tally_data",
#             "csv"
#         )

#         csv_path = (
#             f"data/exports/{csv_filename}"
#         )

#         filtered_df.to_csv(
#             csv_path,
#             index=False
#         )

#         csv_data = filtered_df.to_csv(
#             index=False
#         ).encode("utf-8")

#         st.download_button(
#             label="⬇️ Download Cleaned CSV",
#             data=csv_data,
#             file_name=csv_filename,
#             mime="text/csv"
#         )

#         # -----------------------------------------------------
#         # EXPORT PARQUET
#         # -----------------------------------------------------

#         parquet_filename = generate_export_filename(
#             "cleaned_tally_data",
#             "parquet"
#         )

#         parquet_path = (
#             f"data/exports/{parquet_filename}"
#         )

#         filtered_df.to_parquet(
#             parquet_path,
#             index=False
#         )

#         # -----------------------------------------------------
#         # SAVE FILE FOR POWER BI
#         # -----------------------------------------------------

#         powerbi_dataset_path = (
#             "powerbi/datasets/cleaned_tally_data.csv"
#         )

#         filtered_df.to_csv(
#             powerbi_dataset_path,
#             index=False
#         )

#         st.success(
#             """
#             ✅ CSV, Parquet, and Power BI dataset
#             exports generated successfully.
#             """
#         )

#         logger.info(
#             f"Exports created: {csv_filename}, "
#             f"{parquet_filename}"
#         )

#     except Exception as e:

#         logger.error(
#             f"Error while processing file: {str(e)}"
#         )

#         st.error(
#             "❌ An error occurred while processing the file."
#         )

#         st.exception(e)

# else:

#     st.info(
#         "👆 Upload a Tally Excel or CSV file to begin."
#     )

# # =====================================================
# # OPEN POWER BI DASHBOARD
# # =====================================================

# st.subheader("📊 Power BI Dashboard")

# if st.button(
#     "Open Power BI Dashboard"
# ):

#     powerbi_file = (
#         Path(__file__).resolve().parent.parent
#         / "powerbi"
#         / "templates"
#         / "Tally_Dashboard.pbix"
#     )

#     os.startfile(str(powerbi_file))

#     st.success(
#         "✅ Power BI Dashboard Opened."
#     )
###############################################################################################################################3
#############################################################################################################################33

# import os
# import io
# import sys
# from pathlib import Path

# import pandas as pd
# import plotly.express as px
# import streamlit as st
# from loguru import logger

# try:
#     import streamlit_shadcn_ui as ui
# except ImportError:
#     ui = None

# sys.path.append(str(Path(__file__).resolve().parent.parent))

# from engine.analytics.anomaly_detector import detect_anomalies
# from engine.analytics.dashboard_analytics import calculate_dashboard_metrics
# from engine.analytics.data_quality_engine import calculate_data_quality_scores
# from engine.analytics.insight_engine import generate_business_insights
# from engine.transformers.data_pipeline import run_cleaning_pipeline
# from engine.transformers.export_engine import (
#     ensure_export_directories,
#     generate_export_filename,
# )
# import streamlit as st
# from st_aggrid import AgGrid
# from st_aggrid import GridOptionsBuilder

# st.set_page_config(
#     page_title="Tally Smoothener",
#     page_icon="TS",
#     layout="wide",
#     initial_sidebar_state="expanded",
# )

# Path("logs").mkdir(exist_ok=True)
# try:
#     logger.add(
#         Path("logs/app.log"),
#         rotation="1 MB",
#         retention="5 days",
#         level="INFO",
#         enqueue=True,
#     )
# except PermissionError:
#     logger.warning("File logging is unavailable because logs/app.log is locked.")


# def inject_styles(theme="Light"):
#     if theme == "Dark":

#         app_bg = "#0B1220"
#         panel = "#111827"
#         ink = "#F9FAFB"
#         muted = "#9CA3AF"
#         line = "#374151"
#     else:

#         app_bg = "#F7F8FB"
#         panel = "#FFFFFF"
#         ink = "#111827"
#         muted = "#6B7280"
#         line = "#E5E7EB"

#     st.markdown(
#         f"""
#         <style>
#             @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');


#             :root {{
#                 --app-bg: {app_bg};
#                 --panel: {panel};
#                 --ink: {ink};
#                 --muted: {muted};
#                 --line: {line};
#                 --accent: #2563eb;
#                 --accent-soft: #dbeafe;
#                 --success: #059669;
#                 --warning: #d97706;
#                 --danger: #dc2626;
#             }}

#             html, body, [class*="css"] {{
#                 font-family: "Inter", system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
#             }}

#             .stApp {{
#                 background: var(--app-bg);
#             }}

#             section[data-testid="stSidebar"] {{
#                 background: #ffffff;
#                 border-right: 1px solid var(--line);
#             }}

#             section[data-testid="stSidebar"] div[data-testid="stMarkdownContainer"] p {{
#                 color: var(--muted);
#             }}

#             .block-container {{
#                 padding-top: 1.6rem;
#                 padding-bottom: 2.4rem;
#                 max-width: 1440px;
#             }}

#             h1, h2, h3 {{
#                 color: var(--ink);
#                 letter-spacing: 0;
#             }}

#             div[data-testid="stMetric"] {{
#                 background: var(--panel);
#                 border: 1px solid var(--line);
#                 border-radius: 16px;
#                 padding: 20px;
#                 box-shadow: 0 12px 32px rgba(17, 24, 39, 0.08);
#                 transition: all 0.25s ease;
#             }}

#             div[data-testid="stMetricLabel"] p {{
#                 color: var(--muted);
#                 font-size: 0.85rem;
#                 font-weight: 600;
#             }}

#             div[data-testid="stMetricValue"] {{
#                 color: var(--ink);
#                 font-weight: 800;
#             }}

#             div[data-testid="stFileUploader"] {{
#                 background: #ffffff;
#                 border: 1px dashed #cbd5e1;
#                 border-radius: 8px;
#                 padding: 12px;
#             }}

#             .hero {{
#                 background: #ffffff;
#                 border: 1px solid var(--line);
#                 border-radius: 16px;
#                 padding: 48px 50px;
#                 box-shadow: 0 12px 32px rgba(15, 23, 42, 0.05);
#                 margin-bottom: 24px;
#             }}

#             .hero-kicker {{
#                 color: var(--accent);
#                 font-size: 0.78rem;
#                 font-weight: 800;
#                 letter-spacing: 0.08em;
#                 text-transform: uppercase;
#                 margin-bottom: 8px;
#             }}

#             .hero-title {{
#                 color: var(--ink);
#                 font-size: clamp(3rem, 6vw, 5rem);
#                 font-weight: 900;
#                 line-height: 1;
#                 margin: 0;
#                 letter-spacing: -0.04em;
#             }}

#             .hero-copy {{
#                 color: var(--muted);
#                 font-size: 1rem;
#                 line-height: 1.7;
#                 max-width: 780px;
#                 margin-top: 12px;
#                 margin-bottom: 0;
#             }}

#             .section-title {{
#                 display: flex;
#                 align-items: center;
#                 justify-content: space-between;
#                 gap: 16px;
#                 margin: 22px 0 12px;
#             }}

#             .section-title h2 {{
#                 font-size: 1.18rem;
#                 font-weight: 800;
#                 margin: 0;
#             }}

#             .section-title p {{
#                 color: var(--muted);
#                 font-size: 0.9rem;
#                 margin: 2px 0 0;
#             }}

#             .status-pill {{
#                 display: inline-flex;
#                 align-items: center;
#                 border: 1px solid var(--line);
#                 border-radius: 999px;
#                 color: var(--muted);
#                 font-size: 0.8rem;
#                 font-weight: 700;
#                 padding: 6px 10px;
#                 background: #ffffff;
#                 white-space: nowrap;
#             }}

#             .empty-state {{
#                 background: #ffffff;
#                 border: 1px solid var(--line);
#                 border-radius: 8px;
#                 padding: 42px 34px;
#                 text-align: center;
#                 box-shadow: 0 12px 32px rgba(15, 23, 42, 0.04);
#             }}

#             .empty-state h3 {{
#                 font-size: 1.4rem;
#                 font-weight: 800;
#                 margin-bottom: 8px;
#             }}

#             .empty-state p {{
#                 color: var(--muted);
#                 margin: 0 auto;
#                 max-width: 620px;
#                 line-height: 1.7;
#             }}

#             .info-panel {{
#                 background: #ffffff;
#                 border: 1px solid var(--line);
#                 border-radius: 8px;
#                 padding: 18px;
#                 box-shadow: 0 8px 24px rgba(15, 23, 42, 0.04);
#             }}

#             .insight-item {{
#                 border: 1px solid var(--line);
#                 border-left: 4px solid var(--accent);
#                 border-radius: 8px;
#                 background: #ffffff;
#                 padding: 14px 16px;
#                 margin-bottom: 10px;
#                 color: var(--ink);
#                 font-weight: 500;
#             }}

#             .small-note {{
#                 color: var(--muted);
#                 font-size: 0.84rem;
#                 line-height: 1.55;
#             }}

#             .stPlotlyChart {{
#                 background: #ffffff;
#                 border: 1px solid var(--line);
#                 border-radius: 8px;
#                 padding: 10px;
#                 box-shadow: 0 8px 24px rgba(15, 23, 42, 0.04);
#             }}

#             .ag-theme-streamlit {{
#                 border-radius: 16px !important;
#                 overflow: hidden !important;
#             }}

#             .chart-panel {{
#                 background: #ffffff;
#                 border: 1px solid var(--line);
#                 border-radius: 16px;
#                 padding: 16px;
#                 margin-bottom: 18px;
#                 box-shadow: 0 12px 32px rgba(15, 23, 42, 0.06);
#             }}

#             .action-card {{
#                 background: #ffffff;
#                 border: 1px solid var(--line);
#                 border-radius: 18px;
#                 padding: 28px;
#                 text-align: center;
#                 box-shadow: 0 12px 32px rgba(15, 23, 42, 0.06);
#                 margin-bottom: 16px;
#             }}

#             .action-title {{
#                 font-size: 1.2rem;
#                 font-weight: 800;
#                 color: var(--ink);
#                 margin-bottom: 8px;
#             }}

#            .action-desc {{
#                 color: var(--muted);
#                 font-size: 0.9rem;
#                 margin-bottom: 18px;
#             }}
#             .data-controls {{
#                 background: var(--panel);
#                 border: 1px solid var(--line);
#                 border-radius: 12px;
#                 padding: 16px;
#                 margin-bottom: 18px;
#                 box-shadow: 0 4px 12px rgba(15, 23, 42, 0.04);
#             }}
#             .dataframe-wrapper {{
#                 border-radius: 12px;
#                 overflow: hidden;
#                 border: 1px solid var(--line);
#                 background: var(--panel);
#                 box-shadow: 0 4px 12px rgba(15, 23, 42, 0.04);
#             }}
#             [data-testid="stDataFrame"] {{
#                 max-height: 700px !important;
#                 overflow-y: auto !important;
#             }}

#         </style>
#         """,
#         unsafe_allow_html=True,
#     )


# def hero():
#     st.markdown(
#         """
#         <div class="hero">
#             <div class="hero-kicker">Tally Smoothener</div>
#             <h1 class="hero-title">Clean finance data. Review quality. Export with confidence.</h1>
#             <p class="hero-copy">
#                 Upload a raw Tally export and turn it into a clean, BI-ready dataset with validation,
#                 anomaly checks, quality scoring, business KPIs, and Power BI handoff in one workflow.
#             </p>
#         </div>
#         """,
#         unsafe_allow_html=True,
#     )


# def section_title(title, caption=None, status=None):
#     caption_html = f"<p>{caption}</p>" if caption else ""
#     status_html = f'<span class="status-pill">{status}</span>' if status else ""
#     st.markdown(
#         f"""
#         <div class="section-title">
#             <div>
#                 <h2>{title}</h2>
#                 {caption_html}
#             </div>
#             {status_html}
#         </div>
#         """,
#         unsafe_allow_html=True,
#     )


# def shad_metric(title, value, description, key):
#     if ui:
#         ui.metric_card(
#             title=title,
#             content=str(value),
#             description=description,
#             key=key,
#         )
#     else:
#         st.metric(title, value, help=description)


# def format_currency(value):
#     return f"Rs. {value:,.2f}"


# def format_count(value):
#     return f"{int(value):,}"


# def plot_style(fig):
#     fig.update_layout(
#         template="plotly_white",
#         font=dict(family="Inter, Arial", color="#111827"),
#         title_font=dict(size=16, color="#111827"),
#         margin=dict(l=20, r=20, t=48, b=20),
#         paper_bgcolor="#ffffff",
#         plot_bgcolor="#ffffff",
#         legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
#     )
#     fig.update_xaxes(showgrid=False, zeroline=False)
#     fig.update_yaxes(gridcolor="#eef2f7", zeroline=False)
#     return fig


# def display_cleaned_data(
#     df_cleaned,
#     title="Cleaned Data Preview",
#     caption="First 50 records from the active dataset.",
# ):
#     """
#     Display cleaned data with interactive controls for zoom, row selection,
#     and column selection.

#     Parameters:
#     -----------
#     df_cleaned : pd.DataFrame
#         The cleaned dataframe to display
#     title : str
#         Title for the data section
#     caption : str
#         Subtitle/caption text
#     """

#     section_title(title, caption)

#     # =========== CONTROL ROW: Zoom, Rows, Columns ===========
#     st.markdown('<div class="data-controls">', unsafe_allow_html=True)

#     col1, col2, col3 = st.columns([1, 1.5, 2], gap="medium")

#     with col1:
#         zoom_level = st.slider(
#             "🔍 Zoom Level",
#             min_value=50,
#             max_value=150,
#             value=100,
#             step=10,
#             key=f"zoom_slider_{title}",
#             help="Zoom in/out to adjust text size (50%-150%)",
#         )

#     with col2:
#         num_rows = st.selectbox(
#             "📋 Rows",
#             options=[10, 25, 50, 100, 250, "All"],
#             index=2,
#             key=f"row_selector_{title}",
#             help="How many rows to display?",
#         )

#     with col3:
#         all_columns = df_cleaned.columns.tolist()
#         selected_columns = st.multiselect(
#             "🏷️ Columns",
#             options=all_columns,
#             default=all_columns,
#             key=f"column_selector_{title}",
#             help="Select which columns to show",
#         )

#     st.markdown("</div>", unsafe_allow_html=True)

#     # =========== APPLY FILTERS ===========
#     df_display = df_cleaned[selected_columns].copy()

#     if num_rows != "All":
#         df_display = df_display.head(int(num_rows))

#     df_display = df_display.reset_index(drop=True)
#     df_display.index = df_display.index + 1  # 1-based indexing

#     # =========== METRICS ROW ===========
#     metric_col1, metric_col2, metric_col3, metric_col4 = st.columns(4)

#     with metric_col1:
#         st.metric(
#             "Total Records", format_count(len(df_cleaned)), help="Original dataset size"
#         )

#     with metric_col2:
#         st.metric("Displayed", format_count(len(df_display)), help="Current view")

#     with metric_col3:
#         st.metric(
#             "Columns",
#             format_count(len(selected_columns)),
#             help=f"Out of {len(df_cleaned.columns)} total",
#         )

#     with metric_col4:
#         missing = df_display.isnull().sum().sum()
#         st.metric("Missing", format_count(missing), help="Empty cells")

#     # =========== DISPLAY DATAFRAME ===========
#     st.markdown('<div class="dataframe-wrapper">', unsafe_allow_html=True)

#     st.dataframe(df_display, use_container_width=True, height=700, hide_index=False)

#     st.markdown("</div>", unsafe_allow_html=True)

#     # =========== DATA INFO EXPANDER ===========
#     with st.expander("📋 Column Details & Statistics", expanded=False):
#         col_info = pd.DataFrame(
#             {
#                 "Column": selected_columns,
#                 "Type": [str(df_display[col].dtype) for col in selected_columns],
#                 "Non-Null": [df_display[col].notna().sum() for col in selected_columns],
#                 "Null": [df_display[col].isna().sum() for col in selected_columns],
#                 "Unique": [df_display[col].nunique() for col in selected_columns],
#             }
#         )
#         st.dataframe(col_info, use_container_width=True, hide_index=True)

#     # =========== EXPORT OPTIONS ===========
#     st.markdown("---")

#     col_exp1, col_exp2, col_exp3 = st.columns(3)

#     with col_exp1:
#         csv = df_display.to_csv(index=False)
#         st.download_button(
#             label="📥 CSV",
#             data=csv,
#             file_name="cleaned_data_preview.csv",
#             mime="text/csv",
#             key=f"download_csv_{title}",
#         )

#     with col_exp2:
#         excel_buffer = io.BytesIO()
#         df_display.to_excel(excel_buffer, index=False, engine="openpyxl")
#         excel_buffer.seek(0)
#         st.download_button(
#             label="📥 Excel",
#             data=excel_buffer,
#             file_name="cleaned_data_preview.xlsx",
#             mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
#             key=f"download_excel_{title}",
#         )

#     with col_exp3:
#         json_data = df_display.to_json(orient="records", indent=2)
#         st.download_button(
#             label="📥 JSON",
#             data=json_data,
#             file_name="cleaned_data_preview.json",
#             mime="application/json",
#             key=f"download_json_{title}",
#         )


# def show_aggrid(df):

#     gb = GridOptionsBuilder.from_dataframe(df)

#     gb.configure_default_column(sortable=True, filter=True, resizable=True)

#     gb.configure_pagination(paginationAutoPageSize=True)

#     grid_options = gb.build()

#     AgGrid(df, gridOptions=grid_options, fit_columns_on_grid_load=True, height=450)


# def read_uploaded_file(uploaded_file):
#     if uploaded_file.name.lower().endswith(".csv"):
#         return pd.read_csv(uploaded_file)
#     return pd.read_excel(uploaded_file)


# def normalize_anomalies(anomalies):
#     expected_keys = [
#         "duplicate_invoices",
#         "negative_balances",
#         "missing_gst",
#         "zero_value_invoices",
#         "future_dates",
#     ]
#     for key in expected_keys:
#         if key not in anomalies:
#             anomalies[key] = pd.DataFrame()
#     return anomalies


# def apply_sidebar_filters(df):
#     filtered_df = df.copy()

#     with st.sidebar:
#         st.markdown("### Filters")
#         st.caption("Refine the cleaned dataset before reviewing KPIs or exporting.")

#         if "invoice_date" in filtered_df.columns:
#             filtered_df["invoice_date"] = pd.to_datetime(
#                 filtered_df["invoice_date"],
#                 errors="coerce",
#             )
#             min_date = filtered_df["invoice_date"].min()
#             max_date = filtered_df["invoice_date"].max()

#             if pd.notnull(min_date) and pd.notnull(max_date):
#                 date_range = st.date_input(
#                     "Invoice date range",
#                     value=(min_date, max_date),
#                 )

#                 if len(date_range) == 2:
#                     start_date, end_date = date_range
#                     filtered_df = filtered_df[
#                         (filtered_df["invoice_date"] >= pd.to_datetime(start_date))
#                         & (filtered_df["invoice_date"] <= pd.to_datetime(end_date))
#                     ]

#         filter_columns = [
#             ("state", "State"),
#             ("hospital_name", "Hospital"),
#             ("payment_mode", "Payment mode"),
#             ("product_name", "Product"),
#         ]

#         for column, label in filter_columns:
#             if column in filtered_df.columns:
#                 options = sorted(filtered_df[column].dropna().astype(str).unique())
#                 selected = st.multiselect(
#                     label,
#                     options=options,
#                     default=options,
#                 )
#                 filtered_df = filtered_df[
#                     filtered_df[column].astype(str).isin(selected)
#                 ]

#         search_query = st.text_input(
#             "Global search",
#             placeholder="Search invoice, hospital, state...",
#         )

#         if search_query:
#             filtered_df = filtered_df[
#                 filtered_df.astype(str).apply(
#                     lambda row: row.str.contains(
#                         search_query,
#                         case=False,
#                         na=False,
#                     ).any(),
#                     axis=1,
#                 )
#             ]

#     return filtered_df


# def render_sidebar():
#     with st.sidebar:
#         st.markdown(
#         """
#         <h1 style="
#             font-size:2rem;
#             font-weight:900;
#             margin-bottom:0;
#         ">
#             📊 Tally Smoothener
#         </h1>
#         """,
#         unsafe_allow_html=True,
#     )
#         st.caption("Professional data cleaning and BI readiness workflow.")
#         theme = st.selectbox("🎨 Theme", ["Light", "Dark"], index=0)

#         uploaded_file = st.file_uploader(
#             "Upload Tally export",
#             type=["xlsx", "xls", "csv"],
#             help="Upload a CSV, XLS, or XLSX export from Tally.",
#         )

#         st.divider()

#         selected_page = st.radio(
#             "Navigation",
#             [
#                 "Dashboard",
#                 "Analytics",
#                 "Quality",
#                 "Insights",
#                 "Export",
#                 "Power BI"
#             ]
#      )

#         st.divider()

#         st.markdown("### Review Options")
#         options = {
#             "column_info": st.toggle("Column information", value=False),
#             "primary_key": st.toggle("Primary key validation", value=False),
#             "anomalies": st.toggle("Anomaly details", value=True),
#             "insights": st.toggle("Business insights", value=True),
#             "preview": st.toggle("Data preview", value=True),
#         }

#         st.divider()
#         if ui is None:
#             st.warning(
#                 "streamlit-shadcn-ui is not installed yet. The app will use native Streamlit components until dependencies are installed."
#             )

#     return (uploaded_file, options, selected_page, theme)


# def render_dataset_metrics(filtered_df, source_df):
#     section_title(
#         "Dataset Overview",
#         "A quick read on the active filtered dataset.",
#         status=f"{format_count(filtered_df.shape[0])} active rows",
#     )
#     col1, col2, col3, col4 = st.columns(4)
#     missing_values = int(filtered_df.isnull().sum().sum())
#     filtered_out = max(source_df.shape[0] - filtered_df.shape[0], 0)

#     with col1:
#         shad_metric(
#             "Rows",
#             format_count(filtered_df.shape[0]),
#             "Records after filters",
#             "rows_metric",
#         )
#     with col2:
#         shad_metric(
#             "Columns",
#             format_count(filtered_df.shape[1]),
#             "Cleaned dataset width",
#             "cols_metric",
#         )
#     with col3:
#         shad_metric(
#             "Missing Values",
#             format_count(missing_values),
#             "Blank cells remaining",
#             "missing_metric",
#         )
#     with col4:
#         shad_metric(
#             "Filtered Out",
#             format_count(filtered_out),
#             "Rows hidden by filters",
#             "filtered_metric",
#         )


# def render_business_metrics(metrics):
#     section_title(
#         "Business KPIs",
#         "Commercial summary calculated from the cleaned ledger.",
#     )
#     kpi1, kpi2, kpi3 = st.columns(3)
#     kpi4, kpi5, kpi6 = st.columns(3)

#     with kpi1:
#         shad_metric(
#             "Total Revenue",
#             format_currency(metrics["total_revenue"]),
#             "Credit amount for sales vouchers",
#             "revenue_metric",
#         )
#     with kpi2:
#         shad_metric(
#             "Procurement Cost",
#             format_currency(metrics["procurement_cost"]),
#             "Debit amount for purchase vouchers",
#             "procurement_metric",
#         )
#     with kpi3:
#         shad_metric(
#             "Gross Profit",
#             format_currency(metrics["gross_profit"]),
#             "Revenue minus procurement cost",
#             "profit_metric",
#         )
#     with kpi4:
#         shad_metric(
#             "Profit Margin",
#             f"{metrics['profit_margin']:.2f}%",
#             "Gross profit as a percentage of revenue",
#             "margin_metric",
#         )
#     with kpi5:
#         shad_metric(
#             "Total Invoices",
#             format_count(metrics["total_invoices"]),
#             "Records in the active dataset",
#             "invoice_metric",
#         )
#     with kpi6:
#         shad_metric(
#             "Unique Hospitals",
#             format_count(metrics["unique_hospitals"]),
#             "Distinct hospital accounts",
#             "hospital_metric",
#         )


# def render_charts(filtered_df):
#     section_title(
#         "Business Charts",
#         "Revenue, customer, geography, and payment views.",
#     )

#     chart_col1, chart_col2 = st.columns(2)

#     with chart_col1:
#         if "invoice_date" in filtered_df.columns and "credit_amount" in filtered_df.columns:
#             revenue_df = filtered_df.copy()
#             revenue_df["invoice_date"] = pd.to_datetime(
#                 revenue_df["invoice_date"],
#                 errors="coerce",
#             )
#             revenue_df = revenue_df.dropna(subset=["invoice_date"])
#             revenue_df["month"] = revenue_df["invoice_date"].dt.strftime("%Y-%m")
#             monthly_revenue = (
#                 revenue_df.groupby("month")["credit_amount"].sum().reset_index()
#             )
#             fig = px.line(
#                 monthly_revenue,
#                 x="month",
#                 y="credit_amount",
#                 markers=True,
#                 title="Monthly Revenue Trend",
#             )
#             # st.plotly_chart(plot_style(fig), use_container_width=True)
#             st.markdown(
#                '<div class="chart-panel">',
#                unsafe_allow_html=True
#             )

#             st.plotly_chart(
#                 plot_style(fig),
#                 use_container_width=True
#             )

#             st.markdown(
#                 '</div>',
#                 unsafe_allow_html=True
#             )
#         else:
#             st.info("Invoice date and credit amount are required for revenue trend.")

#     with chart_col2:
#         if "payment_mode" in filtered_df.columns:
#             payment_mode_df = filtered_df["payment_mode"].value_counts().reset_index()
#             payment_mode_df.columns = ["payment_mode", "count"]
#             fig = px.pie(
#                 payment_mode_df,
#                 names="payment_mode",
#                 values="count",
#                 hole=0.58,
#                 title="Payment Mode Distribution",
#                 color_discrete_sequence=px.colors.qualitative.Set2,
#             )
#             st.plotly_chart(plot_style(fig), use_container_width=True)
#         else:
#             st.info("Payment mode is required for payment distribution.")

#     chart_col3, chart_col4 = st.columns(2)

#     with chart_col3:
#         if "state" in filtered_df.columns and "credit_amount" in filtered_df.columns:
#             state_sales = (
#                 filtered_df.groupby("state")["credit_amount"]
#                 .sum()
#                 .sort_values(ascending=False)
#                 .reset_index()
#             )
#             fig = px.bar(
#                 state_sales,
#                 x="state",
#                 y="credit_amount",
#                 title="State-wise Revenue",
#                 color="credit_amount",
#                 color_continuous_scale="Blues",
#             )
#             st.plotly_chart(plot_style(fig), use_container_width=True)
#         else:
#             st.info("State and credit amount are required for state-wise revenue.")

#     with chart_col4:
#         if (
#             "hospital_name" in filtered_df.columns
#             and "credit_amount" in filtered_df.columns
#         ):
#             top_hospitals = (
#                 filtered_df.groupby("hospital_name")["credit_amount"]
#                 .sum()
#                 .sort_values(ascending=False)
#                 .head(10)
#                 .reset_index()
#             )
#             fig = px.bar(
#                 top_hospitals,
#                 x="credit_amount",
#                 y="hospital_name",
#                 title="Top Hospitals by Revenue",
#                 orientation="h",
#                 color="credit_amount",
#                 color_continuous_scale="Teal",
#             )
#             fig.update_layout(yaxis=dict(autorange="reversed"))
#             st.plotly_chart(plot_style(fig), use_container_width=True)
#         else:
#             st.info("Hospital name and credit amount are required for top hospitals.")


# def render_quality(quality_scores, anomalies):
#     section_title(
#         "Data Quality",
#         "Completeness, consistency, compliance, and BI readiness.",
#     )
#     q1, q2, q3 = st.columns(3)
#     q4, q5, q6 = st.columns(3)

#     quality_items = [
#         (q1, "Completeness", quality_scores["completeness_score"], "Non-empty cell coverage"),
#         (q2, "Consistency", quality_scores["consistency_score"], "Master data and value consistency"),
#         (q3, "Compliance", quality_scores["compliance_score"], "GST record coverage"),
#         (q4, "Anomaly Score", quality_scores["anomaly_score"], "Lower issue count means higher score"),
#         (q5, "BI Readiness", quality_scores["bi_readiness_score"], "Required BI fields available"),
#         (q6, "Overall Quality", quality_scores["overall_quality_index"], "Weighted quality index"),
#     ]

#     for column, title, score, description in quality_items:
#         with column:
#             shad_metric(title, f"{score}%", description, f"quality_{title.lower().replace(' ', '_')}")

#     overall = quality_scores["overall_quality_index"]
#     if overall >= 90:
#         st.success("Dataset quality is enterprise-grade.")
#     elif overall >= 75:
#         st.info("Dataset quality is good for BI analytics.")
#     elif overall >= 60:
#         st.warning("Dataset quality is moderate. Review anomalies before final reporting.")
#     else:
#         st.error("Dataset quality is poor. Fix missing values and anomalies before BI use.")

#     anomaly_col1, anomaly_col2, anomaly_col3, anomaly_col4, anomaly_col5 = st.columns(5)
#     anomaly_counts = [
#         (anomaly_col1, "Duplicate Invoices", len(anomalies["duplicate_invoices"])),
#         (anomaly_col2, "Negative Balances", len(anomalies["negative_balances"])),
#         (anomaly_col3, "Missing GST", len(anomalies["missing_gst"])),
#         (anomaly_col4, "Zero Value", len(anomalies["zero_value_invoices"])),
#         (anomaly_col5, "Future Dates", len(anomalies["future_dates"])),
#     ]

#     for column, title, count in anomaly_counts:
#         with column:
#             st.metric(title, format_count(count))


# def render_details(filtered_df, anomalies, metrics, options, selected_page):
#     # selected_page = "Charts"
#     # if ui:
#     #     selected_page = ui.tabs(
#     #         options=["Charts", "Quality", "Insights", "Data", "Export"],
#     #         default_value="Charts",
#     #         key="main_tabs",
#     #     )
#     # else:
#     #     selected_page = st.radio(
#     #         "Workspace",
#     #         ["Charts", "Quality", "Insights", "Data", "Export"],
#     #         horizontal=True,
#     #         label_visibility="collapsed",
#     #     )

#     quality_scores = calculate_data_quality_scores(filtered_df, anomalies)

#     if selected_page == "Analytics":
#         render_charts(filtered_df)
#     elif selected_page == "Quality":
#         render_quality(quality_scores, anomalies)

#         if options["anomalies"]:
#             section_title("Anomaly Records", "Review the records behind the counts.")
#             anomaly_tables = {
#                 "Duplicate invoices": anomalies["duplicate_invoices"],
#                 "Negative balances": anomalies["negative_balances"],
#                 "Missing GST": anomalies["missing_gst"],
#                 "Zero value invoices": anomalies["zero_value_invoices"],
#                 "Future dates": anomalies["future_dates"],
#             }
#             for label, table in anomaly_tables.items():
#                 with st.expander(f"{label} ({format_count(len(table))})"):
#                     show_aggrid(table)
#                 # with st.expander(f"{label} ({format_count(len(table))})"):
#                     # st.dataframe(table, use_container_width=True, hide_index=True)

#     elif selected_page == "Insights":
#         section_title("Business Insights", "Narrative signals generated from the active dataset.")
#         if options["insights"]:
#             insights = generate_business_insights(filtered_df, metrics, anomalies)
#             for insight in insights:
#                 st.markdown(
#                     f'<div class="insight-item">{insight}</div>',
#                     unsafe_allow_html=True,
#                 )
#         else:
#             st.info("Enable Business insights in the sidebar to view this section.")

#     elif selected_page == "Dashboard":
#         if options["preview"]:
#             display_cleaned_data(
#         filtered_df,
#         title="Cleaned Data Preview",
#         caption="Interactive view with zoom, row selection, and column filtering."
#     )
#             # st.dataframe(
#                 # filtered_df.head(50), use_container_width=True, hide_index=True
#             # )
#         else:
#             st.info("Enable Data preview in the sidebar to view this section.")

#         if options["column_info"]:
#             section_title(
#                 "Column Information", "Data types and missing values by field."
#             )
#             column_info = pd.DataFrame(
#                 {
#                     "Column": filtered_df.columns,
#                     "Data Type": [str(dtype) for dtype in filtered_df.dtypes],
#                     "Missing Values": filtered_df.isnull().sum().values,
#                 }
#             )
#             # st.dataframe(column_info, use_container_width=True, hide_index=True)
#             show_aggrid(column_info)

#         if options["primary_key"] and "primary_key" in filtered_df.columns:
#             section_title("Primary Key Validation", "Deterministic row identifiers.")
#             duplicate_keys = filtered_df["primary_key"].duplicated().sum()
#             if duplicate_keys == 0:
#                 st.success("All primary keys are unique.")
#             else:
#                 st.warning(f"{duplicate_keys} duplicate primary keys detected.")
#             # st.dataframe(
#             #     filtered_df[["primary_key"]].head(20),
#             #     use_container_width=True,
#             #     hide_index=True,
#             # )
#             show_aggrid(filtered_df[["primary_key"]].head(20))

#     elif selected_page == "Export":
#         render_export(filtered_df)

#     elif selected_page == "Power BI":
#         section_title(
#             "Power BI Dashboard",
#             "Open the Tally Power BI template and refresh the dataset.",
#         )
#         if st.button("Open Power BI dashboard", use_container_width=True):
#             powerbi_file = (
#                 Path(__file__).resolve().parent.parent
#                 / "powerbi"
#                 / "templates"
#                 / "Tally_Dashboard.pbix"
#             )
#             os.startfile(str(powerbi_file))
#             st.success("Power BI dashboard opened.")


# def render_export(filtered_df):
#     section_title(
#         "Export Cleaned Dataset",
#         "Download CSV, save Parquet, and refresh the Power BI dataset file.",
#     )

#     ensure_export_directories()
#     csv_filename = generate_export_filename("cleaned_tally_data", "csv")
#     parquet_filename = generate_export_filename("cleaned_tally_data", "parquet")
#     csv_path = f"data/exports/{csv_filename}"
#     parquet_path = f"data/exports/{parquet_filename}"
#     powerbi_dataset_path = "powerbi/datasets/cleaned_tally_data.csv"

#     filtered_df.to_csv(csv_path, index=False)
#     filtered_df.to_parquet(parquet_path, index=False)
#     filtered_df.to_csv(powerbi_dataset_path, index=False)

#     actions_col1, actions_col2 = st.columns(2)
#     with actions_col1:
#         st.markdown(
#             """
#             <div class="action-card">
#                 <div class="action-card">
#                     ⬇ Export Cleaned CSV
#                 </div>

#                 <div class="action-desc">
#                     Download the cleaned dataset as a CSV file for use in other tools or manual review.
#                 </div>
#             </div>
#             """,
#             unsafe_allow_html=True,
#         )
#         st.download_button(
#             label="Download cleaned CSV",
#             data=filtered_df.to_csv(index=False).encode("utf-8"),
#             file_name=csv_filename,
#             mime="text/csv",
#             use_container_width=True,
#         )
#     with actions_col2:
#         st.markdown(
#             """
#             <div class="action-card">
#                 <div class="action-title">
#                     📊 Open Power BI Dashboard
#                 </div>
#                 <div class="action-desc">
#                     Open the Tally Power BI template. The dataset will be updated with the cleaned data on refresh.
#                 </div>
#             </div>
#             """,
#             unsafe_allow_html=True,
#         )
#         if st.button("Open Power BI dashboard", use_container_width=True):
#             powerbi_file = (
#                 Path(__file__).resolve().parent.parent
#                 / "powerbi"
#                 / "templates"
#                 / "Tally_Dashboard.pbix"
#             )
#             os.startfile(str(powerbi_file))
#             st.success("Power BI dashboard opened.")
#     st.success("CSV, Parquet, and Power BI dataset exports generated successfully.")
#     st.caption(f"Saved: {csv_path}, {parquet_path}, {powerbi_dataset_path}")

#     # export_col1, export_col2 = st.columns([1, 1])
#     # with export_col1:
#     #     st.download_button(
#     #         label="Download cleaned CSV",
#     #         data=filtered_df.to_csv(index=False).encode("utf-8"),
#     #         file_name=csv_filename,
#     #         mime="text/csv",
#     #         use_container_width=True,
#     #     )
#     # with export_col2:
#     #     if st.button("Open Power BI dashboard", use_container_width=True):
#     #         powerbi_file = (
#     #             Path(__file__).resolve().parent.parent
#     #             / "powerbi"
#     #             / "templates"
#     #             / "Tally_Dashboard.pbix"
#     #         )
#     #         os.startfile(str(powerbi_file))
#     #         st.success("Power BI dashboard opened.")


# def empty_state():
#     st.markdown(
#         """
#         <div class="empty-state">
#             <h3>🚀 Start Your Financial Intelligence Workflow</h3>
#             <p>
#                 The app will clean column names, normalize dates and currency fields,
#                 standardize master data, generate row keys, detect anomalies, calculate
#                 business KPIs, and prepare the dataset for Power BI.
#             </p>
#         </div>
#         """,
#         unsafe_allow_html=True,
#     )


# def main():
#     inject_styles()
#     uploaded_file, options, selected_page, theme = render_sidebar()
#     hero()

#     if not uploaded_file:
#         empty_state()
#         return

#     try:
#         logger.info(f"File uploaded: {uploaded_file.name}")
#         raw_df = read_uploaded_file(uploaded_file)
#         cleaned_df = run_cleaning_pipeline(raw_df)
#         filtered_df = apply_sidebar_filters(cleaned_df)

#         st.success("File loaded, cleaned, and ready for review.")

#         render_dataset_metrics(filtered_df, cleaned_df)

#         metrics = calculate_dashboard_metrics(filtered_df)
#         anomalies = normalize_anomalies(detect_anomalies(filtered_df))

#         render_business_metrics(metrics)
#         render_details(filtered_df, anomalies, metrics, options, selected_page)

#         logger.info("Tally Smoothener dashboard rendered successfully.")

#     except Exception as exc:
#         logger.error(f"Error while processing file: {exc}")
#         st.error("An error occurred while processing the file.")
#         st.exception(exc)


# if __name__ == "__main__":
#     main()
####################################################################################################################
#####################################################################################################################
import os
import io
import sys
from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st
from loguru import logger

try:
    import streamlit_shadcn_ui as ui
except ImportError:
    ui = None

sys.path.append(str(Path(__file__).resolve().parent.parent))

from engine.analytics.anomaly_detector import detect_anomalies
from engine.analytics.dashboard_analytics import calculate_dashboard_metrics
from engine.analytics.insight_engine import generate_business_insights
from engine.transformers.data_pipeline import run_cleaning_pipeline
from engine.transformers.export_engine import (
    ensure_export_directories,
    generate_export_filename,
)
import streamlit as st
from st_aggrid import AgGrid
from st_aggrid import GridOptionsBuilder

st.set_page_config(
    page_title="BIReady Tally",
    page_icon="BT",
    layout="wide",
    initial_sidebar_state="expanded",
)

Path("logs").mkdir(exist_ok=True)
try:
    logger.add(
        Path("logs/app.log"),
        rotation="1 MB",
        retention="5 days",
        level="INFO",
        enqueue=True,
    )
except PermissionError:
    logger.warning("File logging is unavailable because logs/app.log is locked.")


def inject_styles(theme="Light"):
    if theme == "Dark":

        app_bg = "#0B1220"
        panel = "#111827"
        ink = "#F9FAFB"
        muted = "#9CA3AF"
        line = "#374151"
    else:

        app_bg = "#F7F8FB"
        panel = "#FFFFFF"
        ink = "#111827"
        muted = "#6B7280"
        line = "#E5E7EB"

    st.markdown(
        f"""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
            

            :root {{
                --app-bg: {app_bg};
                --panel: {panel};
                --ink: {ink};
                --muted: {muted};
                --line: {line};
                --accent: #2563eb;
                --accent-soft: #dbeafe;
                --success: #059669;
                --warning: #d97706;
                --danger: #dc2626;
            }}

            html, body, [class*="css"] {{
                font-family: "Inter", system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
            }}

            .stApp {{
                background: var(--app-bg);
            }}

            section[data-testid="stSidebar"] {{
                background: #ffffff;
                border-right: 1px solid var(--line);
            }}

            section[data-testid="stSidebar"] div[data-testid="stMarkdownContainer"] p {{
                color: var(--muted);
            }}

            .block-container {{
                padding-top: 1.6rem;
                padding-bottom: 2.4rem;
                max-width: 1440px;
            }}

            h1, h2, h3 {{
                color: var(--ink);
                letter-spacing: 0;
            }}

            div[data-testid="stMetric"] {{
                background: var(--panel);
                border: 1px solid var(--line);
                border-radius: 16px;
                padding: 20px;
                box-shadow: 0 12px 32px rgba(17, 24, 39, 0.08);
                transition: all 0.25s ease;
            }}

            div[data-testid="stMetricLabel"] p {{
                color: var(--muted);
                font-size: 0.85rem;
                font-weight: 600;
            }}

            div[data-testid="stMetricValue"] {{
                color: var(--ink);
                font-weight: 800;
            }}

            div[data-testid="stFileUploader"] {{
                background: #ffffff;
                border: 1px dashed #cbd5e1;
                border-radius: 8px;
                padding: 12px;
            }}

            .hero {{
                background: #ffffff;
                border: 1px solid var(--line);
                border-radius: 16px;
                padding: 48px 50px;
                box-shadow: 0 12px 32px rgba(15, 23, 42, 0.05);
                margin-bottom: 24px;
            }}

            .hero-kicker {{
                color: var(--accent);
                font-size: 0.78rem;
                font-weight: 800;
                letter-spacing: 0.08em;
                text-transform: uppercase;
                margin-bottom: 8px;
            }}

            .hero-title {{
                color: var(--ink);
                font-size: clamp(3rem, 6vw, 5rem);
                font-weight: 900;
                line-height: 1;
                margin: 0;
                letter-spacing: -0.04em;
            }}

            .hero-copy {{
                color: var(--muted);
                font-size: 1rem;
                line-height: 1.7;
                max-width: 780px;
                margin-top: 12px;
                margin-bottom: 0;
            }}

            .section-title {{
                display: flex;
                align-items: center;
                justify-content: space-between;
                gap: 16px;
                margin: 22px 0 12px;
            }}  

            .section-title h2 {{
                font-size: 1.18rem;
                font-weight: 800;
                margin: 0;
            }}

            .section-title p {{
                color: var(--muted);
                font-size: 0.9rem;
                margin: 2px 0 0;
            }}

            .status-pill {{
                display: inline-flex;
                align-items: center;
                border: 1px solid var(--line);
                border-radius: 999px;
                color: var(--muted);
                font-size: 0.8rem;
                font-weight: 700;
                padding: 6px 10px;
                background: #ffffff;
                white-space: nowrap;
            }}

            .empty-state {{
                background: #ffffff;
                border: 1px solid var(--line);
                border-radius: 8px;
                padding: 42px 34px;
                text-align: center;
                box-shadow: 0 12px 32px rgba(15, 23, 42, 0.04);
            }}

            .empty-state h3 {{
                font-size: 1.4rem;
                font-weight: 800;
                margin-bottom: 8px;
            }}

            .empty-state p {{
                color: var(--muted);
                margin: 0 auto;
                max-width: 620px;
                line-height: 1.7;
            }}  

            .info-panel {{
                background: #ffffff;
                border: 1px solid var(--line);
                border-radius: 8px;
                padding: 18px;
                box-shadow: 0 8px 24px rgba(15, 23, 42, 0.04);
            }}

            .insight-item {{
                border: 1px solid var(--line);
                border-left: 4px solid var(--accent);
                border-radius: 8px;
                background: #ffffff;
                padding: 14px 16px;
                margin-bottom: 10px;
                color: var(--ink);
                font-weight: 500;
            }}  

            .small-note {{
                color: var(--muted);
                font-size: 0.84rem;
                line-height: 1.55;
            }}

            .stPlotlyChart {{
                background: #ffffff;
                border: 1px solid var(--line);
                border-radius: 8px;
                padding: 10px;
                box-shadow: 0 8px 24px rgba(15, 23, 42, 0.04);
            }}

            .ag-theme-streamlit {{
                border-radius: 16px !important;
                overflow: hidden !important;
            }}

            .chart-panel {{
                background: #ffffff;
                border: 1px solid var(--line);
                border-radius: 16px;
                padding: 16px;
                margin-bottom: 18px;
                box-shadow: 0 12px 32px rgba(15, 23, 42, 0.06);
            }}

            .action-card {{
                background: #ffffff;
                border: 1px solid var(--line);
                border-radius: 18px;
                padding: 28px;
                text-align: center;
                box-shadow: 0 12px 32px rgba(15, 23, 42, 0.06);
                margin-bottom: 16px;
            }}  

            .action-title {{
                font-size: 1.2rem;
                font-weight: 800;
                color: var(--ink);
                margin-bottom: 8px;
            }}  

           .action-desc {{
                color: var(--muted);
                font-size: 0.9rem;
                margin-bottom: 18px;
            }}
            .data-controls {{
                background: var(--panel);
                border: 1px solid var(--line);
                border-radius: 12px;
                padding: 16px;
                margin-bottom: 18px;
                box-shadow: 0 4px 12px rgba(15, 23, 42, 0.04);
            }} 
            .dataframe-wrapper {{
                border-radius: 12px;
                overflow: hidden;
                border: 1px solid var(--line);
                background: var(--panel);
                box-shadow: 0 4px 12px rgba(15, 23, 42, 0.04);
            }}
            [data-testid="stDataFrame"] {{
                max-height: 700px !important;
                overflow-y: auto !important;
            }}
              
        </style>
        """,
        unsafe_allow_html=True,
    )


def hero():
    st.markdown(
        """
        <div class="hero">
            <div class="hero-kicker"></div>
            <h1 class="hero-title">Clean finance data. Review quality. Export with confidence.</h1>
            <p class="hero-copy">
                Upload a raw Tally export and turn it into a clean, BI-ready dataset with validation,
                anomaly checks, quality scoring, business KPIs, and Power BI handoff in one workflow.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def section_title(title, caption=None, status=None):
    caption_html = f"<p>{caption}</p>" if caption else ""
    status_html = f'<span class="status-pill">{status}</span>' if status else ""
    st.markdown(
        f"""
        <div class="section-title">
            <div>
                <h2>{title}</h2>
                {caption_html}
            </div>
            {status_html}
        </div>
        """,
        unsafe_allow_html=True,
    )


def shad_metric(title, value, description, key):
    if ui:
        ui.metric_card(
            title=title,
            content=str(value),
            description=description,
            key=key,
        )
    else:
        st.metric(title, value, help=description)


def format_currency(value):
    return f"Rs. {value:,.2f}"


def format_count(value):
    return f"{int(value):,}"


def plot_style(fig):
    fig.update_layout(
        template="plotly_white",
        font=dict(family="Inter, Arial", color="#111827"),
        title_font=dict(size=16, color="#111827"),
        margin=dict(l=20, r=20, t=48, b=20),
        paper_bgcolor="#ffffff",
        plot_bgcolor="#ffffff",
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
    )
    fig.update_xaxes(showgrid=False, zeroline=False)
    fig.update_yaxes(gridcolor="#eef2f7", zeroline=False)
    return fig


def display_cleaned_data(
    df_cleaned,
    title="Cleaned Data Preview",
    caption="First 50 records from the active dataset.",
):
    """
    Display cleaned data with interactive controls for zoom, row selection,
    and column selection.

    Parameters:
    -----------
    df_cleaned : pd.DataFrame
        The cleaned dataframe to display
    title : str
        Title for the data section
    caption : str
        Subtitle/caption text
    """

    section_title(title, caption)

    # =========== CONTROL ROW: Zoom, Rows, Columns ===========
    st.markdown('<div class="data-controls">', unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 1.5, 2], gap="medium")

    with col1:
        zoom_level = st.slider(
            "🔍 Zoom Level",
            min_value=50,
            max_value=150,
            value=100,
            step=10,
            key=f"zoom_slider_{title}",
            help="Zoom in/out to adjust text size (50%-150%)",
        )

    with col2:
        num_rows = st.selectbox(
            "📋 Rows",
            options=[10, 25, 50, 100, 250, "All"],
            index=2,
            key=f"row_selector_{title}",
            help="How many rows to display?",
        )

    with col3:
        all_columns = df_cleaned.columns.tolist()
        selected_columns = st.multiselect(
            "🏷️ Columns",
            options=all_columns,
            default=all_columns,
            key=f"column_selector_{title}",
            help="Select which columns to show",
        )

    st.markdown("</div>", unsafe_allow_html=True)

    # =========== APPLY FILTERS ===========
    df_display = df_cleaned[selected_columns].copy()

    if num_rows != "All":
        df_display = df_display.head(int(num_rows))

    df_display = df_display.reset_index(drop=True)
    df_display.index = df_display.index + 1  # 1-based indexing

    # =========== METRICS ROW ===========
    metric_col1, metric_col2, metric_col3, metric_col4 = st.columns(4)

    with metric_col1:
        st.metric(
            "Total Records", format_count(len(df_cleaned)), help="Original dataset size"
        )

    with metric_col2:
        st.metric("Displayed", format_count(len(df_display)), help="Current view")

    with metric_col3:
        st.metric(
            "Columns",
            format_count(len(selected_columns)),
            help=f"Out of {len(df_cleaned.columns)} total",
        )

    with metric_col4:
        missing = df_display.isnull().sum().sum()
        st.metric("Missing", format_count(missing), help="Empty cells")

    # =========== DISPLAY DATAFRAME ===========
    st.markdown('<div class="dataframe-wrapper">', unsafe_allow_html=True)

    st.dataframe(df_display, use_container_width=True, height=700, hide_index=False)

    st.markdown("</div>", unsafe_allow_html=True)

    # =========== DATA INFO EXPANDER ===========
    with st.expander("📋 Column Details & Statistics", expanded=False):
        col_info = pd.DataFrame(
            {
                "Column": selected_columns,
                "Type": [str(df_display[col].dtype) for col in selected_columns],
                "Non-Null": [df_display[col].notna().sum() for col in selected_columns],
                "Null": [df_display[col].isna().sum() for col in selected_columns],
                "Unique": [df_display[col].nunique() for col in selected_columns],
            }
        )
        st.dataframe(col_info, use_container_width=True, hide_index=True)

    # =========== EXPORT OPTIONS ===========
    st.markdown("---")

    col_exp1, col_exp2, col_exp3 = st.columns(3)

    with col_exp1:
        csv = df_display.to_csv(index=False)
        st.download_button(
            label="📥 CSV",
            data=csv,
            file_name="cleaned_data_preview.csv",
            mime="text/csv",
            key=f"download_csv_{title}",
        )

    with col_exp2:
        excel_buffer = io.BytesIO()
        df_display.to_excel(excel_buffer, index=False, engine="openpyxl")
        excel_buffer.seek(0)
        st.download_button(
            label="📥 Excel",
            data=excel_buffer,
            file_name="cleaned_data_preview.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            key=f"download_excel_{title}",
        )

    with col_exp3:
        json_data = df_display.to_json(orient="records", indent=2)
        st.download_button(
            label="📥 JSON",
            data=json_data,
            file_name="cleaned_data_preview.json",
            mime="application/json",
            key=f"download_json_{title}",
        )


def show_aggrid(df):

    gb = GridOptionsBuilder.from_dataframe(df)

    gb.configure_default_column(sortable=True, filter=True, resizable=True)

    gb.configure_pagination(paginationAutoPageSize=True)

    grid_options = gb.build()

    AgGrid(df, gridOptions=grid_options, fit_columns_on_grid_load=True, height=450)


def read_uploaded_file(uploaded_file):
    if uploaded_file.name.lower().endswith(".csv"):
        return pd.read_csv(uploaded_file)
    return pd.read_excel(uploaded_file)


def normalize_anomalies(anomalies):
    expected_keys = [
        "duplicate_invoices",
        "negative_balances",
        "missing_gst",
        "zero_value_invoices",
        "future_dates",
    ]
    for key in expected_keys:
        if key not in anomalies:
            anomalies[key] = pd.DataFrame()
    return anomalies


def apply_sidebar_filters(df):
    filtered_df = df.copy()

    with st.sidebar:
        st.markdown("### Filters")
        st.caption("Refine the cleaned dataset before reviewing KPIs or exporting.")

        if "invoice_date" in filtered_df.columns:
            filtered_df["invoice_date"] = pd.to_datetime(
                filtered_df["invoice_date"],
                errors="coerce",
            )
            min_date = filtered_df["invoice_date"].min()
            max_date = filtered_df["invoice_date"].max()

            if pd.notnull(min_date) and pd.notnull(max_date):
                date_range = st.date_input(
                    "Invoice date range",
                    value=(min_date, max_date),
                )

                if len(date_range) == 2:
                    start_date, end_date = date_range
                    filtered_df = filtered_df[
                        (filtered_df["invoice_date"] >= pd.to_datetime(start_date))
                        & (filtered_df["invoice_date"] <= pd.to_datetime(end_date))
                    ]

        filter_columns = [
            ("state", "State"),
            ("hospital_name", "Hospital"),
            ("payment_mode", "Payment mode"),
            ("product_name", "Product"),
        ]

        for column, label in filter_columns:
            if column in filtered_df.columns:
                options = sorted(filtered_df[column].dropna().astype(str).unique())
                selected = st.multiselect(
                    label,
                    options=options,
                    default=options,
                )
                filtered_df = filtered_df[
                    filtered_df[column].astype(str).isin(selected)
                ]

        search_query = st.text_input(
            "Global search",
            placeholder="Search invoice, hospital, state...",
        )

        if search_query:
            filtered_df = filtered_df[
                filtered_df.astype(str).apply(
                    lambda row: row.str.contains(
                        search_query,
                        case=False,
                        na=False,
                    ).any(),
                    axis=1,
                )
            ]

    return filtered_df


def render_sidebar():
    with st.sidebar:
        st.markdown(
            """
        <h1 style="
            font-size:2rem;
            font-weight:900;
            margin-bottom:0;
        ">
            📊 BIReady Tally 
        </h1>
        """,
            unsafe_allow_html=True,
        )
        st.caption("Professional data cleaning and BI readiness workflow.")
        theme = st.selectbox("🎨 Theme", ["Light", "Dark"], index=0)

        uploaded_file = st.file_uploader(
            "Upload Tally export",
            type=["xlsx", "xls", "csv"],
            help="Upload a CSV, XLS, or XLSX export from Tally.",
        )

        st.divider()

        selected_page = st.radio(
            "Navigation", ["Dashboard", "Analytics", "Insights", "Export"]
        )

        st.divider()

        st.markdown("### Review Options")
        options = {
            "column_info": st.toggle("Column information", value=False),
            "primary_key": st.toggle("Primary key validation", value=False),
            "anomalies": st.toggle("Anomaly details", value=True),
            "insights": st.toggle("Business insights", value=True),
            "preview": st.toggle("Data preview", value=True),
        }

        st.divider()
        if ui is None:
            st.warning(
                "streamlit-shadcn-ui is not installed yet. The app will use native Streamlit components until dependencies are installed."
            )

    return (uploaded_file, options, selected_page, theme)


def render_dataset_metrics(filtered_df, source_df):
    section_title(
        "Dataset Overview",
        "A quick read on the active filtered dataset.",
        status=f"{format_count(filtered_df.shape[0])} active rows",
    )
    col1, col2, col3, col4 = st.columns(4)
    missing_values = int(filtered_df.isnull().sum().sum())
    filtered_out = max(source_df.shape[0] - filtered_df.shape[0], 0)

    with col1:
        shad_metric(
            "Rows",
            format_count(filtered_df.shape[0]),
            "Records after filters",
            "rows_metric",
        )
    with col2:
        shad_metric(
            "Columns",
            format_count(filtered_df.shape[1]),
            "Cleaned dataset width",
            "cols_metric",
        )
    with col3:
        shad_metric(
            "Missing Values",
            format_count(missing_values),
            "Blank cells remaining",
            "missing_metric",
        )
    with col4:
        shad_metric(
            "Filtered Out",
            format_count(filtered_out),
            "Rows hidden by filters",
            "filtered_metric",
        )


def render_business_metrics(metrics):
    section_title(
        "Business KPIs",
        "Commercial summary calculated from the cleaned ledger.",
    )
    kpi1, kpi2, kpi3 = st.columns(3)
    kpi4, kpi5, kpi6 = st.columns(3)

    with kpi1:
        shad_metric(
            "Total Revenue",
            format_currency(metrics["total_revenue"]),
            "Credit amount for sales vouchers",
            "revenue_metric",
        )
    with kpi2:
        shad_metric(
            "Procurement Cost",
            format_currency(metrics["procurement_cost"]),
            "Debit amount for purchase vouchers",
            "procurement_metric",
        )
    with kpi3:
        shad_metric(
            "Gross Profit",
            format_currency(metrics["gross_profit"]),
            "Revenue minus procurement cost",
            "profit_metric",
        )
    with kpi4:
        shad_metric(
            "Profit Margin",
            f"{metrics['profit_margin']:.2f}%",
            "Gross profit as a percentage of revenue",
            "margin_metric",
        )
    with kpi5:
        shad_metric(
            "Total Invoices",
            format_count(metrics["total_invoices"]),
            "Records in the active dataset",
            "invoice_metric",
        )
    with kpi6:
        shad_metric(
            "Unique Hospitals",
            format_count(metrics["unique_hospitals"]),
            "Distinct hospital accounts",
            "hospital_metric",
        )


def render_charts(filtered_df):
    section_title(
        "Business Charts",
        "Revenue, customer, geography, and payment views.",
    )

    chart_col1, chart_col2 = st.columns(2)

    with chart_col1:
        if (
            "invoice_date" in filtered_df.columns
            and "credit_amount" in filtered_df.columns
        ):
            revenue_df = filtered_df.copy()
            revenue_df["invoice_date"] = pd.to_datetime(
                revenue_df["invoice_date"],
                errors="coerce",
            )
            revenue_df = revenue_df.dropna(subset=["invoice_date"])
            revenue_df["month"] = revenue_df["invoice_date"].dt.strftime("%Y-%m")
            monthly_revenue = (
                revenue_df.groupby("month")["credit_amount"].sum().reset_index()
            )
            fig = px.line(
                monthly_revenue,
                x="month",
                y="credit_amount",
                markers=True,
                title="Monthly Revenue Trend",
            )
            # st.plotly_chart(plot_style(fig), use_container_width=True)
            st.markdown('<div class="chart-panel">', unsafe_allow_html=True)

            st.plotly_chart(plot_style(fig), use_container_width=True)

            st.markdown("</div>", unsafe_allow_html=True)
        else:
            st.info("Invoice date and credit amount are required for revenue trend.")

    with chart_col2:
        if "payment_mode" in filtered_df.columns:
            payment_mode_df = filtered_df["payment_mode"].value_counts().reset_index()
            payment_mode_df.columns = ["payment_mode", "count"]
            fig = px.pie(
                payment_mode_df,
                names="payment_mode",
                values="count",
                hole=0.50,
                # title="Payment Mode Distribution",
                color_discrete_sequence=px.colors.qualitative.Set2,
            )

            fig.update_layout(
                title={
                    "text": "<b>Payment Mode Distribution</b>",
                    "x": 0.02,
                    "xanchor": "left",
                    "font": {
                        "size": 22,
                        "color": "#111827",
                        "family": "Inter"
                    }
                },
                height=600,
                margin=dict(t=70, b=20, l=20, r=20),
                legend=dict(
                    orientation="h",
                    yanchor="bottom",
                    y=0.20,
                    xanchor="center",
                    x=0.5,
                    font=dict(size=12),
                ),
                paper_bgcolor="white",
                plot_bgcolor="white",
            )
            fig.update_traces(
                textinfo="percent",
                textfont_size=14,
                hovertemplate="<b>%{label}</b><br>%{percent}<extra></extra>",
            )
            st.plotly_chart(plot_style(fig), use_container_width=True)
        else:
            st.info("Payment mode is required for payment distribution.")

    chart_col3, chart_col4 = st.columns(2)

    with chart_col3:
        if "state" in filtered_df.columns and "credit_amount" in filtered_df.columns:
            state_sales = (
                filtered_df.groupby("state")["credit_amount"]
                .sum()
                .sort_values(ascending=False)
                .reset_index()
            )
            fig = px.bar(
                state_sales,
                x="state",
                y="credit_amount",
                title="State-wise Revenue",
                color="credit_amount",
                color_continuous_scale="Blues",
            )
            st.plotly_chart(plot_style(fig), use_container_width=True)
        else:
            st.info("State and credit amount are required for state-wise revenue.")

    with chart_col4:
        if (
            "hospital_name" in filtered_df.columns
            and "credit_amount" in filtered_df.columns
        ):
            top_hospitals = (
                filtered_df.groupby("hospital_name")["credit_amount"]
                .sum()
                .sort_values(ascending=False)
                .head(10)
                .reset_index()
            )
            fig = px.bar(
                top_hospitals,
                x="credit_amount",
                y="hospital_name",
                title="Top Hospitals by Revenue",
                orientation="h",
                color="credit_amount",
                color_continuous_scale="Teal",
            )
            fig.update_layout(yaxis=dict(autorange="reversed"))
            st.plotly_chart(plot_style(fig), use_container_width=True)
        else:
            st.info("Hospital name and credit amount are required for top hospitals.")


def render_details(filtered_df, anomalies, metrics, options, selected_page):
    # selected_page = "Charts"
    # if ui:
    #     selected_page = ui.tabs(
    #         options=["Charts", "Quality", "Insights", "Data", "Export"],
    #         default_value="Charts",
    #         key="main_tabs",
    #     )
    # else:
    #     selected_page = st.radio(
    #         "Workspace",
    #         ["Charts", "Quality", "Insights", "Data", "Export"],
    #         horizontal=True,
    #         label_visibility="collapsed",
    #     )

    if selected_page == "Analytics":
        render_charts(filtered_df)
    elif selected_page == "Insights":
        section_title(
            "Business Insights", "Narrative signals generated from the active dataset."
        )
        if options["insights"]:
            insights = generate_business_insights(filtered_df, metrics, anomalies)
            for insight in insights:
                st.markdown(
                    f'<div class="insight-item">{insight}</div>',
                    unsafe_allow_html=True,
                )
        else:
            st.info("Enable Business insights in the sidebar to view this section.")

    elif selected_page == "Dashboard":
        if options["preview"]:
            display_cleaned_data(
                filtered_df,
                title="Cleaned Data Preview",
                caption="Interactive view with zoom, row selection, and column filtering.",
            )
            # st.dataframe(
            # filtered_df.head(50), use_container_width=True, hide_index=True
            # )
        else:
            st.info("Enable Data preview in the sidebar to view this section.")

        if options["column_info"]:
            section_title(
                "Column Information", "Data types and missing values by field."
            )
            column_info = pd.DataFrame(
                {
                    "Column": filtered_df.columns,
                    "Data Type": [str(dtype) for dtype in filtered_df.dtypes],
                    "Missing Values": filtered_df.isnull().sum().values,
                }
            )
            # st.dataframe(column_info, use_container_width=True, hide_index=True)
            show_aggrid(column_info)

        if options["primary_key"] and "primary_key" in filtered_df.columns:
            section_title("Primary Key Validation", "Deterministic row identifiers.")
            duplicate_keys = filtered_df["primary_key"].duplicated().sum()
            if duplicate_keys == 0:
                st.success("All primary keys are unique.")
            else:
                st.warning(f"{duplicate_keys} duplicate primary keys detected.")
            # st.dataframe(
            #     filtered_df[["primary_key"]].head(20),
            #     use_container_width=True,
            #     hide_index=True,
            # )
            show_aggrid(filtered_df[["primary_key"]].head(20))

    elif selected_page == "Export":
        render_export(filtered_df)

    elif selected_page == "Power BI":
        section_title(
            "Power BI Dashboard",
            "Open the Tally Power BI template and refresh the dataset.",
        )
        if st.button("Open Power BI dashboard", use_container_width=True):
            powerbi_file = (
                Path(__file__).resolve().parent.parent
                / "powerbi"
                / "templates"
                / "Tally_Dashboard.pbix"
            )
            os.startfile(str(powerbi_file))
            st.success("Power BI dashboard opened.")


def render_export(filtered_df):
    section_title(
        "Export Cleaned Dataset",
        "Download CSV, save Parquet, and refresh the Power BI dataset file.",
    )

    ensure_export_directories()
    csv_filename = generate_export_filename("cleaned_tally_data", "csv")
    parquet_filename = generate_export_filename("cleaned_tally_data", "parquet")
    csv_path = f"data/exports/{csv_filename}"
    parquet_path = f"data/exports/{parquet_filename}"
    powerbi_dataset_path = "powerbi/datasets/cleaned_tally_data.csv"

    filtered_df.to_csv(csv_path, index=False)
    filtered_df.to_parquet(parquet_path, index=False)
    filtered_df.to_csv(powerbi_dataset_path, index=False)

    actions_col1, actions_col2 = st.columns(2)
    with actions_col1:
        st.markdown("""
        <div class="action-card">
            <div>
                <div class="action-icon">📥</div>
                <div class="action-title">Export Cleaned CSV</div>
                <div class="action-desc">
                    Download the cleaned and validated dataset ready for reporting,
                    analysis, and Power BI integration.
                </div>
            </div>
        </div>
            """,
            unsafe_allow_html=True,
        )
        st.download_button(
            label="Download cleaned CSV",
            data=filtered_df.to_csv(index=False).encode("utf-8"),
            file_name=csv_filename,
            mime="text/csv",
            use_container_width=True,
        )
    with actions_col2:
        st.markdown(
            """
            <div class="action-card">
                <div>
                    <div class="action-icon">📊</div>
                    <div class="action-title">Launch Power BI</div>
                    <div class="action-desc">
                        Open the Power BI dashboard template and refresh
                        it with the latest cleaned dataset.
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        if st.button("Open Power BI dashboard", use_container_width=True):
            powerbi_file = (
                Path(__file__).resolve().parent.parent
                / "powerbi"
                / "templates"
                / "Tally_Dashboard.pbix"
            )
            os.startfile(str(powerbi_file))
            st.success("Power BI dashboard opened.")
    st.success("CSV, Parquet, and Power BI dataset exports generated successfully.")
    st.caption(f"Saved: {csv_path}, {parquet_path}, {powerbi_dataset_path}")

    # export_col1, export_col2 = st.columns([1, 1])
    # with export_col1:
    #     st.download_button(
    #         label="Download cleaned CSV",
    #         data=filtered_df.to_csv(index=False).encode("utf-8"),
    #         file_name=csv_filename,
    #         mime="text/csv",
    #         use_container_width=True,
    #     )
    # with export_col2:
    #     if st.button("Open Power BI dashboard", use_container_width=True):
    #         powerbi_file = (
    #             Path(__file__).resolve().parent.parent
    #             / "powerbi"
    #             / "templates"
    #             / "Tally_Dashboard.pbix"
    #         )
    #         os.startfile(str(powerbi_file))
    #         st.success("Power BI dashboard opened.")


def empty_state():
    st.markdown(
        """
        <div class="empty-state">
            <h3>🚀 Start Your Financial Intelligence Workflow</h3>
            <p>
                The app will clean column names, normalize dates and currency fields,
                standardize master data, generate row keys, detect anomalies, calculate
                business KPIs, and prepare the dataset for Power BI.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def main():
    inject_styles()
    uploaded_file, options, selected_page, theme = render_sidebar()
    hero()

    if not uploaded_file:
        empty_state()
        return

    try:
        logger.info(f"File uploaded: {uploaded_file.name}")
        raw_df = read_uploaded_file(uploaded_file)
        cleaned_df = run_cleaning_pipeline(raw_df)
        filtered_df = apply_sidebar_filters(cleaned_df)

        st.success("File loaded, cleaned, and ready for review.")

        render_dataset_metrics(filtered_df, cleaned_df)

        metrics = calculate_dashboard_metrics(filtered_df)
        anomalies = normalize_anomalies(detect_anomalies(filtered_df))

        render_business_metrics(metrics)
        render_details(filtered_df, anomalies, metrics, options, selected_page)

        logger.info("BIReady Tally dashboard rendered successfully.")

    except Exception as exc:
        logger.error(f"Error while processing file: {exc}")
        st.error("An error occurred while processing the file.")
        st.exception(exc)


if __name__ == "__main__":
    main()
