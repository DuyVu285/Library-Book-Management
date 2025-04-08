from pydantic import BaseModel, EmailStr
import uuid
from datetime import datetime, date


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: uuid.UUID
    username: str
    email: EmailStr
    is_admin: bool


class BookCreate(BaseModel):
    title: str
    author: str
    publised_date: datetime


class BookResponse(BaseModel):
    id: uuid.UUID
    available: bool


class BorrowRequest(BaseModel):
    book_id: uuid.UUID


class BorrowResponse(BaseModel):
    id: uuid.UUID
    user_id: uuid.UUID
    book_id: uuid.UUID
    borrowed_date: datetime
    returned_date: datetime | None


class token(BaseModel):
    access_token: str
    token_type: str
