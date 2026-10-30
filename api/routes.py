# FastAPI concept: REST endpoints.
# Each route is a plain Python function decorated with an HTTP verb + path.
# FastAPI serialises the return value to JSON automatically.

from api.app import app
from shared.data import items_db


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/items")
def list_items():
    return items_db


@app.get("/items/{item}")
def get_item(item: str):
    count = items_db.get(item.lower())
    return {"item": item, "stock": count} if count is not None else {"error": "not found"}


@app.post("/items/{item}/{count}")
def set_item(item: str, count: int):
    items_db[item.lower()] = count
    return {"item": item, "stock": count}
