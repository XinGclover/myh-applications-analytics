from datetime import datetime
from pathlib import Path

import requests

from src.myh_pipeline.config import RAW_DATA_PATH


START_YEAR = 2020


def get_source_years() -> list[int]:
    """
    Return source years from 2020 to the previous year.
    """
    current_year = datetime.now().year

    return list(range(START_YEAR, current_year))


def get_candidate_urls(year: int) -> list[str]:
    """
    Return possible MYH source URLs for a given year.
    """
    base_url = (
        "https://assets.myh.se/docs/"
        "utbildningsformer/"
        "yrkeshogskolan/"
        "ansokningsomgangar"
    )

    file_name = f"resultat-ansokningsomgang-{year}.xlsx"

    return [
        f"{base_url}/yh-{year}/{file_name}",
        f"{base_url}/program-yh-{year}/{file_name}",
    ]


def download_source_file(year: int) -> tuple[Path, str]:
    """
    Download one MYH Excel source file.
    """
    RAW_DATA_PATH.mkdir(parents=True, exist_ok=True)

    file_path = RAW_DATA_PATH / f"resultat-ansokningsomgang-{year}.xlsx"

    last_error = None

    for url in get_candidate_urls(year):
        try:
            response = requests.get(url, timeout=30)
            response.raise_for_status()

            file_path.write_bytes(response.content)

            return file_path, url

        except requests.RequestException as error:
            last_error = error

    raise RuntimeError(
        f"Could not download source file for year {year}. "
        f"Last error: {last_error}"
    )


def download_source_files(years: list[int] | None = None) -> list[dict]:
    """
    Download source files for selected years.
    """
    if years is None:
        years = get_source_years()

    records = []

    for year in years:
        file_path, url = download_source_file(year)

        records.append(
            {
                "source_year": year,
                "file_url": url,
                "file_name": file_path.name,
                "file_path": str(file_path),
                "downloaded_at": datetime.now().isoformat(timespec="seconds"),
                "download_status": "success",
            }
        )

    return records


if __name__ == "__main__":
    records = download_source_files()

    for record in records:
        print(
            record["source_year"],
            record["download_status"],
            record["file_name"],
        )