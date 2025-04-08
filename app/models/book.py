from sqlmodel import SQLModel, Field
from uuid import UUID, uuid4

class Book(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True, index=True)
    title: str = Field(nullable=False)
    author: str = Field(nullable=False)
    published_year: int = Field(nullable=False)
    isbn: str = Field(nullable=False)
    is_available: bool = Field(default=True)
