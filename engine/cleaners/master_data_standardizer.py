import yaml
import pandas as pd


def standardize_master_data(df: pd.DataFrame):

    with open(
        "config/master_mappings.yaml",
        "r"
    ) as file:

        mappings = yaml.safe_load(file)

    # =====================================================
    # STATE STANDARDIZATION
    # =====================================================

    if "state" in df.columns:

        state_map = mappings.get(
            "state_mappings",
            {}
        )

        df["state"] = (
            df["state"]
            .astype(str)
            .str.strip()
            .replace(state_map)
        )

    return df