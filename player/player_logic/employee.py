from dataclasses import dataclass

from player.json_class.employee_json import EmployeeJSON
from .my_type import Location, Vegetable
from .field import Field


@dataclass
class Employee:
    id: int
    location: Location = Location.FARM
    _busy_for: int = 0
    _salary: int = 1000

    def __init__(self, id: int) -> None:
        self.id = id
        self.data = EmployeeJSON(
            id=id,
            location="FARM",
            salary=1000,
            tractor=None
        )

    @property
    def busy_for(self) -> int:
        return self._busy_for

    @busy_for.setter
    def busy_for(self, days: int) -> None:
        self._busy_for = days
        if self._busy_for < 0:
            self._busy_for = 0

    def is_too_costly(self) -> bool:
        return self._salary > 1130

    def work(self, field: Field) -> str:
        distance: int = abs(field.location.value - self.location.value)
        self.busy_for = max(distance, 1)
        if field.content == Vegetable.NONE:
            return self.planting(field)
        else:
            return self.watering(field)

    def planting(self, field: Field) -> str:
        field.planting()
        return f"{self.id} SEMER {field.content.name} {field.location.value}"

    def watering(self, field: Field) -> str:
        field.watering()
        return f"{self.id} ARROSER {field.location.value}"

    def __setattr__(self, name: str, value: EmployeeJSON) -> None:
        if name == "data":
            self.location = getattr(Location, value.location)
            self._salary = value.salary
        else:
            super().__setattr__(name, value)
