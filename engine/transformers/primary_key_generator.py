import pandas as pd
import hashlib


def generate_primary_key(df: pd.DataFrame) -> pd.DataFrame:
    """
    Generate unique deterministic primary key for each row.
    """

    def create_row_hash(row):

        row_string = "|".join(
            row.astype(str)
        )

        return hashlib.md5(
            row_string.encode()
        ).hexdigest()

    df["primary_key"] = df.apply(
        create_row_hash,
        axis=1
    )

    return df