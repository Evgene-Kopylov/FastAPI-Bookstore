from datetime import date
from typing import Optional
from typing import List
from pydantic import BaseModel


class AuthorBase(BaseModel):
    first_name: str
    last_name: Optional[str]
    middle_name: Optional[str]


class GA_Book(BaseModel):
    id: int
    title: str
    annotation: Optional[str]
    publish_at: Optional[date]
    total_sells: Optional[int]
    total_views: Optional[int]


class GetAuthor(BaseModel):
    id: int
    first_name: str
    last_name: Optional[str]
    middle_name: Optional[str]
    books_total: Optional[int]
    new_books: Optional[List[GA_Book]]
    hot_books: Optional[List[GA_Book]]


class LA_Author(BaseModel):
    id: int
    first_name: str
    last_name: Optional[str]
    middle_name: Optional[str]
    books_total: int
    

class ListAuthor(BaseModel):
    items: List[LA_Author]
    total: int
    page: int
    size: int

