from pydantic import BaseModel
from typing import List
from .farm_json import FarmJSON


class StateJSON(BaseModel):
    day: int
    farms: List[FarmJSON]
