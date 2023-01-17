from fastapi import FastAPI

from app.api import handlers
from app.api import router as v1_router
from app.core.settings import get_settings
# from app.templates import router as templates_router

app = FastAPI(
    title=get_settings().PROJECT_NAME,
    description=get_settings().DESCRIPTION,
    version=get_settings().VERSION,
    debug=get_settings().DEBUG,
)

app.include_router(v1_router, prefix=get_settings().API_PREFIX)
# app.include_router(templates_router)
handlers.register_api_error_handlers(app)
