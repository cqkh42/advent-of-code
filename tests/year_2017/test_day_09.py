import pytest

from aoc_cqkh42.year_2017 import day_09


@pytest.fixture
def data():
    data = (
        "pbga (66)\n"
        "xhth (57)\n"
        "ebii (61)\n"
        "havc (66)\n"
        "ktlj (57)\n"
        "fwft (72) -> ktlj, cntj, xhth\n"
        "qoyq (66)\n"
        "padx (45) -> pbga, havc, qoyq\n"
        "tknk (41) -> ugml, padx, fwft\n"
        "jptl (61)\n"
        "ugml (68) -> gyxo, ebii, jptl\n"
        "gyxo (61)\n"
        "cntj (57)"
    )
    return data

@pytest.mark.parametrize('input_', [
'<>',
'<random characters>',
'<<<<>',
'<{!>}>',
'<!!>',
'<!!!>>',
'<{o"i!a,<{i<a>',
])
def test_garbage_removal(input_):
    assert day_09.Solution(input_).processed == ''


@pytest.mark.parametrize('input_, output', [
    ('{}', 1),
    ('{{{}}}', 3),
    ('{{},{}}', 3),
    ('{{{},{},{{}}}}', 6),
    ('{<{},{},{{}}>}', 1),
    ('{<a>,<a>,<a>,<a>}', 1),
    ('{{<a>},{<a>},{<a>},{<a>}}', 5),
    ('{{<!>},{<!>},{<!>},{<a>}}', 2)
])
def test_count_groups(input_, output):
    assert day_09.Solution(input_).processed.count('{') == output


@pytest.mark.parametrize('input_, output', [
    ('{}',1),
    ('{{{}}}', 6),
    ('{{}, {}}', 5),
    ('{{{}, {}, {{}}}}', 16),
    ('{<a>,<a>,<a>,<a>}', 1),
    ('{{<ab>},{<ab>},{<ab>},{<ab>}}', 9),
    ('{{<!!>},{<!!>},{<!!>},{<!!>}}', 9),
    ('{{<a!>},{<a!>},{<a!>},{<ab>}}', 3)
])
def test_part_a(input_, output):
    assert day_09.Solution(input_).part_a() == output
