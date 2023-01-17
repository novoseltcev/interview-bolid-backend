from fastapi import APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates

from app.api.base_schemas import Pagination
from app.api.events.schemas import EventSchema
from app.api.events.service import EventService

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@router.get("/")
async def index(
    request: Request,
    pagination: Pagination = Depends(),
    service: EventService = Depends()
):
    raw_data, meta = await service.get_all(page=pagination.page, per_page=pagination.per_page)
    data = [EventSchema.from_orm(event).dict() for event in raw_data]
    print(f"Data: {data}")
    return templates.TemplateResponse("index.html", {"request": request, "events": data})
