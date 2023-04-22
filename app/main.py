from fastapi import FastAPI

from app.routes.role import role

from app.config.database import Base, engine

app = FastAPI()
app.title = "Radar Client"
app.version = "0.0.1"

Base.metadata.create_all(bind=engine)

app.include_router(role)
