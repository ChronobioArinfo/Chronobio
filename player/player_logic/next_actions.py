from typing import List, Dict, Any


def get_my_farm(game_data: object, username: str) -> Dict[str, Any]:
    for farm in game_data["farms"]:
        if farm["name"] == username:
            my_farm = farm
            break
    else:
        raise ValueError(f"My farm is not found ({username})")
    print(my_farm)
    return my_farm


def buy_field(my_farm: Dict[str, Any]) -> List[str]:
    if not my_farm["money"] > 10000:
        return []
    for field in my_farm["fields"]:
        if not field["bought"]:
            return ["0 ACHETER_CHAMP"]
    return []


def get_owner_command(my_farm: Dict[str, Any]):
    commands: List[str] = []
    if not hasattr(get_owner_command, "is_busy"):
        get_owner_command.is_busy = False
    if not get_owner_command.is_busy:
        commands += buy_field(my_farm)
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


def get_next_actions(game_data: object, username: str) -> List[str]:
    my_farm: Dict[str, Any] = get_my_farm(game_data, username)
    commands: List[str]

    commands = get_owner_command(my_farm)

    return commands
