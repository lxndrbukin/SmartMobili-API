from fastapi import APIRouter, status, Depends
from models.items import ItemCreate, ItemResponse, PaginatedResponse, Pagination
from db import get_db
from db_models.items import Item, ItemImage
from sqlalchemy.orm import Session

items_router = APIRouter(prefix="/items", tags=["items"])

@items_router.get("/", status_code=status.HTTP_200_OK, response_model=PaginatedResponse)
def get_items(
        skip: int = 0,
        limit: int = 10,
        db: Session = Depends(get_db)
    ):
    items = db.query(Item).all()
    return PaginatedResponse(
        data=items,
        pagination=Pagination(skip=skip, limit=limit)
    )

@items_router.get("/{item_id}", status_code=status.HTTP_200_OK, response_model=ItemResponse)
def get_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(Item).get(item_id)
    return item

@items_router.post("/", status_code=status.HTTP_201_CREATED, response_model=ItemResponse)
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    try:
        item = Item(
            title=item.title,
            description=item.description,
            price=item.price,
            category_id=item.category_id
        )
        db.add(item)
        db.commit()
        db.refresh(item)

        image = ItemImage(
            item_id=item.id,
            image_url=item.images,
            order=1
        )
        db.add(image)
        db.commit()

        return item
    except Exception as e:
        return {"success": False, "error": str(e)}

@items_router.put("/{item_id}")
def update_item(item_id: int):
    return {"message": "Updated"}

@items_router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(Item).filter(Item.id == item_id).first()
    if item:
        db.delete(item)
        db.commit()
    return None