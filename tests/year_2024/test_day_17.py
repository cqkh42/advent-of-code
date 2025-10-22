from aoc_cqkh42.year_2024 import day_17

def test_part_b():
    string = """
Register A: 2024
Register B: 0
Register C: 0

Program: 0,3,5,4,3,0
    """
    solution = day_17.Solution(string)
    assert solution.part_b() == 117440