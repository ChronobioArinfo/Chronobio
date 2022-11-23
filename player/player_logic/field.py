from dataclasses import dataclass
from random import randint
from .my_type import Location, Vegetable


@dataclass
class Field:
    _location: Location
    _vegetable_wanted: Vegetable
    _content: Vegetable = Vegetable.NONE
    _water_needed: int = 0

    def __init__(self, location: Location) -> None:
        self._location = location
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

    @property
    def water_needed(self) -> int:
        return self._water_needed

    @property
    def location(self) -> int:
        return self._location.value

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
