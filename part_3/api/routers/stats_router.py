from fastapi import APIRouter

from part_3.api.services.stats_service import (
    get_stats_by_year,
    get_stats_by_education_area,
)
from part_3.api.schemas.response_schema import (
    StatsByYearResponse,
    StatsByEducationAreaResponse,
)

router = APIRouter(
    prefix="/stats",
    tags=["Statistics"],
)


@router.get(
    "/by-year",
    response_model=list[StatsByYearResponse],
)
def stats_by_year(
    region: str | None = None,
    municipality: str | None = None,
    decision: str | None = None,
    provider: str | None = None,
    study_form: str | None = None,
):
    """
    Serve yearly application statistics
    filtered by dashboard query parameters.
    """
    return get_stats_by_year(
        region=region,
        municipality=municipality,
        decision=decision,
        provider=provider,
        study_form=study_form,
    )


@router.get(
    "/by-education-area",
    response_model=list[StatsByEducationAreaResponse],
)
def stats_by_education_area(
    year: int | None = None,
    region: str | None = None,
    municipality: str | None = None,
    decision: str | None = None,
    provider: str | None = None,
    study_form: str | None = None,
):
    """
    Serve education-area statistics
    filtered by dashboard query parameters.
    """
    return get_stats_by_education_area(
        year=year,
        region=region,
        municipality=municipality,
        decision=decision,
        provider=provider,
        study_form=study_form,
    )
