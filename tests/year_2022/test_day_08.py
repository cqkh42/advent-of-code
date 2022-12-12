import pytest

from aoc_cqkh42.year_2022 import day_08


@pytest.fixture(scope='module')
def solution():
    data = """30373
25512
65332
33549
35390"""
    return day_08.Solution(data)


def test_part_a(solution):
    assert solution.part_a() == 21


def test_part_b(solution):
    assert solution.part_b() == 8


def test_visible():
    assert day_08.visible([3,0,3,7,3]) == [True, False, False, True, False]
    assert day_08.visible([2, 5, 5]) == [True, True, False]


def test_visible_row():
    assert day_08.visible_row([3,0,3,7,3]) == [2, 1, 1, 1, 0]
    assert day_08.visible_row([2, 5, 5]) == [1,1,0]
