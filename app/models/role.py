import datetime
from sqlalchemy.sql.sqltypes import Integer, String, Boolean, DateTime
from sqlalchemy import Column

from app.config.database import Base


class RoleModel (Base):
    __tablename__ = "roles"
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    description = Column(String(255))
    role_create = Column(Boolean, unique=False, default=False)
    role_view = Column(Boolean, unique=False, default=False)
    role_update = Column(Boolean, unique=False, default=False)
    role_delete = Column(Boolean, unique=False, default=False)
    user_create = Column(Boolean, unique=False, default=False)
    user_view = Column(Boolean, unique=False, default=False)
    user_update = Column(Boolean, unique=False, default=False)
    user_delete = Column(Boolean, unique=False, default=False)
    category_create = Column(Boolean, unique=False, default=False)
    category_view = Column(Boolean, unique=False, default=False)
    category_update = Column(Boolean, unique=False, default=False)
    category_delete = Column(Boolean, unique=False, default=False)
    product_create = Column(Boolean, unique=False, default=False)
    product_view = Column(Boolean, unique=False, default=False)
    product_update = Column(Boolean, unique=False, default=False)
    product_delete = Column(Boolean, unique=False, default=False)
    customer_create = Column(Boolean, unique=False, default=False)
    customer_view = Column(Boolean, unique=False, default=False)
    customer_update = Column(Boolean, unique=False, default=False)
    customer_delete = Column(Boolean, unique=False, default=False)
    sell_create = Column(Boolean, unique=False, default=False)
    sell_view = Column(Boolean, unique=False, default=False)
    state = Column(Boolean, unique=False, default=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)


# RoleModel = Table(
#     "roles",
#     meta,
#     Column("id", Integer, primary_key=True),
#     Column("name", String(255)),
#     Column("description", String(255)),
#     Column("role_create", Boolean, unique=False, default=False),
#     Column("role_view", Boolean, unique=False, default=False),
#     Column("role_update", Boolean, unique=False, default=False),
#     Column("role_delete", Boolean, unique=False, default=False),
#     Column("user_create", Boolean, unique=False, default=False),
#     Column("user_view", Boolean, unique=False, default=False),
#     Column("user_update", Boolean, unique=False, default=False),
#     Column("user_delete", Boolean, unique=False, default=False),
#     Column("category_create", Boolean, unique=False, default=False),
#     Column("category_view", Boolean, unique=False, default=False),
#     Column("category_update", Boolean, unique=False, default=False),
#     Column("category_delete", Boolean, unique=False, default=False),
#     Column("product_create", Boolean, unique=False, default=False),
#     Column("product_view", Boolean, unique=False, default=False),
#     Column("product_update", Boolean, unique=False, default=False),
#     Column("product_delete", Boolean, unique=False, default=False),
#     Column("customer_create", Boolean, unique=False, default=False),
#     Column("customer_view", Boolean, unique=False, default=False),
#     Column("customer_update", Boolean, unique=False, default=False),
#     Column("customer_delete", Boolean, unique=False, default=False),
#     Column("sell_create", Boolean, unique=False, default=False),
#     Column("sell_view", Boolean, unique=False, default=False),
#     Column("state", Boolean, unique=False, default=True)
# )

# meta.create_all(engine)
