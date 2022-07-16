from datetime import datetime
from pydantic import BaseModel
from typing import Optional

class WordBase(BaseModel):
    kazakh: str
    russian: str


class WordCreate(WordBase):
    pass


class WordResponse(WordBase):
    id: int
    who_added: int
    class Config:
        orm_mode = True


class UserBase(BaseModel):
    identification: str
    username: str


class UserCreate(UserBase):
    pass


class UserResponse(BaseModel):
    username: str
    created_at: datetime
    class Config:
        orm_mode = True


class UserLogin(BaseModel):
    identification: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str] = None