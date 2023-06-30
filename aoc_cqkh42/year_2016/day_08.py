import itertools

import numpy as np
import parse

from aoc_cqkh42.helpers.aocr import word
from aoc_cqkh42.helpers.base_solution import BaseSolution


class Solution(BaseSolution):
    rect = parse.compile(r'rect {:d}x{:d}')
    row_parser = parse.compile(r'rotate row y={:d} by {:d}')
    col_parser = parse.compile(r'rotate column x={:d} by {:d}')

    def _process_data(self):
        screen = np.zeros((6, 50))
        for instruction in self.lines:
            if instruction.startswith('rect'):
                x, y = self.rect.parse(instruction)
                screen[:y, :x] = 1
            elif 'row' in instruction:
                y, steps = self.row_parser.parse(instruction)
                screen[y] = np.roll(screen[y], steps)
            else:
                x, steps = self.col_parser.parse(instruction)
                screen[:, x] = np.roll(screen[:, x], steps)
        return screen.astype(int)

    def part_a(self):
        return self.processed.sum()

    def part_b(self):
        return word(itertools.chain.from_iterable(self.processed))
