import pytest

from aoc_cqkh42.year_2015 import day_4


@pytest.mark.parametrize('data,answer', [('abcdef', 609043), ('pqrstuv', 1048970)])
def test_part_a(data, answer):
    assert day_4.part_a(data) == answer
