from typing import Optional
from pydantic import BaseModel,EmailStr


class BookSchema(BaseModel):
    title: str
