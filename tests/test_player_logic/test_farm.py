import pytest
from player.player_logic.employee import Employee
from player.player_logic.farm import Farm
from player.player_logic.field import Field
from player.player_logic.my_type import Location, Vegetable


@pytest.mark.parametrize(
    "number, expected", [
        (2, 2),
        (5, 5)
    ]
)
def test_add_field(number, expected):
    farm: Farm = Farm()

    for _ in range(number):
        farm.add_field()
    assert len(farm.fields) == expected


@pytest.mark.parametrize(
    "number, id, expected", [
        (2, 1, 1),
        (5, 2, 2)
    ]
)
def test_add_employee(number, id, expected):
    farm: Farm = Farm()

    for _ in range(number):
        farm.add_employee()
    assert farm.get_employee_by_id(id).id == expected

def test_employee_index_arror():
    farm: Farm = Farm()
    with pytest.raises(IndexError):
        farm.get_employee_by_id(2)

def test_get_employee_busy():
    field: Field = Field(Location.FIELD5)
    farm: Farm = Farm()

    farm.add_employee()
    farm.get_employee_by_id(1).work(field)
    assert farm.get_employee_not_busy() is None


def test_get_employee_not_busy():
    farm: Farm = Farm()

    farm.add_employee()
    assert farm.get_employee_not_busy() is not None


def test_get_farm_work_not_needed():
    farm: Farm = Farm()

    assert farm.get_farm_work_needed() is None


def test_get_farm_work_needed():
    farm: Farm = Farm()

    farm.add_field()
    farm.add_field()
    farm.fields[0].content = Vegetable.PATATE
    assert farm.get_farm_work_needed() is not None
