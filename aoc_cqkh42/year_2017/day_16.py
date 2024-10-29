from typing import Self
from string import ascii_lowercase

import more_itertools
import parse

from aoc_cqkh42.helpers.base_solution import BaseSolution
from aoc_cqkh42 import submit_answers




class Solution(BaseSolution):
    programs = list(range(16))
    def _process_data(self: Self) -> list[str]:
        return self.input_.split(',')

    def swap(self, num):
        first = self.programs[:-num]
        second = self.programs[-num:]
        self.programs = second + first

    def part_a(self, num_programs=16):
        p = parse.compile(r'{:d}')
        for instruction in self.processed:
            nums = [i[0] for i in p.findall(instruction)]
            x, y = more_itertools.padded(nums, n=2)
            if instruction.startswith('s'):
                self.swap(x)
            elif instruction.startswith('x'):
                a = self.programs[x]
                b = self.programs[y]
                self.programs[x] = b
                self.programs[y] = a
            elif instruction.startswith('p'):
                character_index_a = ascii_lowercase.index(instruction[1])
                character_index_b = ascii_lowercase.index(instruction[3])
                program_index_a = self.programs.index(character_index_a)
                program_index_b = self.programs.index(character_index_b)
                self.programs[program_index_b] = character_index_a
                self.programs[program_index_a] = character_index_b
        chars = [ascii_lowercase[i] for i in self.programs]
        return ''.join(chars)

    def part_b(self):
        print(self.programs)
        return
        mapping = {}
        for index, char in enumerate(ascii_lowercase[:16]):
            mapping[index] = self.programs.index(char)
        for _ in range(1_000_000_000):
            pass



if __name__ == "__main__":
    submit_answers(Solution, 15, 2017)