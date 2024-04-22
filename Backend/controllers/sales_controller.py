from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from models.sales_model import get_sales_data

router = APIRouter()

templates = Jinja2Templates(directory="Frontend/templates")


@router.get("/sales", response_class=HTMLResponse)
async def sales(request: Request):
    sales_data = get_sales_data()
    return templates.TemplateResponse("sales.html", {"request": request, "sales_data": sales_data})
