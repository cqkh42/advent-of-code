import pytest

from aoc_cqkh42.year_2015 import day_05


# noinspection SpellCheckingInspection
@pytest.mark.parametrize(
    'data, answer',
    [
        ('ugknbfddgicrmopn', 1),
        ('aaa', 1),
        ('jchzalrnumimnmhp', 0),
        ('haegwjzuvuyypxyu', 0),
        ('dvszwmarrgswjxmb', 0)
    ]
)
def test_part_a(data, answer):
    assert day_05.part_a(data) == answer


# noinspection SpellCheckingInspection
@pytest.mark.parametrize(
    'data, answer',
    [
        ('qjhvhtzxzqqjkmpb', 1),
        ('xxyxx', 1),
        ('uurcxstgmygtbstg', 0),
        ('ieodomkazucvgmuy', 0)
    ]
)
def test_part_b(data, answer):
    assert day_05.part_b(data) == answer
