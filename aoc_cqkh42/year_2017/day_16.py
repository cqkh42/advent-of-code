import functools
from string import ascii_lowercase
from typing import Self

import more_itertools
import parse

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution

#todo coords
def spin(programs: list, num: int):
    first = programs[:-num]
    second = programs[-num:]
    return second + first


def swap_indices(programs, indices):
    x, y = indices
    a = programs[x]
    b = programs[y]
    programs[x] = b
    programs[y] = a
    return programs


def swap_characters(programs, characters):
    x, y = characters
    program_index_a = programs.index(x)
    program_index_b = programs.index(y)
    programs[program_index_b] = x
    programs[program_index_a] = y
    return programs

#todo number parser
class Solution(BaseSolution):
    programs = list(ascii_lowercase[:16])
    program_history = [ascii_lowercase[:16]]
    num_iterations = 0

    def _parse(self: Self) -> dict[int, list[int]]:
        p = parse.compile(r"{:d}")
        instructions = []
        for instruction in self.input_.split(","):
            nums = [i[0] for i in p.findall(instruction)]
            x, y = more_itertools.padded(nums, n=2)
            if instruction.startswith("s"):
                func = functools.partial(spin, num=x)
                instructions.append(func)
            elif instruction.startswith("x"):
                func = functools.partial(swap_indices, indices=nums)
                instructions.append(func)
            else:
                i = [instruction[1], instruction[3]]
                func = functools.partial(swap_characters, characters=i)
                instructions.append(func)
        return instructions

    def _do_iterations(self):
        for instruction in self.parsed:
            self.programs = instruction(self.programs)
        self.program_history.append("".join(self.programs))
        self.num_iterations += 1

    def part_a(self, num_programs=16):
        self._do_iterations()
        return "".join(self.programs)

    def part_b(self, num_programs=16, num_iters=1_000_000_000):
        while self.programs != list(ascii_lowercase[:16]):
            self._do_iterations()
        l_o = num_iters % self.num_iterations
        return "".join(self.program_history[l_o])


if __name__ == "__main__":
    submit_answers(Solution, 16, 2017)
