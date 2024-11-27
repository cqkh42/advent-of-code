import pytest

from aoc_cqkh42.year_2017.day_21 import Solution, create_thruple, break_into_chunks, rebuild_into_lines


@pytest.fixture
def data():
    return """../.# => ##./#../...
.#./..#/### => #..#/..../..../#..#"""


def test_create_thruple_three():
    a = ('ABC', 'DEF', 'HIJ')
    assert create_thruple(a) == {
        ('ABC', 'DEF', 'HIJ'),
        ('HIJ', 'DEF', 'ABC'),
        ('CBA', 'FED', 'JIH'),
        ('HDA', 'IEB', 'JFC'),
        ('JIH', 'FED', 'CBA'),
        ('CFJ', 'BEI', 'ADH'),
    }

def test_create_thruple_two():
    a = ('AB', 'CD')
    assert create_thruple(a) == {
        ('AB', 'CD'), # LINES,

        ('CD', 'AB') ,# flipped vertically,
        ('BA', 'DC'), # flipped h,
        ('CA', 'DB'),
        ('DC', 'BA'),
        ('BD', 'AC'),

    }

def test_create_thruple_three():
    a = ('.#.', '..#', '###')
    assert ('.##', '#.#', '..#') in create_thruple(a)

def test_break_into_chunks():
    a = ('#..#', '....', '....', '#..#')
    assert tuple(break_into_chunks(a)) == (
        ('#.', '..'),
        ('.#', '..'),
        ('..', '#.'),
        ('..', '.#')
    )

def test_rebuild():
    a = (
        ('#.', '..'),
        ('.#', '..'),
        ('..', '#.'),
        ('..', '.#')
    )
    assert rebuild_into_lines(a) == ('#..#', '....', '....', '#..#')

def test_part_a(data):
    assert Solution(data).part_a(2) == 12


def test_part_b(data_b):
    assert Solution(data_b).part_b() == 1