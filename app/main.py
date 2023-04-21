from fastapi import FastAPI, Path
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()
app.title = "Radar Client"
app.version = "0.0.1"


class User(BaseModel):
    id:  Optional[int]
    name: str = Field(min_length=3, max_length=100)
    surname: str = Field(min_length=3, max_length=100)
    image: str = ""
    email: str = Field(min_length=3, max_length=100)
    password: str = Field(min_length=3, max_length=100)
    state: Optional[bool]

    class Config:
        schema_extra = {
            "example": {
                "name": "user",
                "surname": "admin",
                "image": "",
                "email": "admin@admin.com",
                "password": "secret2022"
            }
        }


@app.post("/user", tags=["User"])
def user_create(user: User):
    return user


@app.get("/users", tags=["User"])
def user_find():
    return []


@app.get("user/{id}", tags=["User"])
def user_find_by_id(id: int = Path(ge=1)):
    return "hola"


@app.put("/user/{id}", tags=["User"])
def user_update(id: int = Path(ge=1)):
    return "hola"


@app.delete("/user/{id}", tags=["User"])
def user_delete(id: int = Path(ge=1)):
    return "hola"
