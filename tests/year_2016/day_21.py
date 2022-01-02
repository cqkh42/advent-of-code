from aoc_cqkh42.year_2016.day_21 import Scrambler

import pytest


def test_swap_position():
    scrambler = Scrambler(list('abcde'))
    assert scrambler.swap_position(4, 0) == list('ebcda')


def test_swap_letter():
    scrambler = Scrambler(list('ebcda'))
    assert scrambler.swap_letter('d', 'b') == list('edcba')


def test_reverse():
    scrambler = Scrambler(list('edcba'))
    assert scrambler.reverse(0, 4) == list('abcde')


def test_rotate_left():
    scrambler = Scrambler(list('abcde'))
    assert scrambler.rotate_left(1) == list('bcdea')


@pytest.mark.parametrize(
    "test_input,x,expected",
    [
        (list('abcde'), 1, list('eabcd')),
        (list('bcdaefgh'), 0,  list('bcdaefgh'))
    ]
)
def test_rotate_right(test_input, x, expected):
    scrambler = Scrambler(test_input)
    assert scrambler.rotate_right(x) == expected


@pytest.mark.parametrize(
    "test_input,x,y,expected",
    [
        (list('bcdea'), 1, 4, list('bdeac')),
        (list('bdeac'), 3, 0, list('abdec'))
     ]
)
def test_move(test_input, x, y, expected):
    scrambler = Scrambler(test_input)
    assert scrambler.move(x, y) == expected


@pytest.mark.parametrize(
    "test_input,x,expected",
    [
        (list('abdec'), 'b', list('ecabd')),
        (list('ecabd'), 'd', list('decab'))
     ]
)
def test_rotate_based_on(test_input, x, expected):
    scrambler = Scrambler(test_input)
    assert scrambler.rotate_based_on(x) == expected
