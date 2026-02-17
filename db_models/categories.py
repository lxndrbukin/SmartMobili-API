from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from db import Base

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    slug = Column(String(100), unique=True, nullable=False)

    items = relationship("Item", back_populates="category")
    translations = relationship("CategoryTranslation", back_populates="category", cascade="all, delete-orphan")

class CategoryTranslation(Base):
    __tablename__ = "category_translations"

    id = Column(Integer, primary_key=True, index=True)
    category_id = Column(Integer, ForeignKey("categories.id"))
    language = Column(String(2), nullable=False)
    name = Column(String(100), nullable=False)

    category = relationship("Category", back_populates="translations")