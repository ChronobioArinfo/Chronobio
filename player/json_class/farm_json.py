from pydantic import BaseModel
from typing import Any, List
from .employee_json import EmployeeJSON
from .field_json import FieldJSON
from .loan_json import LoanJSON
from .soupfactory_json import SoupfactoryJSON
from .tractor_json import TractorJSON


class FarmJSON(BaseModel):
    blocked: bool
    employees: List[EmployeeJSON]
    fields: List[FieldJSON]
    loans: List[LoanJSON]
    money: int
    name: str
    score: int
    soup_factory: SoupfactoryJSON
    tractors: List[TractorJSON]
    events: List[Any]
