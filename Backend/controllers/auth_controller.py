from fastapi import APIRouter, Request, Form, Depends, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.responses import JSONResponse

from Backend.utils.auth_utils import verify_username, verify_password
from models.sign_in_model import UserSignIn

router = APIRouter()
templates = Jinja2Templates(directory="Frontend/templates")


@router.get("/login", response_class=HTMLResponse)
def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@router.post("/login")
async def post_login(body: UserSignIn):
    print("yes")
    sorted_user = verify_username(body.username)
    if sorted_user:
        sorted_password = sorted_user["password"]
        if verify_password(sorted_password, body.password):
            return JSONResponse(content={"success": True})
        else:

            raise HTTPException(status_code=401, detail="Incorrect password")
    raise HTTPException(status_code=404, detail="Username not found")


@router.get("/logout", response_class=HTMLResponse)
def logout(request: Request):
    # Logout logic
    return templates.TemplateResponse("logout.html", {"request": request})
