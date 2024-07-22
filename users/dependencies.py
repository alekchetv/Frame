from fastapi import HTTPException, Depends, Request, status
from jose import jwt, JWTError
from config import SECRET_KEY, ALGORITHM
from datetime import datetime
from users.repository import UserREPO


def get_token(request: Request):
    token = request.cookies["frame_access_token"]
    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return token


async def current_user(token: str = Depends(get_token)):
    try:
        payload = jwt.decode(
            token, SECRET_KEY, ALGORITHM
        )
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    expire: str = payload.get("exp")
    if (not expire) or (int(expire) < datetime.utcnow().timestamp()):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    user_id: str = payload.get("id")
    if not user_id:
        print("user_id")
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    user = await UserREPO.find_by_id(int(user_id))
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return user
