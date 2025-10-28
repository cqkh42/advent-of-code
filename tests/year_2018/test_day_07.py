import pytest

from aoc_cqkh42.year_2018 import day_07

@pytest.fixture
def data():
    return """Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin."""

def test_part_a(data):
    assert day_07.Solution(data).part_a() == "CABDFE"

def test_part_b(data):
    assert day_07.Solution(data).part_b(2, 0) == 15