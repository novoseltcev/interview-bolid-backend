from fastapi import APIRouter

from .events.controller import router as events_router

router = APIRouter()
router.include_router(events_router)
