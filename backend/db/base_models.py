from typing import List, Optional
from pydantic import BaseModel,EmailStr


class BookBase(BaseModel):
    title: str
    authors: Optional[List] = []


class AuthorBase(BaseModel):
    first_name: str
    last_name: str
    middle_name: str

