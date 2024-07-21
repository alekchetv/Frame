from fastapi import FastAPI
from films.router import router as router_films
from database import async_session
from sqlalchemy import select
from models import Film, User
from users.router import router as router_users

app = FastAPI(
    title="Frame"
)

app.include_router(router_films)
app.include_router(router_users)


