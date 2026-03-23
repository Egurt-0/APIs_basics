from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
from auth_routes import auth_router
from order_routes import order_routes
app.include_router(auth_router)
app.include_router(order_routes)
from passlib.context import CryptContext
from dotenv import load_dotenv
import os
from os import getenv

load_dotenv()
SECRET_KEY = os.getenv()