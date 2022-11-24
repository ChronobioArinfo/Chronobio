import pytest
from typing import Optional
from player.player_logic.employee import Employee
from player.player_logic.field import Field
from player.player_logic.next_actions import day_0, init_day, give_job_employee
from player.player_logic.state import State
from player.player_logic.my_type import Vegetable


def test_day_0():
    state: State = State("test")
    commands = day_0(state)
    assert commands == [
        "0 ACHETER_CHAMP",
        "0 ACHETER_CHAMP",
        "0 ACHETER_CHAMP",
        "0 ACHETER_CHAMP",
        "0 ACHETER_CHAMP",
        "0 EMPLOYER",
        "0 EMPLOYER",
        "0 EMPLOYER",
        "0 EMPLOYER",
        "0 EMPLOYER",
    ]


@pytest.mark.parametrize("busy_for, expected", [(1, 0), (0, 0), (2, 1)])
def test_init_day(busy_for, expected):
    state: State = State("test")
    employee: Optional[Employee]

    state._my_farm.add_employee()
    employee = state._my_farm.get_employee_not_busy()
    if employee:
        employee.busy_for = busy_for
        init_day(state)
        assert employee.busy_for == expected


def test_manager_sell():
    state: State = State("test")

    state._my_farm.add_field()
    state._my_farm.add_field()
    state._my_farm.fields[1].content = Vegetable.PATATE
    state._my_farm.fields[1]._is_sellable = True
    state.sell()
    assert state._is_busy == 3


@pytest.mark.parametrize("day, expected", [(1, 2), (2, 1), (3, 0)])
def test_init_day_sell(day, expected):
    state: State = State("test")

    state._my_farm.add_field()
    state._my_farm.fields[0].content = Vegetable.PATATE
    state._my_farm.fields[0]._is_sellable = True
    state.sell()
    for _ in range(day):
        init_day(state)
    assert state._is_busy == expected


def test_give_job_employee():
    state: State = State("test")
    field: Optional[Field]
    state._my_farm.add_employee()
    state._my_farm.add_field()
    field = state._my_farm.get_farm_work_needed()

    commands = give_job_employee(state)
    if field is not None:
        assert commands == [f"1 SEMER {field.content.name} 1"]


def test_give_job_employee_no_field():
    state: State = State("test")
    field: Optional[Field]
    state._my_farm.add_employee()
    field = state._my_farm.get_farm_work_needed()

    commands = give_job_employee(state)
    if field is None:
        assert commands == []
