from json import load as json_load
from pathlib import Path

import player.player_logic.next_actions as next_actions


def load_my_json(jsonfile):
    with open(jsonfile) as file:
        data = json_load(file)
    return data


def test_get_my_farm():
    data = load_my_json(Path('./tests/day0.json'))
    expected = load_my_json(Path('./tests/my_farm_day0.json'))
    assert next_actions.get_my_farm(data, "Roger") == expected


def test_total_number_vegetable():
    data = load_my_json(Path('./tests/day3.json'))
    expected = {
        "POTATO": 7, "LEEK": 0, "TOMATO": 0, "ONION": 0, "ZUCCHINI": 0
        }
    assert next_actions.total_number_vegetable(data) == expected
