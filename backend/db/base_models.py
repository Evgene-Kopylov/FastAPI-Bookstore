from typing import Optional
from pydantic import BaseModel,EmailStr


class BookBase(BaseModel):
    title: str
