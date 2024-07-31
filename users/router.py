from fastapi import APIRouter, HTTPException, status
from exceptions import UserAlreadyExistException, UserNotFoundException
from fastapi import Response, Request
from datetime import timedelta
from users.schemas import UserRegister, UserAuth
from users.repository import UserREPO
from users.auth import get_password_hash, verify_password, create_access_token, authenticate_user

router = APIRouter(
    prefix="/auth",
    tags=["Auth Пользователи"],
)


@router.post("/register")
async def register_user(user: UserRegister):
    existing_user = await UserREPO.find_one_or_none(email=user.email)
    if existing_user:
        raise UserAlreadyExistException
    hashed_password = get_password_hash(user.password)
    await UserREPO.add(username=user.username, email=user.email, password=hashed_password)


@router.post("/login")
async def login_user(response: Response, request: Request, user_data: UserAuth):
    # print(request.json())
    user = await authenticate_user(user_data.email, user_data.password)
    if not user:
        raise UserNotFoundException
    access_token = create_access_token({"id": str(user.id)}, timedelta(minutes=10))
    response.set_cookie("frame_access_token", access_token, httponly=True)


@router.get("/logout")
async def logout_user(response: Response):
    response.delete_cookie("frame_access_token")


