import json
from films import repository
from fastapi import Depends
from films.repository import FilmREPO
from films.schemas import FilmChoose
from users.dependencies import current_user
from models import User, Film


async def elo_rating(choose: FilmChoose, film_id: int):
    choose = choose.model_dump()
    print(choose)
    ra = await FilmREPO.find_by_id(choose["idA"])
    rb = await FilmREPO.find_by_id(choose["idB"])
    ra = ra.score
    rb = rb.score
    print(ra, rb)
    pa = 1/(1+10**((rb-ra)/2))
    print("pa=", pa)
    if choose["AWinner"]:
        ra += (1-pa)*2
        rb += (0-pa)*2
        print(ra, rb)
        if ra > 10:
            ra = 10
        print("after", ra, rb)
        await FilmREPO.update_rating(choose["idA"], ra)
        await FilmREPO.update_rating(choose["idB"], rb)
    else:
        rb += (1 - pa) * 2
        ra += (0 - pa) * 2
        await FilmREPO.update_rating(choose["idA"], ra)
        await FilmREPO.update_rating(choose["idB"], rb)
