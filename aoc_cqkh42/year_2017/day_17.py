import functools
import math
from collections import defaultdict
from typing import Self, Any
from string import ascii_lowercase

import more_itertools
import parse
from numpy.ma.core import indices

from aoc_cqkh42.helpers.base_solution import BaseSolution
from aoc_cqkh42 import submit_answers


class Solution(BaseSolution):
    array = [0]
    index = 0
    step = 1
    indices = [0]

    def _process_data(self: Self) -> Any:
        return int(self.input_)

    def _do_step(self):
        new_index = (self.index + self.processed) % self.step
        self.indices.append(new_index)
        self.array.insert(new_index+1, self.step)
        self.index = new_index+1
        self.step += 1
    def part_a(self):
        for _ in range(2017):
            self._do_step()
        return self.array[self.index+1]


    def part_b(self):
        for num in range(2017, 100_000):
            self._do_step()

            # print(self.array.index(0), self.array[1])
        print(self.indices)


if __name__ == "__main__":
    submit_answers(Solution, 17, 2017)