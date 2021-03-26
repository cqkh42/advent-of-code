import pytest

from aoc_cqkh42.year_2015 import day_18


@pytest.fixture
def data():
    return (
        '.#.#.#\n'
        '...##.\n'
        '#....#\n'
        '..#...\n'
        '#.#..#\n'
        '####..'
    )


def test_part_a(data):
    assert day_18.part_a(data, steps=4) == 4


def test_part_b(data):
    assert day_18.part_b(data, steps=5) == 17
