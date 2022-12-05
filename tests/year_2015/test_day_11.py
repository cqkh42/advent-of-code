import pytest

from aoc_cqkh42.year_2015 import day_11


# noinspection SpellCheckingInspection
@pytest.mark.parametrize(
    "data, answer", [("abcdefgh", "abcdffaa"), ("ghijklmn", "ghjaabcc")]
)
def test_part_a(data, answer):
    solution = day_11.Solution(data)
    assert solution.part_a() == answer
