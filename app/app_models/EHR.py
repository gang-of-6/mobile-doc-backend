from pydantic import BaseModel
from typing import Optional


class Medicine(BaseModel):
    name: str
    generic_name: str
    precautions: Optional[list[str]]
