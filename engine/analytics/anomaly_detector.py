import pandas as pd


def detect_anomalies(df: pd.DataFrame):

    anomalies = {}

    # =====================================================
    # DUPLICATE INVOICES
    # =====================================================

    if "invoice_number" in df.columns:

        duplicate_invoices = df[
            df["invoice_number"].duplicated()
        ]

        anomalies["duplicate_invoices"] = duplicate_invoices

    # =====================================================
    # NEGATIVE BALANCES
    # =====================================================

    if "outstanding_balance" in df.columns:

        negative_balances = df[
            df["outstanding_balance"] < 0
        ]

        anomalies["negative_balances"] = negative_balances

    # =====================================================
    # MISSING GST NUMBERS
    # =====================================================

    if "gst_number" in df.columns:

        missing_gst = df[
            df["gst_number"].isnull()
        ]

        anomalies["missing_gst"] = missing_gst

    # =====================================================
    # ZERO VALUE INVOICES
    # =====================================================

    if "debit_amount" in df.columns:

        zero_value = df[
            df["debit_amount"] == 0
        ]

        anomalies["zero_value_invoices"] = zero_value

    # =====================================================
    # FUTURE DATES
    # =====================================================

    if "invoice_date" in df.columns:

        future_dates = df[
            df["invoice_date"] > pd.Timestamp.today()
        ]

        anomalies["future_dates"] = future_dates

    return anomalies