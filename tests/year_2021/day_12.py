import pytest

from aoc_cqkh42.year_2021 import day_12


@pytest.fixture
def solution():
    data = """start-A
start-b
A-c
A-b
b-d
A-end
b-end"""
    return day_12.Solution(data)


def test_part_a(solution):
    assert solution.part_a() == 10


def test_part_b(solution):
    assert solution.part_b() == 36


def test_part_b_route_valid():
    route = day_12.Route(('start', 'b', 'b', 'b', 'end'))
    assert not route.valid_part_b()
