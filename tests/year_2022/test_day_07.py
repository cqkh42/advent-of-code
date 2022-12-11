import pytest

from aoc_cqkh42.year_2022 import day_07


@pytest.fixture(scope='module')
def solution():
    data = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""
    return day_07.Solution(data)


def test_part_a(solution):
    assert solution.part_a() == 95437


def test_part_b(solution):
    assert solution.part_b() == 24933642
