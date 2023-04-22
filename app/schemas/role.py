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

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "name":  "admin",
                "description": "administrador",
                "role_create": True,
                "role_view": True,
                "role_update": True,
                "role_delete": True,
                "user_create": True,
                "user_view": True,
                "user_update": True,
                "user_delete": True,
                "category_create": True,
                "category_view": True,
                "category_update": True,
                "category_delete": True,
                "product_create": True,
                "product_view": True,
                "product_update": True,
                "product_delete": True,
                "customer_create": True,
                "customer_view": True,
                "customer_update": True,
                "customer_delete": True,
                "sell_create": True,
                "sell_view": True,
                "state": True,
            }
        }
