import httpx
from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@router.get("/")
async def index():
    with httpx.Client() as client:
        response = client.get("http://localhost:8000/api/events")
        data = response.json()["data"]
        return templates.TemplateResponse("index.html", {"events": data})
