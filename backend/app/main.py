from fastapi import FastAPI
from app.api import router as api_router

app = FastAPI(title="SmartShopper API")
app.include_router(api_router, prefix="/api")

@app.get("/")
async def root():
    return {"status": "ok", "message": "SmartShopper backend running"}
