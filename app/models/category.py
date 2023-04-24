from sqlalchemy import Column, Integer, String, Boolean
from app.config.database import Base

class CategoryModel(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True, index=True)
    description = Column(String(255))
    is_active = Column(Boolean, default=True)
