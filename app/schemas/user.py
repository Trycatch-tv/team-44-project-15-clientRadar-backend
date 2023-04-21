from pydantic import BaseModel
from typing import Optional
class User(BaseModel):
    id:  Optional[int]
    name: str = ""
    surname: str = ""
    image: str = ""
    email: str = ""
    password: str = ""
    state: bool = True