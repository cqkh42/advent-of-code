import pytest

from aoc_cqkh42.year_2015 import day_01


@pytest.mark.parametrize(
    "data, answer",
    [
        ("(())", 0),
        ("()()", 0),
        ("(((", 3),
        ("(()(()(", 3),
        ("))(((((", 3),
        ("())", -1),
        ("))(", -1),
        (")))", -3),
        (")())())", -3),
    ],
)
def test_part_a(data, answer):
    solution = day_01.Solution(data)
    assert solution.part_a() == answer


@pytest.mark.parametrize("data, answer", [(")", 1), ("()())", 5)])
def test_part_b(data, answer):
    solution = day_01.Solution(data)
    assert solution.part_b() == answer
