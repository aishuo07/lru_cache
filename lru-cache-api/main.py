from fastapi import FastAPI, HTTPException
from typing import Dict

from LRUCache import LruCache

app = FastAPI()

# Dictionary to store different LRU cache collections
cache_collections: Dict[str, LruCache] = {}


@app.post("/collections/{collection_name}")
def create_cache_collection(collection_name: str, capacity: int):
    if collection_name in cache_collections:
        raise HTTPException(status_code=400, detail="Collection already exists")
    cache_collections[collection_name] = LruCache(capacity)
    return {"message": f"Collection '{collection_name}' created with capacity {capacity}"}


@app.put("/collections/{collection_name}")
def update_cache_collection(collection_name: str, capacity: int):
    if collection_name not in cache_collections:
        raise HTTPException(status_code=404, detail="Collection not found")
    cache_collections[collection_name].setCapacity(capacity)
    return {"message": f"Collection '{collection_name}' updated to capacity {capacity}"}


@app.post("/collections/{collection_name}/items")
def add_item_to_cache(collection_name: str, key: str, value):
    if collection_name not in cache_collections:
        raise HTTPException(status_code=404, detail="Collection not found")
    cache_collections[collection_name].put(key, value)
    return {"message": f"Item added to collection '{collection_name}'"}


@app.get("/collections/{collection_name}/items/{key}")
def get_item_from_cache(collection_name: str, key: str):
    if collection_name not in cache_collections:
        raise HTTPException(status_code=404, detail="Collection not found")
    value = cache_collections[collection_name].get(key)
    if value is None:
        raise HTTPException(status_code=404, detail="Item not found in collection")
    return {"key": key, "value": value}


@app.get("/collections")
def list_all_collections():
    return {"collections": list(cache_collections.keys())}
