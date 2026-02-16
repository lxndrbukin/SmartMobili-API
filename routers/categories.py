from fastapi import APIRouter, status, Depends
from db import get_db
from db_models.items import Category
from sqlalchemy.orm import Session

categories_router = APIRouter(prefix="/categories", tags=["categories"])

@categories_router.get("/", status_code=status.HTTP_200_OK)
def get_categories():
    pass

@categories_router.post("/", status_code=status.HTTP_201_CREATED)
def create_category(category: str, db: Session = Depends(get_db)):
    category = Category(
        name=category,
        slug=category.lower()
    )
    db.add(category)
    db.commit()
    db.refresh(category)
    return {
        "success": True,
        "message": "Category created",
        "category": category
    }