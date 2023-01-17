from fastapi import APIRouter, Depends

from app.api.base_schemas import Pagination, ResponseList

from .schemas import EventSchema
from .service import EventService

router = APIRouter(prefix="/events")


@router.get("/", response_model=ResponseList[EventSchema])
async def get_events(
    pagination: Pagination = Depends(),
    service: EventService = Depends(),
) -> ResponseList[EventSchema]:
    data, meta = await service.get_all(
        page=pagination.page, per_page=pagination.per_page
    )
    return ResponseList[EventSchema](data=[
        EventSchema.from_orm(event) for event in data
    ], meta=meta)


@router.post("/")
async def create_event(
    data: EventSchema, service: EventService = Depends()
):
    await service.create(data)
