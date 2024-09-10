from pydantic import BaseModel
from typing import Literal


class FilmData(BaseModel):
    title: str
    score: float


class FilmChoose(BaseModel):
    idA: int
    idB: int
    AWinner: bool
