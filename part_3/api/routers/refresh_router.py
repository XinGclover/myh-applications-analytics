from fastapi import APIRouter, HTTPException, status, Depends

from part_3.api.services.refresh_service import refresh_database
from part_3.api.schemas.response_schema import RefreshResponse

from part_3.api.dependencies.security import verify_api_key

router = APIRouter(
    prefix="/refresh",
    tags=["Refresh"],
)


@router.post("", response_model=RefreshResponse)
def refresh(
    _=Depends(verify_api_key),
):
    """
    Trigger a full pipeline refresh
    and return operational load metadata.
    """
    try:
        return refresh_database()

    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Refresh failed: {error}",
        )
