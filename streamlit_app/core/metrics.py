from __future__ import annotations


def calculate_kpis(applications_df) -> dict:
    total_applications = len(applications_df)
    approved_applications = 0
    approval_rate = 0.0
    providers_count = 0

    if not applications_df.empty:
        if "is_approved" in applications_df:
            approved_applications = int(applications_df["is_approved"].fillna(False).sum())
            approval_rate = approved_applications / total_applications * 100 if total_applications else 0.0
        if "utbildningsanordnare" in applications_df:
            providers_count = applications_df["utbildningsanordnare"].dropna().nunique()

    return {
        "total_applications": total_applications,
        "approved_applications": approved_applications,
        "approval_rate": approval_rate,
        "providers_count": providers_count,
    }


def format_rate(value: float) -> str:
    return f"{value:.1f}%"
