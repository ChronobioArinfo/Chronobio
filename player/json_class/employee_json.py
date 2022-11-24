from pydantic import BaseModel
from typing import Optional


class EmployeeJSON(BaseModel):
    id: int
    location: str
    salary: int
    tractor: Optional[int]
