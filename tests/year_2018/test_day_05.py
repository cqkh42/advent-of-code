import pytest

from aoc_cqkh42.year_2018 import day_05


@pytest.mark.parametrize('string,expected', [
    ('aA', 0),
    ('abBA', 0),
    ('abAB', 4),
    ('aabAAB', 6),
    ('dabAcCaCBAcCcaDA', 10)
])
def test_part_a(string,expected):
    assert day_05.Solution(string).part_a() == expected