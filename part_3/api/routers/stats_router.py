from fastapi import APIRouter

from part_3.api.services.stats_service import (
    get_stats_by_year,
    get_stats_by_education_area,
)

router = APIRouter(
    prefix="/stats",
    tags=["Statistics"],
)


@router.get("/by-year")
def stats_by_year():
    return get_stats_by_year()


@router.get("/by-education-area")
def stats_by_education_area():
    return get_stats_by_education_area()
