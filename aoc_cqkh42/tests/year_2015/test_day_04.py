import pytest

from aoc_cqkh42.year_2015 import day_04


@pytest.mark.parametrize(
    'data, answer',
    [('abcdef', 609043), ('pqrstuv', 1048970)]
)
def test_part_a(data, answer):
    assert day_04.part_a(data) == answer
