import textwrap

import pytest

from aoc_cqkh42.year_2015 import day_18


@pytest.fixture
def solution():
    data = """\
        .#.#.#
        ...##.
        #....#
        ..#...
        #.#..#
        ####.."""
    solution = day_18.Solution(textwrap.dedent(data))
    return solution


def test_part_a(solution):
    assert solution.part_a(steps=4) == 4


def test_part_b(solution):
    assert solution.part_b(steps=5) == 17
