import pytest

from aoc_cqkh42.year_2015 import day_6


@pytest.mark.parametrize(
    'data,answer',
    [
        ('turn on 0,0 through 999,999', 1_000_000),
        ('toggle 0,0 through 999,0', 1_000),
        ('turn off 499,499 through 500,500', 0)
    ]
)
def test_part_a(data, answer):
    assert day_6.part_a(data) == answer


@pytest.mark.parametrize(
    'data,answer',
    [
        ('turn on 0,0 through 0,0', 1),
        ('toggle 0,0 through 999,999', 2_000_000)
    ]
)
def test_part_b(data, answer):
    assert day_6.part_b(data) == answer
