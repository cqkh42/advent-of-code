import pytest

from aoc_cqkh42.year_2025 import day_11


@pytest.fixture
def solution_a():
    return day_11.Solution(
        """aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out""")


@pytest.fixture
def solution_b():
    return day_11.Solution(
        """svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out""")
def test_part_a(solution_a):
    assert solution_a.part_a() == 5

def test_part_b(solution_b):
    assert solution_b.part_b() == 2