import pytest

from aoc_cqkh42.year_2015 import day_09


@pytest.fixture
def data():
    return (
        'London to Dublin = 464\n'
        'London to Belfast = 518\n'
        'Dublin to Belfast = 141'
    )


def test_part_a(data):
    assert day_09.part_a(data) == 605


def test_part_b(data):
    assert day_09.part_b(data) == 982
