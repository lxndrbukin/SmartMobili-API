from pydantic import BaseModel
from typing import List
from datetime import datetime
from enum import Enum

class Language(str, Enum):
    ro = "ro"
    ru = "ru"

class ItemImageResponse(BaseModel):
    id: int
    image_url: str
    order: int

    class Config:
        from_attributes = True

class ItemTranslationCreate(BaseModel):
    language: Language
    title: str
    description: str | None

class ItemTranslationResponse(BaseModel):
    id: int
    language: Language
    title: str
    description: str | None

    class Config:
        from_attributes = True

class ItemCreate(BaseModel):
    price: float | None = None
    category_id: int
    translations: list[ItemTranslationCreate]

class ItemUpdate(BaseModel):
    price: float | None = None
    category_id: int | None = None

class ItemResponse(BaseModel):
    id: int
    price: float | None = None
    category_id: int
    created_at: datetime
    translations: list[ItemTranslationResponse]
    images: list[ItemImageResponse] = []

    class Config:
        from_attributes = True

class Pagination(BaseModel):
    skip: int
    limit: int

class PaginatedResponse(BaseModel):
    data: List[ItemResponse]
    pagination: Pagination