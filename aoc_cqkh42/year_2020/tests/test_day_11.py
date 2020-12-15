"""
Tests for day 11 of 2020's Advent of Code

"""
import pytest

from aoc_cqkh42.year_2020 import day_11


# noinspection SpellCheckingInspection
@pytest.fixture
def data() -> str:
    """
    Test data for day_01.

    Returns
    -------
    data: str
    """
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


def test_part_a(data) -> None:
    assert day_11.part_a(data) == 37


def test_part_b(data) -> None:
    assert day_11.part_b(data) == 26
