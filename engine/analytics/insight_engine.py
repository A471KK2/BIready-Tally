import pandas as pd


def generate_business_insights(
    df: pd.DataFrame,
    metrics: dict,
    anomalies: dict
):

    insights = []

    # =====================================================
    # REVENUE INSIGHT
    # =====================================================

    revenue = metrics.get(
        "total_revenue",
        0
    )

    if revenue > 10000000:

        insights.append(
            "💰 Revenue performance is very strong."
        )

    elif revenue > 1000000:

        insights.append(
            "📈 Revenue performance is healthy."
        )

    else:

        insights.append(
            "⚠️ Revenue appears relatively low."
        )

    # =====================================================
    # PROCUREMENT COST INSIGHT
    # =====================================================

    procurement_cost = metrics.get(
        "procurement_cost",
        0
    )

    if procurement_cost > revenue:

        insights.append(
            "🚨 Procurement costs exceed revenue."
        )

    elif procurement_cost > revenue * 0.7:

        insights.append(
            "⚠️ Procurement costs are significantly high."
        )

    else:

        insights.append(
            "✅ Procurement costs are under control."
        )

    # =====================================================
    # PROFITABILITY INSIGHT
    # =====================================================

    margin = metrics.get(
        "profit_margin",
        0
    )

    if margin > 30:

        insights.append(
            "📊 Profit margins are excellent."
        )

    elif margin > 15:

        insights.append(
            "✅ Profit margins are acceptable."
        )

    else:

        insights.append(
            "⚠️ Profit margins are critically low."
        )

    # =====================================================
    # DUPLICATE INVOICE INSIGHT
    # =====================================================

    duplicate_count = len(
        anomalies["duplicate_invoices"]
    )

    if duplicate_count > 100:

        insights.append(
            "🚨 High duplicate invoice count detected."
        )

    elif duplicate_count > 0:

        insights.append(
            "⚠️ Some duplicate invoices detected."
        )

    # =====================================================
    # GST COMPLIANCE INSIGHT
    # =====================================================

    missing_gst = len(
        anomalies["missing_gst"]
    )

    if missing_gst > 50:

        insights.append(
            "🚨 GST compliance risk is high."
        )

    elif missing_gst > 0:

        insights.append(
            "⚠️ Some GST records are missing."
        )

    else:

        insights.append(
            "✅ GST compliance quality looks good."
        )

    # =====================================================
    # NEGATIVE BALANCE INSIGHT
    # =====================================================

    negative_balances = len(
        anomalies["negative_balances"]
    )

    if negative_balances > 20:

        insights.append(
            "⚠️ Significant negative balances detected."
        )

    elif negative_balances > 0:

        insights.append(
            "⚠️ Some negative balances detected."
        )

    else:

        insights.append(
            "✅ No major negative balance issues found."
        )

    # =====================================================
    # HOSPITAL REVENUE CONCENTRATION
    # =====================================================

    if (
        "hospital_name" in df.columns
        and "credit_amount" in df.columns
    ):

        hospital_revenue = (
            df.groupby("hospital_name")[
                "credit_amount"
            ]
            .sum()
            .sort_values(ascending=False)
        )

        if len(hospital_revenue) > 0:

            top_share = (
                hospital_revenue.iloc[0]
                / hospital_revenue.sum()
            ) * 100

            if top_share > 40:

                insights.append(
                    "🏥 Revenue dependency on a single hospital is high."
                )

            elif top_share > 25:

                insights.append(
                    "🏥 Moderate revenue concentration detected."
                )

    # =====================================================
    # PAYMENT MODE INSIGHT
    # =====================================================

    if "payment_mode" in df.columns:

        payment_distribution = (
            df["payment_mode"]
            .value_counts(normalize=True)
        )

        if len(payment_distribution) > 0:

            dominant_mode = payment_distribution.index[0]

            dominant_share = (
                payment_distribution.iloc[0] * 100
            )

            insights.append(
                f"💳 Most transactions use {dominant_mode} ({dominant_share:.1f}%)."
            )

    # =====================================================
    # STATE PERFORMANCE INSIGHT
    # =====================================================

    if (
        "state" in df.columns
        and "credit_amount" in df.columns
    ):

        state_revenue = (
            df.groupby("state")[
                "credit_amount"
            ]
            .sum()
            .sort_values(ascending=False)
        )

        if len(state_revenue) > 0:

            top_state = state_revenue.index[0]

            insights.append(
                f"🗺️ Highest revenue is generated from {top_state}."
            )

    return insights