from aoc_cqkh42.year_2015 import day_7


def test_part_a():
    data = '123 -> x\n456 -> y\nx AND y -> d\nx OR y -> e\nx LSHIFT 2 -> f\ny RSHIFT 2 -> g\nNOT x -> a\nNOT y -> i'
    assert day_7.part_a(data) == 65412
