from datetime import date
from os import name
from typing import Optional
from typing import List
from pydantic import BaseModel


class PublisherBase(BaseModel):
    name: str
    description: Optional[str]


class GP_Book(BaseModel):
    id: int
    title: str
    annotation: Optional[str]
    publish_at: Optional[date]
    total_sells: Optional[int]
    total_views: Optional[int]


class GetPublisher(BaseModel):
    id: int
    name: str
    description: str
    books_total: int
    new_books: List[GP_Book]
    hot_books: List[GP_Book]


class LP_Publisher(BaseModel):
    id: int
    name: str
    books_total: Optional[int]


class ListPublisher(BaseModel):
    items: List[LP_Publisher]
    total: int
    page: int
    size: int


class PATCH_Publisher(BaseModel):
    name: Optional[str]
    description: Optional[str]

