from fastapi import FastAPI, APIRouter, Depends
from fastapi.staticfiles import StaticFiles
from routers.items import items_router
from routers.categories import categories_router
from routers.inquiries import inquiries_router
from db import engine, Base, get_db
from db_models.items import Item
from db_models.categories import Category
from sqlalchemy.orm import Session


Base.metadata.create_all(bind=engine)

app = FastAPI(title="SmartMobili", description="SmartMobili", version="1.0")

app.mount("/static", StaticFiles(directory="static"), name="static")

v1_router = APIRouter(prefix="/api/v1")
v1_router.include_router(items_router)
v1_router.include_router(categories_router)
v1_router.include_router(inquiries_router)
app.include_router(v1_router)

@app.get("/")
def home(db: Session = Depends(get_db)):
    return {
        "server": "SmartMobili API",
        "version": "1.0",
        "total_items": db.query(Item).count()
    }