import pytest

from aoc_cqkh42.year_2022 import day_01


@pytest.fixture(scope='module')
def solution():
    data = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""
    return day_01.Solution(data)


def test_part_a(solution):
    assert solution.part_a() == 24000


def test_part_b(solution):
    assert solution.part_b() == 45000
