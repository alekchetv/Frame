from pydantic import BaseModel
from typing import Literal

class FilmData(BaseModel):
    title: str
    score: int