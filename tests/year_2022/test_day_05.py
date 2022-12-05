import pytest

from aoc_cqkh42.year_2022 import day_05


@pytest.fixture(scope='module')
def solution():
    data = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""
    return day_05.Solution(data)


def test_part_a(solution):
    assert solution.part_a() == 'CMZ'


def test_part_b(solution):
    assert solution.part_b() == 'MCD'
