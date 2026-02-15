from pydantic import BaseModel
from typing import List
from datetime import datetime

class Item(BaseModel):
    title: str
    description: str | None = None
    price: float | None = None
    category: str

class ItemResponse(BaseModel):
    id: int
    title: str
    description: str | None = None
    price: float | None = None
    category: str
    created_at: datetime

    class Config:
        from_attributes = True

class Pagination(BaseModel):
    skip: int
    limit: int

class PaginatedResponse(BaseModel):
    data: List[ItemResponse]
    pagination: Pagination
