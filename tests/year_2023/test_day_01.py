from aoc_cqkh42.year_2023 import day_01

import pytest

@pytest.fixture()
def data():
    return """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""

def test_part_b(data):
    solution = day_01.Solution(data)
    assert solution.part_b() == 281