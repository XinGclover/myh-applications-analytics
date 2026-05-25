from io import StringIO

import pandas as pd
from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from part_3.api.services.application_service import get_applications
from part_3.api.services.stats_service import get_stats_by_year

router = APIRouter(
    prefix="/export",
    tags=["Export"],
)


@router.get("/applications")
def export_applications(
    year: int | None = None,
    decision: str | None = None,
    region: str | None = None,
    municipality: str | None = None,
    provider: str | None = None,
    study_form: str | None = None,
):
    """
    Export filtered application records as a CSV response
    for dashboard downloads.
    """
    data = get_applications(
        year=year,
        decision=decision,
        region=region,
        municipality=municipality,
        provider=provider,
        study_form=study_form,
        limit=100000,
    )

    df = pd.DataFrame(data)

    output = StringIO()

    df.to_csv(output, index=False)

    output.seek(0)

    return StreamingResponse(
        output,
        media_type="text/csv",
        headers={"Content-Disposition": "attachment; filename=applications.csv"},
    )


@router.get("/stats/by-year")
def export_stats_by_year():
    """
    Export yearly statistics as a CSV response
    for dashboard downloads.
    """
    data = get_stats_by_year()

    df = pd.DataFrame(data)

    output = StringIO()

    df.to_csv(output, index=False)

    output.seek(0)

    return StreamingResponse(
        output,
        media_type="text/csv",
        headers={"Content-Disposition": "attachment; filename=stats_by_year.csv"},
    )
