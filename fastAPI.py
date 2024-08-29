from fastapi import FastAPI, HTTPExceptionc
from fastapi.responses import JSONResponse
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None, data: str = None):
    json_data = {"item_id": item_id, "q": q, "data": data}
    return JSONResponse(content=json_data, media_type="application/json")
