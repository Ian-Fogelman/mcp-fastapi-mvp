# FastAPI concept: the app instance.
# Routes are registered in routes.py, not here.
# This file exists so routes.py and main.py can both import the same app object.

from fastapi import FastAPI

app = FastAPI(title="Inventory REST API")
