import numpy as np
import parse

from aoc_cqkh42 import BaseSolution


class Solution(BaseSolution):
    parser = parse.compile('{:w} {:d},{:d} through {:d},{:d}')

    def parse_data(self):
        tidied = self.data.replace('turn ', '')
        instructions = self.parser.findall(tidied)
        instructions = [
            (action, slice(x_start, x_end + 1), slice(y_start, y_end + 1))
            for action, x_start, y_start, x_end, y_end in instructions
        ]
        return instructions

    def part_a(self):
        lights = np.zeros((1000, 1000), dtype=int)
        for action, x, y in self.parsed_data:
            if action == 'on':
                lights[x, y] = 1
            elif action == 'off':
                lights[x, y] = 0
            else:
                lights[x, y] ^= 1
        return lights.sum()

    def part_b(self):
        lights = np.zeros((1000, 1000), dtype=int)
        for action, x, y in self.parsed_data:
            if action == 'on':
                lights[x, y] += 1
            elif action == 'toggle':
                lights[x, y] += 2
            else:
                lights[x, y] -= 1
                lights = np.clip(lights, a_min=0, a_max=None)
        return lights.sum()
