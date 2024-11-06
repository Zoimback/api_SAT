# app/main.py
from fastapi import FastAPI
from app.api import endpoints

app = FastAPI()

# Incluir el router de endpoints
app.include_router(endpoints.router)

@app.get("/")
async def root():
    return {"message": "Hello, World!"}
