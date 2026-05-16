from pathlib import Path
import pandas as pd
from part_3.api.db import engine

BASE_DIR = Path(__file__).resolve().parent.parent.parent

file_path = BASE_DIR / "part_2" / "data" / "curated" / "curated_applications.csv"

try:
    df = pd.read_csv(file_path)

    df.to_sql(
        name="yh_applications",
        schema="curated",
        con=engine,
        if_exists="append",
        index=False,
    )

    print("Data loaded successfully.")

except FileNotFoundError:
    print(f"CSV file not found: {file_path}")

except Exception as e:
    print(f"Error loading data: {e}")
