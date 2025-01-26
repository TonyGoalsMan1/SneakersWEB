from pydantic import BaseModel
from typing import Optional


class UserCreate(BaseModel):
    username: str
    password: str


class SneakerCreate(BaseModel):
    name: str
    size: float
    price: float
    description: Optional[str]
    owner_id: Optional[int]


class Token(BaseModel):
    access_token: str
    token_type: str
