import pytest

from aoc_cqkh42.year_2015 import day_08


@pytest.fixture
def solution():
    data = '""\n"abc"\n"aaa\\"aaa"\n"\\x27"'
    solution = day_08.Solution(data)
    return solution


def test_part_a(solution):
    assert solution.part_a() == 12


def test_part_b(solution):
    assert solution.part_b() == 19
