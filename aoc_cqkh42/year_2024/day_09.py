from typing import Self, Any

import more_itertools
from more_itertools import first, iter_index, flatten

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution


class Solution(BaseSolution):
    def _parse(self: Self) -> Any:
        field = []
        # for index, num in enumerate('2333133121414131402'):
        for index, num in enumerate(self.input_):
            if index % 2:
                field.append([None]*int(num))# we're on a storage block
            else:
                field.append([index // 2]*int(num))
        return field

    def part_a(self):
        field = list(more_itertools.flatten(self.parsed))
        nums_to_move = [num for num in field[::-1] if num is not None]

        new_field = [num if num is not None else nums_to_move.pop(0) for num in field[:len(nums_to_move)]]
        return sum(index*num for index, num in enumerate(new_field))

    def part_b(self):
        moved = set()

        for mover in self.parsed[::-1][:-1]:
            to_move = [i for i in mover if i is not None]

            if not to_move:
                continue
            if to_move[0] in moved:
                continue
            moved.add(to_move[0])
            size = len(to_move)
            try:
                f = first(iter_index((len(block) >= size and set(block) == {None} for block in self.parsed), True))
            except ValueError:
                pass
            else:
                z = self.parsed.index(mover)
                if f >= z:
                    continue
                for _ in range(size):
                    self.parsed[f].remove(None)
                self.parsed.remove(mover)
                self.parsed.insert(f, to_move)
                self.parsed.insert(z, [None]*size)

        return sum(index * num for index, num in enumerate(flatten(self.parsed)) if num)


if __name__ == "__main__":
    submit_answers(Solution,9, 2024)
