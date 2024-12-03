from aoc_cqkh42.year_2024 import day_03

def test_part_b():
    string = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    assert day_03.Solution(string).part_b() == 48