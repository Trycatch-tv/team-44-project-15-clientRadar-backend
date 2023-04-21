from fastapi import APIRouter, Path

from app.schemas.user import User


user = APIRouter()


@user.post("/user", tags=["User"])
def user_create(user: User):
    return user


@user.get("/users", tags=["User"])
def user_find():
    return []


@user.get("user/{id}", tags=["User"])
def user_find_by_id(id: int = Path(ge=1)):
    return "hola"


@user.put("/user/{id}", tags=["User"])
def user_update(id: int = Path(ge=1)):
    return "hola"


@user.delete("/user/{id}", tags=["User"])
def user_delete(id: int = Path(ge=1)):
    return "hola"
