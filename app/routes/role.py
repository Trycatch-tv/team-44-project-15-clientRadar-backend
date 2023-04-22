from fastapi import APIRouter, Path
from fastapi.encoders import jsonable_encoder
from typing import List
from fastapi.responses import JSONResponse

from app.config.database import Session
from app.models.role import RoleModel
from app.schemas.role import Role
role = APIRouter()


@role.post("/role", tags=["Role"], response_model=dict, status_code=201)
def role_create(role: Role) -> dict:
    db = Session()
    new_record = RoleModel(**role.dict())
    db.add(new_record)
    db.commit()
    return JSONResponse(status_code=201, content={"message": "Se ha registrado la película"})


@role.get("/roles", tags=["Role"], description="Get a list of all roles",)
def role_find() -> List[Role]:
    db = Session()
    result = db.query(RoleModel).all()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@role.get("/role/{id}", tags=["Role"])
def role_find_by_id(id: int = Path(ge=1)) -> Role:
    db = Session()
    result = db.query(RoleModel).filter(RoleModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@role.put("/role/{id}", tags=["Role"])
def role_update(id: int = Path(ge=1)):
    return "hola"


@role.delete("/role/{id}", tags=["Role"])
def role_delete(id: int = Path(ge=1)):
    return "hola"
