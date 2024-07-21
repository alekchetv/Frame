from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from models import Film
from sqlalchemy import select
from database import async_session
from models import User, Film, Category
from films.repository import FilmREPO

router = APIRouter(
    prefix="/films",
    tags=["Добавление,оценкаы фильмов"],
)


@router.get("")
async def get_films():
    return await FilmREPO.find_all(id=1)


