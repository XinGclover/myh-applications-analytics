import pandas as pd

from src.myh_pipeline.load import load_all_years
from src.myh_pipeline.clean import clean_all_years
from src.myh_pipeline.harmonize import harmonize_all_years
from src.myh_pipeline.enrich import enrich_dataset
from src.myh_pipeline.validate import build_validation_summary
from src.myh_pipeline.config import FULL_REFRESH_YEARS


def build_curated_dataset():

    dfs = load_all_years(years=FULL_REFRESH_YEARS)

    cleaned_dfs = clean_all_years(dfs)

    harmonized_dfs = harmonize_all_years(cleaned_dfs)

    curated_df = pd.concat(
        harmonized_dfs.values(),
        ignore_index=True,
    )

    curated_df = curated_df.convert_dtypes()

    curated_df = enrich_dataset(curated_df)

    validation_summary = build_validation_summary(curated_df)

    return curated_df, validation_summary


