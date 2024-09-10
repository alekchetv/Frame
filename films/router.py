from fastapi import APIRouter, Depends, Request
from models import User, Film
from films.repository import FilmREPO
from users.dependencies import current_user, get_token
from films.schemas import FilmData, FilmChoose
from fastapi import Query
from films.services import elo_rating
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


@router.get("/test")
async def test():
    return await FilmREPO.update_rating(1258, 544)


@router.get("/film_battle")
async def get_two_films(user: User = Depends(current_user)):
    return await FilmREPO.get_two_random(user_id=user.id)


@router.post("/film_battle")
async def choose_one_film(choose: FilmChoose, user: User = Depends(current_user)):
    result = []
    return await elo_rating(choose, user.id)


@router.post("/add_film")
async def add_films(film: FilmData, category: str = Query(enum=categories), user: User = Depends(current_user)):
    return await FilmREPO.add(title=film.title, score=film.score, user_id=user.id, category=category)


async def add_category(category):
    pass

