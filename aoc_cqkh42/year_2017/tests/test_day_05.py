import pytest

from aoc_cqkh42.year_2017 import day_05


@pytest.fixture
def data():
    return '0\n3\n0\n1\n-3'


def test_part_a(data):
    assert day_05.part_a(data) == 5


def test_part_b(data):
    assert day_05.part_b(data) == 10