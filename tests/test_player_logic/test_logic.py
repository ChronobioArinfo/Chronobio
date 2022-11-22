from json import load as json_load
from pathlib import Path
import pytest

from player.player_logic.next_actions import get_my_farm


@pytest.fixture
def load_day_zero():
    jsonfile = Path('./tests/day0.json')
    with open(jsonfile) as file:
        data = json_load(file)
    return data


def load_my_json(jsonfile):
    with open(jsonfile) as file:
        data = json_load(file)
    return data


def test_get_my_farm(load_day_zero):
    expected = load_my_json(Path('./tests/my_farm_day0.json'))
    assert get_my_farm(load_day_zero, "Roger") == expected
