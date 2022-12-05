from aoc_cqkh42.year_2015 import day_23


def test_part_a():
    data = "inc a\njio a, +2\ntpl a\ninc a"
    solution = day_23.Solution(data)
    assert solution.part_a(target="a") == 2
