from pydantic import BaseModel
from typing import Optional

from player.json_class.tractor_json import TractorJSON


class EmployeeJSON(BaseModel):
    id: int
    location: str
    salary: int
    tractor: Optional[TractorJSON]
