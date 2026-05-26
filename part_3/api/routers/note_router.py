from fastapi import APIRouter, HTTPException, status

from part_3.api.schemas.request_schema import (
    ApplicationNoteCreate,
    ApplicationNoteResponse,
)
from part_3.api.services.note_service import (
    upsert_note,
    get_note_by_diarienummer,
    delete_note,
)
from part_3.api.utils.validation import ensure_application_exists


router = APIRouter(
    prefix="/applications",
    tags=["Application Notes"],
)


@router.put(
    "/{diarienummer:path}/note",
    response_model=ApplicationNoteResponse,
)
def upsert_application_note(
    diarienummer: str,
    note: ApplicationNoteCreate,
):
    """
    Create or update the note attached to one application.
    """
    ensure_application_exists(diarienummer)

    return upsert_note(diarienummer, note)


@router.get(
    "/{diarienummer:path}/note",
    response_model=ApplicationNoteResponse,
)
def get_application_note(diarienummer: str):
    """
    Serve the note attached to one application.
    """
    ensure_application_exists(diarienummer)

    note = get_note_by_diarienummer(diarienummer)

    if not note:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Note not found",
        )

    return note


@router.delete(
    "/{diarienummer:path}/note",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_application_note(diarienummer: str):
    """
    Delete the note attached to one application.
    """
    ensure_application_exists(diarienummer)

    deleted = delete_note(diarienummer)

    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Note not found",
        )

    return None