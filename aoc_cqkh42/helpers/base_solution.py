"""Base solution to build solutions for each day."""
__all__ = ["BaseSolution"]
from abc import ABC, abstractmethod
from dataclasses import dataclass
from functools import cached_property
from typing import Any, Self

import parse

NUM_PARSER = parse.compile("{num:d}")


@dataclass
class BaseSolution(ABC):
    """Base solution to build solutions for each day.

    Attributes:
        input_: raw input data
        lines: list of lines in the input data
        processed: processed input data
        numbers: tuple of numbers in the input data
    """

    input_: str

    def __post_init__(self: Self) -> None:
        """Initialise the solution behind the scenes."""
        self.processed: Any = self._process_data()

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

    @abstractmethod
    def part_a(self: Self) -> str | int:
        """Part a for the Solution."""

    @abstractmethod
    def part_b(self: Self) -> str | int:
        """Part b for the Solution."""

    def _process_data(self: Self) -> Any:
        """Process raw input data.

        Returns:
            Processed data
        """
        return self.input_
