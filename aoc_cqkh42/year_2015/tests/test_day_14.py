import pytest

from aoc_cqkh42.year_2015 import day_14


@pytest.fixture
def data():
    return (
        'Comet can fly 14 km/s for 10 seconds, '
        'but then must rest for 127 seconds.\n'
        'Dancer can fly 16 km/s for 11 seconds, '
        'but then must rest for 162 seconds.'
    )


def test_part_a(data):
    assert day_14.part_a(data, 1000) == 1120


def test_part_b(data):
    assert day_14.part_b(data, 1000) == 689
