# from random import choice
from typing import List, Dict, Any

# from player.player_logic.employee import Employee


def get_my_farm(game_data: object, username: str) -> Dict[str, Any]:
    for farm in game_data["farms"]:
        if farm["name"] == username:
            my_farm = farm
            break
    else:
        raise ValueError(f"My farm is not found ({username})")
    return my_farm


# def buy_employee(my_farm: Dict[str, Any]) -> List[str]:
#     count: int = 0
#     command: List[str] = []

#     for staff in Employee.employees:
#         if not staff.busy_for:
#             count += 1
#     for i in range(count):
#         command += ["0 EMPLOYER"]
#         Employee.employees.append(Employee())
#     return command


def get_owner_command(my_farm: Dict[str, Any]) -> List[str]:
    commands: List[str] = []
    if not hasattr(get_owner_command, "is_busy"):
        get_owner_command.is_busy = False
    if not get_owner_command.is_busy:
        # commands += buy_employee(my_farm)
        ...
    else:
        get_owner_command.is_busy = False
    return commands


def total_number_vegetable(game_data: object) -> Dict[str, int]:
    total_vegetable: Dict[str, int] = {
        "POTATO": 0, "LEEK": 0, "TOMATO": 0, "ONION": 0, "ZUCCHINI": 0
        }
    for farm in game_data["farms"]:
        for field in farm["fields"]:
            if not field["content"] == "NONE":
                total_vegetable[field["content"]] += 1
    return total_vegetable


# def get_staff_command(staff: Employee, my_farm: Dict[str, Any]) -> List[str]:
#     command: List[str] = []
#     vegetable = choice(["PATATE", "POIREAU", "TOMATE", "OIGNON", "COURGETTE"])
#     for field in my_farm["fields"]:
#         if field["bought"] and field["content"] == "NONE":
#             return [f"{Employee.id} SEMER {vegetable} {field['location']}"]
#         if field["bought"] and field["needed_water"]:
#             return [f"{Employee.id} AROSER {field['location']}"]
#     return command


def get_next_actions(game_data: object, username: str) -> List[str]:
    my_farm: Dict[str, Any] = get_my_farm(game_data, username)
    commands: List[str] = []
    day: int = game_data["day"]

    if (day == 0):
        commands = [
            "0 ACHETER_CHAMP",
            "0 EMPLOYER",
            "0 EMPLOYER",
            "0 EMPLOYER",
            "0 EMPLOYER",
            "0 EMPLOYER",
            "0 EMPLOYER",
            "0 EMPLOYER",
            "0 EMPLOYER",
            "0 EMPLOYER",
            "0 EMPLOYER"
            ]
    if (day % 2):
        commands += [
            "1 ARROSER 1",
            "2 ARROSER 1",
            "3 ARROSER 1",
            "4 ARROSER 1",
            "5 ARROSER 1",
            "6 ARROSER 1",
            "7 ARROSER 1",
            "8 ARROSER 1",
            "9 ARROSER 1",
            "10 ARROSER 1",
            "0 VENDRE 1"
        ]
    else:
        commands += ["1 SEMER PATATE 1"]

    if (day % 30 and day != 0):
        ...

    # commands = get_owner_command(my_farm)
    # for staff in Employee.employees:
    #     if not staff.busy_for:
    #         commands += get_staff_command(staff, my_farm)

    return commands
