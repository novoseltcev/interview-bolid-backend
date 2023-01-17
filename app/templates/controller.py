import httpx
from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

from app.core.settings import get_settings

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@router.get("/")
async def index(request: Request):
    async with httpx.AsyncClient(http1=True) as client:
        response = await client.get(f"http://localhost:5000{get_settings().API_PREFIX}/events/?page=1&perPage=100")
        return templates.TemplateResponse("index.html", {
            "request": request,
            "events": response.json()["data"],
        })
