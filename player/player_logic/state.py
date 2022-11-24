from dataclasses import dataclass
from typing import List
from .farm import Farm
from .field import Field
from typing import List, Optional


@dataclass
class State:
    _my_farm: Farm
    _username: str
    _day: int = 0
    _is_busy: int = 0  # if sell == 2
    # create function sell, with parameter the field, return the command exemple: 0 sell 1
    # call her in_next_action if only the field can be sell

    @property
    def is_busy(self):
        return self._is_busy

    @is_busy.setter
    def is_busy(self, busy: int) -> None:
        self._is_busy = busy
        if self._is_busy < 0:
            self._is_busy = 0

    def __init__(self, username: str) -> None:
        self._username = username
        self._my_farm = Farm()

    def read_data(self, data: object) -> None:
        self._day = data["day"]
        for farm in data["farms"]:
            if farm["name"] == self._username:
                self._my_farm.read_data(farm)

    def sell(self) -> str:
        field = self._my_farm.sellable_field()
        if field != None and self._is_busy == 0:
            self._is_busy = 3
            return f"0 VENDRE {field.location}"
        return ""

    @property
    def my_farm(self) -> Farm:
        return self._my_farm
