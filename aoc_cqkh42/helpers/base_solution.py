"""Base solution to build solutions for each day."""
__all__ = ["BaseSolution"]
from abc import ABC, abstractmethod
from dataclasses import dataclass
from functools import cached_property
from typing import Any, Self

import parse

NUM_PARSER = parse.compile("{num:d}")


class BaseSolution(ABC):
    """Base solution to build solutions for each day.

    Attributes:
        input_: raw input data
        lines: list of lines in the input data
        parsed: processed input data
        numbers: tuple of numbers in the input data
    """
    def __init__(self: Self, input_) -> None:
        """Initialise the solution behind the scenes."""
        self.input_ = input_
        self.parsed: Any = self._parse()


    @cached_property
    def lines(self: Self) -> list[str]:
        """Iterate through all lines in the input data.

        Returns:
            A list of lines in the input data
        """
        return self.input_.split("\n")

    @cached_property
    def numbers(self: Self) -> tuple[int, ...]:
        """Find all numbers in the input data.

        Returns:
            A tuple of all numbers in the input data
        """
        return tuple(
            result["num"] for result in NUM_PARSER.findall(self.input_)
        )

    def part_a(self: Self) -> str | int:
        """Part a for the Solution."""
        return None

    def part_b(self: Self) -> str | int:
        """Part b for the Solution."""
        return None

    def _parse(self: Self) -> Any:
        """Process raw input data.

        Returns:
            Processed data
        """
        return self.input_

    @cached_property
    def parsed_lines(self) -> tuple[Any, ...]:
        parsed = (self._parse_line(line) for line in self.lines)
        return tuple(line for line in parsed if line)

    @staticmethod
    def _parse_line(self, line: str):
        return line
