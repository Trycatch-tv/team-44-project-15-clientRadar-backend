from fastapi import APIRouter, Path
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from werkzeug.security import check_password_hash

from app.helpers.jwt_manager import create_token
from app.config.database import Session
from app.models.user import UserModel
from app.schemas.auth import Auth

auth = APIRouter()


@auth.post("/auth/login", tags=["Auth"], description="")
def auth_login(user: Auth) -> dict:
    db = Session()
    record = db.query(UserModel).filter(UserModel.email == user.email).first()
    if not record:
        return JSONResponse(status_code=404, content={})
    password_match = check_password_hash(record.password, user.password)
    if not password_match:
        return JSONResponse(status_code=404, content={})
    token = create_token({"sub": record.id, "email": record.email})
    return JSONResponse(status_code=200, content={"token": token, "user": jsonable_encoder(record)})
