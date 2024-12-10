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

    def first_free_index(self):
        return more_itertools.first(
            more_itertools.iter_index((None in block for block in self.parsed), True))

    def last_filled_index(self):
        return more_itertools.last(more_itertools.iter_index(
            (set(block) != {None} and len(set(block)) > 0 for block in
             self.parsed), True))

    def do_single_move(self):
        free = self.first_free_index()
        fill = self.last_filled_index()
        num_available_slots = self.parsed[free].count(None)
        num_taken_slots = len(self.parsed[free]) - num_available_slots
        blocks_to_move = self.parsed[fill][:num_available_slots][::-1]

        num_moving = len(blocks_to_move)

        new_filled_block = self.parsed[fill][num_moving:] + [None for _ in blocks_to_move]
        free_sans_none = self.parsed[free][:num_taken_slots]
        free_post_move = free_sans_none + blocks_to_move
        nones_needed = len(self.parsed[free]) - len(free_post_move)
        free_post_move += [None for _ in range(nones_needed)]
        self.parsed[fill] = new_filled_block
        self.parsed[free] = free_post_move
    def part_a(self):
        field = []
        new_field = []
        for index, num in enumerate(self.input_):
            if index % 2:  # we're on a storage block
                field.extend(None for _ in range(int(num)))
            else:
                field.extend(index // 2 for _ in range(int(num)))
        nums_to_move = [num for num in field[::-1] if num is not None]
        for index, num in enumerate(field[:len(nums_to_move)]):
            if num is None:
                new_field.append(nums_to_move.pop(0))
            else:
                new_field.append(num)
        return sum(index*num for index, num in enumerate(new_field))

    def part_b(self):
        field = []





    def part_b(self):
        ...


if __name__ == "__main__":
    submit_answers(Solution,9, 2024)
