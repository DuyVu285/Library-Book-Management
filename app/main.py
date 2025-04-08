from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.api.routes import books
from app.db.init_db import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    print("Database initialized!")
    yield
    print("Shutting down...")


app = FastAPI(lifespan=lifespan)

app.include_router(books.router)


@app.get("/")
def root():
    return {"message": "Library API is ready"}
