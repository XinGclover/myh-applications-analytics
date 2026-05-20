from pathlib import Path

# Project root
PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATA_DIR = PROJECT_ROOT / "part_2" / "data"

RAW_DATA_PATH = DATA_DIR / "raw"

CURATED_DATA_PATH = DATA_DIR / "curated"


BASELINE_YEARS = [2022, 2023, 2024, 2025]

YEAR_CONFIG = {
    2021: {"sheet_name": "Tabell 3", "header_row": 4},
    2022: {"sheet_name": "Tabell 3", "header_row": 0},
    2023: {"sheet_name": "Tabell 3", "header_row": 5},
    2024: {"sheet_name": "Tabell 3", "header_row": 5},
    2025: {"sheet_name": "Tabell 3", "header_row": 6},
}


TARGET_COLUMNS = [
    "source_year",
    "source_file",
    "source_sheet",
    "diarienummer",
    "utbildningsnamn",
    "utbildningsomrade",
    "beslut",
    "decision_normalized",
    "kommun",
    "lan",
    "yh_poang",
    "studieform",
    "study_form_normalized",
    "studietakt_procent",
    "utbildningsanordnare",
    "huvudmannatyp",
    "sun5_inriktning",
    "sun5_inriktning_namn",
    "seqf_niva",
    "smalt_yrkesomrade",
]

COLUMN_MAPPING = {
    "utbildningsanordnare_administrativ_enhet": "utbildningsanordnare",
}



# create normalized English decision column
DECISION_MAPPING = {
    "Beviljad": "approved",
    "Avslag": "rejected",
    "Återkallad": "withdrawn",
}


# create normalized English study form column
STUDY_FORM_MAPPING = {
    "Distans": "distance",
    "Bunden": "on_site",
}