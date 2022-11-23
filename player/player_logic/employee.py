from dataclasses import dataclass
from typing import ClassVar

from player.player_logic.my_type import Vegetable

from .field import Field


@dataclass
class Employee:
    id_actual: ClassVar[int] = 0
    _id: int
    _busy_for: int = 0
    _salary: int = 1000

    def __init__(self) -> None:
        Employee.id_actual += 1
        self._id = Employee.id_actual

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
        if field.content == Vegetable.NONE:
            return self.planting(field)
        else:
            return self.watering(field)

    def planting(self, field: Field) -> str:
        self.busy_for = 1
        field.planting()
        return f"{self._id} SEMER {field.content.name} {field.location}"

    def watering(self, field: Field) -> str:
        self.busy_for = 1
        field.watering()
        return f"{self._id} ARROSER {field.location}"

    def read_data(self, data: object) -> None:
        ...
