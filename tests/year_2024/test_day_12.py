import pytest

from aoc_cqkh42.year_2024.day_12 import Solution, Region


@pytest.fixture
def complex():
    data = """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE"""
    return Solution(data)

@pytest.fixture
def simple():
    data = """AAAA
BBCD
BBCC
EEEC"""
    return Solution(data)

def test_part_a(complex):
    assert complex.part_a() == 1930

def test_part_b_complex(complex):
    assert complex.part_b() == 1206

def test_part_b_simple(simple):
    assert simple.part_b() == 80

@pytest.mark.parametrize('nodes,sides', [
    (((0,0), (1,0), (2,0), (3, 0)), 4),
    (((0,1), (0,2), (1,1), (1, 2)), 4),
    (((2,1), (2,2), (3,2), (3, 3)), 8),
    (((3,1),), 4),
    (((0,3),(1,3), (2,3)), 4),
])
def test_region_sides(nodes, sides):
    assert Region(nodes).sides == sides

