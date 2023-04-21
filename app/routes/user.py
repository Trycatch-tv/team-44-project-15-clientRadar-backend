from fastapi import APIRouter

user = APIRouter()

@user.get("/")
def hello():
    return "Hello world"