from fastapi import APIRouter, status, Depends
from db import get_db
from models.categories import CategoryCreate, CategoryResponse
from db_models.categories import Category
from sqlalchemy.orm import Session

categories_router = APIRouter(prefix="/categories", tags=["categories"])

@categories_router.get("/", status_code=status.HTTP_200_OK, response_model=list[CategoryResponse])
def get_categories(db: Session = Depends(get_db)):
    categories = db.query(Category).all()
    return categories

@categories_router.post("/", status_code=status.HTTP_201_CREATED, response_model=CategoryResponse)
def create_category(category: CategoryCreate, db: Session = Depends(get_db)):
    db_category = Category(
        name=category.name,
        slug=category.name.lower().replace(" ", "-")
    )
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category