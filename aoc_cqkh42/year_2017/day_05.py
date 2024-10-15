import functools

import itertools

from aoc_cqkh42.helpers.base_solution import BaseSolution
from aoc_cqkh42 import submit_answers

@functools.cache
def part_b_rule(num):
    return (-1) ** (num >= 3)

class Solution(BaseSolution):
    def do_run(self, func, index=0):
        jumps = list(self.numbers)
        for step in itertools.count():
            if index >= len(jumps):
                return step
            else:
                new_index = index + jumps[index]
                jumps[index] += func(jumps[index])
                index = new_index

    def part_a(self):
        func = lambda index: 1
        return self.do_run(func)

    def part_b(self):
        return self.do_run(part_b_rule)


if __name__ == "__main__":
    submit_answers(Solution, 5, 2017)
