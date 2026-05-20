import pandas as pd
from src.myh_pipeline.config import COLUMN_MAPPING, DECISION_MAPPING, STUDY_FORM_MAPPING


# harmonize single dataframe
def harmonize_schema(df, target_columns):

    df = df.copy()

    # rename source columns to target names
    df = df.rename(columns=COLUMN_MAPPING)

    if "beslut" in df.columns:
        df["decision_normalized"] = (
            df["beslut"]
            .astype("string")
            .str.strip()
            .map(DECISION_MAPPING)
            .fillna("other")
        )

    if "studieform" in df.columns:
        df["study_form_normalized"] = (
            df["studieform"]
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
