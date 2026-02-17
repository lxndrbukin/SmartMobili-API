from pydantic import BaseModel
from enum import Enum

class Language(str, Enum):
    ro = "ro"
    ru = "ru"

class CategoryTranslationCreate(BaseModel):
    language: Language
    name: str

class CategoryTranslationResponse(BaseModel):
    id: int
    language: Language
    name: str

    class Config:
        from_attributes = True

class CategoryCreate(BaseModel):
    slug: str
    translations: list[CategoryTranslationCreate]

class CategoryResponse(BaseModel):
    id: int
    slug: str
    translations: list[CategoryTranslationResponse]

    class Config:
        from_attributes = True