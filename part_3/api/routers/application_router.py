from fastapi import APIRouter, HTTPException, status

from part_3.api.schemas.response_schema import ApplicationResponse
from part_3.api.services.application_service import (
    get_applications,
    get_application_by_diarienummer,
)

router = APIRouter(
    prefix="/applications",
    tags=["Applications"],
)


@router.get(
    "",
    response_model=list[ApplicationResponse],
)
def list_applications(
    year: int | None = None,
    decision: str | None = None,
    region: str | None = None,
    municipality: str | None = None,
    provider: str | None = None,
    study_form: str | None = None,
    limit: int = 100,
):
    """
    Serve filtered application records
    for dashboard and export consumers.
    """
    return get_applications(
        year=year,
        decision=decision,
        region=region,
        municipality=municipality,
        provider=provider,
        study_form=study_form,
        limit=limit,
    )


@router.get(
    "/{diarienummer:path}",
    response_model=ApplicationResponse,
)
def get_application(diarienummer: str):
    """
    Serve one application by diarienummer
    or raise 404 when it is missing.
    """
    application = get_application_by_diarienummer(diarienummer)

    if not application:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Application not found",
        )

    return application
