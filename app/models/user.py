from sqlalchemy.sql.sqltypes import Integer, String, Boolean
from sqlalchemy import Column, Table

from app.config.database import Base


class UserModel (Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    role = Column(Integer)
    name = Column(String(255))
    surname = Column(String(255))
    image = Column(String(255))
    email = Column(String(255), unique=True)
    password = Column(String(255))
    state = Column(Boolean, unique=False, default=True)
