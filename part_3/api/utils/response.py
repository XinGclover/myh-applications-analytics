import numpy as np
import pandas as pd

def dataframe_to_records(df: pd.DataFrame) -> list[dict]:
    """
    Some classification fields such as SUN5 and SEQF contain missing values
    for certain applications. These NULL values were preserved in PostgreSQL
    but required explicit handling in the API layer because pandas converts
    SQL NULL values into NaN, which are not JSON compliant in FastAPI responses.
    """
    df = df.replace([np.nan, np.inf, -np.inf], None)

    return df.to_dict(orient="records")