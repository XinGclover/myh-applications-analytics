from fastapi import HTTPException, status

from part_3.api.services.application_service import application_exists


def ensure_application_exists(application_id: str) -> None:
    if not application_exists(application_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Application not found",
        )
