import pytest

from aoc_cqkh42.year_2015 import day_17


@pytest.fixture
def solution():
    data = '20\n15\n10\n5\n5'
    solution = day_17.Solution(data)
    return solution


def test_part_a(solution):
    assert solution.part_a(target=25) == 4


def test_part_b(solution):
    assert solution.part_b(target=25) == 3
