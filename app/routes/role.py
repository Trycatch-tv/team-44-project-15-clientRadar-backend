from fastapi import APIRouter, Path
from app.schemas.role  import Role

role = APIRouter()

@role.post("/role", tags=["Role"])
def role_create(role: Role):
    return role


@role.get("/roles", tags=["Role"])
def role_find():
    return []


@role.get("role/{id}", tags=["Role"])
def role_find_by_id(id: int = Path(ge=1)):
    return "hola"


@role.put("/role/{id}", tags=["Role"])
def role_update(id: int = Path(ge=1)):
    return "hola"


@role.delete("/role/{id}", tags=["Role"])
def role_delete(id: int = Path(ge=1)):
    return "hola"