import numpy as np
import pandas as pd

def dataframe_to_records(df: pd.DataFrame) -> list[dict]:
    """
    Convert pandas dataframes into JSON-compatible records
    for FastAPI responses.
    """
    df = df.replace([np.nan, np.inf, -np.inf], None)

    return df.to_dict(orient="records")
