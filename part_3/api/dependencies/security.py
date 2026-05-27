# api/dependencies/security.py

from fastapi import Header, HTTPException, status

from part_3.api.core.config import REFRESH_API_KEY


def verify_api_key(x_api_key: str = Header(...)):
    if x_api_key != REFRESH_API_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API key",
        )