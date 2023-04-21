from fastapi import APIRouter, Path

from app.helpers.jwt_manager import create_token
from app.schemas.user import User

auth = APIRouter()


@auth.post("/auth/login", tags=["Auth"])
def auth_login(user: User):
    token = create_token(user.dict())
    return token
