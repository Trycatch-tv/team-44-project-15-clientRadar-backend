from sqlalchemy import Column, Table
from sqlalchemy.sql.sqltypes import Integer, String, Boolean
from config.db import meta, engine

users = Table(
    "roles",
    meta,
    Column("id", Integer, primary_key=True),
    Column("name",String(255)),
    Column("description", String(255)),
    Column("role_create", Boolean()),
    Column("role_view", Boolean()),
    Column("role_update", Boolean()),
    Column("role_delete", Boolean()),

    Column("user_create", Boolean()),
    Column("user_view", Boolean()),
    Column("user_update", Boolean()),
    Column("user_delete", Boolean()),
    Column("category_create", Boolean()),
    Column("category_view", Boolean()),
    Column("category_update", Boolean()),
    Column("category_delete", Boolean()),
    Column("product_create", Boolean()),
    Column("product_view", Boolean()),
    Column("product_update", Boolean()),
    Column("product_delete", Boolean()),
    Column("customer_create", Boolean()),
    Column("customer_view", Boolean()),
    Column("customer_update", Boolean()),
    Column("customer_delete", Boolean()),
    Column("sell_create", Boolean()),
    Column("sell_view", Boolean()),
    Column("state", Boolean()),
)

meta.create_all(engine)