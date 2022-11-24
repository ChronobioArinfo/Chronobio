from dataclasses import dataclass
from typing import Any, Dict
from .farm import Farm


@dataclass
class State():
    _my_farm: Farm
    _username: str
    _day: int = 0
    _is_busy: bool = False

    def __init__(self, username: str) -> None:
        self._username = username
        self._my_farm = Farm()

    def read_data(self, data: Dict[str, Any]) -> None:
        self._day = data["day"]
        for farm in data["farms"]:
            if farm["name"] == self._username:
                self._my_farm.read_data(farm)

    @property
    def my_farm(self) -> Farm:
        return self._my_farm
