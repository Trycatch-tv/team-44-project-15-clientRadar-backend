from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.role import role
from app.routes.user import user
from app.routes.auth import auth

from app.config.database import Base, engine

from app.routes.category import router as category_router

app = FastAPI()
app.title = "Radar Client"
app.version = "0.0.1"

Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(role)
app.include_router(user)
app.include_router(auth)
app.include_router(category_router)
