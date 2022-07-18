from typing import Union
from fastapi import FastAPI
import fastapi
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# uvicorn main:app --reload
# main : app (FastAPI() 변수이름)
app = FastAPI()
origins = [
    "http://localhost:3035",
    "http://bdanbonga.com"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"], )
# Union[X, Y] == X | Y

class Item(BaseModel):
    name: str
    pricae : float
    is_offer : Union[bool, None] = None

@app.get('/')
def read_root():
    return { "hello" : "World" }

@app.get('/items/{item_id}')
def read_item(item_id : int, q: Union[str, None] = None):
    return {"item_id": item_id, "q: Union": q}
    
@app.put('/items/{item_id}')
def update_item(item_id : int   , item: Item):
    return {"item_name" : item.name, "item_id" : item_id}

@app.get('/bdanbonga/items')
def read_hanbok():
    return { "hanboks" : "hanbok"}