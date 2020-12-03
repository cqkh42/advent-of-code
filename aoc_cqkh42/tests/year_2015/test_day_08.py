import pytest

from aoc_cqkh42.year_2015 import day_08


@pytest.fixture
def data():
    return '""\n"abc"\n"aaa\\"aaa"\n"\\x27"'


def test_part_a(data):
    assert day_08.part_a(data) == 12


def test_part_b(data):
    assert day_08.part_b(data) == 19
