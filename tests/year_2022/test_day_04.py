import pytest

from aoc_cqkh42.year_2022 import day_04


@pytest.fixture(scope='module')
def solution():
    data = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""
    return day_04.Solution(data)


def test_part_a(solution):
    assert solution.part_a() == 2


def test_part_b(solution):
    assert solution.part_b() == 4
