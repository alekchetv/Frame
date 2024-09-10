from database import async_session
from BaseRepository import BaseREPO
from models import Film
from sqlalchemy import select, insert, values, update
from sqlalchemy.sql.expression import func


class FilmREPO(BaseREPO):
    model = Film

    @classmethod
    async def top_rating(cls):
        async with async_session() as session:
            query = select(cls.model)
            films = await session.execute(query)
            return films.scalars().all()

    @classmethod
    async def get_two_random(cls, **kwargs):
        async with async_session() as session:
            query = select(cls.model).filter_by(**kwargs).order_by(func.random()).limit(2)
            films = await session.execute(query)
            return films.scalars().all()

    @classmethod
    async def update_rating(cls, film_id, rating):
        async with async_session() as session:
            query = update(cls.model).values(score=rating).where(cls.model.id == film_id)
            rating = await session.execute(query)
            await session.commit()
