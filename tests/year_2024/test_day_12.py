from aoc_cqkh42.year_2024 import day_12

def test_part_a():
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
    assert day_12.Solution(data).part_a() == 1930