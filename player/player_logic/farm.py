from dataclasses import dataclass
from typing import Any, Dict, List, Optional
from .employee import Employee
from .field import Field
from .my_type import Location, Vegetable


@dataclass
class Farm:
    _fields: List[Field]
    _employees: Dict[int, Employee]
    _next_id_employee: int = 0

    def __init__(self) -> None:
        self._fields = []
        self._employees = {}

    @property
    def fields(self):
        return self._fields

    @property
    def employees(self):
        return self._employees

    def add_field(self) -> str:
        location: Location = Location(len(self._fields) + 1)
        self._fields.append(Field(location))
        return "0 ACHETER_CHAMP"

    def add_employee(self) -> str:
        self._next_id_employee += 1
        id = self._next_id_employee
        self._employees[id] = Employee(id)
        return "0 EMPLOYER"

    def get_employee_by_id(self, id: int) -> Employee:
        if id in self._employees.keys():
            return self._employees[id]
        raise IndexError("employee not found")

    def get_employee_not_busy(self) -> Optional[Employee]:
        for employee in self._employees.values():
            if employee._busy_for == 0:
                return employee

    def get_farm_work_needed(self) -> Optional[Field]:
        for field in self._fields:
            if field.content == Vegetable.NONE or field._water_needed > 0:
                return field

    def get_field_by_location(self, location: Location) ->Optional[Field]:
        for field in self._fields:
            if field.location == location:
                return field

    def read_data(self, data: Dict[str, Any]) -> None:
        for field in data["fields"]:
            location: Location = getattr(Location, field["location"])
            my_field: Optional[Field] = self.get_field_by_location(location)
            if my_field is not None:
                my_field.read_data(field)
        for employee in data["employees"]:
            self.get_employee_by_id(employee["id"]).read_data(employee)
