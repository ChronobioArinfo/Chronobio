from dataclasses import dataclass
from typing import List
from .employee import Employee
from .field import Field
from .my_type import Location


@dataclass
class Farm:
    _fields: List[Field]
    _employee: List[Employee]

    def __init__(self) -> None:
        self._fields = []
        self._employee = []

    def add_field(self) -> None:
        location: Location = Location(len(self._fields) + 1)
        self._fields.append(Field(location))
        print(self._fields)
    
    def add_employee(self) -> None:
        self._employee.append(Employee())
