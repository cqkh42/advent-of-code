"""
Tests for day 9 of 2020's Advent of Code

"""
import pytest

from aoc_cqkh42.year_2020 import day_09


@pytest.fixture
def data() -> str:
    """
    Test data for day_01.

    Returns
    -------
    data: str
    """
    data = (
        '35\n20\n15\n25\n47\n40\n62\n55\n65\n95\n102\n117\n150\n182\n127\n'
        '219\n299\n277\n309\n576'
    )
    return data


@pytest.mark.parametrize(
    'preamble, target, answer',
    [
        (range(1, 26), 26, True),
        (range(1, 26), 49, True),
        (range(1, 26), 100, False),
        (range(1, 26), 50, False),
        ((*range(1, 20), *range(21, 26), 45), 26, True),
        ((*range(1, 20), *range(21, 26), 45), 65, False),
        ((*range(1, 20), *range(21, 26), 45), 64, True),
        ((*range(1, 20), *range(21, 26), 45), 66, True),
    ]
)
def test__is_valid(preamble, target, answer) -> None:
    assert day_09._is_valid(preamble, target) == answer


def test__find_sequence() -> None:
    data = [
        35, 20, 15, 25, 47, 40, 62, 55, 65, 95, 102, 117, 150, 182, 127, 219,
        299, 277, 309, 576
    ]
    assert day_09._find_sequence(data, 127) == [15, 25, 47, 40]


def test_part_a(data) -> None:
    assert day_09.part_a(data, 5) == 127


def test_part_b(data) -> None:
    assert day_09.part_b(data, 127) == 62
