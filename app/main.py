from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.api.routes import book_route as book
from app.db.init_db import init_db
from app.core.config import get_settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    print("Database initialized!")
    yield
    print("Shutting down...")


app = FastAPI(lifespan=lifespan)

app.include_router(book.router)


@app.get("/")
def root():

    settings = get_settings()
    print(settings.SECRET_KEY)
    print(settings.DATABASE_URL)

    return {"message": "Library API is ready"}
