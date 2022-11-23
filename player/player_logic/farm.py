from dataclasses import dataclass
from typing import List, Optional
from .employee import Employee
from .field import Field
from .my_type import Location, Vegetable


@dataclass
class Farm:
    _fields: List[Field]
    _employees: List[Employee]

    def __init__(self) -> None:
        self._fields = []
        self._employees = []

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
        self._employees.append(Employee())
        return "0 EMPLOYER"

    def get_employee_by_id(self, id: int) -> Employee:
        for employee in self._employees:
            if employee.id == id:
                return employee
        raise IndexError("employee not found")

    def get_employee_not_busy(self) -> Optional[Employee]:
        for employee in self._employees:
            if employee._busy_for == 0:
                return employee

    def get_farm_work_needed(self) -> Optional[Field]:
        for field in self._fields:
            if field.content == Vegetable.NONE or field.water_needed > 0:
                return field

    def read_data(self, data: object) -> None:
        for field in data["fields"]:
            if field["bought"]:
                ...
        for employee in data["employees"]:
            self.get_employee_by_id(employee["id"]).read_data(employee)
