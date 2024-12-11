from typing import Self, Any

from more_itertools import first, iter_index, flatten

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution


class Solution(BaseSolution):
    def _parse(self: Self) -> Any:
        numbers = [int(num) for num in self.input_]
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
        field = []
        # for index, num in enumerate('2333133121414131402'):
        for index, num in enumerate(self.input_):
            if index % 2:
                field.append([None]*int(num))# we're on a storage block
            else:
                field.append([index // 2]*int(num))

        moved = set()

        for mover in field[::-1][:-1]:
            to_move = [i for i in mover if i is not None]

            if not to_move:
                continue
            if to_move[0] in moved:
                continue
            moved.add(to_move[0])
            size = len(to_move)
            try:
                f = first(iter_index((len(block) >= size and set(block) == {None} for block in field), True))
            except ValueError:
                pass
            else:
                z = field.index(mover)
                if f >= z:
                    continue
                for _ in range(size):
                    field[f].remove(None)
                field.remove(mover)
                field.insert(f, to_move)
                field.insert(z, [None]*size)

        return sum(index * num for index, num in enumerate(flatten(field)) if num)


if __name__ == "__main__":
    submit_answers(Solution,9, 2024)
