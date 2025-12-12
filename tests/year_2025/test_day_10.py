import pytest

from aoc_cqkh42.year_2025 import day_10


@pytest.fixture
def solution():
    return day_10.Solution(
        """[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}""")


def test_part_a(solution):
    assert solution.part_a() == 7

def test_part_b(solution):
    assert solution.part_b() == 33

def test_solve_line():
    line = "[.#.###.] (0,2,4,5,6) (0,2,5) (0,2) (0,1,2,4,5) (2,3,5,6) (1,3) (0,1,3,4,5) (1,2,3,4) (1,2,3,5,6) {67,66,93,57,48,71,36}"
    assert day_10.solve_line(line) == 5