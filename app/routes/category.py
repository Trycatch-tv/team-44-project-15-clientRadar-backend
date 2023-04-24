from fastapi import APIRouter, HTTPException
from typing import List

# importamos el schema correspondiente
from app.schemas.category import CategorySchema
# importamos el modelo correspondiente
from app.models.category import CategoryModel
# importamos la función que nos permitirá obtener una sesión de la base de datos
from app.config.database import Session

router = APIRouter()

# Definimos el endpoint para crear una categoría


@router.post("/category", tags=["Category"], response_model=CategorySchema)
def create_category(category: CategorySchema):
    db = Session()
    # Creamos una nueva instancia del modelo CategoryModel y la agregamos a la base de datos
    db_category = CategoryModel(
        name=category.name, description=category.description)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category  # Retornamos la categoría recién creada

# Definimos el endpoint para obtener todas las categorías


@router.get("/category", tags=["Category"], response_model=List[CategorySchema])
def read_categories(skip: int = 0, limit: int = 100, ):
    db = Session()
    # Obtenemos todas las categorías y las retornamos
    categories = db.query(CategoryModel).offset(skip).limit(limit).all()
    return categories

# Definimos el endpoint para actualizar una categoría


@router.put("/category/{id}", tags=["Category"], response_model=CategorySchema)
def update_category(id: int, category: CategorySchema, ):
    db = Session()
    # Buscamos la categoría correspondiente en la base de datos
    db_category = db.query(CategoryModel).filter(CategoryModel.id == id)
    # Si no encontramos la categoría, lanzamos una excepción 404
    if not db_category.first():
        raise HTTPException(status_code=404, detail="Category not found")
    # Actualizamos los atributos de la categoría con los valores recibidos en el payload
    db_category.update(category.dict())
    db.commit()
    db_category = db_category.first()
    return db_category  # Retornamos la categoría actualizada

# Definimos el endpoint para eliminar una categoría


@router.delete("/category/{id}", tags=["Category"],)
def delete_category(id: int):
    db = Session()
    # Buscamos la categoría correspondiente en la base de datos
    db_category = db.query(CategoryModel).filter(CategoryModel.id == id)
    # Si no encontramos la categoría, lanzamos una excepción 404
    if not db_category.first():
        raise HTTPException(status_code=404, detail="Category not found")
    # Cambiamos el estado de la categoría a "False" (en lugar de eliminarla de la base de datos)
    db_category.update({"state": False})
    db.commit()
    # Retornamos un mensaje de éxito
    return {"detail": "Category deleted successfully"}
