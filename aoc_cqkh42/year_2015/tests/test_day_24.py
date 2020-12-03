import pytest

from aoc_cqkh42.year_2015 import day_24


@pytest.fixture
def data():
    return '1\n2\n3\n4\n5\n7\n8\n9\n10\n11'


def test_part_a(data):
    assert day_24.part_a(data) == 99


def test_part_b(data):
    assert day_24.part_b(data) == 44
