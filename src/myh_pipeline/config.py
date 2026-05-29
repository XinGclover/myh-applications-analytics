from pathlib import Path

# Project root
PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATA_DIR = PROJECT_ROOT / "part_2" / "data"

RAW_DATA_PATH = DATA_DIR / "raw"

METADATA_PATH = DATA_DIR / "metadata"

CURATED_DATA_PATH = DATA_DIR / "curated"


FULL_REFRESH_YEARS = [2020, 2021, 2022, 2023, 2024, 2025]



TARGET_COLUMNS = [
    "source_year",
    "source_file",
    "source_sheet",
    "application_id",
    "education_name",
    "education_area",
    "decision",
    "decision_normalized",
    "municipality",
    "region",
    "yh_credits",
    "study_form",
    "study_form_normalized",
    "study_pace_percent",
    "provider_name",
    "provider_type",
    "sun5_field",
    "sun5_field_name",
    "seqf_level",
    "narrow_occupational_area",
]

COLUMN_MAPPING = {
    "diarienummer": "application_id",
    "utbildningsnamn": "education_name",
    "utbildningsomrade": "education_area",
    "beslut": "decision",
    "kommun": "municipality",
    "lan": "region",
    "yh_poang": "yh_credits",
    "studieform": "study_form",
    "studietakt_procent": "study_pace_percent",
    "utbildningsanordnare": "provider_name",
    "utbildningsanordnare_administrativ_enhet": "provider_name",
    "huvudmannatyp": "provider_type",
    "sun5_inriktning": "sun5_field",
    "sun5_inriktning_namn": "sun5_field_name",
    "seqf_niva": "seqf_level",
    "smalt_yrkesomrade": "narrow_occupational_area",
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
