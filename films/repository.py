from database import async_session
from BaseRepository import BaseREPO
from models import Film
from sqlalchemy import select, insert, values


class FilmREPO(BaseREPO):
    model = Film

    @classmethod
    async def top_rating(cls):
        async with async_session() as session:
            query = select(cls.model)
            films = await session.execute(query)
            return films.scalars().all()
