from fastapi import APIRouter
from users.schemas import UserRegister
from users.repository import UserREPO


router = APIRouter(
    prefix="/auth",
    tags=["Auth Пользователи"],
)

@router.post("/register")
async def register_user(user: UserRegister):
    existing_user = UserREPO.find_all()


@router.get("")
async def get_users():
    return await UserREPO.find_all()


@router.post("/add_user")
async def add_user(user: UserRegister):
    return await UserREPO.add(username=user.username, email=user.email, password=user.password)
