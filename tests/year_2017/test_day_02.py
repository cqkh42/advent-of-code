from aoc_cqkh42.year_2017 import day_02


def test_part_a():
    data = "5\t1\t9\t5\n" "7\t5\t3\n" "2\t4\t6\t8"
    assert day_02.part_a(data) == 18


def test_part_b():
    data = "5\t9\t2\t8\n" "9\t4\t7\t3\n" "3\t8\t6\t5"
    assert day_02.part_b(data) == 9
