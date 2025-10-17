# Starter code for FastAPI REST API assignment

# main.py
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Example Pydantic model
class Item(BaseModel):
    id: int
    name: str
    description: str = None

# In-memory storage
items = []

@app.get("/items", response_model=List[Item])
def get_items():
    return items

@app.post("/items", response_model=Item)
def create_item(item: Item):
    items.append(item)
    return item

# Add update and delete endpoints as part of the assignment tasks
