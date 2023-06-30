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
    input_: str

    def __post_init__(self: Self):
        self.processed = self._process_data()

    def _process_data(self: Self) -> Any:
        return self.input_

    @cached_property
    def lines(self: Self) -> list[str, ...]:
        return self.input_.split("\n")

    @cached_property
    def numbers(self: Self) -> tuple[int, ...]:
        return tuple(
            result["num"] for result in NUM_PARSER.findall(self.input_))

    @abstractmethod
    def part_a(self: Self) -> str | int:
        ...

    @abstractmethod
    def part_b(self: Self) -> str | int:
        ...
