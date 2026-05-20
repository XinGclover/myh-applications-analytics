import pandas as pd
from src.myh_pipeline.config import YEAR_CONFIG


def load_excel(file):
    """
    Load and standardize one Excel sheet.
    """

    print(f"Loading file: {file.name}")

    year = int(file.stem[-4:])

    config = YEAR_CONFIG.get(year)

    if config is None:
        raise ValueError(f"No configuration found for year {year}")

    try:
        df = pd.read_excel(
            file,
            sheet_name=config["sheet_name"],
            header=config["header_row"],
        )

        # Add traceability columns
        df["source_year"] = year
        df["source_file"] = file.name
        df["source_sheet"] = config["sheet_name"]

        return df

    except Exception as e:
        print(f"Failed to load {file.name}: {e}")

        return None


def check_schema(dfs):
    schema_df = pd.DataFrame(
        [
            {
                "source_year": year,
                "shape": df.shape,
                "columns": list(df.columns),
            }
            for year, df in dfs.items()
        ]
    )

    return schema_df
