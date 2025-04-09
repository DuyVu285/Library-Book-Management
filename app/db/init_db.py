from app.db.session import engine
from app.models.book_model import SQLModel


def init_db():
    SQLModel.metadata.create_all(engine)
