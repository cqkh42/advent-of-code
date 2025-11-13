import pytest

from aoc_cqkh42.year_2018 import day_13

@pytest.fixture
def data():
    return r"""/->-\        
|   |  /----\
| /-+--+-\  |
| | |  | v  |
\-+-/  \-+--/
  \------/
"""
@pytest.fixture
def part_b_data():
    return r"""/>-<\  
|   |  
| /<+-\
| | | v
\>+</ |
  |   ^
  \<->/"""
def test_turn(data):
    cart = day_13.Solution(data).parsed[0]
    cart.orientation="v"
    cart.current = (4, 2)

    cart.turn()
    assert cart.orientation == ">"
    assert cart.current == (5, 2)
def test_part_a(data):
    assert day_13.Solution(data).part_a() == "7,3"

def test_part_b(part_b_data):
    assert day_13.Solution(part_b_data).part_b() == "6,4"