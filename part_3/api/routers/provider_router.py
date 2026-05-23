from fastapi import APIRouter, HTTPException, status

from part_3.api.services.provider_service import (
    get_providers,
    get_provider_applications,
)

router = APIRouter(
    prefix="/providers",
    tags=["providers"],
)


@router.get("")
def list_providers():
    return get_providers()


@router.get("/{provider_name}/applications")
def list_provider_applications(provider_name: str):
    applications = get_provider_applications(provider_name)

    if not applications:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Provider not found or no applications found",
        )

    return applications
