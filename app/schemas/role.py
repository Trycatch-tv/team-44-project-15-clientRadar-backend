from pydantic import BaseModel
from typing import Optional

class Role(BaseModel):
    id:  Optional[int]
    name: str = ""
    description: str = ""
    role_create: bool = False
    role_view: bool = False
    role_update: bool = False
    role_delete: bool = False
    user_create: bool = False
    user_view: bool = False
    user_update: bool = False
    user_delete: bool = False
    category_create: bool = False
    category_view: bool = False
    category_update: bool = False
    category_delete: bool = False
    product_create: bool = False
    product_view: bool = False
    product_update: bool = False
    product_delete: bool = False
    customer_create: bool = False
    customer_view: bool = False
    customer_update: bool = False
    customer_delete: bool = False
    sell_create: bool = False
    sell_view: bool = False
    state: bool = True