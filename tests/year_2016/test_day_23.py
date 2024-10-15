from aoc_cqkh42.year_2016.day_12 import Computer

from pytest import fixture


@fixture
def data():
    return """cpy 2 a
tgl a
tgl a
tgl a
cpy 1 a
dec a
dec a"""


def test_computer(data):
    c = Computer(data)
    c.run()
    assert c.registers['a'] == 3
