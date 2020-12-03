import pytest

from aoc_cqkh42.year_2015 import day_17


@pytest.fixture
def data():
    return '20\n15\n10\n5\n5'


def test_part_a(data):
    assert day_17.part_a(data, target=25) == 4


def test_part_b(data):
    assert day_17.part_b(data, target=25) == 3
