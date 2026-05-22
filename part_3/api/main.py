from fastapi import FastAPI

# from api.routers.application_router import router as application_router
from part_3.api.routers.note_router import router as note_router


app = FastAPI(
    title="MYH Applications API",
)


# app.include_router(application_router)
app.include_router(note_router)
