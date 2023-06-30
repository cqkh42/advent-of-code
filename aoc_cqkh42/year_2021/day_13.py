import numpy as np
import parse

from aoc_cqkh42.helpers import aocr
from aoc_cqkh42.helpers.base_solution import BaseSolution


class Solution(BaseSolution):
    coord_parser = parse.compile(r'{:d},{:d}')
    fold_parser = parse.compile(r'fold along {}={:d}')

    def _parse_data(self):
        coords = self.coord_parser.findall(self.data)
        self.folds = [i for i in self.fold_parser.findall(self.data)]
        x = max(b for a, b in self.folds if a == 'x')
        y = max(b for a, b in self.folds if a == 'y')
        sheet = np.zeros((y * 2 + 1, x * 2 + 1), dtype=bool)
        for a, b, in coords:
            sheet[b, a] = True
        return sheet

    def fold(self):
        axis, index = self.folds.pop(0)
        fold_axis = axis=='x'
        if axis == 'y':
            a, b = self.parsed_data[:index, :], self.parsed_data[index+1:, :]
        else:
            a, b = self.parsed_data[:, :index], self.parsed_data[:, index+1:]
        b = np.flip(b, axis=fold_axis)
        self.parsed_data = a | b

    def part_a(self):
        self.fold()
        return self.parsed_data.astype(int).sum()

    def part_b(self):
        while self.folds:
            self.fold()
        a = np.concatenate(self.parsed_data)
        return aocr.word(a, True)
