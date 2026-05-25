from __future__ import annotations


APPLICATION_LIMIT = 50000

APPLICATIONS_ENDPOINT = "/applications"
PROVIDERS_ENDPOINT = "/providers"
STATS_BY_YEAR_ENDPOINT = "/stats/by-year"
STATS_BY_EDUCATION_AREA_ENDPOINT = "/stats/by-education-area"
REFRESH_ENDPOINT = "/refresh"
EXPORT_APPLICATIONS_ENDPOINT = "/export/applications"
EXPORT_STATS_BY_YEAR_ENDPOINT = "/export/stats/by-year"

APPLICATION_FILTER_KEYS = [
    "year",
    "region",
    "municipality",
    "decision",
    "provider",
    "study_form",
]

STATS_BY_YEAR_FILTER_KEYS = [
    "region",
    "municipality",
    "decision",
    "provider",
    "study_form",
]

STATS_BY_EDUCATION_AREA_FILTER_KEYS = [
    "year",
    "region",
    "municipality",
    "decision",
    "provider",
    "study_form",
]
