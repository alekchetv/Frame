from database import async_session
from BaseRepository import BaseREPO
from models import Film


class FilmREPO(BaseREPO):
    model = Film

