from pydantic import BaseModel, EmailStr
from uuid import UUID


class UserBase(BaseModel):
    username: str
    email: EmailStr


class UserCreate(UserBase):
    password: str


class UserRead(UserBase):
    id: UUID
    is_active: bool


class UserLogin(BaseModel):
    username: str
    password: str
