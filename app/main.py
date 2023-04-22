from fastapi import FastAPI

from app.routes.role import role
from app.routes.user import user
from app.routes.auth import auth

from app.config.database import Base, engine

app = FastAPI()
app.title = "Radar Client"
app.version = "0.0.1"

Base.metadata.create_all(bind=engine)

app.include_router(role)
app.include_router(user)
app.include_router(auth)
