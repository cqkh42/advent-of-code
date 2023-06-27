"""Tests for day 1 of 2020's Advent of Code."""
import pytest

from aoc_cqkh42.year_2020 import day_01


@pytest.fixture
def data() -> str:
    """
    Test data for day_01.

    Returns
    -------
    data: str
    """
    return "1721\n979\n366\n299\n675\n1456"


def test__find_subset_with_sum(data) -> None:
    numbers = [1721, 979, 366, 299, 675, 1456]
    assert day_01._find_subset_with_sum(numbers, 2020, 2) == (1721, 299)


def test_part_a(data) -> None:
    assert day_01.part_a(data) == 514579


def test_part_b(data) -> None:
    assert day_01.part_b(data) == 241861950
