from typing import Optional
from typing import List
from pydantic import BaseModel,EmailStr


class Book(BaseModel):
    title: str
    authors: Optional[List] = []
    publisher_id: Optional[int]


class Author(BaseModel):
    first_name: str
    last_name: Optional[str]
    middle_name: Optional[str]

class Publisher(BaseModel):
    name: str
    description: Optional[str]
