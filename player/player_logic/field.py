from dataclasses import dataclass
from random import randint
from typing import Dict

from player.json_class.field_json import FieldJSON
from .my_type import Location, Vegetable


@dataclass
class Field:
    location: Location
    vegetable_wanted: Vegetable
    content: Vegetable = Vegetable.NONE
    water_needed: int = 0
    is_sellable: bool = False

    def __init__(self, location: Location) -> None:
        self.location = location
        self.vegetable_wanted = Vegetable(randint(1, 5))
        self.data: FieldJSON = FieldJSON(
            bought=True,
            content="NONE",
            location=location.name,
            needed_water=0
        )

    def planting(self, vegetable: Vegetable = Vegetable.NONE) -> None:
        """planted the same previous type of vegetable or the new one given

        Args:
            vegetable (Vegetable, optional): The type of the vegetable wanted
        """
        if not vegetable == Vegetable.NONE:
            self.vegetable_wanted = vegetable
        self.content = self.vegetable_wanted
        self.water_needed = 10

    def watering(self) -> None:
        if self.water_needed > 0:
            self.water_needed -= 1

    def __setattr__(self, name: str, value: FieldJSON) -> None:
        if name == "data":
            vegetables: Dict[str, Vegetable] = {
                "NONE": Vegetable.NONE,
                "POTATO": Vegetable.PATATE,
                "LEEK": Vegetable.POIREAU,
                "TOMATO": Vegetable.TOMATE,
                "ONION": Vegetable.OIGNON,
                "ZUCCHINI": Vegetable.COURGETTE,
            }
            self.content = vegetables[value.content]
            self.water_needed = value.needed_water
            if self.content is not Vegetable.NONE and self.water_needed == 0:
                self.is_sellable = True
            else:
                self.is_sellable = False
        else:
            super().__setattr__(name, value)
