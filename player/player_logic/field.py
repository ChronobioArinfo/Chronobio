from dataclasses import dataclass
from .my_type import Location, Vegetable


@dataclass
class Field:
    _location: Location
    _vegetable_wanted: Vegetable = Vegetable.NONE
    _content: Vegetable = Vegetable.NONE
    _water_needed: int = 0

    @property
    def vegetable_wanted(self) -> Vegetable:
        return self._vegetable_wanted

    @vegetable_wanted.setter
    def vegetable_wanted(self, vegetable: Vegetable) -> None:
        self._vegetable_wanted = vegetable

    def planting(self, vegetable: Vegetable = Vegetable.NONE) -> None:
        if not vegetable == Vegetable.NONE:
            self.vegetable_wanted = vegetable
        self._content = self.vegetable_wanted
        self._water_needed = 10

    def watering(self) -> None:
        self._water_needed -= 1

    def gathering(self) -> None:
        self._content = Vegetable.NONE
