from dataclasses import dataclass
from random import randint
from typing import Any, Dict
from .my_type import Location, Vegetable


@dataclass
class Field:
    location: Location
    _vegetable_wanted: Vegetable
    _content: Vegetable = Vegetable.NONE
    _water_needed: int = 0
    _is_sellable: bool = False

    def __init__(self, location: Location) -> None:
        self.location = location
        self._vegetable_wanted = Vegetable(randint(1, 5))

    @property
    def vegetable_wanted(self) -> Vegetable:
        return self._vegetable_wanted

    @vegetable_wanted.setter
    def vegetable_wanted(self, vegetable: Vegetable) -> None:
        self._vegetable_wanted = vegetable

    @property
    def content(self) -> Vegetable:
        return self._content

    @content.setter
    def content(self, vegetable: Vegetable) -> None:
        self._content = vegetable

    def planting(self, vegetable: Vegetable = Vegetable.NONE) -> None:
        """planted the same previous type of vegetable or the new one given

        Args:
            vegetable (Vegetable, optional): The type of the vegetable wanted
        """
        if not vegetable == Vegetable.NONE:
            self.vegetable_wanted = vegetable
        self.content = self.vegetable_wanted
        self._water_needed = 10

    def watering(self) -> None:
        if self._water_needed > 0:
            self._water_needed -= 1

    def gathering(self) -> None:
        self._content = Vegetable.NONE

    def read_data(self, data: Dict[str, Any]) -> None:
        vegetables: Dict[str, Vegetable] = {
            "NONE": Vegetable.NONE,
            "POTATO": Vegetable.PATATE,
            "LEEK": Vegetable.POIREAU,
            "TOMATO": Vegetable.TOMATE,
            "ONION": Vegetable.OIGNON,
            "ZUCCHINI": Vegetable.COURGETTE,
        }
        my_vegetable = data["content"]
        self.content = vegetables[my_vegetable]
        self._water_needed = data["needed_water"]
        if self.content is not Vegetable.NONE and self._water_needed == 0:
            self._is_sellable = True
        else:
            self._is_sellable = False
