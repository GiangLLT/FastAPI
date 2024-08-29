from fastapi import FastAPI
from typing import Dict
from Model.models import Item
from Controller.controllers import ItemManager
from typing import List


app = FastAPI()
item_manager = ItemManager()

@app.post("/items_create/", response_model=Item)
def create_item(item: Item):
    return item_manager.create_item(item)

@app.get("/items_all/", response_model=Item)
def read_item():
    return item_manager.get_item_all()

@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int):
    return item_manager.get_item(item_id)

@app.get("/items/search/", response_model=List[Item])
def search_items(query: str):
    return item_manager.search_items(query)

@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: Item):
    return item_manager.update_item(item_id, item)

@app.delete("/items/{item_id}", response_model=Dict[str, str])
def delete_item(item_id: int):
    return item_manager.delete_item(item_id)


