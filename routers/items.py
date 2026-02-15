from fastapi import APIRouter, status
from models.items import Item, ItemResponse, PaginatedResponse

items_router = APIRouter(prefix="/items", tags=["items"])

@items_router.get("/", status_code=status.HTTP_200_OK, response_model=PaginatedResponse)
def get_items(
        skip: int = 0,
        limit: int = 10,
        category: str | None = None
    ):
    return []

@items_router.get("/{item_id}", status_code=status.HTTP_200_OK, response_model=ItemResponse)
def get_item(item_id: int):
    return {"item": "data"}

@items_router.post("/", status_code=status.HTTP_201_CREATED)
def create_item(item: Item):
    print(item.title)
    return True

@items_router.put("/{item_id}")
def update_item(item_id: int):
    return {"message": "Updated"}

@items_router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int):
    return None