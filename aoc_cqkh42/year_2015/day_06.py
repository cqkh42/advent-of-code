import numpy as np
import parse

from aoc_cqkh42 import BaseSolution


class Solution(BaseSolution):
    parser = parse.compile('{:w} {:d},{:d} through {:d},{:d}')

    def map_line(self, line):
        line = line.replace('turn ', '')
        action, x_start, y_start, x_end, y_end = self.parser.parse(line)
        return action, slice(x_start, x_end+1), slice(y_start, y_end+1)

    def parse_data(self):
        lines = [self.map_line(line) for line in self.data.split('\n')]
        return lines

    def part_a(self):
        lights = np.zeros((1000, 1000), dtype=bool)
        for action, x, y in self.parsed_data:
            if action == 'on':
                lights[x, y] = True
            elif action == 'off':
                lights[x, y] = False
            else:
                lights[x, y] ^= True
        return lights.sum(dtype=int)

    def part_b(self):
        lights = np.zeros((1000, 1000))
        for action, x, y in self.parsed_data:
            if action == 'on':
                lights[x, y] += 1
            elif action == 'toggle':
                lights[x, y] += 2
            else:
                lights[x, y] -= 1
                lights = np.clip(lights, a_min=0, a_max=None)
        return lights.sum(dtype=int)
