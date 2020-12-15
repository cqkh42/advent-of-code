"""
Tests for day 13 of 2020's Advent of Code

"""
import pytest

from aoc_cqkh42.year_2020 import day_13


def test_part_a() -> None:
    data = '939\n7,13,x,x,59,x,31,19'
    assert day_13.part_a(data) == 295


@pytest.mark.parametrize(
    'data, answer',
    [
        ('1\n17,x,13,19', 3417),
        ('1\n7,13,x,x,59,x,31,19', 1068781),
        ('1\n67,7,59,61', 754018),
        ('1\n67,x,7,59,61', 779210),
        ('1\n67,7,x,59,61', 1261476),
        ('1\n1789,37,47,1889', 1202161486)
    ]
)
def test_part_b(data, answer) -> None:
    assert day_13.part_b(data) == answer
