from __future__ import annotations

import pandas as pd


COLUMN_TRANSLATIONS = {
    # metadata
    "source_year": "source_year",
    "source_file": "source_file",
    "source_sheet": "source_sheet",
    "record_source": "record_source",

    # identifiers
    "diarienummer": "application_id",

    # education
    "utbildningsnamn": "education_name",
    "utbildningsomrade": "education_area",
    "utbildningsnummer": "education_code",
    "yh_poang": "yh_credits",
    "seqf_niva": "seqf_level",
    "smalt_yrkesomrade": "narrow_occupational_area",
    "education_length": "education_length",
    "sector_category": "sector_category",

    # provider / organization
    "utbildningsanordnare": "provider_name",
    "huvudmannatyp": "provider_type",
    "huvudman": "provider_owner",

    # geography
    "kommun": "municipality",
    "lan": "region",

    # decision
    "beslut": "decision",
    "decision_normalized": "decision_normalized",
    "is_approved": "is_approved",

    # study setup
    "studieform": "study_form",
    "study_form_normalized": "study_form_normalized",
    "studietakt_procent": "study_pace_percent",
    "distans_med_traffar": "remote_with_meetings",

    # applicants / seats
    "platser": "planned_seats",
    "behoriga_forstahandssokande": "qualified_first_choice_applicants",
    "behoriga_sokande": "qualified_applicants",
    "sokande_totalt": "total_applicants",

    # SUN classification
    "sun5_inriktning": "sun5_field",
    "sun5_inriktning_namn": "sun5_field_name",

    # timestamps
    "load_timestamp": "load_timestamp",
}


def translate_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Translate normalized Swedish column names
    into curated English analytics-friendly names.
    """

    return df.rename(columns=COLUMN_TRANSLATIONS)
