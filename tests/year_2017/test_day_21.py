import pytest

from aoc_cqkh42.year_2017.day_21 import Solution, do_three_iteration

import numpy as np

@pytest.fixture
def data():
    return """../.# => ##./#../...
.#./..#/### => #..#/..../..../#..#"""


def test_three_iteration():
    maps = {
        '../.#':  '##./#../...',
        '.#./..#/###': '#..#/..../..../#..#'
    }
    start = np.array([
        [False, True, False],
        [False, False, True],
        [True, True, True]
    ])
    end = np.array([
        [True, False, False, True],
        [False, False, False, False],
        [False, False, False, False],
        [True, False, False, True]
    ])

    np.testing.assert_array_equal(do_three_iteration(start, maps), end)


def test_part_a(data):
    assert Solution(data).part_a(2) == 12


def test_part_b(data_b):
    assert Solution(data_b).part_b() == 1