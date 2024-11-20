from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution


class Solution(BaseSolution):
    def _parse(self):
        return [int(num) for num in self.input_]

    def solve_captcha(self, jump=1):
        jumped = self.parsed[jump:] + self.parsed[:jump]
        return sum(left for left, right in zip(self.parsed, jumped) if left == right)

    def part_a(self):
        return self.solve_captcha()

    def part_b(self):
        jump = len(self.input_) // 2
        return self.solve_captcha(jump)


if __name__ == "__main__":
    submit_answers(Solution, 1, 2017)
