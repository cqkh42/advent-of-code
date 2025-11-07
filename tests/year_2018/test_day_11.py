import pytest

from aoc_cqkh42.year_2018 import day_11

@pytest.fixture
def data():
    return """42"""

@pytest.mark.parametrize(("grid", "location", "expected"), [
    (57, (78, 121), -5),
    (39, (195,216), 0),
    (71, (152,100), 4)
])
def test_power_levels(grid, location, expected):
    parsed = day_11.Solution(str(grid)).parsed
    assert parsed[*location] == expected

@pytest.mark.parametrize(("grid", "expected_location", "expected_total"), [
    (18, "33,45", 29),
    (42, "21,61", 30)
])
def test_part_a(grid, expected_location, expected_total):
    solution = day_11.Solution(str(grid))
    assert solution._window().max() == expected_total
    assert day_11.Solution(str(grid)).part_a() == expected_location

def test_part_b(data):
    assert day_11.Solution("18").part_b() == "90,269,16"