import pytest

from aoc_cqkh42.year_2021 import day_17


@pytest.fixture
def solution():
    data = "target area: x=20..30, y=-10..-5"
    return day_17.Solution(data)


def test_part_a(solution):
    assert solution.part_a() == 45


def test_part_b(solution):
    assert solution.part_b() == 112
