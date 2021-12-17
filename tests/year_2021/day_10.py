import pytest

from aoc_cqkh42.year_2021 import day_10


@pytest.fixture
def solution():
    data = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]"""
    return day_10.Solution(data)


@pytest.mark.parametrize('line, char', [
    ('[({(<(())[]>[[{[]{<()<>>', None),
    ('[(()[<>])]({[<{<<[]>>(', None),
    ('{([(<{}[<>[]}>{[]{[(<()>', '}'),
    ('(((({<>}<{<{<>}{[]{[]{}', None),
    ('[[<[([]))<([[{}[[()]]]', ')'),
    ('[{[{({}]{}}([{[{{{}}([]', ']'),
    ('{<[[]]>}<{[{[{[]{()[[[]', None),
    ('[<(<(<(<{}))><([]([]()', ')'),
    ('<{([([[(<>()){}]>(<<{{', '>'),
    ('<{([{{}}[<[[[<>{}]]]>[]]', None)
])
def test_is_corrupt(line, char):
    assert day_10.is_corrupt(line) == char


def test_part_a(solution):
    assert solution.part_a() == 26397


def test_part_b(solution):
    assert solution.part_b() == 288957
