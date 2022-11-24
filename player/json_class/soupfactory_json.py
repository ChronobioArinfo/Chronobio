from typing import Dict
from pydantic import BaseModel


class SoupfactoryJSON(BaseModel):
    days_off: int
    stock: Dict[str, int]
