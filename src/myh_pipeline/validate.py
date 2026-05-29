import pandas as pd


def build_validation_summary(df: pd.DataFrame) -> pd.DataFrame:
    """
    Build validation checks for key curated English fields
    before database loading.
    """

    validation_summary = pd.DataFrame(
        [
            {
                "check": "missing_application_id",
                "affected_rows": df["application_id"].isna().sum(),
                "severity": "critical",
            },
            {
                "check": "duplicate_application_id",
                "affected_rows": df["application_id"].duplicated().sum(),
                "severity": "warning",
            },
            {
                "check": "missing_provider_name",
                "affected_rows": df["provider_name"].isna().sum(),
                "severity": "warning",
            },
            {
                "check": "invalid_decision_values",
                "affected_rows": (
                    ~df["decision_normalized"].isin(
                        ["approved", "rejected", "withdrawn", "other"]
                    )
                ).sum(),
                "severity": "warning",
            },
            {
                "check": "invalid_study_form_values",
                "affected_rows": (
                    ~df["study_form_normalized"].isin(["distance", "on_site", "other"])
                ).sum(),
                "severity": "warning",
            },
            {
                "check": "missing_sun5_field",
                "affected_rows": df["sun5_field"].isna().sum(),
                "severity": "info",
            },
            {
                "check": "education_name_max_length",
                "affected_rows": df["education_name"].dropna().str.len().gt(250).sum(),
                "max_length_found": df["education_name"].dropna().str.len().max(),
                "severity": "warning",
            },
            {
                "check": "provider_name_max_length",
                "affected_rows": df["provider_name"].dropna().str.len().gt(100).sum(),
                "max_length_found": df["provider_name"].dropna().str.len().max(),
                "severity": "warning",
            },
            {
                "check": "sun5_field_name_max_length",
                "affected_rows": df["sun5_field_name"].dropna().str.len().gt(100).sum(),
                "max_length_found": df["sun5_field_name"].dropna().str.len().max(),
                "severity": "warning",
            },
        ]
    )

    return validation_summary
