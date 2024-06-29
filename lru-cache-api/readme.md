# FastAPI LRU Cache Service

This project is an in-memory LRU (Least Recently Used) cache service built using FastAPI. It allows applications to create and manage multiple cache collections via REST APIs.

## Features

- Create a cache collection with a specified capacity.
- Update the capacity of an existing cache collection.
- Add key-value pairs to a cache collection.
- Retrieve values from a cache collection.
- List all cache collections.

## Installation

### Prerequisites

- Python 3.7+
- pip (Python package installer)

### Steps

1. **Clone the repository**:

    ```bash
    git clone https://github.com/yourusername/fastapi-lru-cache.git
    cd fastapi-lru-cache
    ```

2. **Create and activate a virtual environment**:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the application**:

    ```bash
    uvicorn main:app --reload
    ```

2. **Access the API documentation**:

    - Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
    - ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## API Endpoints

- **Create a cache collection**: `POST /collections/{collection_name}`
    - Parameters: `collection_name` (path), `capacity` (query)
- **Update the capacity of a collection**: `PUT /collections/{collection_name}`
    - Parameters: `collection_name` (path), `capacity` (query)
- **Add an item to a collection**: `POST /collections/{collection_name}/items`
    - Parameters: `collection_name` (path), `key` (query), `value` (query)
- **Get an item from a collection**: `GET /collections/{collection_name}/items/{key}`
    - Parameters: `collection_name` (path), `key` (path)
- **List all collections**: `GET /collections`

## Project Structure

