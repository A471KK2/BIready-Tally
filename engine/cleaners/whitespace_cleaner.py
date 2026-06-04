import pandas as pd


def clean_whitespace(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove extra whitespace from string columns.
    """

    for col in df.select_dtypes(include="object").columns:

        df[col] = df[col].astype(str).str.strip()

    return df