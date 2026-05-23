from fastapi import APIRouter, HTTPException, status

from part_3.api.schemas.request_schema import (
    ApplicationNoteCreate,
    ApplicationNoteResponse,
    ApplicationNoteUpdate,
)
from part_3.api.services.note_service import (
    create_note,
    get_notes_by_diarienummer,
    delete_note,
    update_note,
)


router = APIRouter(
    prefix="/applications",
    tags=["Application Notes"],
)


@router.post(
    "/{diarienummer:path}/notes",
    response_model=ApplicationNoteResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_application_note(
    diarienummer: str,
    note: ApplicationNoteCreate,
):
    return create_note(diarienummer, note)


@router.get(
    "/{diarienummer:path}/notes",
    response_model=list[ApplicationNoteResponse],
)
def get_application_notes(diarienummer: str):
    return get_notes_by_diarienummer(diarienummer)


@router.put(
    "/{diarienummer:path}/notes/{note_id}",
    response_model=ApplicationNoteResponse,
)
def update_application_note(
    diarienummer: str,
    note_id: int,
    note: ApplicationNoteUpdate,
):
    updated_note = update_note(diarienummer, note_id, note)

    if not updated_note:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Note not found",
        )

    return updated_note


@router.delete(
    "/{diarienummer:path}/notes/{note_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_application_note(
    diarienummer: str,
    note_id: int,
):
    deleted = delete_note(diarienummer, note_id)

    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Note not found",
        )

    return None
