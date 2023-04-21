from fastapi import FastAPI

from app.routes.role import role

app = FastAPI()


app.title = "Radar Client"
app.version = "0.0.1"


app.include_router(role)