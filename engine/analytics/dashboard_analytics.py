import pandas as pd


def calculate_dashboard_metrics(df: pd.DataFrame):

    metrics = {}

    # =====================================================
    # TOTAL REVENUE
    # =====================================================

    if (
        "voucher_type" in df.columns
        and "credit_amount" in df.columns
    ):

        sales_df = df[
            df["voucher_type"]
            .astype(str)
            .str.lower()
            == "sales"
        ]

        metrics["total_revenue"] = (
            sales_df["credit_amount"]
            .sum()
        )

    else:

        metrics["total_revenue"] = 0

    # =====================================================
    # PROCUREMENT COST
    # =====================================================

    if (
        "voucher_type" in df.columns
        and "debit_amount" in df.columns
    ):

        purchase_df = df[
            df["voucher_type"]
            .astype(str)
            .str.lower()
            == "purchase"
        ]

        metrics["procurement_cost"] = (
            purchase_df["debit_amount"]
            .sum()
        )

    else:

        metrics["procurement_cost"] = 0

    # =====================================================
    # GROSS PROFIT
    # =====================================================

    metrics["gross_profit"] = (
        metrics["total_revenue"]
        - metrics["procurement_cost"]
    )

    # =====================================================
    # PROFIT MARGIN
    # =====================================================

    if metrics["total_revenue"] > 0:

        metrics["profit_margin"] = (
            metrics["gross_profit"]
            / metrics["total_revenue"]
        ) * 100

    else:

        metrics["profit_margin"] = 0

    # =====================================================
    # TOTAL INVOICES
    # =====================================================

    metrics["total_invoices"] = len(df)

    # =====================================================
    # UNIQUE HOSPITALS
    # =====================================================

    if "hospital_name" in df.columns:

        metrics["unique_hospitals"] = (
            df["hospital_name"]
            .nunique()
        )

    else:

        metrics["unique_hospitals"] = 0

    # =====================================================
    # UNIQUE PRODUCTS
    # =====================================================

    if "product_name" in df.columns:

        metrics["unique_products"] = (
            df["product_name"]
            .nunique()
        )

    else:

        metrics["unique_products"] = 0

    return metrics