import pytest
from player.player_logic.my_type import Location, Vegetable
from player.player_logic.field import Field


@pytest.mark.parametrize(
    "vegetable, expected", [
        (Vegetable.PATATE, (Vegetable.PATATE, 10)),
        (Vegetable.POIREAU, (Vegetable.POIREAU, 10)),
        (Vegetable.NONE, (Vegetable.PATATE, 10))
    ]
)
def test_planting(vegetable, expected):
    field: Field = Field(Location.FIELD1)
    if vegetable == Vegetable.NONE:
        field.vegetable_wanted = Vegetable.PATATE
    field.planting(vegetable)
    assert (field.vegetable_wanted, field._water_needed) == expected


@pytest.mark.parametrize(
    "time, expected", [
        (1, 9),
        (5, 5),
        (10, 0),
        (20, 0)
    ]
)
def test_watering(time, expected):
    field: Field = Field(Location.FIELD1)
    field.planting(Vegetable.PATATE)
    for _ in range(time):
        field.watering()
    assert field._water_needed == expected


def test_gathering():
    field: Field = Field(Location.FIELD1)
    field.planting(Vegetable.PATATE)
    field.gathering()
    assert field.content == Vegetable.NONE
