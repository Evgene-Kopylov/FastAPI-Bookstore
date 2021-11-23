from datetime import date
from typing import Any, Optional
from typing import List
from pydantic import BaseModel


class BookBase(BaseModel):
    title: str
    annotation: Optional[str]
    isbn: Optional[str]
    publish_at: Optional[date]
    total_sells: Optional[int]
    total_views: Optional[int]
    authors: Optional[List]
    publisher_id: Optional[int]


class LBs_BookSchema(BaseModel):
    id: int
    title: str
    annotation: Optional[str]
    publish_at: Optional[date]
    total_sells: int = 0
    total_views: int = 0


class ListBooks(BaseModel):
    items: List[LBs_BookSchema]
    total: int
    page: int
    size: int


class PATCH_Book(BaseModel):
    title: Optional[str]
    annotation: Optional[str]
    isbn: Optional[str]
    publish_at: Optional[date]
    total_sells: Optional[int]
    total_views: Optional[int]
    authors: Optional[List[int]]
    publisher_id: Optional[int]


class GB_Authors(BaseModel):
    id: int
    first_name: str
    last_name: Optional[str]
    middle_name: Optional[str]


class GB_Publisher(BaseModel):
    id: int
    name: str


class GetBook(BaseModel):
    id: int
    title: Optional[str]
    annotation: Optional[str]
    isbn: Optional[str]
    publish_at: Optional[date]
    total_sells: Optional[int]
    total_views: Optional[int]
    # authors: Optional[List[GB_Authors]]
    # publisher: Optional[GB_Publisher]
