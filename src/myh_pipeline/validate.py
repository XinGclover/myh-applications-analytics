# validate.py

import pandas as pd


def build_validation_summary(df):

    validation_summary = pd.DataFrame(
        [
            {
                "check": "missing_diarienummer",
                "affected_rows": df["diarienummer"].isna().sum(),
                "severity": "critical",
            },
            {
                "check": "duplicate_diarienummer",
                "affected_rows": df["diarienummer"].duplicated().sum(),
                "severity": "warning",
            },
            {
                "check": "missing_utbildningsanordnare",
                "affected_rows": df["utbildningsanordnare"].isna().sum(),
                "severity": "warning",
            },
            {
                "check": "invalid_decision_values",
                "affected_rows": (
                    ~df["decision_normalized"].isin(
                        [
                            "approved",
                            "rejected",
                            "withdrawn",
                            "other",
                        ]
                    )
                ).sum(),
                "severity": "warning",
            },
            {
                "check": "invalid_study_form_values",
                "affected_rows": (
                    ~df["study_form_normalized"].isin(
                        [
                            "distance",
                            "on_site",
                            "other",
                        ]
                    )
                ).sum(),
                "severity": "warning",
            },
            {
                "check": "missing_sun5_fields",
                "affected_rows": df["sun5_inriktning"].isna().sum(),
                "severity": "info",
            },
        ]
    )

    return validation_summary
