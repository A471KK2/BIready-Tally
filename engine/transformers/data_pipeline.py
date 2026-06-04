import pandas as pd
from engine.transformers.primary_key_generator import generate_primary_key

from engine.cleaners.master_data_standardizer import (
    standardize_master_data
)
from engine.cleaners.column_cleaner import clean_column_names
from engine.cleaners.currency_cleaner import clean_currency_columns
from engine.cleaners.date_cleaner import clean_date_columns
from engine.cleaners.whitespace_cleaner import clean_whitespace


def run_cleaning_pipeline(df: pd.DataFrame) -> pd.DataFrame:
    """
    Run complete data cleaning pipeline.
    """

    # -------------------------------
    # COLUMN CLEANING
    # -------------------------------

    df = clean_column_names(df)

    # -------------------------------
    # WHITESPACE CLEANING
    # -------------------------------

    df = clean_whitespace(df)

    # -------------------------------
    # MASTER DATA STANDARDIZATION   
    # -------------------------------

    df = standardize_master_data(df)

    # -------------------------------
    # CURRENCY CLEANING
    # -------------------------------

    currency_columns = [
        "debit_amount",
        "credit_amount",
        "outstanding_balance",
        "tax_amount"
    ]

    df = clean_currency_columns(df, currency_columns)

    # -------------------------------
    # DATE CLEANING
    # -------------------------------

    date_columns = [
        "invoice_date",
        "due_date"
    ]

    df = clean_date_columns(df, date_columns)
    
    # -------------------------------
    # PRIMARY KEY GENERATION
    # -------------------------------

    df = generate_primary_key(df)

    return df