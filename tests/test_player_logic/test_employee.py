import pytest
from player.player_logic.employee import Employee
from player.player_logic.field import Field
from player.player_logic.my_type import Location


def test_planting():
    field: Field = Field(Location.FIELD1)
    employee: Employee = Employee(1)

    employee.work(field)
    assert field.content == field.vegetable_wanted


def test_planting_long():
    field: Field = Field(Location.FIELD5)
    employee: Employee = Employee(1)

    employee.work(field)
    assert employee.busy_for == 5

@pytest.mark.parametrize(
    "number, expected", [
        (2, 8),
        (5, 5),
        (10, 0)
    ]
)
def test_watering(number, expected):
    field: Field = Field(Location.FIELD1)
    employee: Employee = Employee(1)

    employee.work(field)
    for _ in range(number):
        employee.work(field)
    assert field._water_needed == expected
