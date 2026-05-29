from datetime import datetime
from pathlib import Path

import pandas as pd

from src.myh_pipeline.config import METADATA_PATH
from src.myh_pipeline.source_downloader import (
    download_source_files,
    get_source_years,
)


HEADER_KEYWORDS = [
    "diarienummer",
    "utbildningsnamn",
    "utbildningsanordnare",
    "kommun",
    "län",
    "beslut",
    "studieform",
]


def detect_header_row(
    file_path: Path,
    sheet_name: str,
    max_rows: int = 20,
) -> int:
    """
    Detect the most likely header row by scoring rows
    against expected MYH column keywords.
    """
    preview = pd.read_excel(
        file_path,
        sheet_name=sheet_name,
        header=None,
        nrows=max_rows,
    )

    best_row = 0
    best_score = 0

    for index, row in preview.iterrows():
        row_values = (
            row.dropna()
            .astype(str)
            .str.strip()
            .str.lower()
            .tolist()
        )

        score = sum(
            any(keyword in value for value in row_values)
            for keyword in HEADER_KEYWORDS
        )

        if score > best_score:
            best_score = score
            best_row = index

    return best_row


def build_source_metadata(
    download_records: list[dict],
    sheet_name: str = "Tabell 3",
) -> pd.DataFrame:
    """
    Detect header rows from downloaded source files
    and save source metadata to CSV.
    """
    records = []

    for record in download_records:
        year = record["source_year"]
        file_path = Path(record["file_path"])

        try:
            header_row = detect_header_row(
                file_path=file_path,
                sheet_name=sheet_name,
            )

            records.append(
                {
                    **record,
                    "sheet_name": sheet_name,
                    "detected_header_row": header_row,
                    "metadata_created_at": datetime.now().isoformat(
                        timespec="seconds"
                    ),
                    "metadata_status": "success",
                }
            )

        except Exception as error:
            records.append(
                {
                    **record,
                    "sheet_name": sheet_name,
                    "detected_header_row": None,
                    "metadata_created_at": datetime.now().isoformat(
                        timespec="seconds"
                    ),
                    "metadata_status": f"failed: {error}",
                }
            )

    metadata_df = pd.DataFrame(records)

    METADATA_PATH.mkdir(parents=True, exist_ok=True)

    output_path = METADATA_PATH / "source_files.csv"

    metadata_df.to_csv(output_path, index=False)

    return metadata_df


def refresh_source_metadata(
    years: list[int] | None = None,
    sheet_name: str = "Tabell 3",
) -> pd.DataFrame:
    """
    Download source files, detect header rows,
    and save metadata.
    """
    if years is None:
        years = get_source_years()

    download_records = download_source_files(years)

    return build_source_metadata(
        download_records=download_records,
        sheet_name=sheet_name,
    )


if __name__ == "__main__":
    metadata_df = refresh_source_metadata()

    print(metadata_df)