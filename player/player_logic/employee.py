from dataclasses import dataclass
from typing import ClassVar


@dataclass
class employee:
    id_actual: ClassVar[int] = 0
    _id: int
    _busy_for: int = 0
    _tractor_id: int = 0

    def __init__(self) -> None:
        self._id = employee.id_actual
        employee.id_actual += 1

    @property
    def id(self):
        return self._id

    @property
    def busy_for(self):
        return self.busy_for

    @busy_for.setter
    def busy_for(self, days: int):
        self.busy_for = days

    @property
    def tractor_id(self):
        return self._tractor_id

    @tractor_id.setter
    def tractor_id(self, id: int):
        self.tractor_id = id
