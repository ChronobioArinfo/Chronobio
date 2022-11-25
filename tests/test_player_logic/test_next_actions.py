from json import load as json_load
import pytest
from pathlib import Path
from random import seed
from typing import List, Optional

from player.player_logic.employee import Employee
from player.player_logic.field import Field
from player.player_logic.my_type import Vegetable
from player.player_logic.next_actions import day_0, init_day, \
    give_job_employee, get_next_actions
from player.player_logic.state import State
from player.json_class.state_json import StateJSON


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
        "0 EMPLOYER",
    ]


@pytest.mark.parametrize("busy_for, expected", [(1, 0), (0, 0), (2, 1)])
def test_init_day(busy_for, expected):
    state: State = State("test")
    employee: Optional[Employee]

    state.my_farm.add_employee()
    employee = state.my_farm.get_employee_not_busy()
    if employee:
        employee.busy_for = busy_for
        init_day(state)
        assert employee.busy_for == expected


@pytest.mark.parametrize("day, expected", [(1, 2), (2, 1), (3, 0)])
def test_init_day_sell(day, expected):
    state: State = State("test")

    state.my_farm.add_field()
    state.my_farm.fields[0].content = Vegetable.PATATE
    state.my_farm.fields[0].is_sellable = True
    state.sell()
    for _ in range(day):
        init_day(state)
    assert state.is_busy == expected


def test_give_job_employee():
    state: State = State("test")
    field: Optional[Field]
    state.my_farm.add_employee()
    state.my_farm.add_field()
    field = state.my_farm.get_farm_work_needed()

    commands = give_job_employee(state)
    if field is not None:
        assert commands == [f"1 SEMER {field.content.name} 1"]


def test_give_job_employee_no_field():
    state: State = State("test")
    field: Optional[Field]
    state.my_farm.add_employee()
    field = state.my_farm.get_farm_work_needed()

    commands = give_job_employee(state)
    if field is None:
        assert commands == []


@pytest.fixture
def load_my_json() -> State:
    seed(0)
    jsonfile = Path('./tests/day0.json')
    with open(jsonfile) as file:
        data = json_load(file)

    state: State = State("AgricultorSimulator")
    stateJSON: StateJSON = StateJSON(**data)
    state.data = stateJSON
    return state


def test_next_actions_day0(load_my_json):
    state: State = load_my_json
    commands: List[str] = get_next_actions(state)
    assert len(commands) == 17


def test_next_actions():
    state: State = State("AgricultorSimulator")
    state.day = 1
    state.my_farm.add_field()
    state.my_farm.fields[0].content = Vegetable.PATATE
    state.my_farm.fields[0].is_sellable = True
    commands: List[str] = get_next_actions(state)
    assert commands == ["0 VENDRE 1"]


def test_next_actions_renew_employee():
    state: State = State("AgricultorSimulator")
    state.day = 1
    state.my_farm.add_employee()
    state.my_farm.employees[1]._salary = 1200
    commands: List[str] = get_next_actions(state)
    assert commands == ["0 LICENCIER 1", "0 EMPLOYER"]


def test_next_actions_manager_busy():
    state: State = State("AgricultorSimulator")
    state.day = 1
    state.my_farm.add_employee()
    state.is_busy = 2
    state.my_farm.employees[1]._salary = 1200
    commands: List[str] = get_next_actions(state)
    assert commands == []
