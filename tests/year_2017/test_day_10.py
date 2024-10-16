import pytest

from aoc_cqkh42.year_2017.day_10 import Solution, ordify_sequence, reduce_xor
import numpy as np

def test_part_a():
    assert Solution('3,4,1,5').part_a(size=5) == 12

@pytest.mark.parametrize('rope,length,position,expected', [
    (np.array([0,1,2,3,4]), 3, 0, np.array([2,1,0,3,4])),
    (np.array([2,1,0,3,4]), 4, 3, np.array([4,3,0,1,2])),
    (np.array([4,3,0,1,2]), 1, 3, np.array([4,3,0,1,2])),
    (np.array([4,3,0,1,2]), 5,1,np.array([3,4,2,1,0]))
])
def test_twist(rope, length, position, expected):
    output= Solution('3,4,1,5').do_twist(
        rope=rope,
        length=length,
        position=position
    )
    np.testing.assert_array_equal(output, expected)


def test_ordify():
    assert ordify_sequence('1,2,3') == [49,44,50,44,51,17,31,73,47,23]


def test_reduce_xor():
    sequence = [65,27,9,1, 4, 3, 40, 50, 91, 7, 6, 0, 2, 5, 68, 22]
    assert reduce_xor(sequence) == 64