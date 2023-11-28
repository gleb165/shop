from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import Annotated

name = 'Pydantic PyCharm Plugin'
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


app = FastAPI()


@app.post('/items/{items}')
async def first_post(items_id: int, item: Item, q: str | None = None):
    if q:
        return {'q': q}

    return {'items_id': items_id, **item.dict()}



@app.get("/items/")
async def read_items(q: Annotated[list[str] | None, Query()] = None):
    query_items = {"q": q}
    return query_items