from fastapi import FastAPI
from . import model
from .database import engine, get_db
from .routers import users, words, auth

# model.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(words.router)
app.include_router(users.router)
app.include_router(auth.router)