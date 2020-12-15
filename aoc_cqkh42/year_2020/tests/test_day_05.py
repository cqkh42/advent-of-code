"""
Tests for day 5 of 2020's Advent of Code

"""
import pytest

from aoc_cqkh42.year_2020 import day_05

# noinspection SpellCheckingInspection
_data = [
        'BFFFBBFRRR',
        'FFFBBBFRRR',
        'BBFFBBFRLL',
        'FBFBBFFRLR'
]


@pytest.mark.parametrize('data, answer', zip(_data, [70, 14, 102, 44]))
def test__row(data, answer) -> None:
    assert day_05._row(data) == answer


@pytest.mark.parametrize('data, answer', zip(_data, [7, 7, 4, 5]))
def test__col(data, answer) -> None:
    assert day_05._col(data) == answer


@pytest.mark.parametrize('data, answer', zip(_data, [567, 119, 820, 357]))
def test__seat_id(data, answer) -> None:
    assert day_05._seat_id(data) == answer
