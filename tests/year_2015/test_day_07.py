import textwrap

from aoc_cqkh42.year_2015 import day_07


def test_part_a():
    data = """\
        123 -> x
        456 -> y
        x AND y -> d
        x OR y -> e
        x LSHIFT 2 -> f
        y RSHIFT 2 -> g
        NOT x -> a
        NOT y -> i
    """
    solution = day_07.Solution(textwrap.dedent(data))
    assert solution.part_a() == 65412
