from typing import Self, Any

import more_itertools

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution


class Solution(BaseSolution):
    def _parse(self: Self) -> Any:
        numbers = [int(num) for num in self.input_]
        files = []
        out = []
        for index, num in enumerate(numbers):
            if index % 2:  # we're on a storage block
                out.append([None for _ in range(num)])
            else:
                out.append([index//2 for _ in range(num)])
        return out

    def part_a(self):
        field = []
        for index, num in enumerate(self.input_):
            if index % 2:  # we're on a storage block
                field.extend(None for _ in range(int(num)))
            else:
                field.extend(index // 2 for _ in range(int(num)))
        nums_to_move = [num for num in field[::-1] if num is not None]

        new_field = [num if num is not None else nums_to_move.pop(0) for num in field[:len(nums_to_move)]]
        return sum(index*num for index, num in enumerate(new_field))

    def part_b(self):
        return 1
        field = []
        for index, num in enumerate(self.input_):
            if index % 2:
                field.append((int(num), int(num)))# we're on a storage block
            else:
                field.append((index // 2, 0))
        return field





    def part_b(self):
        ...


if __name__ == "__main__":
    submit_answers(Solution,9, 2024)
