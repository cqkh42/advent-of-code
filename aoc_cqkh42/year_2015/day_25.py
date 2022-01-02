import re

from aoc_cqkh42 import BaseSolution


class Solution(BaseSolution):
    def part_a(self):
        row, col = re.findall(r'\d+', self.data)
        row = int(row)
        col = int(col)

        triangle_number = col + row - 1
        that_number = triangle_number * (triangle_number + 1) // 2
        my_number = that_number - row
        return (pow(252533, my_number, 33554393) * 20151125) % 33554393
