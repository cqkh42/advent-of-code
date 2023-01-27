import pytest

from aoc_cqkh42.year_2022 import day_15


@pytest.fixture(scope='module')
def solution():
    data = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3"""
    return day_15.Solution(data)


def test_resolve_manhattan():
    assert day_15.resolve_manhattan((8, 7), 9, 10) == [2, 14]
    with pytest.raises(ValueError):
        day_15.resolve_manhattan((0,0), 5, 10)

    with pytest.raises(ValueError):
        day_15.resolve_manhattan((14, 3), 1, 11)
    assert day_15.resolve_manhattan((391282,2038170), 1052098, 2_000_000) == [-622646, 1405210]


def test_part_a(solution):
    assert solution.part_a(9) == 25
    assert solution.part_a(10) == 26
    assert solution.part_a(11) == 27


def test_part_b(solution):
    assert solution.part_b(20) == 56_000_011
