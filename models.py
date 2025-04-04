from sqlmodel import Field, SQLModel
import uuid
from datetime import datetime, date


class User(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    username: str = Field(unique=True, index=True, nullable=False)
    email: str = Field(unique=True, index=True, nullable=False)
    hashed_password: str = Field(nullable=False)
    is_admin: bool = Field(nullable=False)


class Book(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    title: str = Field(nullable=False)
    author: str = Field(nullable=False)
    published_date: date = Field(nullable=False)
    available: bool = Field(default=True)

