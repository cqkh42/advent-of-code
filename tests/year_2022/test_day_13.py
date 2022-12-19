import pytest

from aoc_cqkh42.year_2022 import day_13


@pytest.fixture(scope='module')
def solution():
    data = """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]"""
    return day_13.Solution(data)


def test_part_a(solution):
    assert solution.part_a() == 13


def test_part_b(solution):
    assert solution.part_b() == 140
