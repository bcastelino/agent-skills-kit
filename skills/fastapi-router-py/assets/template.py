"""FastAPI Router Template.

Usage:
    Copy this template and customize for your resource.
    Replace 'Item' with your model name and update fields.
"""
from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel

router = APIRouter(prefix="/items", tags=["items"])


# ---- Schemas ----

class ItemCreate(BaseModel):
    name: str
    description: Optional[str] = None
    price: float


class ItemUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None


class ItemResponse(BaseModel):
    id: int
    name: str
    description: Optional[str]
    price: float

    class Config:
        from_attributes = True


# ---- Endpoints ----

@router.get("/", response_model=list[ItemResponse])
async def list_items(skip: int = 0, limit: int = 100):
    """List all items with pagination."""
    # TODO: Replace with database query
    return []


@router.get("/{item_id}", response_model=ItemResponse)
async def get_item(item_id: int):
    """Get a single item by ID."""
    # TODO: Replace with database query
    raise HTTPException(status_code=404, detail="Item not found")


@router.post("/", response_model=ItemResponse, status_code=status.HTTP_201_CREATED)
async def create_item(item: ItemCreate):
    """Create a new item."""
    # TODO: Replace with database insert
    return {"id": 1, **item.model_dump()}


@router.put("/{item_id}", response_model=ItemResponse)
async def update_item(item_id: int, item: ItemUpdate):
    """Update an existing item."""
    # TODO: Replace with database update
    raise HTTPException(status_code=404, detail="Item not found")


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_item(item_id: int):
    """Delete an item."""
    # TODO: Replace with database delete
    raise HTTPException(status_code=404, detail="Item not found")
