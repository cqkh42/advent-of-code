import pytest

from aoc_cqkh42.year_2022 import day_09


@pytest.fixture(scope='module')
def solution():
    data = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""
    return day_09.Solution(data)


def test_part_a(solution):
    assert solution.part_a() == 13


def test_part_b(solution):
    assert solution.part_b() == 36
