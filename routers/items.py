from fastapi import APIRouter, status, Depends, HTTPException
from models.items import ItemCreate, ItemUpdate, ItemResponse, PaginatedResponse, Pagination
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
    items = db.query(Item).offset(skip).limit(limit).all()
    return PaginatedResponse(
        data=items,
        pagination=Pagination(skip=skip, limit=limit)
    )

@items_router.get("/{item_id}", status_code=status.HTTP_200_OK, response_model=ItemResponse)
def get_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(Item).get(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@items_router.post("/", status_code=status.HTTP_201_CREATED, response_model=ItemResponse)
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    db_item = Item(
        title=item.title,
        description=item.description,
        price=item.price,
        category_id=item.category_id
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)

    return db_item

@items_router.put("/{item_id}", response_model=ItemResponse)
def update_item(item_id: int, data: ItemUpdate, db: Session = Depends(get_db)):
    item = db.query(Item).filter(Item.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    if data.title is not None:
        item.title = data.title
    if data.description is not None:
        item.description = data.description
    if data.price is not None:
        item.price = data.price
    if data.category_id is not None:
        item.category_id = data.category_id
    db.commit()
    db.refresh(item)

    return item

@items_router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(Item).filter(Item.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(item)
    db.commit()

    return None