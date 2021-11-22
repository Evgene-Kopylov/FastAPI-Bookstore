from datetime import date
from typing import Optional
from typing import List
from pydantic import BaseModel,EmailStr


class Book(BaseModel):
    title: str
    annotation: Optional[str]
    isbn: Optional[str]
    publish_at: Optional[date]
    total_sells: Optional[int]
    total_views: Optional[int]
    authors: Optional[List] = []
    publisher_id: Optional[int]


class Author(BaseModel):
    first_name: str
    last_name: Optional[str]
    middle_name: Optional[str]

class Publisher(BaseModel):
    name: str
    description: Optional[str]
