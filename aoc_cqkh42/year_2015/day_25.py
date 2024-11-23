from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution


class Solution(BaseSolution):
    def part_a(self):
        row, col = self.numbers

        triangle_number = col + row - 1
        that_number = triangle_number * (triangle_number + 1) // 2
        my_number = that_number - row
        return (pow(252533, my_number, 33554393) * 20151125) % 33554393



if __name__ == "__main__":
    submit_answers(Solution, 25, 2015)
