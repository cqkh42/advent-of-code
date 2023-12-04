#!/usr/bin/python3
"""Solutions for day 4 of 2023's Advent of Code.

Read the full puzzle at https://adventofcode.com/2023/day/4
"""
__all__ = ["Solution"]

from typing import Self
import functools

import more_itertools

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution

import parse


@functools.cache
def _play_card(row_num, intersection, all_rows):
    new_slice = slice(
        row_num + 1,
        min(row_num + 1 + intersection, len(all_rows))
    )
    new_cards = enumerate(all_rows[new_slice], start=row_num + 1)
    return sum(
        _play_card(num, matches, all_rows) for num, matches in new_cards
    ) + 1


BASE_PARSER = parse.compile('{num:d}')
ID_FINDER = parse.compile('{:d}:')


def parse_line(line):
    winning, numbers = line[10:].split('|')
    numbers = {n.named["num"] for n in BASE_PARSER.findall(numbers)}
    winning = {n.named["num"] for n in BASE_PARSER.findall(winning)}
    return len(numbers.intersection(winning))


class Solution(BaseSolution):
    """Solutions for day 4 of 2023's Advent of Code."""
    def _process_data(self: Self) -> tuple[int, ...]:
        return tuple(parse_line(line) for line in self.lines)

    def part_a(self: Self) -> int:
        return sum(
            2**(card-1) for card in self.processed if card
        )

    def part_b(self: Self) -> int:
        return sum(
            _play_card(num, card, self.processed)
            for num, card in
            more_itertools.always_reversible(enumerate(self.processed))
        )


if __name__ == "__main__":
    submit_answers(Solution, 4, 2023)
