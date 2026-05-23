from fastapi import FastAPI

from part_3.api.routers.application_router import router as application_router
from part_3.api.routers.note_router import router as note_router
from part_3.api.routers.stats_router import router as stats_router
from part_3.api.routers.export_router import router as export_router
from part_3.api.routers.refresh_router import router as refresh_router
from part_3.api.routers.provider_router import router as provider_router

app = FastAPI(
    title="MYH Applications API",
)


app.include_router(application_router)
app.include_router(note_router)
app.include_router(stats_router)
app.include_router(export_router)
app.include_router(refresh_router)
app.include_router(provider_router)