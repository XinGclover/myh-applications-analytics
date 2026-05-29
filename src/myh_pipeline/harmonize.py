import pandas as pd
from src.myh_pipeline.config import (
    COLUMN_MAPPING,
    DECISION_MAPPING,
    STUDY_FORM_MAPPING,
    TARGET_COLUMNS,
)


# harmonize single dataframe
def harmonize_schema(df, target_columns):
    """
    Map one yearly dataframe to the target schema
    and add normalized decision fields.
    """

    df = df.copy()

    # rename source columns to target names
    df = df.rename(columns=COLUMN_MAPPING)

    if "decision" in df.columns:
        df["decision_normalized"] = (
            df["decision"]
            .astype("string")
            .str.strip()
            .map(DECISION_MAPPING)
            .fillna("other")
        )

    if "study_form" in df.columns:
        df["study_form_normalized"] = (
            df["study_form"]
            .astype("string")
            .str.strip()
            .map(STUDY_FORM_MAPPING)
            .fillna("other")
        )

    # add missing columns
    for col in target_columns:
        if col not in df.columns:
            df[col] = pd.NA

    # keep only target columns
    df = df[target_columns]

    return df


def harmonize_all_years(dfs):
    """
    Harmonize every loaded year
    into the shared curated schema.
    """
    harmonized_dfs = {}
    for year, df in dfs.items():
        harmonized_df = harmonize_schema(df=df, target_columns=TARGET_COLUMNS)

        harmonized_dfs[year] = harmonized_df

    return harmonized_dfs
