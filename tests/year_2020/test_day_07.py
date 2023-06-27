"""Tests for day 7 of 2020's Advent of Code."""
import pytest

from aoc_cqkh42.year_2020 import day_07


@pytest.fixture
def data() -> str:
    """
    Test data for day_01.

    Returns
    -------
    data: str
    """
    data = (
        "light red bags contain 1 bright white bag, 2 muted yellow bags.\n"
        "dark orange bags contain 3 bright white bags, 4 muted yellow bags.\n"
        "bright white bags contain 1 shiny gold bag.\n"
        "muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.\n"
        "shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.\n"
        "dark olive bags contain 3 faded blue bags, 4 dotted black bags.\n"
        "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.\n"
        "faded blue bags contain no other bags.\n"
        "dotted black bags contain no other bags."
    )
    return data


@pytest.fixture
def mapping() -> dict:
    """
    Parsed test data for day_01.

    Returns
    -------
    mapping: str
    """
    mapping = {
        "light red": {"bright white": 1, "muted yellow": 2},
        "dark orange": {"bright white": 3, "muted yellow": 4},
        "bright white": {"shiny gold": 1},
        "muted yellow": {"shiny gold": 2, "faded blue": 9},
        "shiny gold": {"dark olive": 1, "vibrant plum": 2},
        "dark olive": {"faded blue": 3, "dotted black": 4},
        "vibrant plum": {"faded blue": 5, "dotted black": 6},
        "faded blue": {},
        "dotted black": {},
    }
    return mapping


def test__parse_bags(data, mapping) -> None:
    assert day_07._parse_bags(data) == mapping


@pytest.mark.parametrize(
    "color, answer",
    [
        ("dotted black", set()),
        ("vibrant plum", {"faded blue", "dotted black"}),
        (
                "shiny gold",
                {"dark olive", "vibrant plum", "faded blue", "dotted black"},
        ),
    ],
)
def test__can_contain(color, answer, mapping) -> None:
    assert day_07._can_contain(color, mapping) == answer


@pytest.mark.parametrize(
    "color, answer",
    [
        ("faded blue", 1),
        ("dotted black", 1),
        ("vibrant plum", 12),
        ("dark olive", 8),
        ("shiny gold", 33),
    ],
)
def test__count_bags(color, answer, mapping) -> None:
    assert day_07._count_bags(color, mapping) == answer


def test_part_a(data) -> None:
    assert day_07.part_a(data) == 4


def test_part_b(data) -> None:
    assert day_07.part_b(data) == 32
