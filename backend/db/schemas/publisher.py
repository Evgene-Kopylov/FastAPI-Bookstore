from datetime import date
from typing import Optional
from typing import List
from pydantic import BaseModel


class PublisherBase(BaseModel):
    name: str
    description: Optional[str]