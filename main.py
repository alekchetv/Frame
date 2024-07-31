from fastapi import FastAPI
from films.router import router as router_films
from users.router import router as router_users
from pages.router import router as router_pages
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    title="Frame"
)
origins = [

    "http://127.0.0.1:3000",
    "http://localhost:3000",

]
app.include_router(router_films)
app.include_router(router_users)
app.include_router(router_pages)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
