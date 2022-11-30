import pytest
import numpy as np
from aoc_cqkh42.year_2021 import day_15


@pytest.fixture
def solution():
    data = """1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581"""
    return day_15.Solution(data)


def test_make_big_square():
    out = day_15.make_big_square(np.array([[8]]))
    expected = [
        [8, 9, 1, 2, 3],
        [9, 1, 2, 3, 4],
        [1, 2, 3, 4, 5],
        [2, 3, 4, 5, 6],
        [3, 4, 5, 6, 7],
    ]
    np.testing.assert_array_equal(out, expected)


def test_part_a(solution):
    assert solution.part_a() == 40


def test_part_b(solution):
    solution.part_a()
    assert solution.part_b() == 315

#
# def test_shortest_path(solution):
#     sh =