import pytest

from aoc_cqkh42.year_2017.day_21 import Solution, create_thruple, break_into_chunks

import numpy as np

@pytest.fixture
def data():
    return """../.# => ##./#../...
.#./..#/### => #..#/..../..../#..#"""


def test_create_thruple():
    a = ('.#.', '#.#', '...')
    assert create_thruple(a) == {
        ('.#.', '#.#', '...'),
        ('...', '#.#', '.#.'),
        ('.#.', '..#', '.#.'),
        ('.#.', '#..', '.#.')
    }

def test_break_into_chunks():
    a = ('#..#', '....', '....', '#..#')
    assert tuple(break_into_chunks(a, 2)) == (
        ('#.', '..'),
        ('.#', '..'),
        ('..', '#.'),
        ('..', '.#')
    )


def test_part_a(data):
    assert Solution(data).part_a(2) == 12


def test_part_b(data_b):
    assert Solution(data_b).part_b() == 1