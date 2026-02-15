from fastapi import FastAPI, APIRouter
from datetime import datetime

app = FastAPI(title="SmartMobili", description="SmartMobili", version="1.0")

v1_router = APIRouter(prefix="/api/v1")
app.include_router(v1_router)

@app.get("/")
def home():
    return {
        "server": "SmartMobili API",
        "version": "1.0",
        "current_date": str(datetime.today())
    }
