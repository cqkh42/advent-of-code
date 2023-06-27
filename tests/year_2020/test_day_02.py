"""Tests for day 2 of 2020's Advent of Code."""
import pytest

from aoc_cqkh42.year_2020 import day_02


# noinspection SpellCheckingInspection
@pytest.fixture
def data() -> str:
    """
    Test data for day_02.

    Returns
    -------
    data: str
    """
    return "1-3 a: abcde\n1-3 b: cdefg\n2-9 c: ccccccccc"


def test_part_a(data) -> None:
    assert day_02.part_a(data) == 2


def test_part_b(data) -> None:
    assert day_02.part_b(data) == 1
