from dataclasses import dataclass
from typing import Optional

from player.json_class.state_json import StateJSON
from .farm import Farm


@dataclass
class State:
    _my_farm: Farm
    _username: str
    _day: int = 0
    _is_busy: int = 0

    def __init__(self, username: str) -> None:
        self._username = username
        self._my_farm = Farm()
        self.data = StateJSON(day=0, farms=[])

    @property
    def is_busy(self) -> int:
        return self._is_busy

    @is_busy.setter
    def is_busy(self, busy: int) -> None:
        self._is_busy = busy
        if self._is_busy < 0:
            self._is_busy = 0

    def sell(self) -> Optional[str]:
        field = self._my_farm.sellable_field()
        if field is not None and self._is_busy == 0:
            self._is_busy = 3
            return f"0 VENDRE {field.location.value}"
        return None

    def __setattr__(self, name: str, value: StateJSON) -> None:
        if name == "data":
            self._day = value.day
            for farm in value.farms:
                if farm.name == self._username:
                    self._my_farm.data = farm
        else:
            super().__setattr__(name, value)
