import pytest

from aoc_cqkh42.year_2022 import day_12


@pytest.fixture(scope='module')
def solution():
    data = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""
    return day_12.Solution(data)


def test_part_a(solution):
    assert solution.part_a() == 31

def test_part_b(solution):
    assert solution.part_b() == 29
