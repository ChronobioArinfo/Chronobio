from typing import List, Optional
from player.player_logic.my_type import Vegetable
from .employee import Employee
from .field import Field
from .state import State


# def total_number_vegetable(game_data: object) -> Dict[str, int]:
#     total_vegetable: Dict[str, int] = {
#         "POTATO": 0, "LEEK": 0, "TOMATO": 0, "ONION": 0, "ZUCCHINI": 0
#         }
#     for farm in game_data["farms"]:
#         for field in farm["fields"]:
#             if not field["content"] == "NONE":
#                 total_vegetable[field["content"]] += 1
#     return total_vegetable


# # def get_staff_command(staff: Employee, my_farm: Dict[str, Any]) -> List[str]:
# #     command: List[str] = []
# #     vegetable = choice(["PATATE", "POIREAU", "TOMATE", "OIGNON", "COURGETTE"])
# #     for field in my_farm["fields"]:
# #         if field["bought"] and field["content"] == "NONE":
# #             return [f"{Employee.id} SEMER {vegetable} {field['location']}"]
# #         if field["bought"] and field["needed_water"]:
# #             return [f"{Employee.id} AROSER {field['location']}"]
# #     return command


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
    ]
    return commands


def init_day(state: State) -> None:
    for employee in state.my_farm.employees:
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


def get_next_actions(state: State) -> List[str]:
    commands: List[str] = []

    init_day(state)
    if state._day == 0:
        commands += day_0(state)
    commands += give_job_employee(state)
    commands.append(state.sell())
    return commands
