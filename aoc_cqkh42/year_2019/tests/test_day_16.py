import pytest

from aoc_cqkh42.year_2019 import day_16


def test__get_patterns():
    signal = '12345678'
    expected = [
        [1,0,-1,0,1,0,-1,0],
        [0,1,1,0,0,-1,-1,0],
        [0,0,1,1,1,0,0,0],
        [0,0,0,1,1,1,1,0],
        [0,0,0,0,1,1,1,1],
        [0,0,0,0,0,1,1,1],
        [0,0,0,0,0,0,1,1],
        [0,0,0,0,0,0,0,1]
    ]
    assert day_16._get_patterns(signal) == expected