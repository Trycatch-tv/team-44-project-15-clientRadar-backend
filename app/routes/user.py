from fastapi import APIRouter, Path
from fastapi.encoders import jsonable_encoder
from typing import List
from fastapi.responses import JSONResponse
from cryptography.fernet import Fernet

from app.config.database import Session
from app.models.user import UserModel
from app.schemas.user import User

user = APIRouter()
key = Fernet.generate_key()
f = Fernet(key)


@user.post("/user", tags=["User"], description="Add record to database")
def role_create(payload: User) -> dict:
    db = Session()
    new_record = UserModel()
    new_record.role = payload.role
    new_record.name = payload.name
    new_record.surname = payload.surname
    new_record.image = payload.image
    new_record.email = payload.email
    new_record.password = f.encrypt(payload.password.encode("utf-8"))
    new_record.state = True
    db.add(new_record)
    db.commit()
    return JSONResponse(status_code=201, content={})


@user.get("/users", tags=["User"], description="Get records from database",)
def role_find() -> List[User]:
    db = Session()
    result = db.query(UserModel).all()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@user.get("/user/{id}", tags=["User"], description="Get record from database")
def role_find_by_id(id: int = Path(ge=1)) -> User:
    db = Session()
    result = db.query(UserModel).filter(UserModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@user.put("/user/{id}", tags=["User"], description="Update data from the record in the database")
def role_update(user: User, id: int = Path(ge=1)) -> dict:
    db = Session()
    result = db.query(UserModel).filter(UserModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={})
    result.name = user.name
    result.surname = user.surname
    db.commit()
    return JSONResponse(status_code=200, content={})


@user.delete("/user/{id}", tags=["User"], description="Delete record from database")
def role_delete(id: int = Path(ge=1)):
    db = Session()
    result = db.query(UserModel).filter(UserModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={})
    db.delete(result)
    db.commit()
    return JSONResponse(status_code=200, content={})
