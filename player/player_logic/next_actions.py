from typing import Dict, List, Optional
from .employee import Employee
from .field import Field
from .state import State


def day_0(state: State) -> List[str]:
    commands = [
        state.my_farm.add_field(),
        state.my_farm.add_field(),
        state.my_farm.add_field(),
        state.my_farm.add_field(),
        state.my_farm.add_field(),
        state.my_farm.add_employee(),
        state.my_farm.add_employee(),
        state.my_farm.add_employee(),
        state.my_farm.add_employee(),
        state.my_farm.add_employee(),
        state.my_farm.add_employee(),
    ]
    return commands


def init_day(state: State) -> None:
    for employee in state.my_farm.employees.values():
        employee.busy_for -= 1
    state.is_busy -= 1


def give_job_employee(state: State) -> List[str]:
    commands: List[str] = []
    employee: Optional[Employee]
    field: Optional[Field]

    employee = state.my_farm.get_employee_not_busy()
    while employee is not None:
        field = state.my_farm.get_farm_work_needed()
        if field is None:
            return commands
        commands.append(employee.work(field))
        employee = state.my_farm.get_employee_not_busy()

    return commands


def renew_employee(state: State) -> List[str]:
    commands: List[str] = []
    if state.is_busy != 0:
        return commands
    for employee in list(state.my_farm.employees.values()):
        if employee.is_too_costly():
            commands.append(state.my_farm.dismss_employee(employee))
            commands.append(state.my_farm.add_employee())
    commands += give_job_employee(state)
    return commands


def get_next_actions(state: State) -> List[str]:
    commands: List[str] = []
    can_sell: Optional[str]

    init_day(state)
    if state.day == 0:
        commands += day_0(state)
    commands += give_job_employee(state)
    commands += renew_employee(state)
    can_sell = state.sell()
    if can_sell is not None:
        commands.append(can_sell)
    return commands
