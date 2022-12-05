import pytest

from aoc_cqkh42.year_2015 import day_10


@pytest.mark.parametrize(
    "data, answer", [("1", 2), ("11", 2), ("21", 4), ("1211", 6), ("111221", 6)]
)
def test_part_a(data, answer):
    solution = day_10.Solution(data)
    assert solution.part_a(iters=1) == answer
