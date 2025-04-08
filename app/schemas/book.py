from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID


class BookBase(BaseModel):
    title: str
    author: str
    published_year: Optional[int]
    isbn: str


class BookCreate(BookBase):
    pass


class BookRead(BookBase):
    id: UUID
    is_available: bool
