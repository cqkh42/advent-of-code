import math
from typing import Self
from string import ascii_lowercase

import more_itertools
import parse
from numpy.core.defchararray import upper

from aoc_cqkh42.helpers.base_solution import BaseSolution
from aoc_cqkh42 import submit_answers




class Solution(BaseSolution):
    def _process_data(self: Self) -> dict[int, list[int]]:
        return self._build_initial_mapping()

    def _build_initial_mapping(self, length=16):
        programs = list(range(length))
        p = parse.compile(r'{:d}')
        for instruction in self.input_.split(','):
            nums = [i[0] for i in p.findall(instruction)]
            x, y = more_itertools.padded(nums, n=2)
            if instruction.startswith('s'):
                first = programs[:-x]
                second = programs[-x:]
                programs = second + first
            elif instruction.startswith('x'):
                a = programs[x]
                b = programs[y]
                programs[x] = b
                programs[y] = a
            elif instruction.startswith('p'):
                character_index_a = ascii_lowercase.index(instruction[1])
                character_index_b = ascii_lowercase.index(instruction[3])
                program_index_a = programs.index(character_index_a)
                program_index_b = programs.index(character_index_b)
                programs[program_index_b] = character_index_a
                programs[program_index_a] = character_index_b
        return {1: programs}


    def part_a(self, num_programs=16):
        programs = self._build_initial_mapping(num_programs)
        return ''.join(ascii_lowercase[i] for i in programs[1])

    def part_b(self, num_programs=16, num_iters=1_000_000_000):
        for i in range(num_iters):
            ...
        return
        upper_bound = math.floor(math.log(num_iters) / math.log(2)) + 1
        print(upper_bound)
        mappings = self._build_initial_mapping(num_programs)
        for n in range(1,upper_bound):
            print(n)
            before = 2**(n-1)
            mappings[2**n] = [mappings[before][i] for i in mappings[before]]
        print(mappings)
        #     self.processed[2**n] = [self.processed[before][i] for i in self.processed[before]]
        # print(self.processed)
        # self.processed[2] = [self.processed[1][i] for i in self.processed[1]]
        # self.processed[4] = [self.processed[2][i] for i in self.processed[2]]
        # self.processed[8] = [self.processed[4][i] for i in self.processed[4]]
        # self.processed[16] = [self.processed[8][i] for i in self.processed[8]]
        # self.processed[32] = [self.processed[16][i] for i in self.processed[16]]
        # self.processed[64] = [self.processed[32][i] for i in self.processed[32]]
        # self.processed[128] = [self.processed[64][i] for i in self.processed[64]]
        # self.processed[256] = [self.processed[128][i] for i in self.processed[128]]
        # self.processed[512] = [self.processed[256][i] for i in self.processed[256]]
        # self.processed[1024] = [self.processed[512][i] for i in self.processed[512]]
        # self.processed[128] = [self.processed[64][i] for i in self.processed[64]]
        # self.processed[128] = [self.processed[64][i] for i in self.processed[64]]
        # self.processed[128] = [self.processed[64][i] for i in self.processed[64]]
        # self.processed[128] = [self.processed[64][i] for i in self.processed[64]]
        # self.processed[128] = [self.processed[64][i] for i in self.processed[64]]

        return
        mappings = {1: dict(enumerate(self.programs))}
        target = 1_000_000_000
        num_iters = 1
        while num_iters <= target:
            max_possible = max(i for i in mappings if i <= (target - num_iters))
            mapping = mappings[mapping]

        print(self.programs, mapping)
        for _ in range(1_000_000_000 -1):
            self.programs = [mapping[i] for i in self.programs]
        chars = [ascii_lowercase[i] for i in self.programs]
        return ''.join(chars)



if __name__ == "__main__":
    submit_answers(Solution, 16, 2017)