from database import async_session
from models import User
from sqlalchemy import select, insert, values


class BaseREPO:
    model = None

    @classmethod
    async def find_all(cls, **kwargs):
        async with async_session() as session:
            query = select(cls.model).filter_by(**kwargs)
            models = await session.execute(query)
            return models.scalars().all()

    @classmethod
    async def find_one_or_none(cls, **kwargs):
        async with async_session() as session:
            query = select(cls.model).filter_by(**kwargs)
            models = await session.execute(query)
            return models.scalars().all()

    @classmethod
    async def add(cls, **kwargs):
        async with async_session() as session:
            query = insert(cls.model).values(**kwargs)
            result = await session.execute(query)
            await session.commit()
            return result
