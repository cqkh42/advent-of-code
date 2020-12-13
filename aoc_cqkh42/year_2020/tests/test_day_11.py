import pytest

from aoc_cqkh42.year_2020 import day_11


@pytest.fixture
def data():
    data = (
    'L.LL.LL.LL\n'
    'LLLLLLL.LL\n'
    'L.L.L..L..\n'
    'LLLL.LL.LL\n'
    'L.LL.LL.LL\n'
    'L.LLLLL.LL\n'
    '..L.L.....\n'
    'LLLLLLLLLL\n'
    'L.LLLLLL.L\n'
    'L.LLLLL.LL'
    )
    return data


def test_part_a(data):
    assert day_11.part_a(data) == 37


def test_part_b(data):
    assert day_11.part_b(data) == 26
