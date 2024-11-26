import pytest

from aoc_cqkh42.year_2017 import day_06


@pytest.fixture
def solution():
    return day_06.Solution("0\t2\t7\t0")


@pytest.mark.parametrize(
    "data, answer",
    [
        ([0, 2, 7, 0], (2, 4, 1, 2)),
        ([2, 4, 1, 2], (3, 1, 2, 3)),
        ([3, 1, 2, 3], (0, 2, 3, 4)),
        ([0, 2, 3, 4], (1, 3, 4, 1)),
        ([1, 3, 4, 1], (2, 4, 1, 2)),
    ],
)
def test__distribute(data, answer):
    assert day_06._distribute(data) == answer


def test_part_a(solution):
    assert solution.part_a() == 5


def test_part_b(solution):
    assert solution.part_b() == 4
