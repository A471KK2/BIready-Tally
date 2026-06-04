import pandas as pd
import numpy as np


def parse_mixed_dates(value):
    """
    Parse multiple possible date formats safely.
    """

    if pd.isna(value):
        return pd.NaT

    value = str(value).strip()

    if value == "":
        return pd.NaT

    # -------------------------------------------------
    # HANDLE EXCEL SERIAL DATES
    # -------------------------------------------------

    try:

        if value.isdigit():

            numeric_value = int(value)

            # Excel serial date range sanity check
            if 20000 < numeric_value < 60000:

                return pd.to_datetime(
                    numeric_value,
                    unit="D",
                    origin="1899-12-30"
                )

    except Exception:
        pass

    # -------------------------------------------------
    # TRY MULTIPLE DATE FORMATS
    # -------------------------------------------------

    date_formats = [

        "%d-%m-%Y",
        "%d/%m/%Y",

        "%Y-%m-%d",
        "%Y/%m/%d",

        "%d-%b-%Y",
        "%d %b %Y",

        "%b-%d-%Y",
        "%b/%d/%Y",

        "%d %B %Y",
        "%Y%m%d"

    ]

    for fmt in date_formats:

        try:

            return pd.to_datetime(
                value,
                format=fmt
            )

        except Exception:
            continue

    # -------------------------------------------------
    # FALLBACK AUTO PARSER
    # -------------------------------------------------

    try:

        return pd.to_datetime(
            value,
            errors="coerce",
            dayfirst=True
        )

    except Exception:

        return pd.NaT


def clean_date_columns(
    df: pd.DataFrame,
    columns: list
) -> pd.DataFrame:
    """
    Clean and normalize mixed-format date columns.
    """

    for col in columns:

        if col in df.columns:

            df[col] = df[col].apply(parse_mixed_dates)

    return df