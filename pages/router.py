from fastapi import APIRouter, Depends
from fastapi.templating import Jinja2Templates
from fastapi import Response, Request
from films.router import get_user_films


router = APIRouter(
    prefix="/pages",
    tags=["Фронтенд"]
)


templates = Jinja2Templates(directory="templates")


@router.get("/films")
async def get_films_page(request: Request, films=Depends(get_user_films)):
    return templates.TemplateResponse(
        name="films.html", context={
            "request": request,
            "films": films,
            })


@router.get("/login")
async def get_login_page(request: Request):
    return templates.TemplateResponse(
        name="auth.html", context={
            "request": request
        })
