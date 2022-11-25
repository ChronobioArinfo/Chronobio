from dataclasses import dataclass
from typing import Dict, List, Optional

from player.json_class.farm_json import FarmJSON
from player.json_class.soupfactory_json import SoupfactoryJSON
from .employee import Employee
from .field import Field
from .my_type import Location, Vegetable


@dataclass
class Farm:
    fields: List[Field]
    employees: Dict[int, Employee]
    _next_id_employee: int = 0

    def __init__(self) -> None:
        self.fields = []
        self.employees = {}
        self.data: FarmJSON = FarmJSON(
            blocked=False,
            employees=[],
            fields=[],
            loans=[],
            money=100000,
            name="",
            score=0,
            soup_factory=SoupfactoryJSON(days_off=0, stock={}),
            tractors=[],
            events=[]
        )

    def add_field(self) -> str:
        location: Location = Location(len(self.fields) + 1)
        self.fields.append(Field(location))
        return "0 ACHETER_CHAMP"

    def add_employee(self) -> str:
        self._next_id_employee += 1
        id = self._next_id_employee
        self.employees[id] = Employee(id)
        return "0 EMPLOYER"

    def dismss_employee(self, employee: Employee) -> str:
        self.employees.pop(employee.id)
        return f"0 LICENCIER {employee.id}"

    def get_employee_by_id(self, id: int) -> Employee:
        if id in self.employees.keys():
            return self.employees[id]
        raise IndexError("employee not found")

    def get_employee_not_busy(self) -> Optional[Employee]:
        for employee in self.employees.values():
            if employee.busy_for == 0:
                return employee
        return None

    def get_farm_work_needed(self) -> Optional[Field]:
        for field in self.fields:
            if field.content == Vegetable.NONE or field.water_needed > 0:
                return field
        return None

    def get_field_by_location(self, location: Location) -> Optional[Field]:
        for field in self.fields:
            if field.location == location:
                return field
        return None

    def sellable_field(self) -> Optional[Field]:
        for field in self.fields:
            if field.content != Vegetable.NONE and field.is_sellable:
                return field
        return None

    def __setattr__(self, name: str, value: FarmJSON) -> None:
        if name == "data":
            for field in value.fields:
                loc: Location = getattr(Location, field.location)
                my_field: Optional[Field] = self.get_field_by_location(loc)
                if my_field is not None:
                    my_field.data = field
            for employee in value.employees:
                self.get_employee_by_id(employee.id).data = employee
        else:
            super().__setattr__(name, value)
