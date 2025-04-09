from sqlmodel import SQLModel, Field
from uuid import UUID, uuid4


class User(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True, index=True)
    username: str = Field(nullable=False, unique=True)
    email: str = Field(nullable=False, unique=True)
    hashed_password: str = Field(nullable=False)
    is_active: bool = Field(default=True)
