import pytest

from aoc_cqkh42.year_2021 import day_13


@pytest.fixture
def solution():
    data = """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5"""
    return day_13.Solution(data)


def test_part_a(solution):
    assert solution.part_a() == 17


def test_part_b(solution):
    assert solution.part_b() == float('inf')
