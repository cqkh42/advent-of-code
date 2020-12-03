import pytest

from aoc_cqkh42.year_2015 import day_11


# noinspection SpellCheckingInspection
@pytest.mark.parametrize(
    'data, answer', [('abcdefgh', 'abcdffaa'), ('ghijklmn', 'ghjaabcc')]
)
def test_part_a(data, answer):
    assert day_11.part_a(data) == answer
