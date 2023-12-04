#!/usr/bin/python3
"""Solutions for day 4 of 2023's Advent of Code.

Read the full puzzle at https://adventofcode.com/2023/day/3
"""
__all__ = ["Solution"]

import itertools
from collections import defaultdict
from dataclasses import dataclass
from typing import Self
import queue
import re

import more_itertools

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution

import numpy as np
import parse


@dataclass
class Card:
    num: int
    numbers: set[int, ...]
    winning: set[int, ...]

    @property
    def matches(self):
        return len(self.winning.intersection(self.numbers))


BASE_PARSER = parse.compile('{num:d}')
ID_FINDER = parse.compile('{:d}:')
class Solution(BaseSolution):
    """Solutions for day 4 of 2018's Advent of Code."""
    def _process_data(self: Self) -> list[Card, ...]:
        cards = []
        for card_num, line in enumerate(self.lines):
            line = line[10:]
            winning, numbers = line.split('|')
            winning = BASE_PARSER.findall(winning)
            numbers = BASE_PARSER.findall(numbers)
            card = Card(
                card_num,
                {n.named["num"] for n in numbers},
                {n.named["num"] for n in winning}
            )
            cards.append(card)
        return cards


    def part_a(self: Self) -> int:
        k = sum(2**(card.matches-1) for card in self.processed if card.matches)
        return int(k)

    def part_b(self: Self) -> int:
        cards = queue.Queue()
        for card in self.processed:
            cards.put(card)
        total = 0

        while not cards.empty():
            card = cards.get()
            total += 1
            to_get = slice(card.num+1, min(card.num+1+card.matches, len(self.lines)))
            for new_card in self.processed[to_get]:
                cards.put(new_card)
        return total

if __name__ == "__main__":
    submit_answers(Solution, 4, 2023)
