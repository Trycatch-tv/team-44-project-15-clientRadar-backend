from sqlalchemy import Column, Integer, String, Boolean
from database import Base

from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.models.category import CategoryModel
from app.schemas.category import CategorySchema
from app.config.database import get_db

router = APIRouter()


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True, index=True)
    description = Column(String(255))
    is_active = Column(Boolean, default=True)


@router.post("/category", response_model=CategorySchema)
def create_category(category: CategorySchema, db: Session = Depends(get_db)):
    db_category = CategoryModel(name=category.name, description=category.description)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

@router.get("/category", response_model=List[CategorySchema])
def read_categories(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    categories = db.query(CategoryModel).offset(skip).limit(limit).all()
    return categories

@router.put("/category/{id}", response_model=CategorySchema)
def update_category(id: int, category: CategorySchema, db: Session = Depends(get_db)):
    db_category = db.query(CategoryModel).filter(CategoryModel.id == id)
    if not db_category.first():
        raise HTTPException(status_code=404, detail="Category not found")
    db_category.update(category.dict())
    db.commit()
    db_category = db_category.first()
    return db_category

@router.delete("/category/{id}")
def delete_category(id: int, db: Session = Depends(get_db)):
    db_category = db.query(CategoryModel).filter(CategoryModel.id == id)
    if not db_category.first():
        raise HTTPException(status_code=404, detail="Category not found")
    db_category.update({"state": False})
    db.commit()
    return {"detail": "Category deleted successfully"}