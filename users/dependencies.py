from fastapi import HTTPException, Depends, Request, status
from jose import jwt, JWTError
from config import SECRET_KEY, ALGORITHM
from datetime import datetime
from users.repository import UserREPO
from exceptions import (TokenNotValidException, TokenNotFoundException, TokenIsExpiredException, TokenIdNotFoundException,
                        UserNotFoundException)


def get_token(request: Request):
    try:
        token = request.cookies["frame_access_token"]
    except KeyError:
        raise TokenNotFoundException
    if not token:
        raise TokenNotFoundException
    return token


async def current_user(token: str = Depends(get_token)):
    try:
        payload = jwt.decode(
            token, SECRET_KEY, ALGORITHM
        )
    except JWTError:
        raise TokenNotValidException
    expire: str = payload.get("exp")
    if (not expire) or (int(expire) < datetime.utcnow().timestamp()):
        raise TokenIsExpiredException
    user_id: str = payload.get("id")
    if not user_id:
        raise TokenIdNotFoundException
    user = await UserREPO.find_by_id(int(user_id))
    if not user:
        raise UserNotFoundException
    return user
