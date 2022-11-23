from dataclasses import dataclass
from typing import Any, Dict

from .my_type import Location, Vegetable
from .field import Field


@dataclass
class Employee:
    _id: int
    location: Location = Location.FARM
    _busy_for: int = 0
    _salary: int = 1000

    def __init__(self, id: int) -> None:
        self._id = id

    @property
    def id(self):
        return self._id

    @property
    def busy_for(self):
        return self._busy_for

    @busy_for.setter
    def busy_for(self, days: int):
        self._busy_for = days
        if self._busy_for < 0:
            self._busy_for = 0

    def work(self, field: Field) -> str:
        distance: int = abs(field.location.value - self.location.value)
        self.busy_for = max(distance, 1)
        if field.content == Vegetable.NONE:
            return self.planting(field)
        else:
            return self.watering(field)

    def planting(self, field: Field) -> str:
        field.planting()
        return f"{self._id} SEMER {field.content.name} {field.location.value}"

    def watering(self, field: Field) -> str:
        field.watering()
        return f"{self._id} ARROSER {field.location.value}"

    def read_data(self, data: Dict[str, Any]) -> None:
        self.location = getattr(Location, data["location"])
        self._salary = data["salary"]
