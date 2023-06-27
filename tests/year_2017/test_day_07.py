import pytest

from aoc_cqkh42.year_2017 import day_07


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


def test_part_a(data):
    assert day_07.part_a(data) == "tknk"


@pytest.mark.xfail
def test_part_b(data):
    assert day_07.part_b(data) == 4
