from collections import defaultdict, Counter

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
    assert solution.flat().total() == 3073
    assert solution.flat()['B'] == 1749
    assert solution.flat()['C'] == 298
    assert solution.flat()['H'] == 161
    assert solution.flat()['N'] == 865


def test_part_b(solution):
    solution.part_a()
    assert solution.part_b() == 2188189693529


def test_one_run(solution):
    solution.run()
    assert solution.polymer == defaultdict(int, {'NC': 1, 'CN': 1, 'NB': 1, 'BC': 1, 'CH': 1, 'HB': 1})
    assert solution.count() == 1


def test_four_run(solution):
    solution.run()
    solution.run()
    solution.run()
    solution.run()
    assert solution.flat() == Counter({'B': 23, 'N': 11, 'C': 10, 'H': 5})
    assert solution.polymer == defaultdict(int, {'NB': 9, 'BB': 9, 'BN': 6, 'BC': 4, 'CC': 2, 'CN': 3, 'NC': 1, 'CB': 5, 'BH': 3, 'HC': 3, 'HH': 1, 'HN': 1, 'NH': 1})
