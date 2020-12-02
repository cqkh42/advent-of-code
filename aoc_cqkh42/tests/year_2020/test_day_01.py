import pytest

from aoc_cqkh42.year_2020 import day_01


@pytest.fixture
def data():
    return '1721\n979\n366\n299\n675\n1456'


def test_part_a(data):
    assert day_01.part_a(data) == 514579


def test_part_b(data):
    assert day_01.part_b(data) == 241861950
