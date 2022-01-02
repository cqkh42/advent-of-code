import itertools

import parse
import numpy as np

from aoc_cqkh42 import BaseSolution
from aoc_cqkh42.helpers import aocr


class Solution(BaseSolution):
    def parse_data(self):
        instructions = self.data.split('\n')
        screen = np.zeros((6, 50))
        for instruction in instructions:
            if instruction.startswith('rect'):
                x, y = RECT_PARSER.parse(instruction)
                screen[:y, :x] = 1
            elif 'row' in instruction:
                y, steps = ROW_PARSER.parse(instruction)
                screen[y] = np.roll(screen[y], steps)
            else:
                x, steps = COL_PARSER.parse(instruction)
                screen[:, x] = np.roll(screen[:, x], steps)
        return screen.astype(int)

    def part_a(self):
        return self.parsed_data.sum()

    def part_b(self):
        return aocr.word(itertools.chain.from_iterable(self.parsed_data))


RECT_PARSER = parse.compile(r'rect {:d}x{:d}')
ROW_PARSER = parse.compile(r'rotate row y={:d} by {:d}')
COL_PARSER = parse.compile(r'rotate column x={:d} by {:d}')
