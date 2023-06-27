"""Tests for day 14 of 2020's Advent of Code."""
import pytest

from aoc_cqkh42.year_2020 import day_14


def test__replace_floater() -> None:
    address = "X1101X"
    answer = {"111011", "111010", "011011", "011010"}
    assert day_14._replace_floater(address) == answer


# noinspection SpellCheckingInspection
@pytest.mark.parametrize("value, answer", [(11, 73), (101, 101), (0, 64)])
def test__mask_value(value, answer) -> None:
    mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X"
    assert day_14._mask_value(value, mask) == answer


@pytest.mark.parametrize(
    "address, mask, answer",
    [
        (42, "000000000000000000000000000000X1001X", {26, 27, 58, 59}),
        (
                26,
                "00000000000000000000000000000000X0XX",
                {16, 17, 18, 19, 24, 25, 26, 27},
        ),
    ],
)
def test__mask_address(address, mask, answer) -> None:
    assert day_14._mask_address(address, mask) == answer


def test_part_a() -> None:
    # noinspection SpellCheckingInspection
    data = (
        "mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X\n"
        "mem[8] = 11\n"
        "mem[7] = 101\n"
        "mem[8] = 0"
    )
    assert day_14.part_a(data) == 165


def test_part_b() -> None:
    data = (
        "mask = 000000000000000000000000000000X1001X\n"
        "mem[42] = 100\n"
        "mask = 00000000000000000000000000000000X0XX\n"
        "mem[26] = 1"
    )
    assert day_14.part_b(data) == 208
