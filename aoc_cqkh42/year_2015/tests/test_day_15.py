import pytest

from aoc_cqkh42.year_2015 import day_15


@pytest.fixture
def data():
    return (
        'Butterscotch: capacity -1, durability -2, flavor 6, '
        'texture 3, calories 8\n'
        'Cinnamon: capacity 2, durability 3, flavor -2, '
        'texture -1, calories 3'
    )


def test_part_a(data):
    assert day_15.part_a(data) == 62_842_880


def test_part_b(data):
    assert day_15.part_b(data) == 57_600_000
