import pandas as pd
from src.myh_pipeline.config import YEAR_CONFIG, BASELINE_YEARS, RAW_DATA_PATH


def load_excel(file):
    """
    Load one configured MYH Excel sheet
    and add source traceability columns.
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


def load_all_years(years=None):
    """
    Load configured source files for the selected years
    into a dictionary keyed by year.
    """

    if years is None:
        years = BASELINE_YEARS

    excel_files = RAW_DATA_PATH.glob("*.xlsx")

    dfs = {}

    for file in excel_files:
        year = int(file.stem[-4:])

        if year not in years:
            continue

        dfs[year] = load_excel(file)

    return dfs


def check_schema(dfs):
    """
    Summarize dataframe shapes and columns
    for quick schema comparison across years.
    """
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
