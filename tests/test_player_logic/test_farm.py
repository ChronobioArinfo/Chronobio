import pytest
from player.player_logic.farm import Farm


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
    assert len(farm._fields) == expected


@pytest.mark.parametrize(
    "number, expected", [
        (2, 2),
        (5, 5)
    ]
)
def test_add_employee(number, expected):
    farm: Farm = Farm()

    for _ in range(number):
        farm.add_employee()
    assert len(farm._employee) == expected
