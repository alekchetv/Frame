from fastapi import APIRouter, Depends, Request
from sqlalchemy.ext.asyncio import AsyncSession
from models import Film
from sqlalchemy import select
from database import async_session
from models import User, Film, Category
from films.repository import FilmREPO
from users.dependencies import current_user, get_token


router = APIRouter(
    prefix="/films",
    tags=["Добавление,оценкаы фильмов"],
)

@router.get("")
async def get_films(user: User = Depends(current_user)):
    print(user, user.id)



