from fastapi import HTTPException, status

from part_3.api.services.application_service import application_exists


def ensure_application_exists(diarienummer: str) -> None:
    if not application_exists(diarienummer):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Application not found",
        )