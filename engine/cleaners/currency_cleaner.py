import pandas as pd


def clean_currency_columns(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    """
    Remove currency symbols and commas.
    """

    for col in columns:

        if col in df.columns:

            df[col] = (
                df[col]
                .astype(str)
                .str.replace("₹", "", regex=False)
                .str.replace("Rs.", "", regex=False)
                .str.replace(",", "", regex=False)
                .str.strip()
            )

            df[col] = pd.to_numeric(df[col], errors="coerce")

    return df