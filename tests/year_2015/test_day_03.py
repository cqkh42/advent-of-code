import pytest

from aoc_cqkh42.year_2015 import day_03


@pytest.mark.parametrize("data, answer", [(">", 2), ("^>v<", 4), ("^v^v^v^v^v", 2)])
def test_part_a(data, answer):
    solution = day_03.Solution(data)
    assert solution.part_a() == answer


@pytest.mark.parametrize("data, answer", [("^v", 3), ("^>v<", 3), ("^v^v^v^v^v", 11)])
def test_part_b(data, answer):
    solution = day_03.Solution(data)
    assert solution.part_b() == answer
