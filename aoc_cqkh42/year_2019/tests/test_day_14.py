import pytest

from aoc_cqkh42.year_2019 import day_14


@pytest.mark.parametrize(
    'needs, gives, answer', [(1, 1, 1), (2, 2, 1), (1, 100, 1), (100, 1, 100)]
)
def test__find_multiple_above(needs, gives, answer):
    assert day_14._count_iterations(needs, gives) == answer