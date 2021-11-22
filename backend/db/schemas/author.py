from datetime import date
from typing import Optional
from typing import List
from pydantic import BaseModel


class AuthorBase(BaseModel):
    first_name: str
    last_name: Optional[str]
    middle_name: Optional[str]