from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware

from .controllers import auth_controller, sales_controller

app = FastAPI()

# Mount static files
app.mount("/Frontend/static", StaticFiles(directory="Frontend/static"), name="static")

# Mount templates
templates = Jinja2Templates(directory="Frontend/templates")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Frontend running on port 3000
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

app.include_router(auth_controller.router)
app.include_router(sales_controller.router)

@app.get('/')
def home_page():
    return "MVC APP !"
