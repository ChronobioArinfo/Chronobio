from pydantic import BaseModel
from typing import Any, List
from .farm_json import FarmJSON


class StateJSON(BaseModel):
    day: int
    events: List[Any]
    farms: List[FarmJSON]
