import pytest

from aoc_cqkh42.year_2018 import day_14

@pytest.mark.parametrize(['steps', 'expected'], [
    (5, "0124515891"),
    (9, "5158916779"),
    (18, "9251071085"),
    (2018, "5941429882"),
])
def test_part_a(steps, expected):
    assert day_14.Solution("").part_a(steps) == expected

@pytest.mark.parametrize(['seq', 'expected'], [
    ("01245", 5),
    ("51589", 9),
    ("92510", 18),
    ("59414", 2018)
])
def test_part_b(seq, expected):
    assert day_14.Solution(seq).part_b() == expected