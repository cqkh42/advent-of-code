"""
Tests for day 12 of 2020's Advent of Code

"""
import pytest

from aoc_cqkh42.year_2020 import day_12


@pytest.fixture
def data() -> str:
    """
    Test data for day_01.

    Returns
    -------
    data: str
    """
    data = 'F10\nN3\nF7\nR90\nF11'
    return data


def test_part_a(data) -> None:
    assert day_12.part_a(data) == 25


def test_part_b(data) -> None:
    assert day_12.part_b(data) == 286
