"""Tests for day 6 of 2020's Advent of Code."""
import pytest

from aoc_cqkh42.year_2020 import day_06


@pytest.fixture
def data() -> str:
    """
    Test data for day_01.

    Returns
    -------
    data: str
    """
    data = (
        "abc\n" "\n" "a\nb\nc\n" "\n" "ab\nac\n" "\n" "a\na\na\na\n" "\n" "b"
    )
    return data


def test_part_a(data) -> None:
    assert day_06.part_a(data) == 11


def test_part_b(data) -> None:
    assert day_06.part_b(data) == 6
