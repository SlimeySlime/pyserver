from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
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