from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
from auth_routes import auth_router
from order_routes import order_routes
app.include_router(auth_router)
app.include_router(order_routes)


@app.get("/")
def first_api():
    return  "OLA"