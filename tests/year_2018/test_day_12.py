import pytest

from aoc_cqkh42.year_2018 import day_12

@pytest.fixture
def data():
    return """initial state: #..#.#..##......###...###

...## => #
..#.. => #
.#... => #
.#.#. => #
.#.## => #
.##.. => #
.#### => #
#.#.# => #
#.### => #
##.#. => #
##.## => #
###.. => #
###.# => #
####. => #"""

def test_part_a(data):
    assert day_12.Solution(data).part_a() == 325

def test_part_b(data):
    assert day_12.Solution(data).part_b() == 66