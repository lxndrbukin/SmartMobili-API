from pydantic import BaseModel
from typing import List
from datetime import datetime

class ItemImageResponse(BaseModel):
    id: int
    image_url: str
    order: int

    class Config:
        from_attributes = True

class ItemListResponse(BaseModel):
    id: int
    title: str
    price: float | None
    thumbnail: str | None

class ItemDetailResponse(BaseModel):
    id: int
    title: str
    description: str | None
    price: float | None
    images: list[ItemImageResponse]

class ItemCreate(BaseModel):
    title: str
    description: str | None = None
    price: float | None = None
    category_id: int

class ItemUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    price: float | None = None
    category_id: int | None = None

class ItemResponse(BaseModel):
    id: int
    title: str
    description: str | None = None
    price: float | None = None
    category_id: int
    created_at: datetime
    images: list[ItemImageResponse] = []

    class Config:
        from_attributes = True

class Pagination(BaseModel):
    skip: int
    limit: int

class PaginatedResponse(BaseModel):
    data: List[ItemResponse]
    pagination: Pagination