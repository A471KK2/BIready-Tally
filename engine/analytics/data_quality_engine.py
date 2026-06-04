import pandas as pd


def calculate_data_quality_scores(
    df: pd.DataFrame,
    anomalies: dict
):

    scores = {}

    total_cells = (
        df.shape[0] * df.shape[1]
    )

    # =====================================================
    # COMPLETENESS SCORE
    # =====================================================

    missing_cells = (
        df.isnull().sum().sum()
    )

    completeness_score = (
        1 - (missing_cells / total_cells)
    ) * 100

    scores["completeness_score"] = round(
        completeness_score,
        2
    )

    # =====================================================
    # CONSISTENCY SCORE
    # =====================================================

    consistency_score = 100

    # State inconsistency check
    if "state" in df.columns:

        unique_states = (
            df["state"]
            .astype(str)
            .str.lower()
            .nunique()
        )

        if unique_states > 15:

            consistency_score -= 15

    scores["consistency_score"] = round(
        consistency_score,
        2
    )

    # =====================================================
    # COMPLIANCE SCORE
    # =====================================================

    missing_gst = len(
        anomalies["missing_gst"]
    )

    compliance_penalty = (
        missing_gst * 0.5
    )

    compliance_score = max(
        0,
        100 - compliance_penalty
    )

    scores["compliance_score"] = round(
        compliance_score,
        2
    )

    # =====================================================
    # ANOMALY SEVERITY SCORE
    # =====================================================

    duplicate_invoices = len(
        anomalies["duplicate_invoices"]
    )

    negative_balances = len(
        anomalies["negative_balances"]
    )

    zero_value = len(
        anomalies["zero_value_invoices"]
    )

    future_dates = len(
        anomalies["future_dates"]
    )

    anomaly_penalty = (
        duplicate_invoices * 0.05
        + negative_balances * 0.1
        + zero_value * 0.03
        + future_dates * 0.05
    )

    anomaly_score = max(
        0,
        100 - anomaly_penalty
    )

    scores["anomaly_score"] = round(
        anomaly_score,
        2
    )

    # =====================================================
    # BI READINESS SCORE
    # =====================================================

    readiness_score = 100

    critical_columns = [

        "invoice_date",
        "credit_amount",
        "voucher_type",
        "hospital_name",
        "state",
        "payment_mode"

    ]

    for col in critical_columns:

        if col not in df.columns:

            readiness_score -= 10

    scores["bi_readiness_score"] = round(
        readiness_score,
        2
    )

    # =====================================================
    # OVERALL DATA QUALITY INDEX
    # =====================================================

    overall_score = (

        scores["completeness_score"]
        + scores["consistency_score"]
        + scores["compliance_score"]
        + scores["anomaly_score"]
        + scores["bi_readiness_score"]

    ) / 5

    scores["overall_quality_index"] = round(
        overall_score,
        2
    )

    return scores