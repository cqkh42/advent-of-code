import pytest

from aoc_cqkh42.year_2015 import day_02


@pytest.mark.parametrize('data, answer', [('2x3x4', 58), ('1x1x10', 43)])
def test_part_a(data, answer):
    solution = day_02.Solution(data)
    assert solution.part_a() == answer


@pytest.mark.parametrize('data, answer', [('2x3x4', 34), ('1x1x10', 14)])
def test_part_b(data, answer):
    solution = day_02.Solution(data)
    assert solution.part_b() == answer
