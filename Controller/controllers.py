from typing import Dict
from fastapi import HTTPException
from Model.models import Item
from typing import List
from fastapi.responses import JSONResponse
import json

class ItemManager1:
    def __init__(self):
        self.items_db: Dict[Item] = []
        # self.items_db: Dict[Item] = [
        #     {
        #         "id"  : 1,
        #         "name": "Máy game PS5",
        #         "description": "Máy game PS5 Premiere",
        #         "price": 25000000,
        #         "tax": 2500000,
        #     },
        #     {
        #         "id"  : 2,
        #         "name": "Máy game PS6",
        #         "description": "Máy game PS6",
        #         "price": 25000000,
        #         "tax": 2500000,
        #     },
        # ]

    def create_item_old(self, item: Item) -> Item:
        item_id = self.current_id
        self.items_db[item_id] = item
        self.current_id += 1
        return item
    
    def create_item(self, item: Item) -> Item:
        items = {
                "id"  : item.id,
                "name": item.name,
                "description": item.description,
                "price": item.price,
                "tax": item.tax
        }
        try:
            self.items_db.append(items)
            sta = "success"
        except Exception as e:
            sta = e
            
        result = {
            "message": sta,
            "data"  : items
        }
        return JSONResponse(content=result, media_type="application/json")

    def get_item_all(self) -> Item:
        item = self.items_db
        if item is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return JSONResponse(content=item, media_type="application/json")
    
    def get_item(self, item_id: int) -> Item:
        # all = self.items_db.get(__name__=="Máy game PS5")
        item = self.items_db.get(item_id)
        if item is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return JSONResponse(content=item, media_type="application/json", status_code=200)
    
    def search_items(self, query: str) -> List[Item]:
        # Tìm tất cả mặt hàng có tên chứa chuỗi query
        results = [item for item in self.items_db if query.lower() in item["name"].lower()]
        # results = [item for item in self.items_db.values() if query.lower() in item.name.lower()]
        if not results:
            raise HTTPException(status_code=404, detail="No items found matching the query")
        return results

    def update_item(self, item_id: int, item: Item) -> Item:
        # Tìm mục theo item_id
        for i, existing_item in enumerate(self.items_db):
            if existing_item["id"] == item_id:
                updated_item = {
                    "id": item.id,
                    "name": item.name if item.name else existing_item["name"],
                    "description": item.description if item.description else existing_item["description"],
                    "price": item.price if item.price > 0 else existing_item["price"],
                    "tax": item.tax if item.tax > 0 else existing_item["tax"],
                }
                # Cập nhật thông tin mục
                try:
                    self.items_db[i] = updated_item
                    # sta = "Success"
                except Exception as e:
                    # sta = e
                    raise HTTPException(status_code=500, detail=str(e))
                    
                result = {
                    "message": "Success",
                    "data"  : updated_item
                }
                return JSONResponse(content=result, media_type="application/json", status_code=200)

        # Nếu không tìm thấy item_id
        return JSONResponse(content={"message": "Item not found"}, status_code=404)

    def delete_item(self, item_id: int) -> Dict[str, str]:
        for i, existing_item in enumerate(self.items_db):
            if existing_item["id"] == item_id:
                # Cập nhật thông tin mục
                try:
                    del self.items_db[i]
                except Exception as e:
                    raise HTTPException(status_code=500, detail=str(e))
                    
                result = {
                    "message": f"Delete success - id: {item_id}",
                    "id"  : item_id
                }
                return JSONResponse(content=result, media_type="application/json", status_code=200)

        # Nếu không tìm thấy item_id
        return JSONResponse(content={"message": "Item not found"}, status_code=404)


class ItemManager:
    def __init__(self):
        self.items_db: Dict[int, Item] = {
            1:{
                "id"  : 1,
                "name": "Máy game PS5",
                "description": "Máy game PS5 Premiere",
                "price": 25000000,
                "tax": 2500000,
            },
            2:{
                "id"  : 2,
                "name": "Máy game PS6",
                "description": "Máy game PS6",
                "price": 25000000,
                "tax": 2500000,
            },
        }
        
    # def update_current_id(self):
    #     self.current_id = max(item["id"] for item in self.items_db.values()) + 1 if self.items_db else 1

    def create_item_old(self, item: Item) -> Item:
        item_id = self.current_id
        self.items_db[item_id] = item
        self.current_id += 1
        return item
    
    def create_item(self, item: Item) -> Item:
        if item.id in self.items_db:
            raise HTTPException(status_code=400, detail="Item ID already exists")
        
        try:
            new_item = item.dict()
            self.items_db[item.id] = new_item
        except Exception as e:
             raise HTTPException(status_code=404, detail=e)
            
        result = {
            "message": "success",
            "data"  : new_item
        }
        return JSONResponse(content=result, media_type="application/json")

    def get_item_all(self) -> Item:
        # item = self.items_db
        items_list = sorted(self.items_db.values(), key=lambda x: x['id'], reverse=True)
        if items_list is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return JSONResponse(content={"items": items_list}, media_type="application/json")
    
    def get_item(self, item_id: int) -> Item:
        # all = self.items_db.get(__name__=="Máy game PS5")
        item = self.items_db.get(item_id)
        if item is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return JSONResponse(content=item, media_type="application/json", status_code=200)
    
    def search_items(self, query: str) -> List[Item]:
        # Tìm tất cả mặt hàng có tên chứa chuỗi query
        results = [item for item in self.items_db if query.lower() in item["name"].lower()]
        # results = [item for item in self.items_db.values() if query.lower() in item.name.lower()]
        if not results:
            raise HTTPException(status_code=404, detail="No items found matching the query")
        return results

    def update_item(self, item_id: int, item: Item) -> JSONResponse:
        if item_id not in self.items_db:
            return JSONResponse(content={"message": "Item not found"}, status_code=404)

        existing_item = self.items_db[item_id]
        updated_item = {
            "id": item_id,
            "name": item.name if item.name else existing_item["name"],
            "description": item.description if item.description else existing_item["description"],
            "price": item.price if item.price > 0 else existing_item["price"],
            "tax": item.tax if item.tax > 0 else existing_item["tax"],
        }

        try:
            self.items_db[item_id] = updated_item
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

        result = {
            "message": "Success",
            "data": updated_item
        }
        return JSONResponse(content=result, media_type="application/json", status_code=200)

    def delete_item(self, item_id: int) -> Dict[str, str]:
        if item_id not in self.items_db:
            return JSONResponse(content={"message": "Item not found"}, status_code=404)
        try:
            del self.items_db[item_id]
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

        result = {
            "message": "Delete Success",
        }
        return JSONResponse(content=result, media_type="application/json", status_code=200)      
