from sqlalchemy import MetaData, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, Mapped, mapped_column
from typing import List


Base = declarative_base()
Base.metadata = MetaData()


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    # films: Mapped[List["Film"]] = relationship()


class Film(Base):
    __tablename__ = "films"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    title: Mapped[str] = mapped_column(nullable=False)
    score: Mapped[int] = mapped_column(nullable=False)
    category: Mapped[str] = mapped_column(nullable=False)
#     category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"))
#
#
# class Category(Base):
#     __tablename__ = "categories"
#
#     id: Mapped[int] = mapped_column(primary_key=True)
#     title: Mapped[str] = mapped_column(nullable=False)
