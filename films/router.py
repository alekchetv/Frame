from fastapi import APIRouter, Depends, Request
from models import User, Film
from films.repository import FilmREPO
from users.dependencies import current_user, get_token
from films.schemas import FilmData
from fastapi import Query

from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache


router = APIRouter(
    prefix="/films",
    tags=["Добавление,оценкаы фильмов"],
)


categories = ["Боевик", "bn", "Драма", "Роман", "Хоррор", "Художественный"]


@router.get("")
@cache(expire=20)
async def get_user_films(user: User = Depends(current_user)):
    return await FilmREPO.find_all(user_id=user.id)


@router.get("/top_films")
async def get_films_rating():
    return await FilmREPO.find_all()


@router.post("/add_film")
async def add_films(film: FilmData, category: str = Query(enum=categories), user: User = Depends(current_user)):
    return await FilmREPO.add(title=film.title, score=film.score, user_id=user.id, category=category)


async def add_category(category):
    pass

