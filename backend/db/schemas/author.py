from datetime import date
from typing import Optional
from typing import List
from pydantic import BaseModel


class AuthorBase(BaseModel):
    first_name: str
    last_name: Optional[str]
    middle_name: Optional[str]


class LA_Book(BaseModel):
    id: int
    title: str
    annotation: Optional[str]
    publish_at: Optional[date]
    total_sells: Optional[int] = 0
    total_views: Optional[int] = 0


class GetAuthor(BaseModel):
    id: int
    first_name: str
    last_name: Optional[str]
    middle_name: Optional[str]
    books_total: Optional[int] = 0
    new_books: Optional[List[LA_Book]]
    hot_books: Optional[List[LA_Book]]




