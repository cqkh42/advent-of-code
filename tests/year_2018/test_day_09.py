import pytest

from aoc_cqkh42.year_2018 import day_09
@pytest.mark.parametrize(["players", "marbles", "expected"], [
    (9, 25, 32),
    (10, 1618, 8317),
    (13, 7999, 146373),
    (17, 1104, 2764),
    (21, 6111, 54718),
    (30, 5807, 37305)
])
def test_solve(players, marbles, expected):
    assert day_09.solve(players, marbles) == expected