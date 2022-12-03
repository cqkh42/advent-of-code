import pytest

from aoc_cqkh42.year_2022 import day_03


@pytest.fixture(scope='module')
def solution():
    data = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""
    return day_03.Solution(data)


def test_part_a(solution):
    assert solution.part_a() == 157


def test_part_b(solution):
    assert solution.part_b() == 70
