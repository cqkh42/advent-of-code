import pytest

from aoc_cqkh42.year_2021 import day_14


@pytest.fixture
def solution():
    data = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""
    return day_14.Solution(data)


def test_part_a(solution):
    assert solution.part_a() == 1588


def test_part_b(solution):
    assert solution.part_b() == 2188189693529
