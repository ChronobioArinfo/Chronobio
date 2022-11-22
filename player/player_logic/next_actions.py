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


def get_next_actions(game_data: object, username: str) -> List[str]:
    my_farm = get_my_farm(game_data, username)

    return ["0 EMPRUNTER 1"]
