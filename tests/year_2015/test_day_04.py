import pytest

from aoc_cqkh42.year_2015 import day_04


@pytest.mark.parametrize("data, answer",
                         [("abcdef", 609_043), ("pqrstuv", 1_048_970)])
def test_part_a(data, answer):
    solution = day_04.Solution(data)
    assert solution.part_a() == answer
