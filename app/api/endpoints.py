# app/api/endpoints.py
from fastapi import APIRouter, HTTPException
from app.models.item import Item

router = APIRouter()

# Endpoint para obtener un item por ID
@router.get("/items/{item_id}", response_model=Item)
async def get_item(item_id: int):
    # Ejemplo: Lógica de negocio para obtener el item
    if item_id == 1:
        return Item(name="Item 1", description="A sample item", price=10.0, tax=1.5)
    raise HTTPException(status_code=404, detail="Item not found")

# Endpoint para crear un nuevo item
@router.post("/items/", response_model=Item)
async def create_item(item: Item):
    # Ejemplo: Lógica de negocio para guardar el item
    return item
