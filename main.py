from fastapi import FastAPI, APIRouter
from datetime import datetime
from routers.items import items_router
from routers.categories import categories_router
from routers.inquiries import inquiries_router
from db import engine, Base
from db_models.items import Item, Category, ItemImage

Base.metadata.create_all(bind=engine)

app = FastAPI(title="SmartMobili", description="SmartMobili", version="1.0")

v1_router = APIRouter(prefix="/api/v1")
v1_router.include_router(items_router)
v1_router.include_router(categories_router)
v1_router.include_router(inquiries_router)
app.include_router(v1_router)

@app.get("/")
def home():
    return {
        "server": "SmartMobili API",
        "version": "1.0",
        "current_date": str(datetime.today())
    }