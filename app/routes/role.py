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
def role_update(role: Role, id: int = Path(ge=1)) -> dict:
    db = Session()
    result = db.query(RoleModel).filter(RoleModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={})
    result.name = role.name
    result.description = role.description
    result.role_create = role.role_create
    result.role_update = role.role_update
    result.role_view = role.role_view
    result.role_delete = role.role_delete
    result.user_create = role.user_create
    result.user_view = role.user_view
    result.user_delete = role.user_delete
    result.category_create = role.category_create
    result.category_view = role.category_view
    result.category_update = role.category_update
    result.category_delete = role.category_delete
    result.product_create = role.product_create
    result.product_view = role.product_view
    result.product_update = role.product_update
    result.product_delete = role.product_delete
    result.customer_create = role.customer_create
    result.customer_view = role.customer_view
    result.customer_update = role.customer_update
    result.customer_delete = role.customer_delete
    result.sell_create = role.sell_create
    result.sell_view = role.sell_view
    db.commit()
    return JSONResponse(status_code=200, content={})


@role.delete("/role/{id}", tags=["Role"])
def role_delete(id: int = Path(ge=1)):
    db = Session()
    result = db.query(RoleModel).filter(RoleModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={})
    db.delete(result)
    db.commit()
    return JSONResponse(status_code=200, content={})
