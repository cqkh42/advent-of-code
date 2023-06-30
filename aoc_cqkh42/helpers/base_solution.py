from abc import ABC, abstractmethod
from dataclasses import dataclass
from functools import cached_property
from typing import Self, Any

import parse

NUM_PARSER = parse.compile('{num:d}')


# TODO do I need to abstract out binary search?
# TODO how many places can we use more_itertools
# todo make parse data an internal function

@dataclass
class BaseSolution(ABC):
    data: str

    def __post_init__(self: Self):
        self.parsed_data = self._parse_data()

    @abstractmethod
    def _parse_data(self: Self) -> Any:
        return self.data

    @cached_property
    def lines(self: Self) -> list[str, ...]:
        return self.data.split("\n")

    @cached_property
    def numbers(self: Self) -> tuple[int, ...]:
        return tuple(result["num"] for result in NUM_PARSER.findall(self.data))

    @abstractmethod
    def part_a(self: Self) -> str | int:
        ...

    @abstractmethod
    def part_b(self: Self) -> str | int:
        ...
