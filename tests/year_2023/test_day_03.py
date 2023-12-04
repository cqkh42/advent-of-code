from aoc_cqkh42.year_2023 import day_03

import pytest


@pytest.fixture()
def data():
    return """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""


def test_part_b(data):
    solution = day_03.Solution(data)
    assert solution.part_b() == 467835
